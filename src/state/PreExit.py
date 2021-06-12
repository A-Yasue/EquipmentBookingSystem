#!/usr/bin/env python


import time
import state as state
import dev.display.Console as Console
import dev.input as input


class PreExit(state.IState):

    def entry(self):
        state.CommonResource.initialize()
        self.__key_pressed_monitor = input.KeyPressedMonitor()
        Console.puts("エントランスでESCキーが入力されました。")
        Console.puts("タイムアウト前にもう一度ESCキーを入力すると完全にプログラムを終了します。")

    def do(self):
        self.__key_pressed_monitor.capture()

    def exit(self):
        pass

    def next(self):
        if self.__key_pressed_monitor.is_pressed_escapekey():
            return state.Exit()
        else:
            return state.Init()

    def event(self):
        return self.__key_pressed_monitor.is_pressed_anykey()

