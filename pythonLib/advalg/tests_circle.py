from advalg.circle_animation import CircleAnimation
from advalg.circle_editor import CircleEditor

def start_animation(circles, sampler):
    if len(circles) == 0:
        print("Add at least one circle!")
    else:
        anim = CircleAnimation(circles, sampler)

def test_circle_sampler(sampler, samples = 1000, delay = 50):
    def start_animation(circles):
        if len(circles) == 0:
            print("Add at least one circle!")
        else:
            anim = CircleAnimation(circles, sampler, samples, delay)
    editor = CircleEditor(start_animation)