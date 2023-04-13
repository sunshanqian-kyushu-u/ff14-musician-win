from pynput.keyboard import Key, Controller, Listener

from threading import Thread
import time
import json

def press_key(tone, delay_s):
    if tone == 'q':
        with kb.pressed(Key.ctrl, 'q'):
            time.sleep(delay_s)
    elif tone == 'w':
        with kb.pressed(Key.ctrl, 'w'):
            time.sleep(delay_s)
    elif tone == 'e':
        with kb.pressed(Key.ctrl, 'e'):
            time.sleep(delay_s)
    elif tone == 'r':
        with kb.pressed(Key.ctrl, 'r'):
            time.sleep(delay_s)
    elif tone == 't':
        with kb.pressed(Key.ctrl, 't'):
            time.sleep(delay_s)
    elif tone == 'y':
        with kb.pressed(Key.ctrl, 'y'):
            time.sleep(delay_s)
    elif tone == 'u':
        with kb.pressed(Key.ctrl, 'u'):
            time.sleep(delay_s)
    elif tone == '1':
        with kb.pressed(Key.ctrl, '2'):
            time.sleep(delay_s)
    elif tone == '2':
        with kb.pressed(Key.ctrl, '3'):
            time.sleep(delay_s)
    elif tone == '3':
        with kb.pressed(Key.ctrl, '5'):
            time.sleep(delay_s)
    elif tone == '4':
        with kb.pressed(Key.ctrl, '6'):
            time.sleep(delay_s)
    elif tone == '5':
        with kb.pressed(Key.ctrl, '7'):
            time.sleep(delay_s)

    elif tone == 'a':
        with kb.pressed('q'):
            time.sleep(delay_s)
    elif tone == 's':
        with kb.pressed('w'):
            time.sleep(delay_s)
    elif tone == 'd':
        with kb.pressed('e'):
            time.sleep(delay_s)
    elif tone == 'f':
        with kb.pressed('r'):
            time.sleep(delay_s)
    elif tone == 'g':
        with kb.pressed('t'):
            time.sleep(delay_s)
    elif tone == 'h':
        with kb.pressed('y'):
            time.sleep(delay_s)
    elif tone == 'j':
        with kb.pressed('u'):
            time.sleep(delay_s)
    elif tone == '6':
        with kb.pressed('2'):
            time.sleep(delay_s)
    elif tone == '7':
        with kb.pressed('3'):
            time.sleep(delay_s)
    elif tone == '8':
        with kb.pressed('5'):
            time.sleep(delay_s)
    elif tone == '9':
        with kb.pressed('6'):
            time.sleep(delay_s)
    elif tone == '0':
        with kb.pressed('7'):
            time.sleep(delay_s)

    elif tone == 'z':
        with kb.pressed(Key.shift, 'q'):
            time.sleep(delay_s)
    elif tone == 'x':
        with kb.pressed(Key.shift, 'w'):
            time.sleep(delay_s)
    elif tone == 'c':
        with kb.pressed(Key.shift, 'e'):
            time.sleep(delay_s)
    elif tone == 'v':
        with kb.pressed(Key.shift, 'r'):
            time.sleep(delay_s)
    elif tone == 'b':
        with kb.pressed(Key.shift, 't'):
            time.sleep(delay_s)
    elif tone == 'n':
        with kb.pressed(Key.shift, 'y'):
            time.sleep(delay_s)
    elif tone == 'm':
        with kb.pressed(Key.shift, 'u'):
            time.sleep(delay_s)
    elif tone == 'i':
        with kb.pressed(Key.shift, '2'):
            time.sleep(delay_s)
    elif tone == 'o':
        with kb.pressed(Key.shift, '3'):
            time.sleep(delay_s)
    elif tone == 'p':
        with kb.pressed(Key.shift, '5'):
            time.sleep(delay_s)
    elif tone == 'k':
        with kb.pressed(Key.shift, '6'):
            time.sleep(delay_s)
    elif tone == 'l':
        with kb.pressed(Key.shift, '7'):
            time.sleep(delay_s)

    elif tone == '-':
        with kb.pressed(Key.shift, 'i'):
            time.sleep(delay_s)
    elif tone == '=':
        time.sleep(delay_s)

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
    global stop_flag, playing_flag

    playing_flag = True
    #############################################
    # really weird
    # if there is nothing here
    # directly go to while
    # it will not work while start this thread
    # the second time
    # function like print or sleep can deal
    # this problem but pass can not
    #############################################
    file_object = open("lemon.ms", 'r')
    try:
        text = file_object.read()
    finally:
        file_object.close()
    plain_text = text.replace(" ", "").replace("\t", "").replace("\n", "")
    # print(plain_text)

    json_obj = json.loads(plain_text)
    # print(json_obj["title"])
    # print(json_obj["title"][0])
    # print(len(json_obj["tie"]))

    delay_s = []
    tone = []
    i = 0
    while True:
        if i < len(json_obj["tie"]) and json_obj["tie"][i] == '0':
            delay_s.append(cal_delay_s(json_obj["bpm"], json_obj["meter"][i]))
            tone.append(json_obj["tone"][i])
            i += 1
        elif i < len(json_obj["tie"]) and json_obj["tie"][i] == '1':
            delay_s.append(cal_delay_s(json_obj["bpm"], json_obj["meter"][i]) + cal_delay_s(json_obj["bpm"], json_obj["meter"][i + 1]))
            tone.append(json_obj["tone"][i])
            i += 2
        else:
            break

    # print(delay_s)
    # print(tone)
    # print(len(delay_s))
    # print(len(tone))

    print("[INFO] Playing...")

    for j in range(len(tone)):
        if stop_flag:
            print("[INFO] Stop")
            break
        else:
            # print("playing...")
            # time.sleep(3)

            # with press_key(tone[j]):
            #     time.sleep(delay_s[j])
            press_key(tone[j], delay_s[j])

    if stop_flag == False:
        print("[INFO] Play end")
    playing_flag = False

# this is the example
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

def on_release(key):
    global stop_flag, playing_flag
    if key == Key.esc:                                          # stop listener
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

    # for i in range(5, 0, -1):
    #     print("[INFO] Count down: " + str(i))
    #     time.sleep(1)

    # print("[INFO] Playing...")

    with Listener(on_release=on_release) as listener:
        listener.join()
