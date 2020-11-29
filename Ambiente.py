from Agente import *
import random

ListBebes=[]
ListRobots=[]

N=0
M=0

CasillasSucias=0
CasillasObstaculos=0
CantN=0


def Rango(x,y,n,m):
    if(x>=0 and x<n and y>=0 and y<m):
        return True
    else: return False
    
def EmpujarObstaculo(xdes,ydes,xobs,yobs,habitacion):
    #print("x:"+str(xobs)+" xdes:"+str(xdes))
    #print("y:"+str(yobs)+" ydes:"+str(ydes))
    if(Rango(xobs+xdes,yobs+ydes,len(habitacion),len(habitacion[0]))==False):
        return False
    elif(habitacion[xobs+xdes][yobs+ydes]==0):
        habitacion[xobs+xdes][yobs+ydes]=3
        return True
    #return False
    elif(habitacion[xobs+xdes][yobs+ydes]==3):
        return EmpujarObstaculo(xdes,ydes,xobs+xdes,yobs+ydes,habitacion)
    
    return False
    #    if pude==False:
    #        return False
    #    else:
    #        habitacion[xobs+xdes][yobs+ydes]=3
    #        return True    

def BuscaAdyacentes(xpos,ypos,n,m):
    devolver=[]
    if(Rango(xpos-1,ypos,n,m)):
        devolver.append((xpos-1,ypos))
    if(Rango(xpos+1,ypos,n,m)):
        devolver.append((xpos+1,ypos))
    if(Rango(xpos,ypos+1,n,m)):
        devolver.append((xpos,ypos+1))
    if(Rango(xpos,ypos-1,n,m)):
        devolver.append((xpos,ypos-1))
    return devolver

def CasillaAMoverte(x,y,habitacion,soybb,n,m):
    posiblesCasillas=[]
    posiblesMov=BuscaAdyacentes(x,y,n,m)
    #print(posiblesMov)
    if(soybb==False):
        for item in posiblesMov:
            if habitacion[item[0]][item[1]]==3:
                posiblesMov.remove(item)
        if len(posiblesMov)!=0:
            item=random.sample(posiblesMov,1)[0]
            return item[0],item[1]
        else: return (-1,-1)
    
    else:
        for item in posiblesMov:
            if(habitacion[item[0]][item[1]]==1 or habitacion[item[0]][item[1]]==2 or HayBB(ListRobots,item[0],item[1]) or HayBB(ListBebes,item[0],item[1])):
                posiblesMov.remove(item)
        if len(posiblesMov)==0:
            return(-1,-1)
        else:
            item=random.sample(posiblesMov,1)[0]
            if habitacion[item[0]][item[1]]==0:
                return item
            else:
                xdes=item[0]-x
                ydes=item[1]-y
                pude=EmpujarObstaculo(xdes,ydes,item[0],item[1],habitacion)
                if pude==False:
                    return (-1,-1)
                habitacion[item[0]][item[1]]=0
                return item

def HayBB(listb,x,y):
    for i in listb:
        if i.X==x and i.Y==y:
            return True
    return False

def DameBB(listb,x,y):
    for i in listb:
        if i.X==x and i.Y==y:
            return i

def AccionRobot(robot,habitacion,n,m,cantm):    
    if habitacion[robot.X][robot.Y]==1:
        #Independientemente d cualkiercosa si el robot esta en una casilla sucia la accion a realizar
        #es limpiarla
        habitacion[robot.X][robot.Y]=robot.Limpia()

    else:
        xnew,ynew=CasillaAMoverte(robot.X,robot.Y,habitacion,False,n,m)
        #xnew,ynew=OtroMov(robot,habitacion,n,m)
        if(xnew!=-1):
            if(habitacion[xnew][ynew]==2 and robot.Bebe!=0 and HayBB(ListBebes,xnew,ynew)==False):
                #El robot entra a una casilla corral y deja al bb
                robot.X=xnew
                robot.Y=ynew
                bb=robot.Bebe
                bb.X=xnew
                bb.Y=ynew
                bb.MeTieneUnRobot=0
                robot.Bebe=0
                bb.EstoyCorral=True
                robot.Tengobb=False
           
            elif(HayBB(ListBebes,xnew,ynew)==True and robot.Bebe==0 and habitacion[xnew][ynew]!=2 ):
                #Aqui se esta haciendo la accion de moverte a la casilla y cargar un bebe
                bb=DameBB(ListBebes,xnew,ynew)
                bb.MeTieneUnRobot=robot
                robot.Tengobb=True
                robot.X=xnew
                robot.Y=ynew
                robot.Bebe=bb

            elif(robot.Bebe!=0 and cantm==0):
                robot.X=xnew
                robot.Y=ynew
                robot.Bebe.X=xnew
                robot.Bebe.Y=ynew
                AccionRobot(robot,habitacion,n,m,cantm+1)


                #xotra,yotra=CasillaAMoverte(robot.X,robot.Y,habitacion,False,n,m)
            
            elif(habitacion[xnew][ynew]!=2):
                #Accion de simplemente moverse
                robot.X=xnew
                robot.Y=ynew

