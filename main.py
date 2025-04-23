import pygame, sys

# Initialize pygame library
pygame.init()


# Initialize window
W, H = 800, 600
display = pygame.display.set_mode([W, H])


# Make display black
display.fill((0, 0, 0))

# Main loop. Run until trying to exit
run = True
while run:
    # Capture all events that can occur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Update screen
    pygame.display.flip()

# Deactivate modules
pygame.quit()
sys.exit()