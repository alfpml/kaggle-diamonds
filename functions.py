#converting categorical columns into numerical after consulting relathionship between these variables and prices
def cut_f(df,n1):
    dict_cut={"Ideal":5/5*n1,"Premium":4/5*n1,"Very Good":3/5*n1,"Good":2/5*n1,"Fair":1/5*n1}
    return df.replace({"cut": dict_cut})

#converting categorical columns into numerical after consulting relathionship between these variables and prices
def color_f(df,n2):
    dict_color={"D":7/7*n2,"E":6/7*n2,"F":5/7*n2,"G":4/7*n2,"H":3/7*n2,"I":2/7*n2,"J":1/7*n2}
    return df.replace({"color":dict_color})

#converting categorical columns into numerical after consulting relathionship between these variables and prices
def clarity_f(df,n3):
    dict_clarity={"FL":11/11*n3,"IF":10/11*n3,"VVS1":9/11*n3,"VVS2":8/11*n3,"VS1":7/11*n3,"VS2":6/11*n3,"SI1":5/11*n3,"SI2":4/11*n3,"I1":3/11*n3,"I2":2/11*n3,"I3":1/11*n3}
    return df.replace({"clarity": dict_clarity})