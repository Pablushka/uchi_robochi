try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print(
        "Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script"
    )
from django.shortcuts import get_object_or_404
from django.db.models import query
from rest_framework import viewsets
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
