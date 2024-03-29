from advalg.circle_animation import CircleAnimation
from advalg.circle_editor import CircleEditor

def test_circle_sampler(sampler, samples: int = 1000, delay: int = 50) -> None:
    """Tests your implementation of the CircleSampler class"""
    print("Left click: Add/drag a circle")
    print("Right click: Remove a circle")

    def start_animation(circles):
        if len(circles) == 0:
            print("Add at least one circle!")
        else:
            anim = CircleAnimation(circles, sampler, samples, delay)
    editor = CircleEditor(start_animation)