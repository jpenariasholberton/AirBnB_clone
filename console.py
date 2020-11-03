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
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCOmmand
    """
    prompt = '(hbnb)'
    file_path = "file.json"
    name_class = {'BaseModel': BaseModel,
                  'User': User, 'State': State,
                  'City': City, 'Place': Place,
                  'Amenity': Amenity, 'Review': Review}

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
            print("** class doesn't exist **")
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
                objectToUpdate.__dict__[args[2]] = eval(args[3])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def default(self, line):
        """
        """
        if not '.' in line:
            print("*** Unknown syntax: " + line)
            return
        No_commands = {"all()": self.do_all, "count()": self.do_count}
        args = line.split(".")
        if args[0] not in self.name_class:
            print("*** Unknown syntax: " + line)
        elif len(args) != 2:
            print("*** Unknown syntax: " + line)
        else:
            if args[1] in No_commands:
                No_commands[args[1]](args[0])
    
    def do_count(self, arg):
        """
        """
        No_count = 0
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if arg in obj.__str__():
                No_count += 1
        print(No_count)

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
