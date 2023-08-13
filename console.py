#!/usr/bin/env python3
"""Command interpreter for AirBnB Clone project."""

import re
import json
from shlex import split
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for HBNB project."""

    prompt = "(hbnb) "

    class_names = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle Ctrl+D to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in storage.all():
            storage.all().pop(obj_key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objects.values()
               if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[obj_key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_count(self, arg):
        """Count the number of instances of a class."""
        args = arg.split()
        if not args or args[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        count = len([obj for obj in storage.all().values()
                     if obj.__class__.__name__ == args[0]])
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
