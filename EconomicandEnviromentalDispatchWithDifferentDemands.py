from gurobipy import *
import pandas as pd
import numpy as np
from gurobipy import GRB, Model, quicksum
#Read data
df=pd.read_excel('Econ_disp.xlsx',sheet_name='Sheet1')
F = df[["a","b","c","d","e","f","pmin","pmax"]]
C=F.shape[0]
parameters=["a","b","c","d","e","f"]
F.columns = [i for i in range(len(F.columns))]
count1=len(parameters)
Penalty=0.1
for k in range(C):
    demand=400+((100)/count1)*(k-1)
    model = Model('520')

    p = model.addVars(C, lb=F[6], ub=F[7],vtype=GRB.CONTINUOUS)

    model.setObjective(quicksum(Penalty*F[3][i]*(p[i]**2)+Penalty*F[4][i]*(p[i])+Penalty*F[5][i]+F[0][i]*(p[i]**2)+F[1][i]*(p[i])+F[2][i] for i in range(C)), GRB.MINIMIZE)

    model.addConstr(quicksum(p[i] for i in range(C)) >= demand)
    





    model.optimize()

    # Check if optimization was successful
    if model.status == GRB.OPTIMAL:
        # Retrieve the optimal values of decision variables
        p_opt = model.getAttr('x', p)
        

        for i in range(0,C):
            print(f"p[{i}] = {p_opt[i]}")
    model.printStats()  