"""Source-column audit: marginal sign readouts versus comparison on the same route."""
from itertools import combinations,combinations_with_replacement,permutations,product
from collections import defaultdict
from pathlib import Path
import json

D=Path(__file__).resolve().parents[1]/'results'

def run():
    rows=('BRNN','BNRN');s=[{i for i,x in enumerate(row) if x!='N'} for row in rows];U=set(range(4));y,=[p for p in permutations(range(4)) if all({p[i] for i in a}==U-a for a in s)];r=(0,2,1,3);G=[tuple(range(4)),r,y,tuple(r[i] for i in y)]
    E=list(combinations(range(4),2));
    def score(p,u,v):
        i,j=u;a,b=v;return int(p[i]==a)+int(p[j]==b)-int(p[i]==b)-int(p[j]==a)
    def marg(h):return tuple(sum(G[t][i]==j for t in h) for i in U for j in U)
    def bits(t):return tuple(score(G[t],e,e)//2 for e in [(0,3),(1,2)])
    def corr(h):return sum(a*b for a,b in map(bits,h))
    # Every single contrast is either one-signed or has only two opposite equal magnitudes.
    for u,v in product(E,repeat=2):
        vals={score(p,u,v) for p in G};assert min(vals)>=0 or max(vals)<=0 or vals in ({-1,1},{-2,2})
    classes=defaultdict(list);joint=set()
    for h in combinations_with_replacement(range(4),4):
        key=marg(h);z=corr(h);x=sum(bits(t)[0] for t in h);w=sum(bits(t)[1] for t in h)
        for t in range(4):
            a,b=bits(t);assert 4*h.count(t)==len(h)+a*x+b*w+a*b*z
        classes[key].append(h);joint.add((key,z))
    assert marg((0,2))==marg((1,3)) and corr((0,2))==2 and corr((1,3))==-2
    out=dict(actions=['identity','(23)','(14)(23)','(14)'],same_route_signs=list(map(bits,range(4))),stationary_columns=[1,4],moving_columns=[2,3],opposite_axis_checks=len(E)**2,route_multisets=sum(map(len,classes.values())),sum_classes=len(classes),sum_plus_joint_classes=len(joint),example=[[0,2],[1,3]],scope='Conditional on the simultaneous side exchange, compares two column contrast signs on the same route; not a source definition of the terminal computeds.');(D/'ramsey_literal_joint_comparison.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':run()
