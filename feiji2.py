#coding=utf-8
import pygame
import random
class EnemyPlane(object):
	def __init__(self,img_path,screen):
		self.screen = screen
		self.x = 0
		self.y = 0
		self.w = 10
		self.h = 12
		self.img_path = img_path
		self.plane = pygame.image.load(self.img_path)
		self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
		self.bullet_list = []
		self.flag = "right"
	def display(self):
		self.screen.blit(self.plane,self.rect)
		self.move()
		num = random.randint(1,100)
		if num == 1:
			self.fire()
		for i in self.bullet_list:
			if i.judge():
				self.bullet_list.remove(i)
			i.display()
			i.move()


	def move(self):
		if self.flag == "right":
			self.rect.x += 2
		else:
			self.rect.x -= 2
		if self.rect.x > 400 - self.rect.width:
			self.flag = "left"
		elif self.rect.x <= 0:
			self.flag = "right"
	def fire(self):
		self.bullet_list.append(EnemyBullet("./images/bullet1.png",self.screen,self.rect.x,self.rect.y))
class EnemyBullet(object):
	def __init__(self,img_path,screen,x,y):
		self.screen = screen
		self.x = x+40
		self.y = y-40
		self.img_path = img_path
		self.bullet = pygame.image.load(self.img_path)
	def display(self):
		self.screen.blit(self.bullet,(self.x,self.y))
	def move(self):
		self.y += 5
	def judge(self):
		if self.y > 500:
			return True
		else:
			return False



class HeroPlane(object):
	def __init__(self,img_path,screen):
		self.screen = screen
		self.x = (400-200)/2
		self.y = 350
		self.w = 200
		self.h = 200
		self.img_path = img_path
		self.hero_plane = pygame.image.load(self.img_path)
		self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
		self.bullet_list = []

	def display(self):
		self.screen.blit(self.hero_plane,self.rect)
		for i in self.bullet_list:
			if i.judge():
				self.bullet_list.remove(i)
			i.display()
			i.move()

	def fire(self):
		self.bullet_list.append(Bullet("./images/bullet.png",self.screen,self.rect.x,self.rect.y))		
class Bullet(object):
	def __init__(self,img_path,screen,x,y):
		self.screen = screen
		self.x = x+40
		self.y = y-40
		self.img_path = img_path
		self.bullet = pygame.image.load(self.img_path)
	def display(self):
		self.screen.blit(self.bullet,(self.x,self.y))
	def move(self):
		self.y -= 5
	def judge(self):
		if self.y < 0:
			return True
		else:
			return False


def key_control(hero,move_step):
	for event in pygame.event.get():#游戏事件的监听　控制`
		if event.type == pygame.QUIT:#退出游戏
			print("游戏退出")
			pygame.quit()
			exit()#(退出程序)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				hero.fire()
#	hero.fire()

	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
		hero.rect.x += move_step
	if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
		hero.rect.x -= move_step
	if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
		hero.rect.y -= move_step
	if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
		hero.rect.y += move_step
	if hero.rect.x < 0:
		hero.rect.x = 0
	if hero.rect.x > 300:
		hero.rect.x = 300
	if hero.rect.y < 0:
		hero.rect.y = 0
	if hero.rect.y > 380:
		hero.rect.y = 380


def main():
	screen = pygame.display.set_mode((400,500),0,23) #游戏窗口
	background = pygame.image.load('./images/background.png')#添加照片
	hero = HeroPlane("./images/hero2.png",screen)
	enemy_hero = EnemyPlane("./images/enemy1.png",screen)
	clock = pygame.time.Clock()#获得游戏时钟
	move_step = 15
	while True:
		screen.blit(background,(0,0))#吧照片添加到游戏里
		hero.display()
		enemy_hero.display()
		key_control(hero,move_step)	

		pygame.display.update() #刷新显示
		clock.tick(60)#60/1秒　移动一次
if __name__ == "__main__":
	main()






