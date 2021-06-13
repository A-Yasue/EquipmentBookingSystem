#!/usr/bin/env python

import time
import state as state
import dev.display.Console as Console
import dev.input as input


class StateController():
    def __init__(self):
        self.__current = state.Init()
        self.__current.entry()
        self.__start_time = time.time()
        self.__pressed_key = input.PressedKey()

    def step(self):
        self.__pressed_key.capture()

        # 現在の状態を実行する
        self.__current.do()

        if (self.__current.event()):

            # 遷移イベントが検出された場合、現在の状態を終了する
            self.__current.exit()

            # 次の状態を取得し、状態遷移を行う
            self.__current = self.__current.next()

            # 遷移先の状態を開始する
            self.__current.entry()

            # タイムアウト時間をクリアする
            self.__restart_timer()

        elif (self.__current.__class__ is not state.Init().__class__ and
              self.__current.__class__ is not state.Restart().__class__):
            # Init でも Restart でもない場合はタイムアウトとESCの入力を監視しRestartに遷移する
            # 前状態のexitは実行しないためリソースの解放はデストラクタに実装すること

            if self.__timeout_detected() or self.__pressed_key.is_escape():
                self.__current = state.Restart()
                self.__current.entry()
                self.__restart_timer()
                
    def run(self):
        while self.__current.__class__ is not state.Exit().__class__:
            time.sleep(0.010)
            self.step()

    # 5秒経過でタイムアウト
    def __restart_timer(self):
        self.__start_time = time.time()

    def __timeout_detected(self):
        # Refresh timer when any key pressed
        if self.__pressed_key.exists():
            self.__restart_timer()

        elapsed_time = time.time() - self.__start_time
        if (5 < elapsed_time):
            timeout_detected = True
            self.__restart_timer()

        else:
            timeout_detected = False

        return timeout_detected
