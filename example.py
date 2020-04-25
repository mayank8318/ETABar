from etabar.ETA import ETA
import time

eta = ETA(5, ending_message="Executed successfully")
time.sleep(2)
for i in range(5):
    eta.update()
    time.sleep(2)

