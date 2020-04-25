from etabar.ETA import ETA
import time

eta = ETA(100)
time.sleep(2)
for i in range(100):
    eta.update()
    time.sleep(2)

