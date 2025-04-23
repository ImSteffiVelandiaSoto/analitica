import pandas as pd

l = [1,2,3,4]

l_df = pd.DataFrame(l).transpose()
l_df.to_csv("archivo.csv", index=False, header=False)