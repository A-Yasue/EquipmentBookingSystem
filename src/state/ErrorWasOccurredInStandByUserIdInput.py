#!/usr/bin/env python

import state
import time

import dev.display.Console as Console
import dev.input as input

class ErrorWasOccurredInStandByUserIdInput(state.IState):
    def entry(self):
        self.__start_time = time.time()
        self.__pressed_key = input.PressedKey()
        Console.puts("")
        Console.puts("未登録の社員番号です。")
        Console.puts("新規ユーザー登録と言いたいところですが、未実装なのでちょっとしたら元の画面に戻ります")

    def do(self):
        self.__pressed_key.capture()

    def exit(self):
        pass

    def get_next_state(self):
        return state.StandbyUserIdInput()

    def should_exit(self):
        return self.__pressed_key.exists() or self.__timeout_detected()

    # 3秒経過でタイムアウト
    def __timeout_detected(self):
        elapsed_time = time.time() - self.__start_time
        return ( 3 < elapsed_time)
