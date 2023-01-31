import threading


class Loop:

    def __init__(self):

        self.COUNT_TASK_IN_QUEUE = 0
        self.TASK_IN_QUEUE = False
        self.IS_RUNNING = False
        self.QUEUE_LIST_TASK = []
        self.LIST_TASK = []

    def add(self,task):
        self.LIST_TASK.append(task)
        return self.LIST_TASK

    def list_task_clear(self):
        self.LIST_TASK = []

    def completed(self):
        self.IS_RUNNING = False
        self.list_task_clear()

    def start(self):
        if self.IS_RUNNING == False:
            self.IS_RUNNING = True
            def target(loop):
                """
                    Thread
                """
                for Task in loop.LIST_TASK:
                    Task.run()
                # Completed All
                loop.completed()

            t = threading.Thread(target=target,args=(self,))
            t.start()
            self.THREAD = t
            if self.TASK_IN_QUEUE:
                self.TASK_IN_QUEUE = False
                self.start()
        else:
            self.TASK_IN_QUEUE = True



class Task:

    def __init__(self,func,args=()):
        self._func = func
        self.args = args

    def run(self):
        self._func(*self.args)
        
        