def OtroMov(robot,habitacion,n,m):
    posiblesMov=BuscaAdyacentes(robot.X,robot.Y,n,m)
    #print(posiblesMov)
    for item in posiblesMov:
        if habitacion[item[0]][item[1]]==3:
            posiblesMov.remove(item)
    for i in posiblesMov:
        if habitacion[i[0]][i[1]]==1:
            return i[0], i[1]
    if len(posiblesMov)!=0:
        item=random.sample(posiblesMov,1)[0]
        return item[0],item[1]
    else: return (-1,-1)


def AccionBebe(bebe,habitacion,n,m):
    if(bebe.MeTieneUnRobot!=0):
        #Si el bebe lo carga un robot entonces no hace nada
        return 
    else:
        xnew,ynew=CasillaAMoverte(bebe.X,bebe.Y,habitacion,True,n,m)
        #print(str(xnew)+" "+str(ynew))
        if(xnew==-1):
            return 
        x=random.randint(1,2)
        if x==1:
            #El bebe se movio de casilla
            bebe.X=xnew
            bebe.Y=ynew
            
        else:
            #El bebe ensucio
            habitacion[bebe.X][bebe.Y]=1
    
def SesentaPorCiento(todo):
    return (todo*6)/10

def VerificaSuciedadMax(habitacion,n,m):
    sucias=0
    for i in range(0,n):
        for j in range(0,m):
            if habitacion[i][j]==1:
                sucias+=1
    
    porciento=SesentaPorCiento(n*m)
    if(sucias<porciento):
        return False
    else:
        return True

def EstanBebesCorral(habitacion):
    for i in ListBebes:
        if habitacion[i.X][i.Y]!=2:
            return False
    return True

def HabitacionSucia(habitacion,n,m):
    cants=0
    for i in habitacion:
        if i==0:
            cants+=1
    
    if((n*m)-CasillasObstaculos-CantN==cants):
        return True
    return False


def GenerarAmbiente(n,m):
    habitacion=[]
    for i in range(0,n):
        habitacion.append([0 for n in range(0,m)])
    return habitacion

def LlenaHabitacion(habitacion,n,m,cantobs,cantsucias,cantcorral):
    corrales=cantcorral
    q=0
    while(corrales>0):
        habitacion[q][m-1]=2
        q+=1
        corrales-=1
    
    obstaculos=cantobs
    while(obstaculos>0):
        x=random.randint(0,n-1)
        y=random.randint(0,m-1)
        if(habitacion[x][y]==0):
            habitacion[x][y]=3
            obstaculos-=1

    sucias=cantsucias
    while(sucias>0):
        x=random.randint(0,n-1)
        y=random.randint(0,m-1)
       # print(x)
       # print(y)
        if(habitacion[x][y]==0):
            habitacion[x][y]=1
            sucias-=1
    
    return habitacion

def PonRobot(habitacion,n,m):
    
    posibles=[]
    for i in range(0,n):
        for j in range(0,m):
            if habitacion[i][j]==0:
               posibles.append((i,j)) 
    
    item=random.sample(posibles,1)[0]
    return item

def PonBebes(habitacion,n,m,cantbb,robot):
    posibles=[]
    for i in range(0,n):
        for j in range(0,m):
            if habitacion[i][j]==0:
                if(robot.X==i and robot.Y==j):
                    pass
                else:
                    posibles.append((i,j))     
    
    count=1
    bb=cantbb
    while(bb>0):
        item=random.sample(posibles,1)[0]
        B=Bebe(count,item[0],item[1])
        ListBebes.append(B)
        count+=1
        bb-=1
    


    

    






