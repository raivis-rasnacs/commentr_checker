import sys
from rich import print as richprint

args = sys.argv

def open_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.readlines()
    except:
        print("Can not open file!")
        return None

def check_single_function(comment_line, line_number, function_name):
    if "#" in comment_line:
        if len(comment_line) > 10: # good comment is at least 10 symbols
            richprint(f"Function {function_name.strip()[4:-1]}\n[green]Comment is okay[/green]")
        else:
             richprint(f"Function {function_name.strip()[4:]}\n[yellow]Comment is too short[/yellow]")
    else:
        richprint(f"Function {function_name.strip()[4:]}\n[red]No comment found[/red]")

def look_for_functions(file_content):
    for line_number, line in enumerate(file_content, start=1):
        if "def " in line:
            check_single_function(
                file_content[line_number - 2], 
                line_number,
                function_name = line)

if len(args) > 1:
    file_names = args[1:]

    for file_name in file_names:
        if not file_name.endswith(".py"):
            print(f"{file_name} is not a valid python file name")
            continue

        print(f"Checking {file_name}...")
        file_content = open_file(file_name)
        if not file_content:
            continue

        look_for_functions(file_content)
        print("File check done\n--------------")
