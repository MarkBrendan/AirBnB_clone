#!/usr/bin/python3
""" Command interpreter module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command processor"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        "Exit from the program with quit"
        return True

    def do_EOF(self, line):
        "Exit from the program with ctrl+D"
        return True

    def emptyline(self):
        """do nothing when an empty line is enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
