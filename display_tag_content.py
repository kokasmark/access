from utils import *
def display_tag_content(self, term,tag):
    """Display folders and files interactively using blessed."""
    selected_index = 0
    selected_action = 0
    items_per_page = term.height//3 -3

    opened_menu = False

    combined_items = [f"{Symbols.PLUS}Add to Category"] + tag["folders"] + tag["files"]

    run_action = []

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.move(0, 0) + self.render_tag(f'{tag["title"]} - {len(tag["folders"])} folders | {len(tag["files"])} files', tag["color"], tag["color"]))
            print(self.render_tag(f"{Color.CGREEN2}{Symbols.UP_ARROW}{Symbols.DOWN_ARROW}{Color.CEND} Scroll | {Color.CGREEN2}{Symbols.LEFT_ARROW} {Symbols.RIGHT_ARROW}{Color.CEND} Select Action | {Color.CRED2}{Symbols.ESC}{Color.CEND} Save | {Color.CBLUE2}{Symbols.ENTER}{Color.CEND} Select",Color.CWHITE2,hasSymbol=True,offset=-1))
            
            for i in range(selected_index,selected_index+items_per_page):
                item_index = (i)
                y_position = (i-selected_index) * 3 + 7
                for ii in range(3):
                    print(term.move(y_position+ii, 0) + " " * 100)

                if i < len(combined_items):
                    item_title = combined_items[item_index]
                    if i != 0:
                        item_title = combined_items[item_index]["name"]
                        if combined_items[item_index] in tag["folders"]:
                            item_title = f"{Symbols.FOLDER} {item_title}"
                        else:
                            item_title = f"{Symbols.FILE} {item_title}"
                        if item_index == selected_index:
                            t = self.render_tag(item_title, tag["color"], tag["color"],True)
                            open = self.render_tag(f'{Symbols.OPEN_FOLDER} Open folder', Color.CBLUE2, hasSymbol=True)
                            run = self.render_tag(f'{Symbols.RUN} Run', Color.CGREEN2)
                            remove = self.render_tag(f'- Remove', Color.CRED2)
                            code = self.render_tag(f'{Symbols.PENCIL} Code', Color.CBEIGE2)

                            actions = [open,run,code,remove]
                            run_action = [self.action_open_folder, self.action_run, self.action_code, self.action_remove]
                            if combined_items[item_index] in tag["folders"]:
                                actions.remove(run)
                                run_action.remove(self.action_run)
                            else:
                                actions.remove(open)
                                run_action.remove(self.action_open_folder)

                            if not opened_menu:
                                print(term.move(y_position, 0) + Color.CBLINK2+t)
                            else:
                                print(term.move(y_position, 0) + actions[selected_action])
                        else:
                            print(term.move(y_position, 0) + self.render_tag(item_title, tag["color"],hasSymbol=True))
                    else:
                        print(term.move(y_position, 0) + self.render_tag(item_title, tag["color"], tag["color"],True))

            key = term.inkey(timeout=0.1)

            if key.name == "KEY_UP" and selected_index > 0:
                opened_menu = False
                selected_action = 0
                selected_index -= 1
            elif key.name == "KEY_DOWN" and selected_index < len(combined_items) - 1:
                opened_menu = False
                selected_action = 0
                selected_index += 1
            elif key.name == "KEY_ENTER":
                if selected_index != 0:
                    if opened_menu:
                        run_action[selected_action](combined_items[selected_index]["path"])
                        opened_menu = False     
                else:
                    self.display_folder_content(term,tag)
                    return None
            elif key.name == "KEY_ESCAPE":
                return None
            
            if key.name == "KEY_LEFT" and selected_action > 0:
                if not opened_menu:
                    opened_menu = True
                else:
                    selected_action -= 1
            elif key.name == "KEY_RIGHT" and selected_action < 2:
                if not opened_menu:
                    opened_menu = True
                else:
                    selected_action += 1