# Importy
import pygame
import random

# Inicializace pygame
pygame.init()

# Screen
width = 960
height = 681
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Football click game")

# Nastavení
score = 0
heighest_score = score

# Obrázky
# Fotbalové hřiště
football_pitch_image = pygame.image.load("img/football_pitch.png")
football_pitch_image_rect = football_pitch_image.get_rect()
# football_pitch_image_rect.topleft = (0, 0)
football_pitch_image_rect.bottomright = (width, height)

# Fotbalový míč
ball_image = pygame.image.load("img/ball.png")
ball_image_rect = ball_image.get_rect()
ball_image_rect.top = random.randint(101, height-68)
ball_image_rect.left = random.randint(45, width-93)

# Ikona pauznutí
pause_image = pygame.image.load("img/Pause_image.png")
pause_image_rect = pause_image.get_rect()
pause_image_rect.top = 15
pause_image_rect.right = width - 5

# Ikona spuštění
play_image = pygame.image.load("img/Play_image.png")
play_image_rect = play_image.get_rect()
play_image_rect.top = 15
play_image_rect.right = width - 5

# Ikona again full game
refresh_image = pygame.image.load("img/Refresh_image.png")
refresh_image_rect = refresh_image.get_rect()
refresh_image_rect.top = 15
refresh_image_rect.right = width - 63

# Kolik + obrázek hodin
number_clocks = random.randint(0, 3)
clock_image = pygame.image.load("img/Clock.png")
clock_image_rect = clock_image.get_rect()
clock_image_rect.top = random.randint(101, height-68)
clock_image_rect.left = random.randint(45, width-93)
# List clocks
clocks = []

# Přidání počtu hodin do listu
if number_clocks >= 1:
    # Náhodný čas
    clock_1 = random.randint(0, 3400)
    clocks.append(clock_1)
if number_clocks >= 2:
    # Náhodný čas
    clock_2 = random.randint(0, 3400)
    clocks.append(clock_2)
if number_clocks == 3:
    # Náhodný čas
    clock_3 = random.randint(0, 3400)
    clocks.append(clock_3)

