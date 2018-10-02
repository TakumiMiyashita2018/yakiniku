import lightgbm as lgbm
import pandas as pd
import numpy as np
import ember__init__ as init

lgbm_model = lgbm.Booster(model_file="data/model.txt")
X_test, y_test = init.read_vectorized_features("data/", subset="test")

print(lgbm_model.predict(X_test, num_iteration=lgbm_model.best_iteration))
