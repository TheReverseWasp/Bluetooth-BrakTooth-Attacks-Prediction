import pandas as pd

def parse_Delta(delta_col_val):
    if delta_col_val <= 0.001381:
        return 0.001380
    elif delta_col_val >= 0.005305:
        return 0.005306
    return delta_col_val

def custom_drop_dummies(col_name, col, metadata):
    ans = pd.DataFrame()
    for elem in metadata:
        col_list = list()
        for item in list(col):
            if elem == item:
                col_list.append(1)
            else:
                col_list.append(0)
        ans[f"{col_name}_{elem}"] = col_list
    return ans

def preprocess(X, metadata):
    ans = pd.DataFrame()
    ans["Delta"] = X["Delta"].apply(parse_Delta)
    temp = custom_drop_dummies("Protocol", X["Protocol"], metadata)
    for col in temp.columns:
        ans[col] = temp[col]
    return ans
