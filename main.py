# this Python script uses your camera to take pictures
import pyscreenshot

def full_screen_shots():
    # To capture the full screen
    image = pyscreenshot.grab()
    # To display the captured screenshot
    image.show()
    # To save the screenshot
    image.save("Photo1.png")

def partial_screen_shots():
    # To capture the full screen
    # (x1, x2, y1, y2)
    image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
    # To display the captured screenshot
    image.show()
    # To save the screenshot
    image.save("Photo1.png")


if __name__ == '__main__':
    # to capture full screen
    full_screen_shots()

    # to capture partial screen
    partial_screen_shots()

