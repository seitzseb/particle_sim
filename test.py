import numpy as np
import cv2
import random

HEIGHT, WIDTH = 480,640


class particle:
    def __init__(self,canv_dims) -> None:
        self.size = 20
        self.pos = [random.randint(0,WIDTH), random.randint(0,HEIGHT)]
        self.v = [random.random(),random.random()]
        self.canv_dims = canv_dims

    def step(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        if self.pos[0] > self.canv_dims[0] or self.pos[0] < 0:
            self.v[0]*=-1

        if self.pos[1] > self.canv_dims[1] or self.pos[1] < 0:
            self.v[1]*=-1
        
        self.v[1]+=.01
        self.v[0]*=.999
        self.v[1]*=.999


particles = []
for i in range(500):
    particles.append(particle([WIDTH,HEIGHT]))



img = np.zeros((480,640,3),dtype='uint8')


while True:
    # Display the image
    cv2.imshow('a',img)
    k = cv2.waitKey(10)
    img = np.zeros((480,640,3),dtype='uint8')
    # Increment the position
    for part in particles:
        part.step()
        cv2.circle(img,(int(part.pos[0]),int(part.pos[1])),part.size,(255,0,0),-1)
    img = cv2.GaussianBlur(img,(51,51),25)
    if k != -1:
        break
cv2.destroyAllWindows()