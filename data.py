import pandas as pd
from string import Template
from pathlib import Path

import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

data_path = Path('/kaggle/input/kaggle-llm-science-exam')

test = pd.read_csv('/kaggle/input/kaggle-llm-science-exam/test.csv', index_col='id')
test.head()

