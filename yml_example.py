"""
тут кажется что-то похожее:
https://qudata.com/ml/ru/NLP_RASA_Actions.html

тут вроде прямо то, что мне надо (судя по названию):
https://gist.github.com/magdalini-anastasiadou/1d34fe7a4f54f0d263796bdf82dde81d
"""

import os
import yaml
import operator
import pandas as pd
from itertools import groupby

test_dict = {'text': 'hello',
             'intent': 'greet',
             'metadata': {'intent': {'sentiment': 'neutral'}}}

with open(os.path.join("data", "test.yml"), 'w+') as f:
    yaml.dump(test_dict, f, allow_unicode=True)

test_dict2 = {"nlu":
                  [{'examples': ['Доброго времени суток', 'Добрый здравствуйте'], 'intent': 'greet'},
                   {'intent': 'gratitude', 'examples': ['Спасибо большое , хорошего вам дня.', 'Спасибо .']}]
              }

with open(os.path.join("data", "test2.yml"), 'w+') as f:
    yaml.dump(test_dict2, f, allow_unicode=True)

df = pd.read_csv(os.path.join("data", "intents.csv"), sep="\t")
print(df)

dt_dct = df.to_dict(orient="records")
print(dt_dct)

int_dct = {"version": "3.1", "nlu": {}}
int_dct["nlu"]["intent"] = {}
for key, value in groupby(
        sorted([(x, y) for x, y in zip(list(df["intent"]), list(df["examples"]))], key=lambda t: t[0]),
        operator.itemgetter(0)):
    int_dct["nlu"]["intent"] = {**int_dct["nlu"]["intent"], **{key: [x[1] for x in value]}}

print(int_dct)
with open(os.path.join("data", "my_nlu.yml"), 'w+') as f:
    yaml.dump(int_dct, f, allow_unicode=True)
