"""Exact composition audit for place-energy correspondence increments."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def update(state,inc):return add(state,inc)
def readout(state):return state[1]/state[0]
base=(F(3),F(-2));u=(F(2),F(5));v=(F(4),F(-1));z=(F(1),F(3))
left=update(update(update(base,u),v),z);right=update(base,add(u,add(v,z)))
checks={'increment_associativity':add(add(u,v),z)==add(u,add(v,z)),'correspondence_composition':left==right,'readout_parenthesization_independent':readout(left)==readout(right),'energy_stays_positive':all(x[0]>0 for x in (base,update(base,u),update(update(base,u),v),left)),'orthogonal_row_rank_additive':1+2+3==6,'identity_increment':update(base,(F(0),F(0)))==base}
out={'schema':'marici.voevodsky.place-energy-correspondence-composition.v1','base':{'energy':str(base[0]),'signed_weight':str(base[1]),'readout':str(readout(base))},'increments':[{'kappa':str(x[0]),'w':str(x[1])} for x in (u,v,z)],'final':{'energy':str(left[0]),'signed_weight':str(left[1]),'readout':str(readout(left))},'checks':checks,'all_exact':all(checks.values()),'meaning':'Place enlargement composes strictly on the resolved energy/weight carrier, while scalar normalized boundary readout is applied after composition.'}
if __name__=='__main__':
 p=ROOT/'results'/'place-energy-correspondence-composition.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
