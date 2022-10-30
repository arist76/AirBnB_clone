#!/usr/bin/env python3
"""
"""
from ast import arg
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import shlex


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnB console v0.1\nType "?" for more information'
    prompt = "(hbnb) "

    ALL_MODELS = ["BaseModel"]

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
        print(f"Quit command that ends the program")

    def do_create(self, arg):
        """Creates an instance according to a given class"""

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.ALL_MODELS:
            print("** class doesn't exist **")
        else:
            dct = {"BaseModel": BaseModel}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def help_create(self):
        print(
            """
Takes a class name and creates and saves a new object then returns the id of the object. 
for e.g :
    ... 
    (hbnb) create BaseModel
    423a64b0-1fff-43b3-90c7-6fe130390ce8
    ...
"""
        )

    def do_show(self, arg):
        """Shows string representation of an instance passed"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")

        if args[0] not in HBNBCommand.ALL_MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def help_show(self):
        pass

    def do_destroy(self, arg):
        """Deletes an instance passed"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")

        if args[0] not in HBNBCommand.ALL_MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string represention of all instances of a given class"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")

        if args[0] not in HBNBCommand.ALL_MODELS:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(","):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.ALL_MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
