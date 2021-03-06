#coding=utf-8
import pygame
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
		self.y -= 1


def key_control(hero,move_step):
	for event in pygame.event.get():#游戏事件的监听　控制`
		if event.type == pygame.QUIT:#退出游戏
			print("游戏退出")
			pygame.quit()
			exit()#(退出程序)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				hero.fire()
	hero.fire()

	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
		hero.rect.x += move_step
	if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
		hero.rect.x -= move_step
	if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
		hero.rect.y -= move_step
	if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
		hero.rect.y += move_step

def main():
	screen = pygame.display.set_mode((400,500),0,23) #游戏窗口
	background = pygame.image.load('./images/background.png')#添加照片
	hero = HeroPlane("./images/hero2.png",screen)
	clock = pygame.time.Clock()#获得游戏时钟
	move_step = 15
	while True:
		screen.blit(background,(0,0))#吧照片添加到游戏里
		hero.display()
		key_control(hero,move_step)	

		pygame.display.update() #刷新显示
		clock.tick(60)#60/1秒　移动一次
if __name__ == "__main__":
	main()






