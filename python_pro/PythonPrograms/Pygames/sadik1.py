import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Bouncing Ball")

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = random.uniform(-0.5, 0.5)
        self.velocity_y = random.uniform(-0.5, 0.5)
        self.mass = radius  

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Collision detection
def check_collision(ball1, ball2):
    distance = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if distance <= ball1.radius + ball2.radius:
        return True
    return False

# Physics calculations
def resolve_collision(ball1, ball2):
    n_x = ball2.x - ball1.x
    n_y = ball2.y - ball1.y
    
    unit_normal = (n_x / ((n_x**2 + n_y**2)**0.5), n_y / ((n_x**2 + n_y**2)**0.5))
    unit_tangent = (-unit_normal[1], unit_normal[0])

    # Project velocities of each ball along normal and tangent lines
    v1n = ball1.velocity_x * unit_normal[0] + ball1.velocity_y * unit_normal[1]
    v1t = ball1.velocity_x * unit_tangent[0] + ball1.velocity_y * unit_tangent[1]
    v2n = ball2.velocity_x * unit_normal[0] + ball2.velocity_y * unit_normal[1]
    v2t = ball2.velocity_x * unit_tangent[0] + ball2.velocity_y * unit_tangent[1]

    # After collision, velocities along tangent don't change
    # Normal velocities swap according to conservation of momentum
    v1n_after = (v1n * (ball1.mass - ball2.mass) + 2 * ball2.mass * v2n) / (ball1.mass + ball2.mass)
    v2n_after = (v2n * (ball2.mass - ball1.mass) + 2 * ball1.mass * v1n) / (ball1.mass + ball2.mass)

    # Combine normal and tangential velocities back 
    v1_after = v1n_after * unit_normal[0] + v1t * unit_tangent[0], v1n_after * unit_normal[1] + v1t * unit_tangent[1]
    v2_after = v2n_after * unit_normal[0] + v2t * unit_tangent[0], v2n_after * unit_normal[1] + v2t * unit_tangent[1]

    ball1.velocity_x, ball1.velocity_y = v1_after
    ball2.velocity_x, ball2.velocity_y = v2_after


# Create some balls
balls = []
for _ in range(3):
    balls.append(Ball(
        random.randint(50, width - 50),
        random.randint(50, height - 50),
        random.randint(10, 30),
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ))

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball positions
    for ball in balls:
        ball.update()

        # Wall collisions
        if ball.x - ball.radius <= 0 or ball.x + ball.radius >= width:
            ball.velocity_x = -ball.velocity_x
        if ball.y - ball.radius <= 0 or ball.y + ball.radius >= height:
            ball.velocity_y = -ball.velocity_y

    # Check for collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)): 
            if check_collision(balls[i], balls[j]):
                resolve_collision(balls[i], balls[j])

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the balls
    for ball in balls:
         ball.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()