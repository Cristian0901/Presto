#!/usr/bin/python

from sys import argv
from json import dump
from shutil import copytree
from tabulate import tabulate
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)


def error(arg: str): print(Fore.RED + Style.BRIGHT + f"[ERROR]: {arg}")


def user_help():
    head = ["Command", "Arguments", "Description"]
    commands = []
    for command in command_palette.values():
        commands += [[command["name"],
                      command["arguments"], command["description"]]]

    print(tabulate(commands, headers=head))


def query_data() -> dict:
    data = {}
    
    data["name"] = input(Fore.YELLOW + "Project name: " + Style.RESET_ALL)
    data["path"] = f'{input(Fore.YELLOW + "Project path: " + Style.RESET_ALL)}/{data["name"]}/'
    data["version"] = input(Fore.YELLOW + "Project version: " + Style.RESET_ALL)
    data["author"] = input(Fore.YELLOW + "Project author: " + Style.RESET_ALL)

    data["creation date"] = datetime.now().strftime("%d/%m/%Y")

    data["nid"] = str(hash((data.values())))

    return data

def create_project():
    project_data = query_data()
    print(project_data)

    replace_words = {
        "[[{Project Name}]]": project_data["name"],
        "[[{Project Author}]]": project_data["author"]
    }

    if project_data["name"] == "" or project_data["path"] == "":
        error("Name or path not specificated")
        return

    for index in prog_langs:
        print(
            Fore.YELLOW + f"{index}" + " --- " + Fore.GREEN + f"{prog_langs[index]['name']}")

    try:
        user_input = int(
            input(Fore.YELLOW + "Choice an option: " + Style.RESET_ALL))

    except ValueError:
        error("Invalid option")

    copytree(prog_langs[user_input]["path"],
             f"{project_data['path']}/{project_data['name']}/")

    # customing files ".md"
    with open(f"{project_data['path']}/{project_data['name']}/readme.md", "r") as file:
        data = file.read()

        for key in replace_words.keys():
            data = data.replace(key, replace_words[key])
        #print(data)

    with open(f"{project_data['path']}/{project_data['name']}/docs/index.md", "r") as file:
        data = file.read()

        for key in replace_words.keys():
            data = data.replace(key, replace_words[key])
        #print(data)
        
    with open(f"{project_data['path']}/{project_data['name']}/settings/settings.json", "w") as file:
        dump(project_data, file)

def menu():
    deprecate_commands = ["other"]

    for index in command_palette:
        if command_palette[index]['name'] in deprecate_commands:
            print(
                Fore.YELLOW + f"{index}" + " --- " + Fore.RED + f"{command_palette[index]['name']}")

        else:
            print(
                Fore.YELLOW + f"{index}" + " --- " + Fore.GREEN + f"{command_palette[index]['name']}")

    try:
        user_input = int(
            input(Fore.YELLOW + "Choice an option: " + Style.RESET_ALL))

        if command_palette[user_input]['name'] in deprecate_commands:
            error("Command deprecate or unable...")
        else:
            command_palette[user_input]["command"]()
    except ValueError:
        error("Invalid option")

command_palette: dict[int, dict[str:"name", str:"function"]] = {
    1: {"name": "help",
        "command": user_help,
        "arguments": "...",
        "description": "Show this message"},

    2: {"name": "create",
        "command": create_project,
        "arguments": "name: string",
        "description": "Create a project"},

    3: {"name": "other",
        "command": lambda: print(len(range(10))),
        "arguments": "...",
        "description": "Show 10"},
}

prog_langs = {
    1: {"name": "Python",
        "path": "./templates/python/"}}
"""
    2: {"name": "Rust",
        "path": "./templates/rust/"},

    3: {"name": "C/C++",
        "path": "./templates/c\c++/"},

    4: {"name": "Shell",
        "path": "./templates/shell/"},

    5: {"name": "Nim",
        "path": "./templates/nim/"}
"""

# Start program
menu()
#print(argv)