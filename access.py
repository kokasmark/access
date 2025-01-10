import os
import json
from blessed import Terminal
import time
import re
import subprocess
import sys
from utils import *

from display import display
from display_tag_content import display_tag_content
from display_folder_content import display_folder_content

term = Terminal()


class Access():
    structure = {
        "tags": []
    }

    display = display
    display_tag_content = display_tag_content
    display_folder_content = display_folder_content

    def __init__(self):
        program_folder = os.path.dirname(os.path.abspath(__file__))
        if program_folder not in os.environ["PATH"]:
            self.render_tag("Access added to PATH!",Color.CVIOLET)
            os.environ["PATH"] += os.pathsep + program_folder
            sys.path.append(program_folder)
            time.sleep(1)

        self.load_structure()
        display(self, term)
        pass
    
    def visible_length(self,text):
        """Calculate the visible length of a string, ignoring terminal escape sequences."""
        ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        return len(ansi_escape.sub('', text))
    def render_tag(self,tag: str, color: Color, textColor = Color.CWHITE2, hasSymbol = False,offset = 0) -> str:
        tag_length = self.visible_length(tag) + (1 if hasSymbol else 0)+offset
        line = "─" * (tag_length + 2)
        if textColor is Color.CWHITE2:
            textColor = Color.contrast_map.get(color)
        render = (
            f"{color}╭{line}╮\n"
            f"│ {textColor+tag+color} │\n"
            f"╰{line}╯{Color.CEND}"
        )
        return render
    
    def action_open_folder(self,path):
        """Opens the selected folder in the file explorer."""
        if os.path.isdir(path):
            os.startfile(path)
        else:
            print(f"The path '{path}' is not a valid folder.")

    def action_run(self,path):
        """Runs the selected target file."""
        if os.path.isfile(path):
            try:
                subprocess.run(path, check=True, shell=True)
            except Exception as e:
                print(f"Failed to run '{path}': {e}")
        else:
            print(f"The path '{path}' is not a valid file.")

    def action_code(self,path):
        """Opens the selected folder or file in Visual Studio Code."""
        try:
            subprocess.run(["code", path], check=True)
        except FileNotFoundError:
            print("Visual Studio Code is not installed or 'code' is not in PATH.")
        except Exception as e:
            print(f"Failed to open '{path}' in VS Code: {e}")

    def action_remove(self,target):
        pass

    def load_structure(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        structure_path = os.path.join(script_dir, "structure.json")
        with open(structure_path,"r") as f:
            self.structure = json.loads(f.read())

    def save_structure(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        structure_path = os.path.join(script_dir, "structure.json")
        with open(structure_path,"w") as f:
            f.write(json.dumps(self.structure))
    
if __name__ == "__main__":
    os.system("")
    access = Access()