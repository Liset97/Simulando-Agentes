from Agente import *
from Ambiente import *
import random


l=[0 for i in range(0,5)]
#print(l)

def main(n,m,obs,sucias,bebes,time):
    lista=GenerarAmbiente(n,m)
    newAmbiente=LlenaHabitacion(lista,n,m,obs,sucias,bebes)
    #print(newAmbiente)
    x,y=PonRobot(newAmbiente,n,m)
    Rob=Robot(1,x,y)
    ListRobots.append(Rob)
    PonBebes(newAmbiente,n,m,bebes,Rob)
   # print("El robot: "+str(Rob.Id)+" en la casilla: ("+str(Rob.X)+","+str(Rob.Y)+").")
   # for i in ListBebes:
   #     print("El bebe: "+str(i.Id)+" en la casilla: ("+str(i.X)+","+str(i.Y)+"). Estoy en corral: "+str(i.EstoyCorral))
    
    MeDespidieron=False
    RobotPerfect=False

    t1=time
    while t1>0:
        if t1!=time:
            lista=GenerarAmbiente(n,m)
            newAmbiente=LlenaHabitacion(lista,n,m,obs,sucias,bebes)
        t=100
        while(t>0):
            if(VerificaSuciedadMax(newAmbiente,n,m)):
                print("El Robot es despedido xq no cumplio su rol")
                MeDespidieron=True
                break
            if(EstanBebesCorral(newAmbiente)==True and HabitacionSucia(newAmbiente,n,m)==True):
                print("El Robot es la tiza, Hiso su trabajo a la perfeccion")
                RobotPerfect=True
                break
            AccionRobot(Rob,newAmbiente,n,m,0)
            for i in ListBebes:
                if i.EstoyCorral==False:
                    AccionBebe(i,newAmbiente,n,m)     
            t-=1
        if MeDespidieron==True or RobotPerfect==True:
            break
        #print(newAmbiente)
        
      #  print(newAmbiente)
        t1-=1
    cantsucias=0
    for i in range(n):
        for j in range(m):
            if newAmbiente[i][j]==1:
                cantsucias+=1
    

    cantncorral=0
    for i in ListBebes:
        if i.EstoyCorral==True:
            cantncorral+=1
    
    return cantsucias,MeDespidieron,RobotPerfect,cantncorral
    '''    
    print("-----------------------------------------")
    print("Han transcurrido "+str(100-t)+" instantes d tiempo")
    print("Al final todo queda:")
    print("El robot: "+str(Rob.Id)+" en la casilla: ("+str(Rob.X)+","+str(Rob.Y)+").")
    for i in ListBebes:
        print("El bebe: "+str(i.Id)+" en la casilla: ("+str(i.X)+","+str(i.Y)+"). Estoy en corral: "+str(i.EstoyCorral))
    print(newAmbiente)    
    '''


N=int(input('Introduce n: '))
M=int(input('Introduce m: '))
CasSucias=int(input('Introduce la cantidad de casillas sucias: '))
CasObstaculos=int(input('Introduce la cantidad de casillas obstaculos: '))
CantBebes=int(input('Introduce la cantidad de Bebes: '))
time=int(input('Introduce t: '))

simulaciones=30
cantsucias=0
despidos=0
perfecto=0
ninoscorral=0
while simulaciones>0:
    sucias,d,p,n=main(N,M,CasObstaculos,CasillasObstaculos,CantBebes,time)
    cantsucias+=sucias
    if d==True:
        despidos+=1
    if p==True:
        perfecto+=1
    ninoscorral+=n
    print("Cant de ninnos en corral: "+str(n))
    simulaciones-=1

print("Total de casillas sucias: "+str(cantsucias))
print("Total de despidos: "+str(despidos))
print("Total de perfectos: "+str(perfecto))
print(ninoscorral)




