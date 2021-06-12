#!/usr/bin/env python


if __name__ == "__main__":
    import time
    import sys
    sys.path.append('../')
    sys.path.append('../../')


import dev.display.Console as Console
import dev.input as input


class KeyPressedBuffering(input.IUserInputReader):
    def __init__(self):
        self.__key_pressed_monitor = input.KeyPressedMonitor()
        self.__string = ""
        self.__submitted = False
        self.__updated = False
        self.__is_real_time_display_mode = True

    def capture(self):
        self.__key_pressed_monitor.capture()

        if self.__key_pressed_monitor.is_pressed_anykey():
            self.__updated = True

            if self.__key_pressed_monitor.is_pressed_enterkey():
                # Submit keyboard input
                self.__submitted = True
                if self.__is_real_time_display_mode:
                    Console.puts("")  # New line

            elif self.__key_pressed_monitor.is_pressed_escapekey():
                # Clear buffer
                self.__string = ""
                if self.__is_real_time_display_mode:
                    Console.remove_line()

            elif self.__key_pressed_monitor.is_pressed_deletekey():
                # Remove a last charcter
                self.__string = self.__string[:-1]
                if self.__is_real_time_display_mode:
                    Console.remove_char()
            else:
                # Join a character to last position
                key = chr(ord(self.__key_pressed_monitor.get_pressed_key()))
                if key.isascii():
                    self.__string += key
                    if self.__is_real_time_display_mode:
                        Console.puts(key, end='')

        else:
            self.__updated = False

    def get_string(self):
        return self.__string

    def submitted(self):
        return self.__submitted

    def updated(self):
        return self.__updated

    def real_time_display(self, enabled):
        self.__is_real_time_display_mode = enabled


def debug_this_module():
    Console.clear()

    kpb = KeyPressedBuffering()

    while not kpb.submitted():
        kpb.capture()
        time.sleep(0.010)

    Console.puts("Your input is :", kpb.get_string())
    time.sleep(3)

    del kpb


if __name__ == "__main__":
    help(debug_this_module)
    time.sleep(1)
    debug_this_module()
