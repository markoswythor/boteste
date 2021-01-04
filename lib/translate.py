from googletrans import Translator
import sys

trans = Translator()

t = trans.translate(sys.argv[1], dest='pt')

print(t.text)