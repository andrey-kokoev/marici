"""Search intrinsic input-relative counts. Marginalize named deletions and supports, exclude output restorations. Cache legal continuations per output. Test conjugates on the full source group."""
from ramsey38_matching_continuations import data,C,J,D,P,json,ls,combinations,Counter
from itertools import combinations as comb
from functools import lru_cache
@lru_cache(None)
def families(idx):
 h,_,t=data[idx];I=[0]
 for i,v in enumerate(h):I.extend([s|1<<i for s in I if not s&v]);
 out=[]
 for x,y in comb(ls(h[0]),2):
  m=1<<x|1<<y;ts=[q for q in t if not q&m];out.append((x,y,[s for s in I if not s&m and s not in (h[x]&~m,h[y]&~m) and all(q&s for q in ts)]))
 return out
names=['deleted_deg_low','deleted_deg_high','deleted_common','support_size','input_edges_in_support','input_sevens_missed','root_in_support','root_neighbors_in_support','input_deleted_support_links'];K=range(len(names))
@lru_cache(None)
def observations(i,j):
 h,_,t=data[i];rows=[]
 for x,y,fam in families(j):
  deg=sorted([h[x].bit_count(),h[y].bit_count()]);m=1<<x|1<<y
  for s in fam:rows.append((*deg,(h[x]&h[y]).bit_count(),s.bit_count(),sum((h[z]&s).bit_count() for z in ls(s))//2,sum(not q&(m|s) for q in t),s&1,(s&h[0]).bit_count(),(s&h[x]).bit_count()+(s&h[y]).bit_count()))
 return rows

def counts(i,j,cols):return Counter(tuple(row[c] for c in cols) for row in observations(i,j))
i=0;a=C[i];b=J[i];found=None
for n in range(1,len(names)+1):
 for cols in comb(K,n):
  L,R=counts(i,a,cols),counts(i,b,cols)
  if L!=R:
   val=min(k for k in L.keys()|R.keys() if L[k]!=R[k]);found=(cols,val,L[val],R[val]);break
 if found:break
if found:
 cols,val,l,r=found;replay=[(counts(g[i],g[a],cols)[val],counts(g[i],g[b],cols)[val]) for g in P.values()];assert set(replay)=={(l,r)};o=dict(fields=[names[c] for c in cols],values=val,counts=[l,r],relabels=len(replay),per_input=[[counts(k,z,cols)[val] for z in (C[k],J[k])] for k in range(8)],totals=[len(observations(i,z)) for z in (a,b)])
 hi=[C[k] if x>y else J[k] for k,(x,y) in enumerate(o['per_input'])];lo=[J[k] if hi[k]==C[k] else C[k] for k in range(8)];A=P[(1,0,3,2,4,5,6)];B=P[(1,0,2,3,5,4,6)];o['intrinsic_selectors']=[]
 for sel in (lo,hi):
  assert all(sel[sel[k]]==k and all(g[sel[k]]==sel[g[k]] for g in P.values()) for k in range(8));squares_preserved=all(sel[v] in (A[sel[k]],B[sel[k]]) for k in range(8) for v in (A[k],B[k]));o['intrinsic_selectors'].append(dict(involutive=True,equivariant=True,square_interface=squares_preserved,partners=sel))
else:o=dict(no_hit=True)
print(o);(D/'ramsey38_relative_query.json').write_text(json.dumps(o,indent=2)+'\n')
