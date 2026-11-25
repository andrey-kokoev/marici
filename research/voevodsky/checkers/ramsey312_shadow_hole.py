"""Inverse search for legal supports with zero saturated shadow rows. For each independent S on degree-ten vertices, solve exactly for transversal D of {E minus N(b) : E independent eleven disjoint from S, b in S}. Empty S uses E directly."""
from ramsey312_google_two_step import *
from pysat.card import CardEnc,EncType
from itertools import combinations
import sys

def run(E,s,ks,enumerate_min=False):
 rows={e&~adj[b] for e in E if not e&s for b in bits(s)} if s else set(E);assert 0 not in rows;forced=sum(u for u in rows if u.bit_count()==1);rs=sorted((u for u in rows if not u&forced),key=lambda u:(u.bit_count(),u));mins=[];inc=[0]*52
 for u in rs:
    # A previously retained edge contained in u? Filter by subtracting edges containing any outside label.
    rest=(1<<len(mins))-1
    for i in bits(F^u):
        rest&=~inc[i]
        if not rest:break
    if rest:continue
    flag=1<<len(mins);mins.append(u)
    for i in bits(u):inc[i]|=flag
 base=[[i+1 for i in bits(u)] for u in mins];vs=list(bits(F&~(s|forced)));out={}
 for k in ks:
    kk=k-forced.bit_count()
    if kk<0:out[k]=None;continue
    cnf=CardEnc.atmost([v+1 for v in vs],kk,top_id=52,encoding=EncType.totalizer)
    with Solver(name='g4',bootstrap_with=base+cnf.clauses) as sl:
        if not sl.solve():out[k]=None;continue
        ds=[]
        while True:
            m=set(sl.get_model());d=forced|sum(1<<i for i in vs if i+1 in m);assert not d&s and d.bit_count()<=k and all(u&d for u in rows);ds.append(d)
            if not enumerate_min:break
            assert d.bit_count()==k;sl.add_clause([-i-1 for i in bits(d&~forced)])
            if not sl.solve():break
        out[k]=sorted(ds) if enumerate_min else d;break
 return dict(s=s,forced=forced,minimal=len(mins),answers=out)

def main():
 part,parts,low,high=map(int,sys.argv[1:5]);E=list(sets(F,11));lo=sum(1<<i for i in range(52) if adj[i].bit_count()<11);ss=sorted(s for k in range(lo.bit_count()+1) for s in sets(lo,k));assert len(ss)==336
 with (D/f'ramsey312_shadow_hole_{low}_{high}_{part}.jsonl').open('w') as f:
    for s in ss[part::parts]:
        r=run(E,s,range(low,high+1));f.write(json.dumps(r)+'\n');f.flush()
if __name__=='__main__':main()
