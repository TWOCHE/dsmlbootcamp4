"""
Diğer Proje dosyalarının eklenmesi

- requirements.txt : projenin çalıştırılması için gerekli olan dosyaları ifade eder
- setup.cfg : setup konfigurasyon oluşturuken oluşturulan konfig dosyası
- README.md : projenin beni oku dosyası
- LICENSE.md : bu kitap, kütüphane vs nasıl lisanslandığını ifade eder. örn MIT license ını kullanacağız
- setup.py : tüm paketi ziplemek gibi bir program haline getirip pypi da yayınlamaya hazır hale getirme işlevi

"""




from dsmlbootcamp4.hi import *

hello()

hello2()

from dsmlbootcamp4.eda.helpers import *

import seaborn as sns
df=sns.load_dataset("tips")

check_df(df)

# kütüphanemizin ana hiyerarşisi:
import dsmlbootcamp4
help(dsmlbootcamp4)

# bir yerde  __init__ varsa bu bir modüldür muhtemelen.
# çağrıldığında ne yaptığı bilgisini taşıyan bölüm burası
help(dsmlbootcamp4.eda)
"""
PACKAGE CONTENTS
    eda
    helpers
FILE
    /Users/tugcedogan/Desktop/dsmlbootcamp4/dsmlbootcamp4/eda/__init__.py
"""

import dsmlbootcamp4.data_prep

help(dsmlbootcamp4.data_prep)

# fonks.ları yapısal bir şekilde görmek için döküman hazırlamak lazım

import pandas as pd

help(pd)

import pandas.tseries.frequencies

