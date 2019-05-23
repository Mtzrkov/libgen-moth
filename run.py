import libgenapi
import pandas as pd 
from pylibgen import Library 

MIRRORS = [
    'http://libgen.io/',
    'https://libgen.unblocked.cab/',
    'https://libgen.immunicity.cab/',
    'https://libgen.unblockall.xyz/',
    'https://libgen.unblocked.team/'
]

lg = libgenapi.Libgenapi(MIRRORS)

df = pd.DataFrame(lg.search("Portuguese",'language'))
print(df.head())