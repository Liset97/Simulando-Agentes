import random




class Robot:
    def __init__(self,id,coordXinit,coordYinit):
        self.Id=id
        self.X=coordXinit
        self.Y=coordYinit
        self.Bebe=0 
        self.Tengobb=False

    def Muevete(self,newx,newy):
        self.X=newx
        self.Y=newy
    
    def __name__(self):
        return "Robot "+str(self.Id)
    
    def Limpia(self):
        return 0
    
    def CargaBB(self,bebe):
        self.Bebe=bebe
        self.Tengobb=True
    
    def DejaBB(self):
        self.Tengobb=False
        b=self.Bebe
        self.Bebe=0
        return b


class Bebe:
    def __init__(self,ide,coordXinit,coordYinit):
        self.Id=ide
        self.X=coordXinit
        self.Y=coordYinit
        self.EstoyCorral=False
        self.MeTieneUnRobot=0
    
    def Muevete(self,newx,newy):
        self.X=newx
        self.Y=newy

    def Ensucia(self):
        return 1
    
    def MetidoEnCorral(self):
        self.EstoyCorral=True
    
    def CapturadoPorRobot(self,idr):
        self.MeTieneUnRobot=idr


