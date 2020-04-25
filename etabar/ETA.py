import time
import datetime


class ETA:
    def __init__(self, total_tasks):
        self.total_tasks = total_tasks
        self.current_tasks = 0
        self.start_time = time.time()
        self.printETA(0, "NA")

    def update(self):
        self.current_tasks += 1
        cur_time = time.time()
        time_taken = cur_time - self.start_time
        final_time = (self.total_tasks * time_taken) / self.current_tasks
        eta = self.start_time + final_time - cur_time

        completed_perc = (self.current_tasks * 100) / self.total_tasks
        self.printETA(completed_perc, eta)

    def printETA(self, completed, eta):
        if type(eta) is str:
            print("\rCompleted : " + "{:.2f}".format(completed) + "%\t ETA = " + eta, end="")
            return
        print("\rCompleted : " + "{:.2f}".format(completed) + "%\t ETA = " + str(datetime.timedelta(seconds=eta)) + "s", end="")
