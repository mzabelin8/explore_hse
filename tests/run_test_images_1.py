import pandas as pd
import seaborn as sns
from overview.overview_class import Overview
from separator.data_separator import Separator
from jinja2 import Environment, Template, FileSystemLoader
import random
from images.make_plot import MakePlot

from overview.overview_class import Overview
from types_clases.type_numeric import Numeric
from types_clases.type_categorical import Categorical
from types_clases.type_boolean import Boolean

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
data = pd.Series(a)
N = Numeric(data, 'colonka')

b = ['asdf', 'fdas', 'qwer', 'asdf']
df = pd.Series(b)
C = Categorical(df, 'categ')

c = [True, True, False]
dt = pd.Series(c)
B = Boolean(dt, 'boole')

all = [N, C, B]

O = Overview(all)

env = Environment(loader=FileSystemLoader('../html_templates/templates_for_typeclasses'))
t = env.get_template('main_test_forplots.html').render(ov=O, obj=N, obj2=C, obj3=B)

with open('/Users/maximzabelin/desktop/plot_1.html', 'w') as f:
    f.write(t)
