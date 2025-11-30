import pygame as pg
import target
import table
import input_table
pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BOUND = 50 # Pushes target bounds away from screen edges.
TARGET_RADIUS = 40
START_X = SCREEN_WIDTH / 2
START_Y = SCREEN_HEIGHT / 2
VELOCITY = 5
INTERVAL = 10 # 10 miliseconds

win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Target Game")

# Fonts
font = pg.font.SysFont('Arial', 20)
time_font = pg.font.SysFont('Arial', 40, True)
prompt_font = pg.font.SysFont('Arial', 60)


# Inbuilt timer
clock = pg.time.Clock
timer_event = pg.event.custom_type()
pg.time.set_timer(timer_event, 10)

# Cursor
cursor_img = pg.image.load('imgs/cursor_1.png')
cursor_width = cursor_img.get_rect().width
cursor_height = cursor_img.get_rect().height
cursor = pg.transform.scale(cursor_img, (cursor_width / 30, cursor_height / 30))
pg.mouse.set_visible(False)
cursor_x = 0
cursor_y = 0

# Entities
tar = target.target(START_X, START_Y, TARGET_RADIUS)
tar.set_random_position_bounds(BOUND, SCREEN_WIDTH - BOUND, BOUND, SCREEN_HEIGHT - BOUND)
scoreboard = table.table(SCREEN_WIDTH, SCREEN_HEIGHT, font)
input_box = input_table.input_table(SCREEN_WIDTH * 3 / 16, SCREEN_HEIGHT / 3)

x = -1
y = -1
clicks = 0
max_clicks = 20
time = 0
show_scoreboard = False
started = False
ended = False
taken_participant_info = False

# Test type & handling mouse behavior
static = True
near = False
very_near = False
diff_x = 0
diff_y = 0
stationary_timer = 0
very_near_speed_reduction = 3
near__speed_reduction = 1.5

def smooth_exp(dist):
    res = pow(3, (4/3) - dist/30)
    if res < 1:
        res = 1
    # print(res)
    return res

def smooth_lin(dist):
    res = dist / 45 + 1/9
    if res < 1:
        res = 1
    # print(res)
    return res

run = True
while run:
    pg.time.delay(INTERVAL)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == timer_event and started and not ended:
             time += INTERVAL

        if event.type == pg.KEYDOWN and not taken_participant_info:
            if event.key == pg.K_BACKSPACE:
                input_box.delete()
            elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                taken_participant_info = True
                static = input_box.send_participant_info(scoreboard)
                # input_box.test_tests()
            else:
                input_box.append_participant_info(event.unicode)
        
        if event.type == pg.MOUSEMOTION and not static:
            diff_x = event.rel[0]
            diff_y = event.rel[1]
        else:
            diff_x, diff_y = 0, 0

    if not static:
        if very_near:
            cursor_x += diff_x / very_near_speed_reduction
            cursor_y += diff_y / very_near_speed_reduction
        elif near:
            cursor_x += diff_x / smooth_exp(tar.dist_from_center(cursor_x, cursor_y))
            cursor_y += diff_y / smooth_exp(tar.dist_from_center(cursor_x, cursor_y))
        else:
            cursor_x = pg.mouse.get_pos()[0]
            cursor_y = pg.mouse.get_pos()[1]
    else:
        cursor_x = pg.mouse.get_pos()[0]
        cursor_y = pg.mouse.get_pos()[1]
    
    if not static:
        if tar.dist_from_center(cursor_x, cursor_y) < 10:
            very_near = True
            near = False
        elif tar.dist_from_center(cursor_x, cursor_y) < 40:
            near = True
            very_near = False
        else:
            near = False
            very_near = False

    keys = pg.key.get_pressed()
    mouse = pg.mouse.get_pressed()

    if keys[pg.K_TAB]:
        show_scoreboard = not show_scoreboard
        pg.time.delay(100)

    if keys[pg.K_SPACE] and taken_participant_info:
        started = True
        time = 0
        tar.random_position()
        pg.time.delay(120)
    
    if mouse[0] and taken_participant_info:
        # x, y = pg.mouse.get_pos()
        # tar_x = tar.get_x()
        # tar_y = tar.get_y()
        total_dist = tar.dist_from_center(cursor_x, cursor_y)
        # print("x:", x, "y:", y, "total_dist:", total_dist)
        # print("tar_x:", tar_x, "tar_y:", tar_y)
        if started and clicks < 20:
             scoreboard.add_data(total_dist, time / 1000.0)
             clicks += 1
        time = 0
        tar.random_position()
        pg.time.delay(300)


    win.fill((255,255,255))

    # Draw entities
    tar.draw(win)
    if show_scoreboard or ended:
            scoreboard.draw_table(win, 50, 50, font)
    if clicks >= max_clicks:
         ended = True
    text = font.render("Time: " + str(time / 1000.0), 1, (0,0,0))
    win.blit(text, (SCREEN_WIDTH - 150, 10))
    if not taken_participant_info:
         input_box.draw(win, prompt_font)
    win.blit(cursor, (cursor_x, cursor_y))

    pg.display.update()

pg.quit()