from nltk.corpus import cess_esp as cess
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt


def init():
    cess_sents = cess.tagged_sents()
    unitag = ut(cess_sents)
    pass

def func():
    pass
