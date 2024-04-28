from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath, Vec3
def addAdditionalModel(self,ModelFile,scale,CoordX,CoordY,CoordZ,TextureFile,Yaw,Pitch,Rotation):
        new_obj = self.loader.loadModel(ModelFile) 
        new_obj.setScale(scale)
        new_obj.setColorScale(1.0,1.0,1.0,1.0)
        new_obj.reparentTo(self.render)
        new_obj.setPos(CoordX,CoordY,CoordZ)
        new_obj_tex = self.loader.loadTexture(TextureFile)
        new_obj.setTexture(new_obj_tex)
        new_obj.setHpr(Yaw,Pitch,Rotation)



#---------------------------------------------------------------------PLANET INIT---------------------------------------------------------------------
class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
        self.modelNode = self.model
#---------------------------------------------------------------------UNIVERSE INIT---------------------------------------------------------------------
class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
#---------------------------------------------------------------------DRONE INIT---------------------------------------------------------------------
class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)
#---------------------------------------------------------------------SPACESTATION INIT---------------------------------------------------------------------
class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)        
#---------------------------------------------------------------------SHIP INIT---------------------------------------------------------------------
class Ship(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)           
        
#---------------------------------------------------------------------PLAYER INIT---------------------------------------------------------------------
class Player(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.model = loader.loadModel(modelPath)
        self.model.reparentTo(parentNode)
        self.model.setPos(posVec)
        self.model.setScale(scaleVec)
        
        self.model.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.model.setTexture(tex, 1)    
        
# class MovementControls():    
#     def negX(self,keyDown):
#         if keyDown:
#             taskMgr.add(self.mvNegX, 'moveNegX')
#         else:
#             taskMgr.remove('moveNegX')
#             self.acceptOnce('arrow_left', self.negX, [1])
#             self.acceptOnce('arrow_left-up',self.negX,[0])
#     def mvNegX(self, task):
#         self.player.setX(self.player,-1)                  
#         return task.cont
#     def negY(self,keyDown):
#         if keyDown:
#             taskMgr.add(self.mvNegY, 'moveNegY')
#         else:
#             taskMgr.remove('moveNegY')
#             self.acceptOnce('arrow_down', self.negY, [1])
#             self.acceptOnce('arrow_down-up',self.negY,[0])
#     def mvNegY(self, task):
#         self.player.setY(self.player,-1)                  
#         return task.cont
#     def plusX(self,keyDown):
#         if keyDown:
#             taskMgr.add(self.mvPlusX, 'movePlusX')
#         else:
#             taskMgr.remove('movePlusX')
#             self.acceptOnce('arrow_right', self.plusX, [1])
#             self.acceptOnce('arrow_right-up',self.plusX,[0])
#     def mvPlusX(self, task):
#         self.player.setX(self.player,1)                  
#         return task.cont
#     def plusY(self,keyDown):
#         if keyDown:
#             taskMgr.add(self.mvPlusY, 'movePlusY')
#         else:
#             taskMgr.remove('movePlusY')
#             self.acceptOnce('arrow_up', self.plusY, [1])
#             self.acceptOnce('arrow_up-up',self.plusY,[0])      
#     def mvPlusY(self, task):
#         self.player.setY(self.player,1) 
#         return task.cont
        