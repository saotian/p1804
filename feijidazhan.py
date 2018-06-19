#coding=utf-8
import pygame
def main():
	screen = pygame.display.set_mode((400,500),0,23) #游戏窗口
	background = pygame.image.load('./images/background.png')#添加照片
	feiji = pygame.image.load('./images/plane.png')
	fj_daxiao = pygame.Rect((200-400)/2,350,100,124)
	clock = pygame.time.Clock()#获得游戏时钟
	while True:
		screen.blit(background,(0,0))#吧照片添加到游戏里
		screen.blit(feiji,fj_daxiao)
		fj_daxiao.x += 1
		if fj_daxiao.x > 400:
			fj_daxiao.x = 0
		pygame.display.update() #刷新显示
		clock.tick(60)#60/1秒　移动一次

if __name__ == "__main__":
	main()






