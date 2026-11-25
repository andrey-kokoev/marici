"""Class-restricted packing LP using exact rational simplex, slack basis and Bland pivoting. Primal maximizes mass on attachments, dual gives one test weight per disjointness degree. Verify both optima directly."""
import sys,gzip,json,collections
from fractions import Fraction as Q
from pathlib import Path
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[]
for record,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(x.bit_count() for x in A)!=66:continue
 F=independent_fives(A);D=[[j for j,b in enumerate(F) if not a&b] for a in F];deg=list(map(len,D));ks=sorted(set(deg));b=[deg.count(k) for k in ks];C=[[sum(deg[j]==k for j in ds) for ds in D] for k in ks];n=len(F);m=len(b);B=list(range(n,n+m));tab=[list(map(Q,row+[int(i==j) for j in range(m)]+[b[i]])) for i,row in enumerate(C)];obj=list(map(Q,[-1]*n+[0]*(m+1)));piv=0
 while any(t<0 for t in obj[:-1]):
  j=next(j for j,t in enumerate(obj[:-1]) if t<0);i=min((i for i in range(m) if tab[i][j]>0),key=lambda i:(tab[i][-1]/tab[i][j],B[i]));v=tab[i]=[a/tab[i][j] for a in tab[i]]
  for h,u in enumerate(tab):
   if h!=i and u[j]:tab[h]=[a-u[j]*x for a,x in zip(u,v)]
  obj=[a-obj[j]*x for a,x in zip(obj,v)];B[i]=j;piv+=1
 x={j:tab[i][-1] for i,j in enumerate(B) if j<n and tab[i][-1]};y=obj[n:n+m];opt=obj[-1];assert min(y)>=0 and all(v>=0 for v in x.values()) and sum(x.values())==sum(u*v for u,v in zip(b,y))==opt;assert all(sum(v*row[j] for j,v in x.items())<=rhs for row,rhs in zip(C,b));assert all(sum(v*row[j] for row,v in zip(C,y))>=1 for j in range(n));rows.append(dict(record=record,opt=str(opt),passes=opt<6,classes=m,pivots=piv,weights={k:str(v) for k,v in zip(ks,y) if v},dualWitness={F[j]:str(v) for j,v in x.items()}))
print(collections.Counter(v['passes'] for v in rows));print('range',min(Q(x['opt']) for x in rows),max(Q(x['opt']) for x in rows));print('equal',sum(Q(x['opt'])==6 for x in rows));(root/'voevodsky/results/ramsey_37_miss_count_lp.json').write_text(json.dumps(rows,indent=2)+'\n')
