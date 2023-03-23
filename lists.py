import curses

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()

    list1 = ["item1", "item2", "item3", "item4"]
    list2 = ["item5", "item6", "item7", "item8"]
    list3 = ["item9", "item10", "item11", "item12"]
    lists = [list1, list2, list3]

    current_list = 0
    current_item = 0

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        for i, lst in enumerate(lists):
            for j, item in enumerate(lst):
                x = (width // len(lists)) * i
                y = j
                if i == current_list and j == current_item:
                    stdscr.attron(curses.color_pair(2))
                else:
                    stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, item)
                stdscr.attroff(curses.color_pair(1))
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()
        c = stdscr.getch()

        if c == curses.KEY_UP and current_item > 0:
            current_item -= 1
        elif c == curses.KEY_DOWN and current_item < len(lists[current_list]) - 1:
            current_item += 1
        elif c == curses.KEY_LEFT and current_list > 0:
            current_list -= 1
        elif c == curses.KEY_RIGHT and current_list < len(lists) - 1:
            current_list += 1
        elif c == ord("q"):
            break

curses.wrapper(main)
