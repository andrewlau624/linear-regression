import pygame

from error_metrics import calculate_mse

class Point:
    def __init__(self, pos):
        self.pos = pos

class Line:
    def __init__(self, m, b):
        self.m = m
        self.b = b

lines = [Line(0.3, 50.0), Line(-1, 200.0), Line(0.7, 80.0)]
data_points = [] 

def update_graph(learning_rate, screen, width):
    update_line(learning_rate)
    draw_points(screen)
    draw_line(screen, width)

def draw_points(screen):
    for p in data_points:
        pygame.draw.circle(screen, [255, 255, 255], p.pos, 5)

def draw_line(screen, width):
    for index, l in enumerate(lines):
        color = (255 * ((index + 1) * 20)) % 200 + 55,  (255 * ((index + 1) * (index + 10))) % 200 + 55, (255 * (index + 1)) % 200 + 55
        pygame.draw.line(screen, (color), [0, l.b], [width, l.m * width + l.b], 1)

def update_line(learning_rate):
    if len(data_points) > 0:
        for l in lines:
            regression_error = calculate_mse(l.m, l.b, data_points)
            l.m -= learning_rate * regression_error[0]
            l.b -= learning_rate * 10000 * regression_error[1]

def fetch_stats():
    stats = []
    if len(data_points) > 0:
        for l in lines:
            regression_error = calculate_mse(l.m, l.b, data_points)
            stats.append([regression_error[2], l.m, l.b])
        
    if len(data_points) <= 0:
        for l in lines:
            stats.append([0, l.m, l.b])
    return stats