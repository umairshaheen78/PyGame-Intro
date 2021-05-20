'''
5/17/2021 Notes
PyGame - Intro

Pygame:
- A set of Python modules made for creating a game

Coordinates of PyGame WScreen:
- The middle is (0,0). 
- The bottom right is (width, height)
- Positive (x) is to the right.
- Negative (y) is to the left.
- Positive (y) is downward.
- Negative (y) is upward.
'''

# 1. Import PyGame library
import pygame

# 2. Initiable PyGame
pygame.init()

# 3. Make a PyGame Window
window = pygame.display.set_mode((500,500))

# 4. Setup a caption on the window
pygame.display.set_caption("First PyGame")

# 5. Set variables and values (coordinates)
x = 10
y = 10

# 6. Create an object (width and height) and speed
width = 10
height = 15
speed = 5

# 7. Create a control variable
run = True 

# 8. Launch a game with the control variable
while (run): 

  # 9. Setup delay time to 100ms
  pygame.time.delay(100)

  # 10. Function the button
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      # 11. Terminate game when the button is pressed
      run = False

  #12. Activate Keys
  keys = pygame.key.get_pressed(0)

  #13. Left arrow key pressed, then decrease value for x
  if keys[pygame.K_LEFT]:
    x -= speed

  #14. Right arrow key pressed, then increase value for x
  if keys[pygame.K_RIGHT]:
    x += speed

  #15. Up arrow key pressed, then decrease value for x
  if keys[pygame.K_UP]:
    y -= speed

  #16. Down arrow key pressed, then increase value for x
  if keys[pygame.K_DOWN]:
    y += speed

  #17. Setup a rectangle as a moving object
  pygame.draw.rect(window, (50,150,23), (x,y, width, height))

  #18. Update the game
  pygame.display.update()

# 19. Quit out of the game
pygame.quit()