import pygame
from pygame.constants import K_LEFT, K_RIGHT, KEYUP
import random, math

def main():

    #initialize pygame
    pygame.init()

    #title and icon
    pygame.display.set_caption("Snow Ninja")    
    logo = pygame.image.load("ninja.png")
    pygame.display.set_icon(logo)

    #creating the screen with the height and width of 600
    screen = pygame.display.set_mode((600,600))
    bg = pygame.image.load("backdrop.png")

    #creating a snow ninja (snowman object)
    snowmanImg = pygame.image.load("snowman.png")
    snowmanX = 2 #this was changed
    snowmanY = 480 
    snowmanChange = 0.5

    #creating a snowflake    
    snowflakeImg = pygame.image.load("snowflakes.png")
    snowflakeX = random.randint(2, 585)
    snowflakeY = 30
    snowflakeChange = 0.8

    #creating score text
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    def isCollision(fx,fy,sx,sy):
        distance = math.sqrt(math.pow((sx-fx),2)+math.pow((fy-sy),2))
        if distance < 20:
            return True
        else:
            return False

    score_value = 0

    def snowman(x,y):
        screen.blit(snowmanImg, (x, y))  
    
    def snowflake(x,y):
        screen.blit(snowflakeImg, (x, y)) 

    def show_score(x,y):
        score = font.render("Score : "+ str(score_value), True, (0,0,0))
        screen.blit(score, (x,y))

    running = True
    while running:
        #calling snowman on screen
        #snow_ninja.__init__()
        screen.blit(bg, (0, 0))

        #checking for the status of all the events
        for event in pygame.event.get():                   

            #check if the "Close" button has been pressed
            if event.type == pygame.QUIT:
                running = False  #stops the game  

            #updating x and y position of snowman    
            if event.type == pygame.KEYDOWN:
                #checking if left key or "a" is pressed
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #changing X coordinate of snowman by 0.1 towards left
                    snowmanChange = -0.5
                #checking if right key or "d" is pressed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_b:
                    #changing X coordinate of snowman by 0.1 towards Right
                    snowmanChange = 0.5
            if event.type == pygame.KEYUP:
                snowmanChange = 0

        snowmanX += snowmanChange
        snowflakeY += snowflakeChange

        #keep snowman on screen
        if snowmanX < 0:
            snowmanX = 0
        elif snowmanX > 568:
            snowmanX = 568

        #make snowflake disappear 
        if snowflakeY >550:
            snowflakeY = 620

        #calling snowflake 
        snowflake(snowflakeX, snowflakeY)
        
        #displaying snowman
        snowman(snowmanX, snowmanY)  

        show_score(textX, textY)

        collision = isCollision(snowflakeX, snowflakeY, snowmanX, snowmanY)    
        if collision:
            score_value += 1

        #displaying everything on the screen
        pygame.display.flip()

        #updating the display
        pygame.display.update()


if __name__ == "__main__":
    main()
    
    
