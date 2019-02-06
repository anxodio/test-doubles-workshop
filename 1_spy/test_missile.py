from tenx_missile import MissileLauncher

_VALID_CODES = ['DPRK', 'BOOM', 'ACME']


class Missile:
    def __init__(self):
        self._launcher = MissileLauncher()

    def fire(self):
        self._launcher.fire()


def launch_missile(missile, code):
    if check_code(code):
        missile.fire()


def check_code(code):
    return code in _VALID_CODES


#############
# TEST CODE #
#############

# 007 FTW


def test_launch_missile():
    missile_spy = None  # replace with the spy
    launch_missile(missile_spy, 'DPRK')
    # interrogate spy and assert that was fired


def test_launch_missile_with_invalid_code():
    missile_spy = None  # replace with the spy
    launch_missile(missile_spy, 'INVALID')
    # interrogate spy and assert that wasn't fired
