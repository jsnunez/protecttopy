import json
from os import system
with open('data.json') as file:
    data = json.load(file)
def mod_reg(i):

    with open('data.json') as file:
        data = json.load(file)        
        print("Ingrese los datos de la persona", i + 1)
        data.append({
        "id": input("id:"),
        "nombres" : input("Nombre: "),
        "Apellidos" : input ("Apellidos: "),
        "direccion" : input ("direccion: "),
        "acudiente" : input ("acudiente: "),
        "telefonos_celular" : input ("telefonos_celular: "),
        "telefonos_fijo" : input ("telefonos_fijo: "),
        "estado" :input("estado: "),
        "ruta":"" ,
        "notaskill1": -1,
        "pruebats": -1,
        "pruebaps": -1,
        "pruebatrs": -1,
        "rendimiento": "",
        "rutaasignada": 1,
        "notaskill2": 10,
        "notaskill3": -1,
        "notaskill4": -1,
        "notaskill5": -1
        
})
               
        with open('data.json', 'w') as file:
                json.dump(data, file)

        data =  open("data.json") 
        usuarios = json.load(data)

        for usuarios in usuarios:
            print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"],
                usuarios["estado"] )
        sig=input("desea ingresar un nuevo campers si o no")


        if sig=="si":
         x=1
        else:
           x=0                   
    return x   
    system("cls")                                  

def mod_prueba():
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
      
    for usuarios in usuarios:
        print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["estado"] )

    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
    seletuser=input("escriba id para agregar notas: ")
    for usuarios in usuarios:

 
        if seletuser == usuarios["id"] and "inscrito" ==usuarios["estado"]:
            usuarios["notat"]=input("ingrese nota teorica 0-100: ")
            usuarios["notap"]=input("ingrese nota practica 0-100: ")
            promedionota=(int(usuarios["notat"])+int(usuarios["notap"]))/2
            if promedionota>=60:
                usuarios["estado"]="aprobado"
            if promedionota<60:
                usuarios["estado"]="reprobado"
        if seletuser == usuarios["id"] and "aprobado" ==usuarios["estado"]:    
               print("el usuario se encuentra aprobado")
        
        data1.append(usuarios)

        
    with open('data.json', 'w') as file:
        json.dump(data1, file)


    sig=input("desea ingresar un nueva nota campers si o no: ")
    if sig=="si":
        x=3
    else:
        x=0    
    return x
    system("cls")   
        
def mod_cruta():
    data =  open("rutas.json") 
    rutas = json.load(data)
    x=0
   
    i=len(rutas)
    print(rutas)
    crear=input("Desea crear una nueva ruta de entrenamiento si o no: ")
    if crear=="si":
     with open('rutas.json') as file:
        data = json.load(file)        
        print("Ingrese los datos de ruta", i + 1)
        data.append({
        "id":i+1,
        "Fundamentos de programación" : input("Fundamentos de programación: "),
        "programación Web" : input ("programación Web: "),
        "programación formal" : input ("programación formal: "),
        "Bases de datos" : input ("Bases de datos SGDB principa: "),
        "Backend": input ("Backend: ")

})       
        with open('rutas.json', 'w') as file:
                json.dump(data, file)
        sig=input("desea ingresar un nueva ruta si o no")


        if sig=="si":
         x=5
        else:
         x=0   
    system("cls")                     
    return x   

