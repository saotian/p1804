import pygame
import time
import random
from random import randint
pygame.init()
class Plane(object):#飞机的父类
    def __init__(self,lujing,screen,x,y):

        self.lujing=lujing
        self.screen=screen
        self.x=x
        self.y=y
        self.width=22
        self.height=22
        self.feiji1=pygame.image.load(self.lujing)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.flag="right"
        self.bulletlist=[]
        self.score=0
    def display(self):
        self.screen.blit(self.feiji1,self.rect)
        for i in self.bulletlist:
            if i.xiaoshi():
                self.bulletlist.remove(i)

            i.display()
            i.mv()

