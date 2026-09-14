"""Integral Smith audit of the soft-axis plus Cartier defect."""
import argparse,json,math
from collections import Counter
from math import comb
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def columns(D):
    mons=[(a,t-a) for t in range(D+1) for a in range(t+1)]
    pos={m:i for i,m in enumerate(mons)}; cols=[]; degrees=[]
    def emit(terms):
        terms={m:c for m,c in terms.items() if c}
        if not terms or any(sum(m)>D for m in terms):return
        v=[0]*len(mons)
        for m,c in terms.items():v[pos[m]]=c
        cols.append(v);degrees.append(max(map(sum,terms)))
    for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
      ea,eb=2-sa,2-sb
      for t in range(D+1):
       for i in range(t+1):
        j=t-i;p={}
        if j:
         for k in range(ea+1):p[(i+eb,j-1+k)]=p.get((i+eb,j-1+k),0)-j*comb(ea,k)
        if sa:
         for k in range(ea):p[(i+eb,j+k)]=p.get((i+eb,j+k),0)+comb(ea-1,k)
        emit(p);q={}
        if i:
         for k in range(ea+1):q[(i-1+eb,j+k)]=q.get((i-1+eb,j+k),0)+i*comb(ea,k)
        for k in range(ea+1):q[(i+eb-1,j+k)]=q.get((i+eb-1,j+k),0)-(sb+6)*comb(ea,k)
        emit(q)
    products=[]
    for v,d in zip(cols,degrees):
      if d+2>D:continue
      w=[0]*len(mons)
      for n,c in enumerate(v):
       if c:
        a,b=mons[n];w[pos[(a+2,b)]]=c
      products.append(w)
    return mons,cols,products

def smith_summary(cols):
    M=sp.Matrix(cols).T
    rank=M.rank(); S=smith_normal_form(M,domain=ZZ)
    diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
    return rank,diag,sum(d!=1 for d in diag),math.prod(diag)

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();rows=[]
 for D in (12,16,20,24,28):
  mons,image,products=columns(D)
  ri,di,ti,ii=smith_summary(image)
  ra,da,ta,ia=smith_summary(image+products)
  assert ra-ri==1
  M=sp.Matrix(image+products).T
  null=M.T.nullspace(); assert len(null)==1
  den=math.lcm(*[x.q for x in null[0]])
  detector=[int(x*den) for x in null[0]]
  gcd=math.gcd(*detector); detector=[x//gcd for x in detector]
  expected=[((-1)**b if a==0 else 0) for a,b in mons]
  if detector[0]<0: detector=[-x for x in detector]
  assert detector==expected
  rows.append({'D':D,'target_rank':len(mons),'image_rank':ri,'completed_rank':ra,'defect_rank':1,
   'image_nonunit_smith_count':ti,'completed_nonunit_smith_count':ta,
   'image_smith_factor_counts':dict(sorted(Counter(di).items())),
   'completed_smith_factor_counts':dict(sorted(Counter(da).items())),
   'image_index_in_saturation':ii,'completed_index_in_saturation':ia,
   'image_index_prime_factors':sp.factorint(ii),
   'completed_index_prime_factors':sp.factorint(ia),
   'primitive_free_cokernel_detector':'coefficient sum on a=0 weighted by (-1)^b'})
 for row in rows:
  n=row['D']//4; counts={int(k):v for k,v in row['completed_smith_factor_counts'].items()}
  assert set(counts)<= {1,2,14,42}
  assert counts.get(1,0)==n*(6*n+5)
  assert counts.get(2,0)==n*(2*n-3)
  assert row['completed_nonunit_smith_count']==n*(2*n+1)
  assert row['completed_index_prime_factors']=={2:n*(2*n+1),3:counts.get(42,0),7:row['D']}
 out={'schema':'marici.nima.soft-axis-plus-defect-smith.v1','status':'passed','rows':rows,
  'verified_five_cutoff_patterns':{'completed_factor_support':[1,2,14,42],
   'unit_count':'n*(6*n+5)','pure_two_count':'n*(2*n-3)',
   'nonunit_count_and_two_exponent':'n*(2*n+1)','seven_exponent':'D=4*n'},
  'scope':'Exact integer Smith forms at bounded cutoffs; not an all-degree theorem or global chain map.'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
