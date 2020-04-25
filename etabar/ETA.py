import time
import datetime


class ETA:
    def __init__(self, total_tasks, ending_message=None):
        self.total_tasks = total_tasks
        self.current_tasks = 0
        self.start_time = time.time()
        self.printETA(0, "NA")
        self.ending_message = ending_message
        self.finish_flag = False

    def update(self):
        if self.finish_flag:
            print("WARNING : Current tasks has crossed the specified total tasks!!")
            return

        self.current_tasks += 1
        cur_time = time.time()
        time_taken = cur_time - self.start_time
        final_time = (self.total_tasks * time_taken) / self.current_tasks
        eta = self.start_time + final_time - cur_time

        completed_perc = (self.current_tasks * 100) / self.total_tasks
        self.printETA(completed_perc, eta)
        if self.current_tasks == self.total_tasks:
            self.finish()

    def printETA(self, completed, eta):
        if type(eta) is str:
            print("\rCompleted : " + "{:.2f}".format(completed) + "%\t ETA = " + eta, end="")
            return
        print("\rCompleted : " + "{:.2f}".format(completed) + "%\t ETA = " + str(datetime.timedelta(seconds=eta)), end="")

    def finish(self):
        self.finish_flag = True
        print("\n")
        if self.ending_message:
            print(self.ending_message)
