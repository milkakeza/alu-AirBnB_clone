#!/usr/bin/python3

import cmd
"""
A command line interface (CLI) for the HBNB project.
"""

class HBNBCommand(cmd.Cmd):
    """A command line interface (CLI) for the HBNB project."""
    prompt = '(hbnb) '

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
