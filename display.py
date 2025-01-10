from utils import *
def display(self,term):
    """Display tags interactively using blessed."""
    selected_index = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.move(0, 0) + self.render_tag(f"Access - Files simply and fast",Color.CBLUE2))
            print(self.render_tag(f"{Color.CGREEN2}{Symbols.UP_ARROW}{Symbols.DOWN_ARROW}{Color.CEND} Scroll | {Color.CRED2}{Symbols.ESC}{Color.CEND} Exit/Cancel | {Color.CBLUE2}{Symbols.ENTER}{Color.CEND} Select/Save",Color.CWHITE2,hasSymbol=True,offset=-1))


            tags = self.structure["tags"][:]
            tags.append({"title": f"New Tag", "color":Color.CBLUE2, "files": [], "folders": []})
            for i, tag in enumerate(tags):
                y_position = i * 3 + 7

                for ii in range(3):
                    print(term.move(y_position+ii, 0) + " " * 100)
                if i == selected_index:
                    if i != len(tags)-1 :
                        print(term.move(y_position, 0) + Color.CBLINK2+self.render_tag(f'{tag["title"]} - {len(tag["folders"])} folders | {len(tag["files"])} files', tag["color"]))
                    else:
                        print(term.move(y_position, 0) + self.render_tag(f'{tag["title"]} - Create a new category', tag["color"],tag["color"]))
                else:
                    print(term.move(y_position, 0) + self.render_tag(tag["title"], tag["color"]))

            key = term.inkey(timeout=0.1)

            if key.name == "KEY_UP" and selected_index > 0:
                selected_index -= 1
            elif key.name == "KEY_DOWN" and selected_index < len(tags) - 1:
                selected_index += 1
            elif key.name == "KEY_ENTER":
                if selected_index != len(tags)-1:
                    self.display_tag_content(term,self.structure["tags"][selected_index])
                    print(term.clear)
                
                else:
                    new_tag_name = "New Tag"
                    cursor_position = len(new_tag_name)
                    colors = [Color.CRED,Color.CRED2,Color.CGREEN,Color.CGREEN2,Color.CBLUE,Color.CBLUE2, Color.CBEIGE, Color.CBEIGE2, Color.CYELLOW, Color.CYELLOW2,Color.CVIOLET,Color.CVIOLET,Color.CGREY]
                    selected_color = 0
                    while True:
                        for ii in range(3):
                            print(term.move(y_position+ii, 0) + " " * 50)

                        
                        y_position = selected_index * 3 + 3+ 5
                        for i,color in enumerate(colors):
                            if i != selected_color:
                                print(term.move(y_position-1, i*2+1) + color+Symbols.BLOCK+Color.CEND)
                            else:
                                print(term.move(y_position-1, i*2+1) + Color.CBLINK+color+Symbols.BLOCK+Color.CEND)

                        print(term.move(y_position-1, len(colors)*2+1) + f"{Color.CGREEN2}{Symbols.LEFT_ARROW} {Symbols.RIGHT_ARROW}{Color.CEND} Select Color")

                        print(term.move(y_position, 0) + " " * 50)
                        print(term.move(y_position, 0) + self.render_tag(new_tag_name, colors[selected_color]))

                        key = term.inkey()

                        if key.name == "KEY_ENTER" and new_tag_name.strip():
                            new_tag = {"title": new_tag_name.strip(), "color": colors[selected_color], "files": [], "folders": []}
                            self.structure["tags"].append(new_tag)
                            self.save_structure()
                            break
                        elif key.name == "KEY_ESCAPE":
                            print(term.clear)
                            break
                        elif key.name == "KEY_BACKSPACE" and cursor_position > 0:
                            new_tag_name = new_tag_name[:cursor_position - 1] + new_tag_name[cursor_position:]
                            cursor_position -= 1
                        elif key.isprintable():
                            new_tag_name = new_tag_name[:cursor_position] + key + new_tag_name[cursor_position:]
                            cursor_position += 1  

                        elif key.name == "KEY_LEFT" and selected_color > 0:
                            selected_color -= 1
                        elif key.name == "KEY_RIGHT" and selected_color < len(colors)-1:
                            selected_color += 1

            elif key.name == "KEY_ESCAPE":
                return None            
                    