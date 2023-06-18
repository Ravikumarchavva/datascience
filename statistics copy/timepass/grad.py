import numpy as np
import pandas as pd
dictionary={"x":[1,3,5],"y":[2,5,6]}
df=pd.DataFrame(dictionary)
def gradient_descent(df):
    w=0
    b=0
    lr=0.12
    iteration=250
    for i in range(iteration):
        y_hat=w*df.x+b
        dj_dw=-sum((df.y-y_hat)*df.x)/len(df.index)
        dj_db=-sum(df.y-y_hat)/len(df.index)
        w=w-lr*dj_dw
        b=b-lr*dj_db
        print(f"iteration:{i} w:{w} b:{b}")
gradient_descent(df)