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
    __base_module = importlib.import_module("models.base_model")

    def do_create(self, class_name):
        """Creates a new instance of a class and save it as json file"""
        if hasattr(HBNBCommand.__base_module, class_name):
            class_new = getattr(HBNBCommand.__base_module, class_name)
            class_created = class_new()
            class_created.save()
        elif not name_class:
            print("** class name missing **")
        elif (hasattr(HBNBCommand.__base_module, name_class)) is not True:
            print("** class doesn't exist **")

    def do_show(self, args):
        """shows string representation of instance using class name, id
        """
        args = args.split()
        if len(args) > 0:
            class_name = args[0]
            if hasattr(HBNBCommand.__base_module, class_name):
                if len(args) > 1:
                    class_id = args[1]
                    class_obj = storage.all()
                    key_list = class_obj.keys()
                    key_list = list(map(lambda key: key.split(".")[1], key_list))
                    key_obj = f"{class_name}.{class_id}"
                    if class_id in key_list:
                        print(class_obj[key_obj])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args = args.split()
        if len(args) > 0:
            class_name = args[0]
            if hasattr(HBNBCommand.__base_module, class_name):
                if len(args) > 1:
                    class_id = args[1]
                    class_obj = storage.all()
                    key_list = list(map(lambda key: key.split(".")[1], class_obj.keys()))
                    key_obj = f"{class_name}.{class_id}"
                    if class_id in key_list:
                        del class_obj[key_obj]
                        storage.new(class_obj)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
           
    def do_quit(self, line):
        """This command quit command interpreter, to quit write quit
        """
        return True

    def do_EOF(self):
        """Exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
