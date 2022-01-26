import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("2048 cuy!")
current_display = "start"
start_timer = None
timer_started = False


class GameTimer:
    def __init__(self):
        self.passed_time = 0
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 15)

    def get_time(self):
        global timer_started
        global start_timer
        if not timer_started:
            start_timer = pygame.time.get_ticks()
            timer_started = True
        if timer_started:
            self.passed_time = pygame.time.get_ticks() - start_timer
        return self.passed_time

    def clock_tick(self, sec):
        self.clock.tick(sec)


# Start Menu GUI
class StartMenu:
    # Constructor
    def __init__(self, size_x, size_y):
        self.window = pygame.display.set_mode((size_x, size_y))
        self.bg = pygame.Surface((size_x, size_y))
        self.bg.fill(pygame.Color('#FFFFFF'))
        self.start_menu = pygame_gui.UIManager((size_x, size_y), "start_menu.json")
        self.title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((size_x - 350, size_y * 1 / 4), (200, 50)),
            text='2048',
            manager=self.start_menu)

        self.ayo_main = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((190, 250), (120, 50)),
                                                     text='Ayo Main',
                                                     manager=self.start_menu)

        self.skor = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((190, 325), (120, 50)),
                                                 text='Waktu Terendah',
                                                 manager=self.start_menu)

        self.keluar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((190, 400), (120, 50)),
                                                   text='keluar',
                                                   manager=self.start_menu)

    # Button Event Listener
    def event_listener(self, event):
        global current_display
        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == self.ayo_main:
                    current_display = "game"
                elif event.ui_element == self.skor:
                    current_display = "highscore"
                else:
                    quit()
        self.start_menu.process_events(event)

    # Display object
    def execute(self):
        self.window.blit(self.bg, (0, 0))
        self.start_menu.draw_ui(self.window)


class HighScore:
    # Constructor
    def __init__(self, size_x, size_y):
        self.bg = pygame.Surface((size_x, size_y))
        nama = pygame.font.SysFont("monospace", 20)
        self.white = (255, 255, 255)
        self.gold = (227, 208, 2)
        self.abu = (201, 201, 201)
        self.size_x = size_x
        self.size_y = size_y
        self.display = pygame.display.set_mode((size_x, size_y), 0, 32)
        self.highscore = pygame_gui.UIManager((size_x, size_y), "start_menu.json")
        self.telkom_image = pygame.image.load('3.png')
        self.skor = nama.render("Waktu Terendah!", 1, self.white)
        self.nama = nama.render("Nama", 1, self.white)
        self.waktu = nama.render("Waktu", 1, self.white)
        self.kembali = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((366, 123), (70, 25)),
                                                    text="kembali",
                                                    manager=self.highscore)

    # Draw object
    def draw_ui(self):
        k = 64
        self.display.fill(self.gold)
        pygame.draw.rect(self.display, self.abu, ((50, 150), (400, 400)))
        for i in range(1):
            l = 176
            for j in range(12):
                pygame.draw.rect(self.display, self.white, ((k, l), (250, 20)))
                l += 30
            k += 10
        k = 370
        for i in range(1):
            l = 176
            for j in range(12):
                pygame.draw.rect(self.display, self.white, ((k, l), (60, 20)))
                l += 30
            k += 10

    def event_listener(self, event):
        global current_display
        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == self.kembali:
                    current_display = "start"
        self.highscore.process_events(event)

    # Display object
    def execute(self):
        self.draw_ui()
        self.display.blit(self.skor, (66, 123))
        self.display.blit(self.nama, (66, 153))
        self.display.blit(self.waktu, (370, 153))
        self.display.blit(self.telkom_image, (200, 3))
        self.highscore.draw_ui(self.display)


class GameGui:
    # Constructor
    def __init__(self, size_x, size_y):
        text = pygame.font.SysFont("monospace", 40)
        text_time = pygame.font.SysFont("monospace", 15)
        self.white = (255, 255, 255)
        self.gold = (227, 208, 2)
        self.abu = (201, 201, 201)
        self.size_x = size_x
        self.size_y = size_y
        self.display = pygame.display.set_mode((size_x, size_y), 0, 32)
        self.telkom_image = pygame.image.load('3.png')
        self.label_2048 = text.render("2048", 1, self.white)
        self.label_time = text_time.render("waktu", 1, self.white)
        self.timer_obj = GameTimer()

    # Draw object
    def draw_ui(self):
        k = 66
        self.display.fill(self.gold)
        pygame.draw.rect(self.display, self.white, ((360, 118), (70, 25)))
        pygame.draw.rect(self.display, self.abu, ((50, 150), (400, 400)))
        for i in range(4):
            l = 166
            for j in range(4):
                pygame.draw.rect(self.display, self.white, ((k, l), (80, 80)))
                l += 96
            k += 96

    # Display object
    def execute(self):
        self.draw_ui()
        self.display.blit(self.label_2048, (66, 100))
        self.display.blit(self.label_time, (372, 100))
        self.display.blit(self.timer_obj.font.render(str(round(self.timer_obj.get_time()/1000)), True, (0, 0, 0)),
                          (362, 123))
        self.display.blit(self.telkom_image, (200, 3))


# PSVM
class Main:
    @staticmethod
    def run(size_x, size_y):
        start_menu_obj = StartMenu(size_x, size_y)
        game_gui_obj = GameGui(size_x, size_y)
        high_score_obj = HighScore(size_x, size_y)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if current_display == "start":
                    start_menu_obj.event_listener(event)
                elif current_display == "highscore":
                    high_score_obj.event_listener(event)

            if current_display == "start":
                start_menu_obj.execute()
            elif current_display == "game":
                game_gui_obj.execute()
            elif current_display == "highscore":
                high_score_obj.execute()

            pygame.display.update()
            game_gui_obj.timer_obj.clock_tick(30)


Main.run(500, 600)
