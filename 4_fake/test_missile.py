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
class MissileMock:

    def __init__(self):
        self.launch_was_called = False
        self.disable_was_called = False

    def fire(self):
        self.launch_was_called = True

    def disable(self):
        self.disable_was_called = True

    def verify_code_red_abort(self):
        assert not self.launch_was_called
        assert self.disable_was_called


# Copy here the correct stub from the last exercice (and add a text method!)
class CorrectCodeStub:

    def is_unsigned(self):
        return False

    def is_invalid(self):
        return False

    def text(self):
        return 'code'


# And here... do your faker magic!
class UsedLaunchCodesFake:
    def __init__(self):
        self._used_codes = set()

    def add(self, code):
        self._used_codes.add(code)

    def contains(self, code):
        return code in self._used_codes

    def close(self):
        pass


def test_launch_missile_with_repeated_code():
    missile_1_mock = MissileMock()  # replace with the mock
    missile_2_mock = MissileMock()  # replace with the mock
    correct_code_stub = CorrectCodeStub()  # replace with the stub
    used_launch_codes_fake = UsedLaunchCodesFake()  # replace with the fake
    launch_missile(missile_1_mock, correct_code_stub, used_launch_codes_fake)
    launch_missile(missile_2_mock, correct_code_stub, used_launch_codes_fake)
    # assert code red abort
    missile_2_mock.verify_code_red_abort()
