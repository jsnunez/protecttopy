
import json
from commons.funciones import mod_reg,mod_regr,mod_prueba,mod_cruta,mod_entrena,mod_asignacion,validar_opcion,mod_matricula,mod_skill,mod_riesgo,mod_listar
with open('data.json') as file:
    data = json.load(file)
rutas=["1) Ruta NodeJS 6am", "2) Ruta Java 6am", "3) Ruta NetCore 6am",
       "4) Ruta NodeJS 10am", "5) Ruta Java 10am", "6) Ruta NetCore 10am",
       "7) Ruta NodeJS 2pm", "8) Ruta Java 2pm", "9) Ruta NetCore 2pm",
       "10) Ruta NodeJS 6pm", "11) Ruta Java 6pm", "12) Ruta NetCore 6pm"]
salones=["artemisa","apolo","spunik"]
from os import system

users=len(data)

while True:  

    print("1. Registro de campers")
    print("2. Registro ruta")
    print("3. Registro prueba")
    print("4. Creación de rutas de entrenamiento")
    print("5. asignacion de rutas de entrenamiento")
    print("6. asignacion de entrenadores")
    print("7. Gestor de matriculas")
    print("8. evaluacion campers")
    print("9. Estudiantes en riesgos")
    print("10. Modulo de reportes")
    print("11. salir")    
    x=validar_opcion("Opcion: ",1,12)

    while x==1:
            x=mod_reg(users)
    while x==2:
            x=mod_regr(rutas)        
    while x==3:
            x=mod_prueba()
    while x==4:
            x=mod_cruta()
    while x==5:
            x=mod_asignacion()
    while x==6:
            x=mod_entrena(rutas)   
    while x==7:
            x=mod_matricula(salones,rutas)   
    while x==8:
            x=mod_skill()
    while x==9:
            x=mod_riesgo()
    while x==10:
            x=mod_listar()
    if x==1:
            print("saliendo")
            break
