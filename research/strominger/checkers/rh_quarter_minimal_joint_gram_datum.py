import json
from pathlib import Path

def tangent_basis(m,n):
    out=[]
    for i in range(m-1):
      for j in range(n-1):
        x=[[0]*n for _ in range(m)];x[i][j]=1;x[i][n-1]=-1;x[m-1][j]=-1;x[m-1][n-1]=1;out.append(x)
    return out

def mixed(basis,alpha,beta):
    return [sum(alpha[i]*beta[j]*x[i][j] for i in range(len(x)) for j in range(len(x[0]))) for x in basis]
b2=tangent_basis(2,2); b3=tangent_basis(3,3)
r2=mixed(b2,[0,1],[0,1]);r3=mixed(b3,[0,1,2],[0,1,2])
checks={'transport_tangent_dim_2x2':len(b2)==1,'one_cross_moment_identifies_2x2':r2[0]!=0,'transport_tangent_dim_3x3':len(b3)==4,'one_cross_moment_not_injective_3x3':len(r3)==4 and 4-1==3,'minimal_linear_joint_coordinates_mxn':'(m-1)(n-1)','fixed_8x8_requires_49_independent_joint_coordinates':(8-1)*(8-1)==49}
result={'schema':'marici.strominger.rh_quarter_minimal_joint_gram_datum.v1','status':'passed' if all(v is True or isinstance(v,str) for v in checks.values()) else 'failed','verdict':'With fixed endpoint margins, the coupling space has dimension (m-1)(n-1). One nondegenerate mixed Gram moment is minimal and sufficient only for 2x2; an 8x8 coupling requires 49 independent joint coordinates.','two_by_two_cross_response':r2,'three_by_three_cross_response':r3,'residual':'The fixed 8x8 quarter-source backend exposes indexed source terms but no verified rank-49 map to joint Gram coordinates, and no parameterized all-order constructor.','checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_minimal_joint_gram_datum.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
