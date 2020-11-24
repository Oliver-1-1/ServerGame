import pygame
import socket


q = int(input("1. Server 2. Client"))
if q == 1:
    ServerorNo = True
if q == 2:
    ServerorNo = False

if ServerorNo:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1236))
    s.listen(5)
if not ServerorNo:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1236))

pygame.init()
window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption(str(ServerorNo))
running = True

rect1 = pygame.Rect(50,50,50,50)
rect2 = pygame.Rect(100,100,50,50)
if ServerorNo:
    clientsocket, ipAdress = s.accept()
    print(ipAdress)
    clientsocket.send(bytes(rect1.center))
else:
    pos = s.recv(1024)
    print(pos)

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect1.move_ip(10,10)
                if ServerorNo:
                    clientsocket.send(bytes(rect1.center))
                    print(str(rect1.center))
    if not ServerorNo:
        pos = s.recv(1024)
        rect1.center = pos

    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,0), rect1)
    pygame.draw.rect(window, (255,0,0), rect2)
    pygame.display.flip()
    pygame.display.update()

s.close()
print("hi")