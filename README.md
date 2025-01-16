The AirBnb clone Project is a software development project that teaches programming and system design. It emulates the features of the AirBnb platform, focusing on backend development, Data management and user interface. The project introduces students to different features namely Object Oriented Programming, Command Line interfaces and Frontend to Backend Interaction. It is divided into several phases which gradually builds a fully functional web application.

The Command Interpreter provides a CLI tool to manage the data system.

How to start it:
clone the repository: https://github.com/milkakeza/alu-AirBnB_clone.git

Navigate to the project directory 

run the console.py file or run this command ./console.py

how to use it:
There are different functions this AirBnb clone provides which are create, show, destroy, all, update.
To use, all you have to do is type in whatever feature you want. to create a basemodel, you have to type "create BaseModel" and a basemodel will be created and if you want to make any changes to the basemodel, all you have to do is type out one of the features with the basemodel id you got after creating the basemodel next to it. for examnple "show Basemodel <id>" or "destroy Basemodel <id>"


example:
create BaseModel
17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d

show BaseModel 17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d
[BaseModel] (17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d) {'id': '17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d', 'created_at': datetime.datetime(2025, 1, 17, 0, 3, 53, 566962), 'updated_at': datetime.datetime(2025, 1, 17, 0, 3, 53, 566975)}

update BaseModel 17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d first_name "Kolade"

destroy BaseModel 17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d

show BaseModel 17c5a8a8-feef-4eb1-b1c3-ffe5dfa6144d
** no instance found **
