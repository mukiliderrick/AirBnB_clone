#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import shlex
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def help_quit(self):
        """Help information for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for the EOF command"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = models.storage.all()
        for key, value in instances.items():
            if class_name in key and instance_id in key:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = models.storage.all()
        for key, value in instances.items():
            if class_name in key and instance_id in key:
                del instances[key]
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        args = shlex.split(args)
        instances = models.storage.all()
        if len(args) == 0:
            print([str(v) for v in instances.values()])
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return




if __name__ == '__main__':
    HBNBCommand().cmdloop()
