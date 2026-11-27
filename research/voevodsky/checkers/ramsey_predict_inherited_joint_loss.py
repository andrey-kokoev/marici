"""Predict joint-only loss from the old swap and added column, before consulting cycles."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from ramsey_inherited_swap_selector import run


def predict(sq,mark):
    U=set().union(*sq);W=set(range(1,11))-U;mov=U-set.intersection(*map(set,sq));s,t=map(set,mark);A=s-U;B=t-U
    if A==B:return False,'same outside pair'
    a,=A&B;b,=A-B;c,=B-A;d,e=sorted(W-A-B);z,=s&U;partner,=[p for p in mov-{z} if not any({p,z}<=set(r) for r in sq)]
    if any(abs(partner-i)==1 for i in (d,e)):return False,'partner blocks seven'
    # Forbid ab,ac. Residual pentagon degrees force ad,ae,bc red and de blue.
    # Unfilled red slots form one perfect matching from {b,c} to {d,e}.
    dist=lambda x,y:abs(x-y)
    if any(dist(i,j)==2 for i,j in [(a,d),(a,e),(b,c)]) or dist(d,e)==1:return False,'forced edge clash'
    # a,b and a,c nonadjacent because each probe is a separated triple.
    assert min(dist(a,b),dist(a,c))>1
    mandatory={(i,j) for i in (b,c) for j in (d,e) if dist(i,j)==1};edges={(i,j) for i in (b,c) for j in (d,e) if dist(i,j)!=2}
    # Contract mandatory pairs; Hall on the remaining at most two rows.
    if len({i for i,j in mandatory})<len(mandatory) or len({j for i,j in mandatory})<len(mandatory):return False,'matching clash'
    L={b,c}-{i for i,j in mandatory};R={d,e}-{j for i,j in mandatory}
    for n in range(1,len(L)+1):
        for sub in combinations(L,n):
            if len({j for i,j in edges if i in sub and j in R})<n:return False,'matching clash'
    return True,'joint only'


def main():
    counts=Counter();demo=None
    def inspect(sq,path,marks,children):
        nonlocal demo
        for mark in sorted(marks):
            pred,tag=predict(sq,mark);A,B=[tuple(sorted(set(s)-set().union(*sq))) for s in mark];alone=any(A not in c and B not in c for c,_ in children);joint=any(mark in v for _,v in children);assert pred==(alone and not joint);counts[tag]+=1
            if pred and demo is None:demo=dict(square=sq,old_outside=path,mark=mark)
    run(inspect);assert counts['joint only']==87;result=dict(counts=counts,example=demo);print(result);(Path(__file__).resolve().parents[1]/'results/ramsey_predict_inherited_joint_loss.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
