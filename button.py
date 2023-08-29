import pygame

import constants as const


class Button:
    def __init__(
        self,
        pos_x_y: tuple[int, int],
        width: int,
        height: int,
        text: str,
        font_size: int = 20,
        button_color: tuple[int, int ,int] = const.GRAY,
        text_color: tuple[int, int ,int] = const.BLACK,
        hover_color: tuple[int, int ,int] = const.WHITE
    ):
        self.rect = pygame.Rect(pos_x_y[0], pos_x_y[1], width, height)
        self.button_color = button_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.is_hovered = False

    def draw(self, screen):
        # Draw the button
        color = self.hover_color if self.is_hovered else self.button_color
        pygame.draw.rect(screen, color, self.rect)

        # Draw the text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse is hovering over the button
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            # Execute the callback function when the button is clicked
            return True
        return False