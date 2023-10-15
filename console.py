#!/usr/bin/python3
"""
Module console.py

This module will be described below
"""

import cmd
import importlib
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class contains methods that help for interacting with
    the interpreter
    """
    prompt = "(hbnb)"
    __base_model = importlib.import_module("models.base_model")
    __user = importlib.import_module("models.user")
    __place = importlib.import_module("models.place")
    __state = importlib.import_module("models.state")
    __city = importlib.import_module("models.city")
    __amenity = importlib.import_module("models.amenity")
    __review = importlib.import_module("models.review")
    show_all = storage.all()

    def emptyline(self):
        """when it's empty line do nothing
        """
        pass

    def do_create(self, class_name):
        """Creates a new instance of a class and save it as json file"""
        if self.check_module(class_name.split()):
            class_created = (self.get_attribute(class_name))()
            print(class_created.id)
            class_created.save()

    def do_show(self, args):
        """shows string representation of instance using class name, id
        """
        args = args.split()
        if self.check_module(args):
            if self.check_id(args):
                key_obj = f"{args[0]}.{args[1]}"
                print(HBNBCommand.show_all[key_obj])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args = args.split()
        if self.check_module(args):
            if self.check_id(args):
                key_obj = f"{args[0]}.{args[1]}"
                del HBNBCommand.show_all[key_obj]
                storage.new(HBNBCommand.show_all)
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances of class
        """
        arg = arg.split()
        class_list = list(map(lambda key: key.split(".")[0],
                              HBNBCommand.show_all.keys()))
        list_obj = []
        for key in HBNBCommand.show_all.keys():
            if len(arg) == 1:
                if arg[0] in class_list:
                    if arg[0] == key.split('.')[0]:
                        key_value = f"{arg[0]}.{key.split('.')[1]}"
                        list_obj.append(str(HBNBCommand.show_all[key_value]))
                else:
                    print("** class doesn't exist **")
                    break
            else:
                list_obj.append(str(HBNBCommand.show_all[key]))
        if len(list_obj) > 0:
            print(list_obj)

    def do_update(self, args):
        """This method will update instances and save them
        """
        args = args.split()
        if self.check_module(args):
            if self.check_id(args):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                elif len(args) >= 4:
                    key = f"{args[0]}.{args[1]}"
                    setattr(HBNBCommand.show_all[key], args[2], args[3])
                    storage.new(HBNBCommand.show_all[key])
                    storage.save()

    def do_quit(self, line):
        """This command quit command interpreter, to quit write quit
        """
        return True

    def do_EOF(self):
        """Exit the program"""
        return True

    def check_module(self, args):
        """This module will check if the class name pressent in the module

        Args:
            class_name (str): contain the class name
        """
        if len(args) <= 0:
            print("** class name missing **")
            return False
        elif hasattr(HBNBCommand.__base_model, args[0]):
            return True
        elif hasattr(HBNBCommand.__user, args[0]):
            return True
        elif hasattr(HBNBCommand.__place, args[0]):
            return True
        elif hasattr(HBNBCommand.__state, args[0]):
            return True
        elif hasattr(HBNBCommand.__city, args[0]):
            return True
        elif hasattr(HBNBCommand.__amenity, args[0]):
            return True
        elif hasattr(HBNBCommand.__review, args[0]):
            return True
        else:
            print("** class doesn't exist **")
            return False

    def check_id(self, args):
        """This will check if the id present in the instance

        Args:
            args (str): value contain the id

        Returns:
            bool: return true if preset false if not
        """
        if len(args) >= 2:
            key_list = list(map(lambda key: key.split(".")[1],
                                HBNBCommand.show_all.keys()))
            if args[1] in key_list:
                return True
            else:
                print("** no instance found **")
                return False
        else:
            print("** instance id missing **")
            return False

    def get_attribute(self, args):
        """This method will set the instance of the class

        Args:
            class_name (str): the name of the class

        Retruns:
            object : will return instace of class
        """
        args = args.split()
        if hasattr(HBNBCommand.__base_model, args[0]):
            return getattr(HBNBCommand.__base_model, args[0])
        elif hasattr(HBNBCommand.__user, args[0]):
            return getattr(HBNBCommand.__user, args[0])
        if hasattr(HBNBCommand.__place, args[0]):
            return getattr(HBNBCommand.__place, args[0])
        elif hasattr(HBNBCommand.__city, args[0]):
            return getattr(HBNBCommand.__city, args[0])
        elif hasattr(HBNBCommand.__state, args[0]):
            return getattr(HBNBCommand.__state, args[0])
        if hasattr(HBNBCommand.__amenity, args[0]):
            return getattr(HBNBCommand.__amenity, args[0])
        elif hasattr(HBNBCommand.__review, args[0]):
            return getattr(HBNBCommand.__review, args[0])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
