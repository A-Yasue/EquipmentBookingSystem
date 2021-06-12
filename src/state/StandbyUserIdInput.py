#!/usr/bin/env python



import state as state
import dev.display.Console as Console
import dev.input as input

class StandbyUserIdInput(state.IState):
    def entry(self):
        Console.clear()
        Console.puts("社員証をかざしてください")
        Console.puts(">", end="")
        self.__input = input.UserInputReader()
        self.__next = state.ErrorWasOccurredInStandByUserIdInput()

    def do(self):
        self.__input.capture()

    def exit(self):
        employee_id = self.__input.get_string()
        if (employee_id != ""):
            Console.puts("社員番号「", employee_id, "」を問い合わせます")

            if (employee_id == "0079522"):
                state.CommonResource.employeeId = employee_id

            # 現状は未実装なので必ず失敗
            self.__next = state.ErrorWasOccurredInStandByUserIdInput()
        else:
            self.__next = state.StandbyUserIdInput()

    def next(self):
        return self.__next

    def event(self):
        return self.__input.submitted()
