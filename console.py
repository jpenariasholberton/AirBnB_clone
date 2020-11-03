#!/usr/bin/python3
"""
Program called console.py that contains the entry
point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCOmmand
    """
    prompt = '(hbnb)'
    file_path = "file.json"
    name_class = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """
        This method a command to exit of the program
        """

        return True

    def emptyline(self):
        """
        This method to pass when the prompt is empty
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
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
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split(" ")
        valueFounded = []
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.name_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, obj in all_objs.items():
                if key == (args[0] + '.' + args[1]):
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.name_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, obj in all_objs.items():
                if key == (args[0] + '.' + args[1]):
                    del storage.all()[key]
                    storage.save()
                    storage.reload()
                    return
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split(" ")
        my_list = []
        all_objs = storage.all()
        if len(args[0]) == 0:
            for key, obj in all_objs.items():
                my_list.append(obj.__str__())
            print(my_list)
        elif args[0] not in self.name_class:
            print("** class doesn't exist **")
        else:
            for key, obj in all_objs.items():
                my_list.append(obj.__str__())
            print(my_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.name_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            try:
                objectToUpdate = all_objs[args[0] + '.' + args[1]]
                objectToUpdate.__dict__[args[2]] = args[3]
                storage.save()
            except KeyError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
