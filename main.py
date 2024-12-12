import pygame

from graph import update_graph, fetch_stats, data_points, Point

background_colour = (0, 0, 0)
(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Linear Regression')
screen.fill(background_colour)
pygame.display.update()

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)

def update():
  screen.fill(background_colour)
  update_graph(0.000001, screen, width)
  stats = fetch_stats()

  for index, data in enumerate(stats):
    color = (255 * ((index + 1) * 20)) % 200 + 55,  (255 * ((index + 1) * (index + 10))) % 200 + 55, (255 * (index + 1)) % 200 + 55
    line_text = my_font.render("Line " + str(index + 1), False, (color))
    m_text = my_font.render("Slope (m): " + str(-round(data[1], 7)), False, (color))
    b_text = my_font.render("Y-Intercept (b): " + str(height - round(data[2],7)), False, (color))
    eq_text = my_font.render("Equation: " + str(round(data[1], 7)) + "x + " + str(round(data[2],7)), False, (color))
    mse_text = my_font.render("Mean Squared Error (MSE): " + str(round(data[0], 7)), False, (color))
    screen.blit(line_text, (0, index * 100))
    screen.blit(m_text, (0, index * 100 + 20))
    screen.blit(b_text, (0, index * 100 + 40))
    screen.blit(eq_text, (0, index * 100 + 60))
    screen.blit(mse_text, (0, index * 100 + 80))
  pygame.display.update()

running = True
while running:
  update()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        data_points.append(Point(pos))
    if event.type == pygame.QUIT:
      running = False