import pygame
import table

class input_table:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.input_rect = pygame.Rect(self.x, self.y, 600, 300)
        self.prompt_text = "Participant number/test:"
        self.user_text = "p"

    def draw(self, win, font):
        pygame.draw.rect(win, (225,225,225), self.input_rect, 0, 20)
        pygame.draw.rect(win, (0, 0, 0), self.input_rect, 2, 20)
        prompt_surface = font.render(self.prompt_text, True, (0, 0, 0))
        win.blit(prompt_surface, (self.x + 20, self.y + 10))
        text_surface = font.render(self.user_text, True, (0, 0, 0))
        win.blit(text_surface, (self.x + 20, self.y + 80))
    
    # For debugging
    def print_text(self):
        print(self.user_text)

    # For debugging
    def test_tests(self):
        letters = ("a", "b")
        for i in range(8, 14):
            for let in letters:
                self.user_text = "p" + str(i) + let
                tf = self.get_participant_test()
                print("Num:", i, "Letter:", let, "Result:", tf)

    def append_participant_info(self, text):
        self.user_text = self.user_text + text

    def send_participant_info(self, data_table):
        num_participant = self.user_text[:-1]
        num_test = self.user_text[-1:]
        data_table.add_row([num_participant, num_test])
        return self.get_participant_test()

    def get_participant_num(self):
        return int(self.user_text[1:-1])
    
    def get_participant_test(self):
        res = self.get_participant_num() % 2 # 0 for even, 1 for odd
        add = 0 if self.user_text[-1:] == "a" else 1 # 0 for a, 1 for else
        # print("For", self.user_text, "Test is", (res + add) % 2)
        return True if (res + add) % 2 == 1 else False


    def delete(self):
        self.user_text = self.user_text[:-1]