def mod_regr(rutas):
    i=0
    ban=0
    ban1=0
    ruta=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
        print("seleccione modo de  registras campers")
        print("1) automaticos")
        print("2) manual")
        print("3) salir")
        modo=input("escriba 1 o 2 o 3: ")  
    if modo=="1" :
        with open('data.json') as file:
            data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
        for usuarios in usuarios:
            if "aprobado" ==usuarios["estado"]:
                i=i+1
                if i<=33:
                    usuarios["ruta"]=  rutas[0] 
                elif i<=66:
                    usuarios["ruta"]=  rutas[1]   
                elif i<=99:
                    usuarios["ruta"]=  rutas[2]  
                elif i<=132:
                    usuarios["ruta"]=  rutas[3]   
                elif i<=165:
                    usuarios["ruta"]=  rutas[4] 
                elif i<=198:
                    usuarios["ruta"]=  rutas[5]   
                elif i<=231:
                    usuarios["ruta"]=  rutas[6] 
                elif i<=264:
                    usuarios["ruta"]=  rutas[7]   
                elif i<=297:
                    usuarios["ruta"]=  rutas[8] 
                elif i<=330:
                    usuarios["ruta"]=  rutas[9]   
                elif i<=363:
                    usuarios["ruta"]=  rutas[10] 
                elif i<=396:
                    usuarios["ruta"]=  rutas[11]  
            else:
                    usuarios["ruta"]=  []  
            data1.append(usuarios)

    if modo=="2":
        
        with open('data.json') as file:
            data = json.load(file)
            data =  open("data.json") 
            usuarios = json.load(data)
            data1 = []
        for usuarios in usuarios:
            print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"],
                usuarios["estado"],
                usuarios["ruta"])
            
            cantruta=usuarios["ruta"]
            if cantruta==rutas[0]:
                ruta[0]=ruta[0]+1
            if usuarios["ruta"]==rutas[1]:
                ruta[1]=ruta[1]+1                   
            if usuarios["ruta"]==rutas[2]:
                ruta[2]=ruta[2]+1
            if usuarios["ruta"]==rutas[3]:
                ruta[3]=ruta[3]+1
            if usuarios["ruta"]==rutas[4]:
                ruta[4]=ruta[4]+1                    
            if usuarios["ruta"]==rutas[5]:
                ruta[5]=ruta[5]+1
            if usuarios["ruta"]==rutas[6]:
                ruta[6]=ruta[6]+1
            if usuarios["ruta"]==rutas[7]:
                ruta[7]=ruta[7]+1                     
            if usuarios["ruta"]==rutas[8]:
                ruta[8]=ruta[8]+1 
            if usuarios["ruta"]==rutas[9]:
                ruta[9]=ruta[9]+1
            if usuarios["ruta"]==rutas[10]:
                ruta[10]=ruta[10]+1                    
            if usuarios["ruta"]==rutas[11]:
                ruta[11]=ruta[11]+1
        print("cantidad de campers por ruta")
        seletuser=int(input("escriba id para seleccionar ruta: "))
        for x in range(0,12): 
            print(rutas[x], " : ",ruta[x])
            

          
        selecruta=int(input("escriba ruta: "))
        with open('data.json') as file:
            data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        for usuarios in usuarios:
            if seletuser == int(usuarios["id"]) and usuarios["estado"]=="aprobado" and ruta[selecruta-1]<33:
                usuarios["ruta"]=  rutas[selecruta-1]
                ban=1
                print("se asigno al la ruta",usuarios["ruta"])
            data1.append(usuarios)  

            if ruta[selecruta-1]==33 :
                ban1=1
                ban=1
        
        if ban1==1: 
            print("ruta llena seleccione otra ruta")
            
        if ban==0:
             print("no se encontro usurario o no aprobo examen inicio") 

    
        
    with open('data.json', 'w') as file:
        json.dump(data1, file)
    input("oprima enter para continuar")
    system("cls")   

