import pygame
import random
# initialize pygame
pygame.init()

# define width of screen
width = 2000
# define height of screen
height = 1200
screen_res = (width, height)

pygame.display.set_caption("Particle Sim")
screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 0, 0)
black = pygame.color.Color(0, 0, 0)

class particle:
    def __init__(self,canv_dims,screen) -> None:
        self.size = 20
        self.screen = screen
        self.color = pygame.color.Color(red)
        self.pos = [random.randint(0,canv_dims[0]), random.randint(0,canv_dims[1])]
        self.v = [random.uniform(-1,1),random.uniform(-1,1)]
        self.canv_dims = canv_dims
        self.particle_draw = pygame.draw.circle(
              surface=self.screen,
              color=self.color,
              center=self.pos,
              radius=self.size
        )


    def step(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        vcolor = min(360,abs(self.v[1]*20))

        self.color.hsla=(vcolor,100,50,1)
        if self.pos[0] > self.canv_dims[0] or self.pos[0] < 0:
            self.v[0]*=-1

        if self.pos[1] > self.canv_dims[1] or self.pos[1] < 0:
            self.v[1]*=-1
        
        self.v[1]+=.01
        self.v[0]*=.999
        self.v[1]*=.999

        if self.pos[0]<self.canv_dims[0]*.8 and self.pos[0]>self.canv_dims[0]*.2:
            self.v[1] = -1*self.pos[1]//self.canv_dims[1]

particles = []


particles.append(particle([width,height],screen))


# game loop
while True:
    if len(particles)<1000:
         particles.append(particle([width,height],screen))
      
    for part in particles:
        part.step()
	
    # event loop
    for event in pygame.event.get():
	    # check if a user wants to exit the game or not
	    if event.type == pygame.QUIT:
	        exit()

	# fill black color on screen
    screen.fill(black)

    for part in particles:
        pygame.draw.circle(surface=screen,
                        color = part.color,
                        center = [part.pos[0],part.pos[1]],
                        radius=part.size)
        

	
    pygame.display.flip()
