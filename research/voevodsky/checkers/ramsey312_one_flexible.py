"""Can five simple anchored rectangles plus one arbitrary pairwise-incompatible residual class suffice? CEGAR on exact rectangle choices. Residual must avoid every edge including conflicts with its own anchor."""
from ramsey312_google_two_step import *
from pysat.card import CardEnc
from pysat.formula import IDPool
from functools import reduce
from operator import or_

def main():
 if len(sys.argv)>3:d,*s=map(int,open(sys.argv[3]).read().split())
 else:r=json.loads((D/'ramsey312_no_budget_coloring.json').read_text());d=r['d'];s=r['supports']
 h=F^d;A=[s.index(adj[i]&h) for i in bits(d)];N=[0]*len(s)
 for line in open(sys.argv[1]):i,j=map(int,line.split());N[i]|=1<<j;N[j]|=1<<i
 ts=list(sets(h,10));f=int(sys.argv[2]);dom=[[t for t in ts if not s[i]&t] for i in A];sel=[k for k in range(6) if k!=f];ss=set(A);turn=0
 while True:
    turn+=1;ls=sorted(ss);idx={v:i for i,v in enumerate(ls)};n=len(ls);cm=[sum(1<<j for j,x in enumerate(ls) if s[x]>>v&1) for v in range(52)];rows=[];groups=[]
    for k in sel:
        opt={}
        for t in dom[k]:
            miss=((1<<n)-1)&~reduce(or_,(cm[i] for i in bits(t))); 
            for v in bits(s[A[k]]):opt.setdefault(miss&cm[v],(1<<v,t))
        mx=[];ids=[]
        for p in sorted(opt,key=int.bit_count,reverse=True):
            if not any(p&m==p for m in mx):mx.append(p);rows.append((*opt[p],p));ids.append(len(rows))
        groups.append(ids)
    pool=IDPool(start_from=1+len(rows));clauses=[];un=[pool.id(('u',i)) for i in ls];inc=[[] for _ in ls]
    for j,(_,_,p) in enumerate(rows,1):
        for i in bits(p):inc[i].append(j)
    for ids in groups:clauses+=CardEnc.equals(ids,1,vpool=pool).clauses
    clauses.extend([un[i],*inc[i]] for i in range(n));clauses.extend([-un[i],-un[j]] for i,x in enumerate(ls) for j,y in enumerate(ls[:i]) if N[x]>>y&1)
    with Solver(name='g4',bootstrap_with=clauses) as sl:
        if not sl.solve():result=dict(unsat_challenge=[s[i] for i in ls]);break
        m=set(sl.get_model());rect=[(b,t) for j,(b,t,p) in enumerate(rows,1) if j in m];assert len(rect)==5
    left=[i for i,x in enumerate(s) if not any(x&b and not x&t for b,t in rect)];rem=sum(1<<i for i in left);edges=[(i,N[i]&rem) for i in left if N[i]&rem];
    if not edges:result=dict(rect=rect,residual=len(left));break
    for i,ne in edges[::max(1,len(edges)//16)][:17]:ss.update([i,next(bits(ne))]);
 print('flex',f,'turn',turn,'challenge',len(ss),'residual',result.get('residual'));(D/f"ramsey312_flexible_{sys.argv[4]+'_' if len(sys.argv)>4 else ''}{f}.json").write_text(json.dumps(result))
if __name__=='__main__':main()
