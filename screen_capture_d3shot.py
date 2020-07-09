import d3dshot
import time

d = d3dshot.create(capture_output="numpy")

d.capture()

time.sleep(1)