def mod_entrena(rutas):
    
    with open('docente.json') as file:
        data = json.load(file)
        data =  open("docente.json") 
        usuarios = json.load(data)
        data1 = []
    for usuarios in usuarios:
            print("Nombre del docente:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                "horario",
                usuarios["horario"],"-",usuarios["horario"]+8
                        )
    x= input("Desea asigar grupo  a entrenador si o no: ")
    if x=="si":
        id=int(input("ingrese id del docente"))


        with open('docente.json') as file:
            data = json.load(file)
            data =  open("docente.json") 
            usuarios = json.load(data)
            data1 = []
        for usuarios in usuarios:
            if id == int(usuarios["id"]) :
                if  usuarios["horario"]==6:
                    rutah=int(input("seleccione ruta 6 am 1) Ruta NodeJS  2) Ruta Java 3) Ruta NetCore : "))
                    usuarios["ruta0"]=  rutas[rutah-1]
                    grupo2=int(input("seleccione ruta 10 am 1) Ruta NodeJS  2) Ruta Java 3) Ruta NetCore : "))
                    usuarios["ruta1"]=  rutas[grupo2+2]
                    print(usuarios) 
                if  usuarios["horario"]==14:
                    rutah=int(input("seleccione ruta 2 pm 1) Ruta NodeJS  2) Ruta Java 3) Ruta NetCore : "))
                    usuarios["ruta0"]=  rutas[rutah+5]
                    grupo2=int(input("seleccione ruta 6 pm 1) Ruta NodeJS  2) Ruta Java 3) Ruta NetCore : "))
                    usuarios["ruta1"]=  rutas[grupo2+8]
                    print(usuarios)                  
            data1.append(usuarios)               
        with open('docente.json', 'w') as file:
            json.dump(data1, file)
    system("cls")              

def mod_asignacion():
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios1 = json.load(data)
        data1 = []
    with open('rutas.json') as file:
        rut = json.load(file)
        rut =  open("rutas.json") 
        rutuser1 = json.load(rut)

      
    for usuarios in usuarios1:
        print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["estado"] )    
    

    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
    seletuser=int(input("escriba id del usuario para agregar rutas: ")  )
    
    for rutuser in rutuser1:
        print("rutas:",
            rutuser["id"] ,         
            rutuser["Fundamentos de programaci\u00f3n"],
            rutuser["programaci\u00f3n Web"],
            rutuser["programaci\u00f3n formal"],
            rutuser["Bases de datos"],
            rutuser["Backend"] )  
    selectrut=int(input("escriba id de ruta para agregar al usuario: ")  )
    
    for usuarios in usuarios:
        if int(usuarios["id"])==seletuser:
            usuarios["rutaasignada"]=selectrut
        data1.append(usuarios)        
    with open('data.json', 'w') as file:
        json.dump(data1, file)
    system("cls")   
                             
