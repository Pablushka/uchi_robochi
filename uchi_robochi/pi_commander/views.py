# try:
#     import RPi.GPIO as GPIO
# except RuntimeError as e:
#     print(
#         f" {e} Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script"
#     )
from django.core import serializers as djs
from django.db.models.fields import CommaSeparatedIntegerField
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import query
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import (
    RelaySerializer,
    UserSerializer,
    RaspberrySerializer,
    ActionSerializer,
)
from django.contrib.auth.models import User
from .models import Raspberry
from .models import Relay, Action
import time

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RaspberryViewSet(viewsets.ModelViewSet):
    queryset = Raspberry.objects.all()
    serializer_class = RaspberrySerializer


class RelayViewSet(viewsets.ModelViewSet):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


@api_view()
def test_GPIO(request):
    print("Starting GPIO Test....")

    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(20, GPIO.IN)
        test_result = "Andó"
    except Exception as e:
        print(str(e))
        test_result = "Falló"

    print("GPIO Test finished")

    return Response(data={"test": test_result}, status=200)


@api_view()
def set_action_status(request, id):
    # Buscar la accion para cambiarle el status
    action = get_object_or_404(Action, pk=id)
    # Le cambio el status, si la encuentro

    action.status = not action.status

    # if action.status == True:
    #     action.status = False
    # else:
    #     action.status = True

    # TODO: revisar si el save falla
    action.save()

    # Si no la encuentro la accion es inválida
    return Response(data={"respuesta": {"status": action.status}}, status=200)


# TODO: Crear una funcion que permita resetear los valores de status por default
# TODO: Clarita


@api_view(["POST"])
def reset_action_status(request):
    """
    Apaga todas las acciones de una raspberry
    """
    user_id = request.data["user_id"]

    raspberry_id = request.data["raspberry_id"]

    if not type(user_id) is int:
        return Response(data={"respuesta": "Please enter a User number"}, status=400)

    if not type(raspberry_id) is int:
        return Response(
            data={"respuesta": "Please enter a Raspberry number"}, status=400
        )

    actions = Action.objects.filter(user__exact=user_id, raspberry__exact=raspberry_id)
    if len(actions) > 0:
        for action in actions:
            action.status = False
            action.save()
        return Response(
            data={
                "respuesta": f"Le cambie a todo, gracias, vuelva prontos, cambié {len(actions)} acciones"
            },
            status=200,
        )

    return Response(data={"respuesta": "No encontre raspberries"}, status=200)


@api_view(["GET", "POST"])
def switch_action(request):

    """
    Cambia el estado una action
    """

    if request.method == "GET":
        # el navegador me solicita algo
        acciones = Action.objects.values(
            "id", "raspberry", "description", "relay", "user", "status"
        )
        data = list(acciones)
    else:
        # el navegador me envía algo
        data = request.data
        id = data["action_id"]

        action = get_object_or_404(Action, pk=id)

        previous_status = action.status

        # Si en el json envio un new_status cambia el estado por ese new_status
        # de lo contario invierte el estado actual de la acción
        if "new_status" in data.keys():
            action.status = data["new_status"]
        else:
            action.status = not action.status

        action.save()

        # Esto lo tiene que hacer el TaskWorker
        # chequeo si hay timeout
        # if action.time_out != None:

        #     match action.time_unit:
        #         case 'D':
        #             segundos = (60 * 60 * 24) * action.time_out
        #         case 'H':
        #             segundos = (60 * 60 ) * action.time_out
        #         case 'M':
        #             segundos = 60 * action.time_out
        #         case 'S':
        #             segundos = action.time_out

        #     #si hay timeout tengo que esperar x tiempo
        #     time.sleep(segundos)

        #     #volver al estado original
        #     action.status = previous_status
        #     action.save()

    return Response(data={"respuesta": data}, status=200)
