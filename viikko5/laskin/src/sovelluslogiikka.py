class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._history = []

    def miinus(self, operandi):
        self._history.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._history.append(self._arvo)
        self._arvo = self._arvo + operandi

    def kumoa(self):
        if len(self._history):
            self._arvo = self._history.pop(-1)

    def nollaa(self):
        self._history.clear()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._history.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo
