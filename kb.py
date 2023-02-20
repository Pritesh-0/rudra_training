import time
import keyboard

key_press_times = {'w': None, 'a': None, 's': None, 'd': None}

while True:
    for key in key_press_times.keys():
        if keyboard.is_pressed(key):
            if key_press_times[key] is None:
                key_press_times[key] = time.time()
        else:
            if key_press_times[key] is not None:
                duration = time.time() - key_press_times[key]
                print(int(1000*duration))
                key_press_times[key] = None

    time.sleep(0.01)

