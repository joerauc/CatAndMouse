import pygame

PADDING = 4
BORDER_COLOR = (0, 0, 0)
TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (245, 245, 245)

class table:
    def __init__(self, screen_width, screen_height, font):
        self.cell_width = screen_width / 12
        self.cell_height = screen_height / 24
        self.data= []
        self.data.append(["dist (px)", "time (s)"])

    def draw_table(self, win, start_x, start_y, font):
        for row_index, row_data in enumerate(self.data):
            for col_index, cell_value in enumerate(row_data):
                
                # Calculate cell position
                x = start_x + col_index * self.cell_width
                y = start_y + row_index * self.cell_height

                # Draw cell background
                pygame.draw.rect(win, BACKGROUND_COLOR, (x, y, self.cell_width, self.cell_height))

                # Draw cell border
                pygame.draw.rect(win, BORDER_COLOR, (x, y, self.cell_width, self.cell_height), 1)

                # Render and draw text
                text_surface = font.render(str(cell_value), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=(x + self.cell_width // 2, y + self.cell_height // 2))
                win.blit(text_surface, text_rect)

    def add_data(self, dist, time):
        self.data.append([round(dist, 3), round(time, 3)])

    def add_row(self, tup):
        self.data.append(tup)

    def get_table(self):
        return self.data