from tenx_missile import MissileLauncher

_VALID_CODES = ['RDPC', 'ZULO', 'C3P0']


class Missile(object):
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

# DUMMY WHOT?


def test_launch_missile_with_invalid_code():
    pass  # launch_missile(¿?¿?, 'INVALID')