# Again ikona, pokud skončí kolo
again_image = pygame.image.load("img/Again.png")
again_image_rect = again_image.get_rect()
again_image_rect.center = (width//2+10, height//2+80)
# za again ikonu (teď nechceme)
# pygame.draw.rect(screen, "black", (again_image_rect.topleft, again_image_rect.bottomright))

# Fonty
h_font = pygame.font.Font("font/football_font.ttf", 70)
big_font = pygame.font.Font("font/football_font.ttf", 60)
mid_font = pygame.font.Font("font/football_font.ttf", 40)
small_font = pygame.font.Font("font/football_font.ttf", 30)

# Texty
# Nadpis hry
main_text = big_font.render("Football click game", True, "grey")
main_text_rect = main_text.get_rect()
main_text_rect.top = -5
main_text_rect.centerx = width//2

# Score kola
score_text = small_font.render(f"score: {score}", True, "grey")
score_text_rect = score_text.get_rect()
score_text_rect.top = 0
score_text_rect.left = 20

# vypsání skóre na konci hry
final_score = small_font.render(f"Your score for this round: {score}", True, "purple", "black")
final_score_rect = final_score.get_rect()
final_score_rect.center = (width//2, height//2+20)

# Nejvyšší skóre
best_score_text = small_font.render(f"best score: {heighest_score}", True, "grey")
best_score_text_rect = best_score_text.get_rect()
best_score_text_rect.top = 35
best_score_text_rect.left = 20

# Text pro pokračování hry nebo pro začátek
click_play_text = mid_font.render("Click anywhere on the screen to play.", True, "black")
click_play_text_rect = click_play_text.get_rect()
click_play_text_rect.center = (width//2, height//2+30)

autor_font = pygame.font.SysFont("Arial", 15)
autor_name_text = autor_font.render("Šimon Drápal 24. 10. 2023", True, "black")
autor_name_text_rect = autor_name_text.get_rect()
autor_name_text_rect.bottomright = (width - 5, height)

# Nastavení času
time_1 = 0
time_2_set = 60
# Jak dlouho tíkají hodiny
clock_time = 70
time_2 = time_2_set

# Čas
time_text = h_font.render(f"{time_2}", True, "yellow")
time_text_rect = time_text.get_rect()
time_text_rect.top = -10
time_text_rect.right = width - 130

# písnička a zvuky
names_list = ["b_g_music.mp3", "b_g_music_2.mp3", "b_g_music_3.mp3", "b_g_music_4.mp3", "b_g_music_5.mp3", "b_g_music_6.mp3", "b_g_music_7.mp3"]
the_music = random.choice(names_list)
pygame.mixer.music.load(f"media/{the_music}")
pygame.mixer.music.set_volume(0.2)

# Zvuk po kliknutí na míč
ball_sound = pygame.mixer.Sound("media/ball_sound.mp3")
ball_sound.set_volume(20)

# Zvuk na konci kola (písknutí rozhodčího)
referee_sound = pygame.mixer.Sound("media/referee-blowing-whistle-sound-effect.mp3")

# Zvuk pípání hodin
tick_sound = pygame.mixer.Sound("media/tick_sound.mp3")

# Zvuk bonusového času
fast_tick_sound = pygame.mixer.Sound("media/fast_tick.mp3")

# Pokud klikne a netrefí se do míče
miss_click = pygame.mixer.Sound("media/miss_click.mp3")
miss_click.set_volume(0.5)

# barva nevyššího skore
b = 0

# Pokud se rovná True - Restart hry
ref = False

# Pokud někdo klikne na clock_click = False - změna polohy
clock_click = True

# fps & clock
fps = 60
clock = pygame.time.Clock()

# cyklus pro hru
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        # Pokud chceme hru ukončit
        if event.type == pygame.QUIT:
            lets_continue = False

        # Pokud klikneme - spustí se celá hra (zapneme pouze jednou potom až v tom dalším cyklu)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Spuštění hudby
            pygame.mixer.music.play(-1, 0.0)
            while lets_continue:
                # Počítání času
                time_1 += 1
                # Pokud se má odečíst čas
                if time_1 % 60 == 0:
                    time_2 -= 1
                    # Pokud je čas menší nebo stejný jako 10
                    if time_2 <= 10:
                        tick_sound.play()
                    # Pokud není
                    else:
                        tick_sound.stop()
                # Hlavní event
                for event in pygame.event.get():
                    # Pokud chceme hru ukončit
                    if event.type == pygame.QUIT:
                        lets_continue = False

                    # Pokud klikneme
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Zaznamenání pozice kliknutí
                        click_x = event.pos[0]
                        click_y = event.pos[1]
                        # Pokud klikneme na míč
                        if ball_image_rect.collidepoint(click_x, click_y):
                            # Přidání skóre, přemístění míče a zvuk kopnutí
                            score += 1
                            ball_image_rect.top = random.randint(101, height - 68)
                            ball_image_rect.left = random.randint(45, width - 93)
                            ball_sound.play()

                        # Pokud chceme hru pauznout
                        elif pause_image_rect.collidepoint(click_x, click_y):
                            cykle_2 = True
                            # Vypsíní ikonky pro pokračování
                            screen.blit(play_image, play_image_rect)
                            # Vypnou se zvuky a pozastaví se hudba
                            tick_sound.stop()
                            fast_tick_sound.stop()
                            pygame.mixer.music.pause()
                            # Update
                            pygame.display.update()
                            while cykle_2:
                                for event_2 in pygame.event.get():
                                    # Pokud při pauznutí ukončíme hru
                                    if event_2.type == pygame.QUIT:
                                        lets_continue = False
                                        cykle_2 = False
                                    # Pokud klikneme myší
                                    elif event_2.type == pygame.MOUSEBUTTONDOWN:
                                        # Zaznamenání pozice
                                        click_2_x = event_2.pos[0]
                                        click_2_y = event_2.pos[1]
                                        # Pokud chceme s hrou pokračovat
                                        if play_image_rect.collidepoint(click_2_x, click_2_y):
                                            # Spuštění hry
                                            pygame.mixer.music.unpause()
                                            cykle_2 = False
                        # Pokud chceme hru restartovat
                        elif refresh_image_rect.collidepoint(click_x, click_y):
                            # Pro cyklus
                            ref = True

                        # Pokud klikneme na plusový čas
                        elif clock_image_rect.collidepoint(click_x, click_y):
                            clock_click = False
                            # Přidání času
                            time_2 += 5

                        # Pokud klikneme vedle
                        else:
                            # Spustí se miss_click zvuk
                            miss_click.play()

                # screen fill
                screen.fill("black")

                # Pokud je nové nejvyšší skóre
                if heighest_score < score:
                    # Změníme nejvyšší skóre na stejné jako je skóre
                    heighest_score = score
                    # Pro změnu barvy best_score
                    b = 1

                # blit obrázků
                screen.blit(football_pitch_image, football_pitch_image_rect)
                screen.blit(ball_image, ball_image_rect)
                screen.blit(pause_image, pause_image_rect)
                screen.blit(refresh_image, refresh_image_rect)

                # blit textů
                score_text = small_font.render(f"score: {score}", True, "grey")
                # Pokud nebylo překonáno nejvyšší skóre
                if b == 0:
                    color = "grey"
                # Pokud bylo překonáno nejvyšší skóre
                elif b == 1:
                    color = "yellow"
                best_score_text = small_font.render(f"best score: {heighest_score}", True, color)

                # Pokud je čas menší nebo roven 10 = Červená
                if time_2 <= 10:
                    color_2 = "red"
                # Jinak se rovná žlutá
                else:
                    color_2 = "yellow"
                time_text = h_font.render(f"{time_2}", True, color_2)

                # Blit textů
                screen.blit(main_text, main_text_rect)
                screen.blit(score_text, score_text_rect)
                screen.blit(best_score_text, best_score_text_rect)
                screen.blit(time_text, time_text_rect)
                screen.blit(autor_name_text, autor_name_text_rect)

                # Kontrola jestli se nemají zobrazit hodiny
                for one_number in clocks:
                    # Pokud se to číslo rovná času a nebo je čas větší, ale číslo + čas na ploše musí být větší
                    if one_number == time_1 or (one_number < time_1 and one_number + clock_time >= time_1) and clock_click:
                        # Vypsání bonusových hodin
                        screen.blit(clock_image, clock_image_rect)

                    # Pokud se to číslo rovná času
                    if one_number == time_1:
                        # Spuštění tikání
                        fast_tick_sound.play()

                    # Pokud číslo + čas na obrazovce se rovná času nebo už jsme na hodiny klikli
                    if one_number + clock_time == time_1 or clock_click == False:
                        # Náhodné umístění příštích hodin
                        clock_image_rect.top = random.randint(101, height - 68)
                        clock_image_rect.left = random.randint(45, width - 93)
                        # Zastavení tikání
                        fast_tick_sound.stop()
                        # Pokud jsme pouze klikli
                        if one_number + clock_time == time_1:
                            # Aby se stále nespouštěla podmínka
                            clock_click = True

                # Update obrazovky
                pygame.display.update()

                # Pokud nezbývá čas nebo pokud jsme dali restart hry
                if time_2 == 0 or ref:
                    # Pokud nezbývá čas
                    if time_2 == 0:
                        # Vypsání skóre, ikonky again
                        final_score = small_font.render(f"Your score for this round: {score}", True, "purple", "black")
                        screen.blit(again_image, again_image_rect)
                        screen.blit(final_score, final_score_rect)

                    if ref:
                        screen.blit(click_play_text, click_play_text_rect)

                    # Update
                    pygame.display.update()
                    # Pozastavení hudby a tikání
                    pygame.mixer.music.stop()
                    tick_sound.stop()
                    if time_2 == 0:
                        # Zapískání rozhodčího (nedal jsem to nahoru, protože to nefungovalo, asi jak jsem dával stop)
                        referee_sound.play()

                    cykle = True
                    while cykle:
                        for event in pygame.event.get():
                            # Pokud klikneme na obrazovku nebo pokud jsme dali restart
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click_3_x = event.pos[0]  # x
                                click_3_y = event.pos[1]  # y
                                # Pokud jsme klikli na ikonu nebo jsme restartovali
                                if again_image_rect.collidepoint(click_3_x, click_3_y) or ref:
                                    # Kolikrát chceme promítnout hodiny + náhodné umístění + náhodný čas zobrazení
                                    number_clocks = random.randint(0, 3)
                                    clock_image_rect.top = random.randint(101, height - 68)
                                    clock_image_rect.left = random.randint(45, width - 93)
                                    clocks = []
                                    if number_clocks >= 1:
                                        clock_1 = random.randint(0, 3400)
                                        clocks.append(clock_1)
                                    if number_clocks >= 2:
                                        clock_2 = random.randint(0, 3400)
                                        clocks.append(clock_2)
                                    if number_clocks == 3:
                                        clock_3 = random.randint(0, 3400)
                                        clocks.append(clock_3)

                                    # Reset proměnných
                                    ref = False
                                    score = 0
                                    time_1 = 0
                                    time_2 = time_2_set
                                    b = 0
                                    # Náhodné umístění míče
                                    ball_image_rect.top = random.randint(101, height - 68)
                                    ball_image_rect.left = random.randint(45, width - 93)
                                    cykle = False
                                    music_2 = the_music
                                    # Náhodné vybrání písničky + nastavení a zapnutí
                                    while music_2 == the_music:
                                        the_music = random.choice(names_list)
                                    pygame.mixer.music.load(f"media/{the_music}")
                                    pygame.mixer.music.set_volume(0.3)
                                    pygame.mixer.music.play()

                            # Pokud chceme hru ukončit
                            elif event.type == pygame.QUIT:
                                lets_continue = False
                                cykle = False

                # fps
                clock.tick(fps)

    # blit obrázků- na začátku
    screen.blit(football_pitch_image, football_pitch_image_rect)

    # blit textů- na začátku
    screen.blit(main_text, main_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(best_score_text, best_score_text_rect)
    if lets_continue != False:
        screen.blit(click_play_text, click_play_text_rect)
    screen.blit(time_text, time_text_rect)
    screen.blit(autor_name_text, autor_name_text_rect)

    # Update obrazovky- na začátku
    pygame.display.update()

    # fps- na začátku
    clock.tick(fps)

# Konec pygame
pygame.quit()
