#!/usr/bin/env python3

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """A command line interface (CLI) for the HBNB project."""
    prompt = '(hbnb) '
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
    }

    def do_EOF(self, line):
        """Handles the EOF signal to exit the program."""
        return True

    def do_quit(self, line):
        """Handles the 'quit' command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class."""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.valid_classes[command[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
    """Deletes an instance based on class name and id."""
    command = shlex.split(arg)
    if len(command) == 0:
        print("** class name missing **")
    elif command[0] not in self.valid_classes:
        print("** class doesn't exist **")
    elif len(command) < 2:
        print("** instance id missing **")
    else:
        objects = storage.all()
        key = "{}.{}".format(command[0], command[1])
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objects = storage.all()
        command = shlex.split(arg)
        if len(command) == 0:
            for obj in objects.values():
                print(str(obj))
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in objects.items():
                if key.split('.')[0] == command[0]:
                    print(str(obj))

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        command = shlex.split(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = command[2]
                attr_value = command[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def emptyline(self):
        """Does nothing on an empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

