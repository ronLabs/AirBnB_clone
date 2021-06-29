#!/usr/bin/python3
""" main program executable """

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    prompt = '(hbnb)'

    def emptyline(self):
        """ override emptyline func """
        pass

    def do_quit(self, arg):
        """ Close """
        exit()

    def do_EOF(self, arg):
        """ close """
        exit()

    def help_EOF(self):
        """ eof help """
        print("Quit command to exit program:\n")

    def do_create(self, arg):
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
