#!/usr/bin/env python

import state
import time

import dev.display.Console as Console
import dev.input as input

class ErrorWasOccurredInStandByUserIdInput(state.IState):
    def entry(self):
        self.__start_time = time.time()
        self.__key_pressed_monitor = input.KeyPressedMonitor()
        Console.puts("")
        Console.puts("未登録の社員番号です。")
        Console.puts("新規ユーザー登録と言いたいところですが、未実装なのでちょっとしたら元の画面に戻ります")

    def do(self):
        self.__key_pressed_monitor.capture()

    def exit(self):
        pass

    def next(self):
        return state.StandbyUserIdInput()

    def event(self):
        return self.__key_pressed_monitor.is_pressed_anykey() or self.__timeout_detected()

    # 3秒経過でタイムアウト
    def __timeout_detected(self):
        elapsed_time = time.time() - self.__start_time
        return ( 3 < elapsed_time)
