import time

class Calculator:
    def sum(self, a, b):
        return a + b

class SleepyCalculator:
    def sum(self, a, b):
        time.sleep(10) # Long Running Process
        return a + b
