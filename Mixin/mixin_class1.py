import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


sent = Sentence(" skjvbscb iuwch iewhc uiiuewvh yuewvicuhe uivcheriuvh eruvbi eurhvu ye"
                "viuh weiuvh iewuv hieru vhiuerhv iuerhiuvh reiuvh ieruvh iuerhviue h")


it = iter(sent)
print(it)
all = min(it)
print(all)





