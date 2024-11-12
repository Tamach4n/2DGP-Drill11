import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie
from random import randint

# boy = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, balls, zomble

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    zombie = Zombie()
    game_world.add_object(zombie, 1)

    balls = [Ball(randint(100, 1600), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    # fill here
    game_world.add_collision_pair("boy:ball", boy, None)
    game_world.add_collision_pair("zombie:ball", zombie, None)
    game_world.add_collision_pair("boy:zombie", boy, zombie)

    for ball in balls:
        game_world.add_collision_pair("boy:ball", None, ball)
        game_world.add_collision_pair("zombie:ball", None, ball)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()  #   소년과 공의 위치 업데이트 완료
    # fill here
    game_world.handle_collisions()

    #   아마추어 방식
    # for ball in balls:
    #     if collide(boy, ball):
    #         print(f"boy:ball[{ball}] COLLIDE")
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass
