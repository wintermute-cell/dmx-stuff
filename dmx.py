from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Eyourlife import Small_Flat_Par
from PyDMXControl.profiles.defaults import Fixture

import colors
import random
import time



class uking(Fixture):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._register_channel('dimmer')
        self._register_channel_aliases('dimmer', 'dim', 'd')
        self._register_channel('red')
        self._register_channel_aliases('red', 'r')
        self._register_channel('green')
        self._register_channel_aliases('green', 'g')
        self._register_channel('blue')
        self._register_channel_aliases('blue', 'b')
        self._register_channel('strobe')
        self._register_channel('function')
        self._register_channel('shade')

dmx = OpenDMXController()
f1 = dmx.add_fixture(uking, name="RGB1")
f2 = dmx.add_fixture(uking, name="RGB2")
f3 = dmx.add_fixture(uking, name="RGB3")
f4 = dmx.add_fixture(uking, name="RGB4")

fixtures = [f1, f2, f3, f4]


f1.color(colors.NIGHT_SKY_BLUE)
f1.dim(255, 5000)

f2.color(colors.R)
f2.dim(255, 5000)

f3.color(colors.G)
f3.dim(255, 5000)

f4.color(colors.B)
f4.dim(255, 5000)


def lightning():
    curr_color = colors.NIGHT_SKY_BLUE
    flashes_amount = 400
    while flashes_amount > 0:
        flashes_amount -= 1
        fix = random.choice(fixtures)
        fix.color(colors.W_FULL)
        time.sleep(random.random() * 0.3)
        fix.color(curr_color)
        if random.random() > 0.5:
            time.sleep(random.random() * 0.4)
        else:
            time.sleep(random.randint(2, 4))

def clouds():
    base_color = colors.NIGHT_SKY_BLUE
    for fix in fixtures:
        fix.color(base_color)
    while True:
        fix = random.choice(fixtures)
        if fix.get_color() == base_color:
            fix.color(colors.LIGHTBLUE, 5000)
        else:
            fix.color(base_color, 5000)
        time.sleep(random.randint(2,5))
    
def colortest():
    def s(color):
        b=color[2]
        color = [color[0],color[1],b-(29.5*b)/100]
        print(color)
        for fix in fixtures:
            fix.color(color)
        dmx.sleep_till_enter()
    s(colors.R)
    s(colors.G)
    s(colors.B)
    #s(colors.W2000K)
    #s(colors.W3000K)
    #s(colors.W4000K)
    #s(colors.W5000K)
    #s(colors.W6000K)
    #s(colors.W7000K)
    #s(colors.W8000K)
    #s(colors.W_FULL)
    s(colors.ORANGE)
    s(colors.YELLOW)
    s(colors.WARMGREEN)
    s(colors.COLDGREEN)
    s(colors.CYAN)
    s(colors.LIGHTBLUE)
    s(colors.PURPLE)
    s(colors.PINK)
    s(colors.HOTPINK)
    s(colors.NIGHT_SKY_BLUE)


dmx.web_control()
colortest()
#lightning()
dmx.sleep_till_enter()
