#!/usr/bin/bash

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A command line interface (CLI) for the HBNB project."""
    prompt = '(hbnb) '
    valid_classes = ['BaseModel']


    def do_EOF(self, line):

        """
        Handles the EOF signal (Ctrl+D in Unix, Ctrl+Z in Windows)

        Returns:
            bool: True
        """
        return True

    def do_quit(self, line):        
        """
        Handles the 'quit' command.
        Args:
        line (str): The command line input (not used).
        Returns:
        bool: True, indicating the command loop should terminate.
        """
        return True

        def do_create(self, arg):
            """
            Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
            """
            command = shlex.split(arg)
    
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

        def do_show(self, arg):
            """
            Prints the string representation of an instance based on the class name and id.
            """
            command = shlex.split(arg)
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
            else:
                objects= storage.all()
                key = "{}.{}".format(command[0], command[1])
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

        def do_destroy(self, arg):
            """
            Deletes an instance based on the class name and id
            """
            command = shlex.split(arg)
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in HBNBCommand.valid_classes:
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
            """
            Prints all string representation of all instances based or not on the class name.
            """
            objects = storage.all()
            command = shlex.split(arg)
            if len(command) == 0:
                for key, value in objects.items():
                    print(str(value))
            elif command[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                for key, value in objects.items():
                    if key.split('.')[0] == command[0]:
                        print(str(value))

        def do_update(self, arg):
            """
            Updates an instance based on the class name and id by adding or updating attribute
            """
            command = shlex.split(arg)
            if len(command) == 0:
                print("** class name missing **")
            elif command[0] not in HBNBCommand.valid_classes:
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



    def do_help(self, line):
        """
        Handles the 'help' command.
        Args:
        line (str): The command line input (not used).
        Returns:
        None
        """
        return super().do_help(line)

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        Default behavior is to repeat the last nonempty command. We override
        this behavior to do nothing.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    