def mod_matricula(salones,rutas):
    flag=0
    ruta=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
      
    for usuarios in usuarios:
        print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["estado"] )
    with open('docente.json') as file:
        datad = json.load(file)
        datad =  open("docente.json") 
        usuariosd = json.load(datad)        
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
    seletuser=int(input("escriba id para modificar: "))
    for usuarios in usuarios:   
        cantruta=usuarios["ruta"]
        if cantruta==rutas[0]:
                ruta[0]=ruta[0]+1
        if usuarios["ruta"]==rutas[1]:
                ruta[1]=ruta[1]+1                   
        if usuarios["ruta"]==rutas[2]:
                ruta[2]=ruta[2]+1
        if usuarios["ruta"]==rutas[3]:
                ruta[3]=ruta[3]+1
        if usuarios["ruta"]==rutas[4]:
                ruta[4]=ruta[4]+1                    
        if usuarios["ruta"]==rutas[5]:
                ruta[5]=ruta[5]+1
        if usuarios["ruta"]==rutas[6]:
                ruta[6]=ruta[6]+1
        if usuarios["ruta"]==rutas[7]:
                ruta[7]=ruta[7]+1                     
        if usuarios["ruta"]==rutas[8]:
                ruta[8]=ruta[8]+1 
        if usuarios["ruta"]==rutas[9]:
                ruta[9]=ruta[9]+1
        if usuarios["ruta"]==rutas[10]:
                ruta[10]=ruta[10]+1                    
        if usuarios["ruta"]==rutas[11]:
                ruta[11]=ruta[11]+1        
        if seletuser == int(usuarios["id"]) and usuarios["estado"]== "aprobado":

            for usuariosd in usuariosd:
                print(usuariosd["id"],usuariosd["nombres"])
            with open('docente.json') as file:
                datad = json.load(file)
                datad =  open("docente.json") 
                usuariosd = json.load(datad) 
            experto=int(input("seleccionar experto"))
            
            for usuariosd in usuariosd:
                if usuariosd["id"]==experto:
                    usuarios["experto"]=usuariosd["nombres"] 
                    print(usuarios["experto"])
                    print(usuariosd["ruta0"],ruta[experto-1])  
                    print(usuariosd["ruta1"],ruta[experto+2])
                    rsel=int(input("seleccione horario") )                    
                    flag=1
                    if  ruta[experto-1]< 33 and (rsel== 1 or rsel== 2 or rsel== 3 or rsel== 7 or rsel== 8 or rsel== 9) :

                        sal=int(input( "seleccione salon segun Ruta NodeJS 1) artemisa, Ruta Java 2)spunik, Ruta NetCore 3)apolo"))
                        usuarios["salon"]=salones[sal-1]
                        usuarios["ruta"]=rutas[rsel-1] 
                        usuarios["inicio"]=input("ingrese fecha de inicio dd/mm/aaaa :")
                        usuarios["fin"]=input("ingrese fecha de finalizacion dd/mm/aaaa :")
                       
                    elif  ruta[experto+2]< 33 and (rsel== 4 or rsel== 5 or rsel== 6 or rsel== 10 or rsel== 11 or rsel== 12) :

                        sal=int(input( "seleccione salon segun Ruta NodeJS 1) artemisa, Ruta Java 2)spunik, Ruta NetCore 3)apolo"))
                        usuarios["salon"]=salones[sal-1]
                        usuarios["ruta"]=rutas[rsel-1] 
                        usuarios["inicio"]=input("ingrese fecha de inicio dd/mm/aaaa :")
                        usuarios["fin"]=input("ingrese fecha de finalizacion dd/mm/aaaa :")
     
                    elif  ruta[experto-1]== 33 and (rsel== 1 or rsel== 2 or rsel== 3 or rsel== 7 or rsel== 8 or rsel== 9) :
                        print("el grupo esta lleno") 
                        input("oprima enter para continuar")
                    elif  ruta[experto+2]==33 and (rsel== 4 or rsel== 5 or rsel== 6 or rsel== 10 or rsel== 11 or rsel== 12) :
                        print("el grupo esta lleno") 
                        input("oprima enter para continuar")   
              
        data1.append(usuarios)   
    if flag==0: 
            print("no se encontro camper o se encunetra reprobado")
            input("oprima enter para continuar")       
              
 
        
    with open('data.json', 'w') as file:
        json.dump(data1, file)                  
   

def mod_skill():
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
    with open('data.json') as file:
        rut = json.load(file)
        rut =  open("rutas.json") 
        rutuser = json.load(rut)   
          
    for usuarios in usuarios:
        print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["estado"] )
    seletuser=int(input("escriba id para evaluar: "))
    print(        
            "1) Fundamentos de programaci\u00f3n",'\n'
            "2) programaci\u00f3n Web",'\n'
            "3) programaci\u00f3n formal",'\n'
            "4) Bases de datos",'\n'
            "5) Backend")  
    seletskill=int(input("selecionar skill a evaluar: "))   
    
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
    for usuarios in usuarios:

        if seletuser == int(usuarios["id"]) and "aprobado"==usuarios["estado"]:
            usuarios["pruebats"]=int(input("ingrese nota teorica"))
            usuarios["pruebaps"]=int(input("ingrese nota practica"))
            usuarios["pruebatrs"]=int(input("ingrese nota trabajos"))
            nota=usuarios["pruebats"]*.3+usuarios["pruebaps"]*.6+usuarios["pruebatrs"]*.1
            if seletuser==1:             
                usuarios["notaskill1"]=nota
            if seletuser==2:             
                usuarios["notaskill2"]=nota
            if seletuser==3:             
                usuarios["notaskill3"]=nota
            if seletuser==4:             
                usuarios["notaskill4"]=nota                                
            if seletuser==5:             
                usuarios["notaskill5"]=nota
            if nota<60:
                usuarios["rendimiento"]="bajo"
                print("rendimiento bajo")
            else: 
                usuarios["rendimiento"]="paso"
                print("paso examen, nota:",nota)
        
        data1.append(usuarios)   
    input("opriam enter para continuar")    
    with open('data.json', 'w') as file:
        json.dump(data1, file)       
    system("cls")   

