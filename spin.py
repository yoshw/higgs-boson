# This Python file uses the following encoding: utf-8

import curses


dial = ["| -1  |","|-1/3 |","|  0  |","| 1/2 |","| 2/3 |","|  1  |"]

box1 = "Z      e      s      t      γ"
box2 = "-----  -----  -----  -----  -----"
box3 = "[ KEEP OUT - W. Pauli ]"

clear = "       "
pointer = "   ^   "
subdials = [clear,clear,clear,clear,clear]

d = {'d0':{},'d1':{},'d2':{},'d3':{},'d4':{}}
d['d0'] = {'val':2,'disp':dial[2]}
d['d1'] = {'val':2,'disp':dial[2]}
d['d2'] = {'val':2,'disp':dial[2]}
d['d3'] = {'val':2,'disp':dial[2]}
d['d4'] = {'val':2,'disp':dial[2]}

def spin(scr):
    try:
        curses.curs_set(0)
    except: pass

    solved = 0
    p = 2
    subdials[p] = pointer
    dials = [d['d0']['disp'],d['d1']['disp'],d['d2']['disp'],d['d3']['disp'],d['d4']['disp']]
    
    maxy,maxx = scr.getmaxyx()    
    for y in range(0, maxy-22):
        scr.addstr(1+y, 0, '.'*51)
    for y in range(maxy-12, maxy-5):
        scr.addstr(1+y, 0, '.'*51)
    scr.refresh()
    
    newscr = scr.subwin(10,51,maxy-21,0)
    newscr.border(ord('|'),ord('|'),ord('='),ord('='),ord('.'),ord('.'),ord('\''),ord('\''))
    newscr.addstr(2,11,box1)
    newscr.addstr(3,9,box2)
    newscr.addstr(4,8,''.join(dials))
    newscr.addstr(5,9,box2)
    newscr.addstr(6,8,''.join(subdials))
    newscr.addstr(7,14,box3)
    newscr.refresh()

    while solved == 0:
        r = scr.getch()
        subdials[p] = clear
        currd = 'd'+str(p)
        
        if r == ord('q') or r == ord('Q'):
            break
        elif r == curses.KEY_LEFT:
            if p > 0 and p < 5:
                p -= 1
            else: pass
        elif r == curses.KEY_RIGHT:
            if p >= 0 and p < 4:
                p += 1
            else: pass
        elif r == curses.KEY_UP:
            if d[currd]['val'] >= 0 and d[currd]['val'] < 5:
                d[currd]['val'] += 1
                d[currd]['disp'] = dial[d[currd]['val']]
            else: pass
        elif r == curses.KEY_DOWN:
            if d[currd]['val'] > 0 and d[currd]['val'] <= 5:
                d[currd]['val'] -= 1
                d[currd]['disp'] = dial[d[currd]['val']]
            else: pass
        else: pass

        subdials[p] = pointer
        dials = [d['d0']['disp'],d['d1']['disp'],d['d2']['disp'],d['d3']['disp'],d['d4']['disp']]
        
        newscr.addstr(4,8,''.join(dials))
        newscr.addstr(6,8,''.join(subdials))
        newscr.refresh()

        if d['d0']['val'] == 5 and d['d1']['val'] == 3 and d['d2']['val'] == 3\
        and d['d3']['val'] == 3 and d['d4']['val'] == 5:
            solved = 1

    if solved == 0:
        scr.addstr(maxy-3,0,"You can't figure out the lock, and give up for the time being.")
        scr.addstr(maxy-1,0,"(HIT SPACE/ENTER)")
    else:
        scr.addstr(maxy-3,0,"You hear a click. The lock is open!")
        scr.addstr(maxy-1,0,"(HIT SPACE/ENTER)")
    while True:
        r = scr.getch()
        if r in (curses.KEY_ENTER, ord(' '), 10):
            break
        else: pass
    scr.clear()
    return solved

def openchest():
    solved = curses.wrapper(spin)
    return solved
