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
class MissileSpy:

    def __init__(self):
        self.launch_was_called = False

    def fire(self):
        self.launch_was_called = True


def test_launch_missile():
    missile_spy = MissileSpy()  # replace with the spy
    launch_missile(missile_spy, 'DPRK')
    # interrogate spy and assert that was fired
    assert missile_spy.launch_was_called


def test_launch_missile_with_invalid_code():
    missile_spy = MissileSpy()  # replace with the spy
    launch_missile(missile_spy, 'INVALID')
    # interrogate spy and assert that wasn't fired
    assert not missile_spy.launch_was_called
