import shelve
from tenx_missile import MissileLauncher


class Missile:
    def __init__(self):
        self._launcher = MissileLauncher()
        self._disabled = False

    def fire(self):
        if self._disabled:
            raise Exception('Missile is disabled')
        self._launcher.fire()

    def disable(self):
        self._disabled = True


class Code:
    _VALID_CODES = ['DPRK', 'BOOM', 'ACME']
    _PASSWORD = 'JONG'

    def __init__(self, code, password):
        self._unsigned = False
        self._invalid = False
        self._check_code(code, password)
        self._text = code

    def _check_code(self, code, password):
        if password != self._PASSWORD:
            self._unsigned = True
        elif code not in self._VALID_CODES:
            self._invalid = True

    def is_unsigned(self):
        return self._unsigned

    def is_invalid(self):
        return self._invalid

    def text(self):
        return self._text


class UsedLaunchCodes:
    def __init__(self):
        self._db = shelve.open('database')

    def add(self, code):
        try:
            codes = self._db['codes']
        except KeyError:
            codes = []
        self._db['codes'] = codes+[code]

    def contains(self, code):
        try:
            codes = self._db['codes']
        except KeyError:
            return False
        return code in codes

    def close(self):
        self._db.close()


def launch_missile(missile, code, used):
    if used.contains(code.text()) or code.is_unsigned() or code.is_invalid():
        # CODE RED ABORT
        missile.disable()
    else:
        used.add(code.text())
        missile.fire()


#############
# TEST CODE #
#############

# Copy here the mock from the last exercice

# Copy here the correct stub from the last exercice (and add a text method!)

# And here... do your faker magic!


def test_launch_missile_with_repeated_code():
    missile_1_mock = None  # replace with the mock
    missile_2_mock = None  # replace with the mock
    correct_code_stub = None  # replace with the stub
    used_launch_codes_fake = None  # replace with the fake
    launch_missile(missile_1_mock, correct_code_stub, used_launch_codes_fake)
    launch_missile(missile_2_mock, correct_code_stub, used_launch_codes_fake)
    # assert code red abort
