import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()

print(iris.data)

print(iris.target)

print(iris.target_names)