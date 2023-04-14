from pynput.keyboard import Key, Controller, Listener

from threading import Thread
import time
import json
from os import listdir
import random

def cal_key(tone_i, ctrl_shift, tone_o):
    if tone_i == 'q':
        ctrl_shift.append(0)
        tone_o.append('q')
    elif tone_i == 'w':
        ctrl_shift.append(0)
        tone_o.append('w')
    elif tone_i == 'e':
        ctrl_shift.append(0)
        tone_o.append('e')
    elif tone_i == 'r':
        ctrl_shift.append(0)
        tone_o.append('r')
    elif tone_i == 't':
        ctrl_shift.append(0)
        tone_o.append('t')
    elif tone_i == 'y':
        ctrl_shift.append(0)
        tone_o.append('y')
    elif tone_i == 'u':
        ctrl_shift.append(0)
        tone_o.append('u')
    elif tone_i == '1':
        ctrl_shift.append(0)
        tone_o.append('2')
    elif tone_i == '2':
        ctrl_shift.append(0)
        tone_o.append('3')
    elif tone_i == '3':
        ctrl_shift.append(0)
        tone_o.append('5')
    elif tone_i == '4':
        ctrl_shift.append(0)
        tone_o.append('6')
    elif tone_i == '5':
        ctrl_shift.append(0)
        tone_o.append('7')

    elif tone_i == 'a':
        ctrl_shift.append(1)
        tone_o.append('q')
    elif tone_i == 's':
        ctrl_shift.append(1)
        tone_o.append('w')
    elif tone_i == 'd':
        ctrl_shift.append(1)
        tone_o.append('e')
    elif tone_i == 'f':
        ctrl_shift.append(1)
        tone_o.append('r')
    elif tone_i == 'g':
        ctrl_shift.append(1)
        tone_o.append('t')
    elif tone_i == 'h':
        ctrl_shift.append(1)
        tone_o.append('y')
    elif tone_i == 'j':
        ctrl_shift.append(1)
        tone_o.append('u')
    elif tone_i == '6':
        ctrl_shift.append(1)
        tone_o.append('2')
    elif tone_i == '7':
        ctrl_shift.append(1)
        tone_o.append('3')
    elif tone_i == '8':
        ctrl_shift.append(1)
        tone_o.append('5')
    elif tone_i == '9':
        ctrl_shift.append(1)
        tone_o.append('6')
    elif tone_i == '0':
        ctrl_shift.append(1)
        tone_o.append('7')

    elif tone_i == 'z':
        ctrl_shift.append(2)
        tone_o.append('q')
    elif tone_i == 'x':
        ctrl_shift.append(2)
        tone_o.append('w')
    elif tone_i == 'c':
        ctrl_shift.append(2)
        tone_o.append('e')
    elif tone_i == 'v':
        ctrl_shift.append(2)
        tone_o.append('r')
    elif tone_i == 'b':
        ctrl_shift.append(2)
        tone_o.append('t')
    elif tone_i == 'n':
        ctrl_shift.append(2)
        tone_o.append('y')
    elif tone_i == 'm':
        ctrl_shift.append(2)
        tone_o.append('u')
    elif tone_i == 'i':
        ctrl_shift.append(2)
        tone_o.append('2')
    elif tone_i == 'o':
        ctrl_shift.append(2)
        tone_o.append('3')
    elif tone_i == 'p':
        ctrl_shift.append(2)
        tone_o.append('5')
    elif tone_i == 'k':
        ctrl_shift.append(2)
        tone_o.append('6')
    elif tone_i == 'l':
        ctrl_shift.append(2)
        tone_o.append('7')

    elif tone_i == '-':
        ctrl_shift.append(2)
        tone_o.append('i')
    elif tone_i == '=':
        ctrl_shift.append(-1)
        tone_o.append('o')

def cal_delay_s(bpm, meter):
    if meter == '1':
        return 60.0 / bpm / 8
    elif meter == '2':
        return 60.0 / bpm / 4
    elif meter == '3':
        return 60.0 / bpm / 3
    elif meter == '4':
        return 60.0 / bpm / 2
    elif meter == '5':
        return 60.0 / bpm / 4 * 3
    elif meter == '6':
        return 60.0 / bpm
    elif meter == '7':
        return 60.0 / bpm * 1.25
    elif meter == '8':
        return 60.0 / bpm * 1.5
    elif meter == '9':
        return 60.0 / bpm * 2
    elif meter == '0':
        return 60.0 / bpm * 3
    elif meter == '-':
        return 60.0 / bpm * 4
    elif meter == '=':
        return 60.0 / bpm * 8
    elif meter == 'r':
        return 60.0 / bpm / 3 * 2
    elif meter == '[':
        return 60.0 / bpm * 7
    else:
        return 0

def playing():
    #############################################
    # really weird
    # if there is nothing here
    # directly go to while
    # it will not work while start this thread
    # the second time
    # function like print or sleep can deal
    # this problem but pass can not
    #############################################
    global stop_flag, playing_flag
    playing_flag = True

    ms_list = []
    for ms in listdir("ms/"):
        if str(ms).endswith(".ms"):
            ms_list.append(ms)

    file_object = open("ms/" + ms_list[random.randint(0, len(ms_list) - 1)], 'r')
    try:
        text = file_object.read()
    finally:
        file_object.close()
    plain_text = text.replace(" ", "").replace("\t", "").replace("\n", "")

    json_obj = json.loads(plain_text)

    delay_s = []
    ctrl_shift = []
    tone = []
    i = 0
    while True:
        if i < len(json_obj["tie"]) and json_obj["tie"][i] == '0':
            delay_s.append(cal_delay_s(json_obj["bpm"], json_obj["meter"][i]))
            cal_key(json_obj["tone"][i], ctrl_shift, tone)
            i += 1
        elif i < len(json_obj["tie"]) and json_obj["tie"][i] == '1':
            delay_s.append(cal_delay_s(json_obj["bpm"], json_obj["meter"][i]) + cal_delay_s(json_obj["bpm"], json_obj["meter"][i + 1]))
            cal_key(json_obj["tone"][i], ctrl_shift, tone)
            i += 2
        else:
            break

    print("[INFO] Playing...")

    for j in range(len(ctrl_shift)):
        if stop_flag:
            with kb.pressed('f'):
                pass
            print("[INFO] Stop")
            break
        else:
            if ctrl_shift[j] == 0:
                with kb.pressed(Key.ctrl, tone[j]):
                    time.sleep(delay_s[j])
            elif ctrl_shift[j] == 1:
                with kb.pressed(tone[j]):
                    time.sleep(delay_s[j])
            elif ctrl_shift[j] == 2:
                with kb.pressed(Key.shift, tone[j]):
                    time.sleep(delay_s[j])
            else:
                time.sleep(delay_s[j])

    if stop_flag == False:
        print("[INFO] Play end")
    playing_flag = False

def on_release(key):
    global stop_flag, playing_flag
    if key == Key.esc:                                          # stop listener
        stop_flag = True
        print("[INFO] Exit")
        return False
    elif key == Key.f8 and playing_flag == False:               # start playing thread
        Thread(target=playing).start()
        stop_flag = False
    elif key == Key.f8 and playing_flag == True:                # stop playing thread
        stop_flag = True
    else:
        pass

if __name__ == '__main__':
    stop_flag = False
    playing_flag = False

    kb = Controller()

    # keyboard.press('a')                                       # can't work
    # time.sleep(5)
    # keyboard.release('a')

    # with kb.pressed(Key.shift, 's'):                          # can't work without with
    #     pass

    with Listener(on_release=on_release) as listener:
        listener.join()
