class Interpreter:
    def __init__(self, code):
        self.commands = code.splitlines()
        self.current_command_index = 0

    def execute_next_command(self, creep):
        if self.current_command_index < len(self.commands):
            commands = self.commands[self.current_command_index]
            command = commands[0]
            value = commands[1:]
            if command == "move":  # creep的移动
                creep.move(value)
            elif command == "goto":  # 语句的跳转
                line_number = int(value)
                if line_number < len(self.commands) and line_number >= 0:
                    self.current_command_index = line_number - 2
            self.current_command_index += 1
        if self.current_command_index >= len(self.commands):  # 运行到结尾返回第一句
            self.current_command_index = 0
