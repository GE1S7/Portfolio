import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True

color = (255,255,255)

#menu 
font_press = pygame.font.Font(None, 42)
font_title = pygame.font.Font(None, 64)


press_to_start = font_press.render("Naciśnij spację, aby rozpocząć.", True, color)
press_to_start_poss = press_to_start.get_rect(centerx=400,y=300)

title = font_title.render("P A L E T K I", True, color)
title_pos = title.get_rect(centerx=400, y=200)

#game screen

p1points = 0
p2points = 0
font_score = pygame.font.Font(None, 42)

p1score = font_score.render(f'{p1points}', True, color)
p1score_pos = p1score.get_rect(centerx = 600, y = 100)

p2score = font_score.render(f'{p2points}', True, color)
p2score_pos = p2score.get_rect(centerx = 200, y = 100)

player1 = pygame.Rect(20,250,15,75)
player1.center = [20, 250]

player2 = pygame.Rect(780,250,15,75)
player2.center = [780, 250]

ball = pygame.Rect(400,250,10,10)
x_ball = 400
y_ball = 250
ball.center = [x_ball,y_ball]

# the side towards which the ball goes
turn = 'right'
a = 0

menu = True


while running:
    if menu == True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
        screen.blit(press_to_start, press_to_start_poss)
        screen.blit(title,title_pos)
        pygame.display.flip()
    else:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        keys = pygame.key.get_pressed()

        
        #player1 movment
        if keys[pygame.K_w] and player1.top > 0:
            player1.top -= 5
        if keys[pygame.K_s] and player1.bottom < 500:
            player1.top += 5
        #player2 movement
        if keys[pygame.K_KP8] and player2.top > 0:
            player2.top -= 5
        if keys[pygame.K_KP2] and player2.bottom < 500:
            player2.top += 5
            
        #ball movement
            

        
        
        #collisions
        (x_ballcenterleft,y_ballcenterleft) = ball.midleft
        #the angle at which the ball bounces of the paddle is different depending on where it hits
        #right paddle
        if ball.colliderect(player2):
            if ball.midright[1] > player2.topleft[1] and ball.midright[1] < player2.topleft[1] + 15:
                a = -3
                turn = 'left'
            elif ball.midright[1] >= player2.topleft[1] + 15 and ball.midright[1] < player2.topleft[1] + 30:
                a = -1
                turn = 'left'
            elif ball.midright[1] >= player2.topleft[1] + 30 and ball.midright[1] < player2.topleft[1] + 45:
                a = 0
                turn = 'left'
            elif ball.midright[1] >= player2.topleft[1] + 45 and ball.midright[1] < player2.topleft[1] + 60:
                a = 1
                turn = 'left'
            elif ball.midright[1] >= player2.topleft[1] + 60 and ball.midright[1] < player2.topleft[1] + 75:
                a = 3
                turn = 'left'
            

        #left paddle
        if ball.colliderect(player1):
            if ball.midleft[1] > player1.topright[1] and ball.midleft[1] < player1.topright[1] + 15:
                a = -3
                turn = 'right'
            elif ball.midleft[1] >= player1.topright[1] + 15 and ball.midleft[1] < player1.topright[1] + 30:
                a = -1
                turn = 'right'
            elif ball.midleft[1] >= player1.topright[1] + 30 and ball.midleft[1] < player1.topright[1] + 45:
                a = 0
                turn = 'right'
            elif ball.midleft[1] >= player1.topright[1] + 45 and ball.midleft[1] < player1.topright[1] + 60:
                a = 1
                turn = 'right'
            elif ball.midleft[1] >= player1.topright[1] + 60 and ball.midleft[1] < player1.topright[1] + 75:
                a = 3
                turn = 'right'

    # mirror the angle it ball hits the top/bottom of the screen
        if ball.midtop[1] <= 0:
            a = a * -1

        if ball.midbottom[1] >= 500:
            a = a * -1

        # return the center if ball hits left/right side of the screen
        if ball.midright[0] <= -15:
            x_ball = 400
            y_ball = 255
            a = 0
            p1points += 1
            p1score = font_score.render(f'{p1points}', True, color)
        if ball.midleft[0] >= 815:
            x_ball = 400
            y_ball = 255
            a = 0
            p2points += 1
            p2score = font_score.render(f'{p2points}', True, color)

        if p2points >= 10 or p1points >= 10:
            menu = True

    #     

        if turn == 'right':
            x_ball += 5
        if turn == 'left':
            x_ball -= 5

        
        y_ball += a
        ball.center = [x_ball,y_ball]
        
        # ball movement left-right


        # mirror the angle if ball hits the top or the bottom
        
        pygame.draw.rect(screen, color, ball)
        pygame.draw.rect(screen, color, player1)
        pygame.draw.rect(screen, color, player2)
        
        screen.blit(p1score, p1score_pos)
        screen.blit(p2score, p2score_pos)
        
        pygame.display.update()
        clock.tick(60)

        print(f'player1: {p1points}')
        print(f'player2: {p2points}')


pygame.quit()
