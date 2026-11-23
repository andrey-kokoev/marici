"""Decompose the 42 vs 46 score by actual (deleted pair, support) witnesses on input 0. Set difference, not subtraction of cardinalities."""
from ramsey38_relative_query import families,data,C,J,D,json,ls
h=data[0][0];sets=[{((x,y),s) for x,y,F in families(j) for s in F if not any(h[z]&s for z in ls(s))} for j in (C[0],J[0])];a,b=sets;rows=[]
for d in sorted({d for d,s in a|b}):
 aa={s for e,s in a if e==d};bb={s for e,s in b if e==d};
 if aa!=bb:rows.append(dict(deleted=d,common=len(aa&bb),low_only=list(map(ls,sorted(aa-bb))),high_only=list(map(ls,sorted(bb-aa)))))
o=dict(input_index=0,output_indices=[C[0],J[0]],common=len(a&b),low_only=len(a-b),high_only=len(b-a),rows=rows);print(o);(D/'ramsey38_score_difference.json').write_text(json.dumps(o,indent=2)+'\n')
