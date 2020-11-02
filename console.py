#!/usr/bin/python3
"""
Program called console.py that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCOmmand
    """
    prompt = '(hbnb)'
    file_path = "file.json"
    name_class = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """
        """
        return True

    def do_create(self, arg):
        """
        """
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.name_class:
            print("** class doesn exist **")
        else:
            new_obj = self.name_class[args[0]]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        """
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.name_class:
            print("** class doesn't exist **")
        elif len(args)== 1:
            print("** instance id missing **")
        else:
            print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()