#!/usr/bin/env python

import time

import state as state
import dev.display.Console as Console
import dev.input as input


class Init(state.IState):

    def entry(self):
        state.CommonResource.initialize()
        self.__key_pressed_monitor = input.KeyPressedMonitor()
        Console.clear()
        Console.puts("備品管理システムにようこそ")
        Console.puts("何かキーを押すとサービスを開始します")

    def do(self):
        self.__key_pressed_monitor.capture()

    def exit(self):
        pass

    def next(self):
        if self.__key_pressed_monitor.is_pressed_escapekey():
            return state.PreExit()
        else:
            return state.StandbyUserIdInput()

    def event(self):
        return self.__key_pressed_monitor.is_pressed_anykey()

