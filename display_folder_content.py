from utils import *
import os
def display_folder_content(self,term, tag): 
    selected_index = 0
    items_per_page = term.height//3 -3

    combined_items = os.listdir(os.getcwd())

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.move(0, 0) + self.render_tag(f'{os.getcwd()}', Color.CRED2, Color.CRED2))
            print(self.render_tag(f"{Color.CGREEN2}{Symbols.UP_ARROW}{Symbols.DOWN_ARROW}{Color.CEND} Scroll | {Color.CRED2}{Symbols.ESC}{Color.CEND} Save | {Color.CBLUE2}{Symbols.ENTER}{Color.CEND} Select",Color.CWHITE2,hasSymbol=True,offset=-1))
            for i in range(selected_index, selected_index + items_per_page):
                item_index = i
                y_position = (i - selected_index) * 3 + 7


                for ii in range(3):
                    print(term.move(y_position + ii, 0) + " " * 100)

                if i < len(combined_items):
                    item_title = combined_items[item_index]
                    is_folder = os.path.isdir(item_title)

                    item_path = combined_items[item_index]

                    display_title = item_title
                    for folder in tag["folders"]:
                        if folder["name"] == item_path:
                            display_title = f"+ {item_title}"
                            break

                    if display_title == item_title:
                        for file in tag["files"]:
                            if file["name"] == item_path:
                                display_title = f"+ {item_title}"
                                break

                    if not is_folder:
                        display_title += f" ({os.path.splitext(item_title)[1]})"

                    if item_index == selected_index:
                        print(term.move(y_position, 0) + Color.CBLINK2+self.render_tag(display_title, tag["color"]))
                    else:
                        print(term.move(y_position, 0) + self.render_tag(display_title, tag["color"], hasSymbol=False))

            key = term.inkey(timeout=0.1)

            if key.name == "KEY_UP" and selected_index > 0:
                selected_index -= 1
            elif key.name == "KEY_DOWN" and selected_index < len(combined_items) - 1:
                selected_index += 1
            elif key.name == "KEY_ENTER":
                selected_item = combined_items[selected_index]
                is_folder = os.path.isdir(selected_item)

                item = {"name": selected_item, "path": os.path.join(os.getcwd(),selected_item)}

                if is_folder:
                    if selected_item in tag["folders"]:
                        tag["folders"].remove(item)
                    else:
                        tag["folders"].append(item)
                else:
                    if selected_item in tag["files"]:
                        tag["files"].remove(item)
                    else:
                        tag["files"].append(item)

                self.save_structure()
            elif key.name == "KEY_ESCAPE":
                return None