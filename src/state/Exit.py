#!/usr/bin/env python


import state as state
import dev.display.Console as Console

class Exit(state.IState):

    def entry(self):
        Console.puts("プログラムを終了します")

    def do(self):
        pass

    def exit(self):
        pass

    def next(self):
        return state.Exit()

    def event(self):
        return False