def mod_riesgo():
    with open('data.json') as file:
        data = json.load(file)
        data =  open("data.json") 
        usuarios = json.load(data)
        data1 = []
      
    for usuarios in usuarios:
        if usuarios["rendimiento"]=="bajo": 
            print("Nombre del usuario:",
            usuarios["id"] ,         
            usuarios["nombres"],
            usuarios["Apellidos"],
            usuarios["direccion"],
            usuarios["acudiente"],
            usuarios["rendimiento"])    
    input("estos campers tienen rendimiento bajo, oprima enter para continuar")         
    system("cls")   

def mod_listar():
              
    print(f"a. Listar los campers que se encuentren en estado de inscrito",'\n'
            "b. Listar los campers que aprobaron el examen inicial", '\n'
            "c. Listar los entrenadores que se encuentran trabajando con campuslands.", '\n'
            "d. Listar los estudiantes que cuentan con bajo rendimiento.", '\n'
            "e. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.", '\n'
            "f. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado."       )
    x=input("seleccione opcion:" )
    with open('data.json') as file:
            data = json.load(file)
            data =  open("data.json") 
            usuarios = json.load(data)
            data1 = []
    with open('docente.json') as file:
            datad = json.load(file)
            datad =  open("docente.json") 
            usuariosd = json.load(datad)
            data1 = []
    if x=="a" :
        for usuarios in usuarios:
            if usuarios["estado"]=="inscrito": 
                print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"])
        input("campers inscritos oprima enter para continuar")

    if x=="b" :
        for usuarios in usuarios:
            if usuarios["estado"]=="aprobado": 
                print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"],
                usuarios["rendimiento"]) 
        input("campers aprobaron examen inicial oprima enter para continuar")
 
    if x=="c" :
        for usuariosd in usuariosd:
            print("Nombre del docente:",
                usuariosd["id"] ,         
                usuariosd["nombres"],
                usuariosd["Apellidos"],
                "horario",
                usuariosd["horario"],
                        )  
        input("docentes campus oprima enter para continuar")
     
    if x=="d":
        for usuarios in usuarios: 
            if usuarios["rendimiento"]=="bajo": 
                print("Nombre del usuario:",
                usuarios["id"] ,         
                usuarios["nombres"],
                usuarios["Apellidos"],
                usuarios["direccion"],
                usuarios["acudiente"],
                usuarios["notaskill1"],
                usuarios["rendimiento"]) 
        input("campers con rendimiento bajo oprima enter para continuar")
    if x=="e":
        for usuariosd in usuariosd:
                print("Nombre del docente:",
                     usuariosd["id"] ,         
                     usuariosd["nombres"],
                     usuariosd["Apellidos"] )

                for usuarios in usuarios:

                    if usuariosd["ruta0"]==usuarios["ruta"]:
                        print("Nombre del camper:",
                        usuarios["id"] ,         
                        usuarios["nombres"],
                        usuarios["Apellidos"],
                        usuariosd["ruta0"])
                    if usuariosd["ruta1"]==usuarios["ruta"]:
                        print("hola")
                        print("Nombre del camper:",
                        usuarios["id"] ,         
                        usuarios["nombres"],
                        usuarios["Apellidos"],
                        usuariosd["ruta1"])
                with open('data.json') as file:
                        data = json.load(file)
                        data =  open("data.json") 
                        usuarios = json.load(data)
        input("esta es la lista de campers con entrenador y ruta asignada, oprima enter para continuar")                                                 
    if x=="f":
        for usuario in usuariosd:
                skill1=0
                skill2=0
                skill3=0
                skill4=0
                skill5=0              
                print("Nombre del docente:",
                     usuario["id"] ,         
                     usuario["nombres"],
                     usuario["Apellidos"] ) 
                print(usuario["ruta0"])
                for usuarios1 in usuarios:
                    if usuario["ruta0"]==usuarios1["ruta"]:    
                        if usuarios1["notaskill1"]<60 and usuarios1["notaskill1"]>=0 :
                            skill1=skill1+1
                        if usuarios1["notaskill2"]<60 and usuarios1["notaskill2"]>=0 :
                            skill1=skill2+1                        
                        if usuarios1["notaskill3"]<60 and usuarios1["notaskill3"]>=0 :
                            skill1=skill3+1
                        if usuarios1["notaskill4"]<60 and usuarios1["notaskill4"]>=0 :
                            skill1=skill4+1                               
                        if usuarios1["notaskill5"]<60 and usuarios1["notaskill5"]>=0 :
                            skill1=skill5+1
                print("perdieron skilll : ",skill1)            
                print("perdieron skill2 : ",skill2)            
                print("perdieron skill3 : ",skill3)            
                print("perdieron skill4 : ",skill4)            
                print("perdieron skill5 : ",skill5)            
                for usuarios1 in usuarios:
                    if usuario["ruta1"]==usuarios1["ruta"]:    
                        if usuarios1["notaskill1"]<60 and usuarios1["notaskill1"]>=0 :
                            skill1=skill1+1
                        if usuarios1["notaskill2"]<60 and usuarios1["notaskill2"]>=0 :
                            skill1=skill2+1                        
                        if usuarios1["notaskill3"]<60 and usuarios1["notaskill3"]>=0 :
                            skill1=skill3+1
                        if usuarios1["notaskill4"]<60 and usuarios1["notaskill4"]>=0 :
                            skill1=skill4+1                               
                        if usuarios1["notaskill5"]<60 and usuarios1["notaskill5"]>=0 :
                            skill1=skill5+1
                print(usuario["ruta1"])
                print("perdieron skilll : ",skill1)            
                print("perdieron skill2 : ",skill2)            
                print("perdieron skill3 : ",skill3)            
                print("perdieron skill4 : ",skill4)            
                print("perdieron skill5 : ",skill5)            
        for usuario in usuariosd:
                skill1=0
                skill2=0
                skill3=0
                skill4=0
                skill5=0 
                print("Nombre del docente:",
                     usuario["id"] ,         
                     usuario["nombres"],
                     usuario["Apellidos"] ) 
                print(usuario["ruta0"]) 
                for usuarios1 in usuarios:
                    if usuario["ruta0"]==usuarios1["ruta"]:    
                        if usuarios1["notaskill1"]>=60  :
                            skill1=skill1+1
                        if usuarios1["notaskill2"]>=60 :
                            skill1=skill2+1                        
                        if usuarios1["notaskill3"]>=60 :
                            skill1=skill3+1
                        if usuarios1["notaskill4"]>=60 :
                            skill1=skill4+1                               
                        if usuarios1["notaskill5"]>=60 :
                            skill1=skill5+1
                print("pasaron skill1 : ",skill1)            
                print("pasaron skill2 : ",skill2)            
                print("pasaron skill3 : ",skill3)            
                print("pasaron skill4 : ",skill4)            
                print("pasaron skill5 : ",skill5)            
                for usuarios1 in usuarios:
                    if usuario["ruta1"]==usuarios1["ruta"]:    
                        if usuarios1["notaskill1"]>=60  :
                            skill1=skill1+1
                        if usuarios1["notaskill2"]>=60 :
                            skill1=skill2+1                        
                        if usuarios1["notaskill3"]>=60 :
                            skill1=skill3+1
                        if usuarios1["notaskill4"]>=60 :
                            skill1=skill4+1                               
                        if usuarios1["notaskill5"]>=60 :
                            skill1=skill5+1
                print(usuario["ruta1"])
                print("pasaron skill1 : ",skill1)            
                print("pasaron skill2 : ",skill2)            
                print("pasaron skill3 : ",skill3)            
                print("pasaron skill4 : ",skill4)            
                print("pasaron skill5 : ",skill5)    
        input("oprima enter para continuar")                                      
    system("cls")   

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            print(enunciando,inferior,superior)
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")