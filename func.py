#go to README
def important_featurs(X, model):
    coefs = model.coef_
    columns = X.columns
    dic = dict(zip(columns, coefs))
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict
important_featurs(X, model)
