# FPS counter

import time

class FPS_counter():
    def __init__(self):
        self.start = None
        self.fps = None
    def start_fps(self):
        self.x = 1
        self.counter = 0
        self.start = time.time()

    def update_fps(self):
        # Update fps counter
        self.counter += 1
        end = time.time()
        seconds = end - self.start
        if seconds > self.x:
            self.fps = self.counter / seconds
            self.counter = 0
            self.start = time.time()
        return self.fps