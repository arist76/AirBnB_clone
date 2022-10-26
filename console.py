#!/usr/bin/env python3
"""
"""
import cmd


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnB console v0.1\nType "?" for more information'
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def default(self, line: str):
        print(f"Command not found: {line} is not defined")

    def do_EOF(self, arg):
        exit()

    def help_EOF(self):
        print(f"Ends the program")

    def do_quit(self, arg):
        exit()

    def help_quit(self):
        print(f"Ends the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
