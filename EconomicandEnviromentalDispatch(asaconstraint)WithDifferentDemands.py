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
Elimit=9000000
for k in range(11):
    
    demand=281+(71.7)*(k)
    model = Model('520')

    p = model.addVars(C, lb=F[6], ub=F[7],vtype=GRB.CONTINUOUS)

    model.setObjective(quicksum(F[0][i]*(p[i]*p[i])+F[1][i]*(p[i])+F[2][i] for i in range(C)), GRB.MINIMIZE)

    model.addConstr(quicksum(p[i] for i in range(C)) >= demand)
    model.addConstr(quicksum((F[3][i])*(p[i]*p[i])+(F[4][i])*p[i]+F[5][i] for i in range(C)) <= Elimit) #Env. const





    model.optimize()

    # Check if optimization was successful
    if model.status == GRB.OPTIMAL:
        # Retrieve the optimal values of decision variables
        p_opt = model.getAttr('x', p)
        lower_bound_p = model.getAttr("LB", p)
        upper_bound_p = model.getAttr("UB", p)
        

        for i in range(0,C):
            print(f"p[{i}] = {p_opt[i]}")
            print(f"p[{i}] lower bound = {lower_bound_p[i]}")
            print(f"p[{i}] upper bound = {upper_bound_p[i]}")

    model.printStats() 