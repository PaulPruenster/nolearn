import curses
import os
import json

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_GREEN)

    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.erase()

    # check if the file exists, if yes, load the data from it
    if os.path.isfile("learning_list.json"):
        with open("learning_list.json", "r") as f:
            data = json.load(f)
            learning_list = data["learning_list"]
            current_index = data["current_index"]
            states = data["states"]
    else:
        learning_list = []
        current_index = 0
        states = ["todo", "seen", "done"]

    while True:
        stdscr.erase()
        stdscr.addstr(0, 0, "Things to Learn:")
        for i, item in enumerate(learning_list):
            if i == current_index:
                if item['state'] == 'todo':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(4))
                elif item['state'] == 'seen':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(5))
                elif item['state'] == 'done':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(6))
            else:
                if item['state'] == 'todo':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(1))
                elif item['state'] == 'seen':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(2))
                elif item['state'] == 'done':
                    stdscr.addstr(i + 1, 0, f"({item['state']}) {item['item']}", curses.color_pair(3))

        stdscr.addstr(len(learning_list)+1, 0, "Press 'a' to add an item, 'd' to delete an item, 'q' to quit")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            # save the data to the file
            data = {"learning_list": learning_list, "current_index": current_index, "states": states}
            with open("learning_list.json", "w") as f:
                json.dump(data, f)
            break
        elif key == ord("a"):
            stdscr.addstr(len(learning_list)+2, 0, "Enter the item:")
            stdscr.refresh()
            curses.echo()
            item = stdscr.getstr().decode("utf-8")
            curses.noecho()
            learning_list.append({"item": item, "state": states[0]})

        elif key == ord("d"):
            if len(learning_list) > 0:
                del learning_list[current_index]
                if current_index == len(learning_list):
                    current_index -= 1

        elif key == curses.KEY_UP:
            if current_index > 0:
                current_index -= 1

        elif key == curses.KEY_DOWN:
            if current_index < len(learning_list) - 1:
                current_index += 1 

        elif key in (ord("+"), ord("-")):
            if key == ord("+"):
                current_state = learning_list[current_index]["state"]
                current_state_index = states.index(current_state)
                if current_state_index < len(states) - 1:
                    learning_list[current_index]["state"] = states[current_state_index + 1]
            elif key == ord("-"):
                current_state = learning_list[current_index]["state"]
                current_state_index = states.index(current_state)
                if current_state_index > 0:
                    learning_list[current_index]["state"] = states[current_state_index - 1]

if __name__ == "__main__":
    curses.wrapper(main)

