
from arambadge import badge
import displayio
import terminalio
from adafruit_display_text import bitmap_label
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect

class HelloApp:
    def __init__(self):
        self.run()

    def render(self):
        display = badge.display
        screen = displayio.Group()
        screen.append(Rect(0, 32, display.width, display.height - 32, fill=0xffffff))
        text_area = label.Label(terminalio.FONT, text="Hello World!", color=0xffffff, x=76, y=20)
        screen.append(text_area)
        display.show(screen)

    def run(self):
        display = badge.display
        self.running = True

        self.render()
        while display.time_to_refresh > 0:
            pass
        display.refresh()

        while self.running:
            self.render()
            while display.time_to_refresh > 0:
                pass
            display.refresh()

def main():
    return HelloApp()
