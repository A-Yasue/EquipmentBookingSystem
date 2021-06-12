#!/usr/bin/env python


if __name__ == "__main__":
    import time
    import sys
    sys.path.append('../')
    sys.path.append('../../')

import dev.display.Console as Console
import dev.input as input


class KeyPressedMonitor():
    def __init__(self):
        self.__keyboard = input.SingletonKeyboard()
        self.__pressed_count = self.__keyboard.get_pressed_count()
        self.__pressed_key = ""

        if self.__keyboard.is_finished:
            self.__keyboard.start()

    def __del__(self):
        self.__keyboard.terminate()

    def capture(self):
        self.__keyboard.get_lock_object().acquire()
        now = self.__keyboard.get_pressed_count()
        key = self.__keyboard.get_last_pressed_key()
        self.__keyboard.get_lock_object().release()

        if self.__pressed_count != now:
            self.__pressed_count = now
            self.__pressed_key = key
        else:
            self.__pressed_key = ""

    def get_pressed_key(self):
        return self.__pressed_key

    def is_pressed_anykey(self):
        return self.__pressed_key

    def is_pressed_escapekey(self):
        return self.__pressed_key == b'\x1b'

    def is_pressed_enterkey(self):
        return self.__pressed_key == b'\r'

    def is_pressed_deletekey(self):
        return self.__pressed_key == b'\x08'

    def terminate(self):
        self.__keyboard.terminate()


def debug_this_module():
    Console.clear()

    kpM = KeyPressedMonitor()
    Console.clear()

    while True:
        kpM.capture()
        if kpM.is_pressed_escapekey():
            break
        if kpM.is_pressed_anykey():
            key = kpM.get_pressed_key()
            Console.puts(key, "\t", ord(key), "\t", chr(ord(key)))

        time.sleep(0.010)
    del kpM


if __name__ == "__main__":
    help(debug_this_module)
    time.sleep(1)
    debug_this_module()