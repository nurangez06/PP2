import pygame
import os

#2
pygame.init()
pygame.mixer.init()

playlist = ["coin.mp3", "crash.mp3", "song3.mp3"]
current_track = 0
playing = False

def play_song():
    global playing
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    playing = True

def stop_song():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_song():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_song()

def prev_song():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_song()

print("Press SPACE to Play/Pause, S to Stop, N for Next, P for Previous")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                prev_song()

pygame.quit()
