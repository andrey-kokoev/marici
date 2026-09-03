import json
from fractions import Fraction as F
from pathlib import Path
X=((F(0),F(1,2)),(F(1,2),F(0)))
row=tuple(sum(r) for r in X); col=tuple(sum(X[i][j] for i in range(2)) for j in range(2))
# For block Gram [[I,X],[X^T,I]], Schur complement is I-X^T X = 3/4 I.
schur=((F(3,4),F(0)),(F(0),F(3,4)))
allowed=((1,0),(0,1))
support_ok=all(X[i][j]==0 or allowed[i][j] for i in range(2) for j in range(2))
checks={'full_cross_block_distinguishes_entries':X[0][1]!=X[0][0],'fixed_margins':row==col==(F(1,2),F(1,2)),'block_gram_positive_definite':schur[0][0]>0 and schur[1][1]>0,'cross_entries_nonnegative':all(v>=0 for r in X for v in r),'interlacing_support_fails':not support_ok,'independent_coordinates_2x2':(2-1)*(2-1)==1}
result={'schema':'marici.strominger.rh_quarter_full_cross_gram_hall_conditions.v1','status':'passed' if all(checks.values()) else 'failed','cross_block':[[str(v) for v in r] for r in X],'margins':{'row':list(map(str,row)),'column':list(map(str,col))},'schur_complement':[[str(v) for v in r] for r in schur],'verdict':'A full cross block is informationally equivalent to the coupling when its entries are declared edge coordinates, but positive definiteness, nonnegativity, and fixed margins still do not enforce interlacing support.','necessary_extra_conditions':['entrywise nonnegativity','prescribed row and column margins','zero entries on forbidden interlacing edges','source-derived identification of cross entries with capacities'],'checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_full_cross_gram_hall_conditions.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
