"""Exact joint edge coloring on seven compatible supports. For each subset that could complete an independent twelve with the core, require an internal red edge."""
from ramsey312_google_two_step import *
from itertools import combinations
from functools import lru_cache
from collections import Counter

def main():
 out=[];hist=Counter();T={}
 @lru_cache(maxsize=200000)
 def ind(p,k):
    if not k:return True
    while p.bit_count()>=k:
        b=p&-p;p-=b
        if ind(p&~adj[b.bit_length()-1],k-1):return True
    return False
 for line in open(sys.argv[1]):
    if not line.startswith('K '):continue
    d,*s=map(int,line.split()[1:]);h=F^d;assert len(s)==d.bit_count()+1;V=range(len(s));E=list(combinations(V,2));lit=lambda i,j:1+E.index((i,j));assert all(not ind(h&~x,11) and not x&~h and all(not adj[i]&x for i in bits(x)) for x in s)
    clauses=[[-lit(i,j)] for i,j in E if s[i]&s[j]]+ [[-lit(i,j),-lit(i,k),-lit(j,k)] for i,j,k in combinations(V,3)];r=dict(d=d,s=s);dead=0
    with Solver(name='g4',bootstrap_with=clauses) as sl:
        for k in range(2,len(s)+1):
            for group in combinations(V,k):
                p=h
                for i in group:p&=~s[i]
                if ind(p,12-k):sl.add_clause([lit(i,j) for i,j in combinations(group,2)])
            if not sl.solve():dead=k;break
        # Pairwise allowed colors can already force a red triangle.
        assert all(not (s[i]&s[j]) or not ind(h&~(s[i]|s[j]),10) for i,j in E)
        if not dead:
            model=set(sl.get_model());nn=tuple(range(52,52+len(s)));a=list(adj)+[0]*len(s)
            for i,x in enumerate(s):
                a[nn[i]]=x
                for v in bits(x):a[v]|=1<<nn[i]
            for (i,j) in E:
                if lit(i,j) in model:a[52+i]|=1<<(52+j);a[52+j]|=1<<(52+i)
            vertices=list(bits(h))+list(nn);assert len(vertices)==53;M=[sum(1<<j for j,w in enumerate(vertices) if a[v]>>w&1) for v in vertices];assert all(not M[i]&M[j] for i in range(53) for j in bits(M[i]));
            def check(p,k):
                if not k:return True
                while p.bit_count()>=k:
                    b=p&-p;p-=b
                    if check(p&~M[b.bit_length()-1],k-1):return True
                return False
            assert not check((1<<53)-1,12);r['matrix']=M
    hist[dead]+=1;r['first_unsat_arity']=dead;out.append(r)
 print('tested',len(out),'hist',hist);(D/(sys.argv[2] if len(sys.argv)>2 else 'ramsey312_joint_seven.json')).write_text(json.dumps(out))
if __name__=='__main__':main()
