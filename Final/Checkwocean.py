# check if the enhanced ocean values are present in the resume


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pdfminer.high_level import extract_text

trial = extract_text("../resumes/shardul cv updated.pdf")
print(trial)

dataset = pd.read_csv('Enhanced_ocean_traits.csv')