# Uchi-robochi
## Objetivos

## Funcionalidades de servicio

1. Administrar usuarios ✔
2. Asignar raspberrys a los usuarios ✔
3. Eliminar raspberrys ✔
4. Crear/Listar/Asocio los dispositivos con un relé (relay) ✔ 
   1. Validar que no se repita el nombre del puerto por cada raspberry ✔
5. Listar las acciones (Regar, prender luz (Iluminacion), apagar luz, aire acondicionado...) ✔
   1. Prender/apagar un dispositvo electrico ✔
   
   actions model
   |description    | user     | raspeberry| relay     | status
   |---------------|----------|-----------|-----------|----------|
   | luz living    | LaBlonda | Raspy1    | luz living| [on|off] |
   | luz cuarto    | LaBlonda | Raspy1    | luz cuarto| [on|off] |

   2. Validaciones
      1. No repetir description por user, raspberry, relay, action ✔
      2. Agregar timeout a las acciones ✔
      3. Agregar schedule triggers para ejecutar una accion (@TheClarinet) respetando los timeouts

   3. Tests by @Rochimo

   4. TaskWorker: Agendar y controlar el tiempo de encendido/apagado de las acciones (@Rocío)

6. Programar acciones para los dispositivos

8. Alertas (definir disparadores) $$$ 
9.  Parental suicidal control
10. Redirigir la home a /pi_commander respetando el path de la app

## Funcionalidades empresarial/proyecto/de negocio

- Como le cobro
- caracteristicas servicio
...


Nota: Nadie hizo nada ☢