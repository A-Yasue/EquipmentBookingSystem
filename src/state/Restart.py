#!/usr/bin/env python

import time

import state as state
import dev.display.Console as Console
import dev.input as input


class Restart(state.IState):
    def entry(self):
        self.__start_time = time.time()
        self.__key_pressed_monitor = input.KeyPressedMonitor()
        Console.clear()
        if state.CommonResource.employeeId != "":
            Console.puts(state.CommonResource.employeeId, "さん。")
        Console.puts("一定時間操作がなかったか終了コードを受け付けたためエントランスに戻ります。")

    def do(self):
        self.__key_pressed_monitor.capture()

    def exit(self):
        pass

    def next(self):
        return state.Init()

    def event(self):
        return self.__key_pressed_monitor.is_pressed_anykey() or self.__timeout_detected()

    # 3秒経過でタイムアウト
    def __timeout_detected(self):
        elapsed_time = time.time() - self.__start_time
        return (3 < elapsed_time)