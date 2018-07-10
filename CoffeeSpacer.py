import time
import os
import subprocess

time_start = time.time()


hour = int(input('At what interval do you want to drink caffee? (seconds) '))


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


prev_coffee_time = time_start
while True:
    time_new = time.time()
    if time_new - prev_coffee_time >= 2*hour:
        prev_coffee_time = time.time()
        sendmessage('You drink some coffee boi')

    if time_new % 1 == 0:
        rows, columns = os.popen('stty size', 'r').read().split()

        progress_front = 'Progress till next coffee cup: ['
        progress_end = ']'
        available_size = int(columns) - len(progress_front) - len(progress_end)
        progress = int((time_new - prev_coffee_time) / (2*hour) * available_size)
        progress_str = '#' * progress
        negative_progress_str = '-' * int(available_size-progress)
        print(progress_front + progress_str + negative_progress_str + progress_end, end="\r")
