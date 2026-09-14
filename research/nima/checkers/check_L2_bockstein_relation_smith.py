"""Integral relation-kernel presentation for the labelled L2 Bockstein."""
import argparse,importlib.util,json,math
from pathlib import Path
from flint import fmpz_mat

def load_formula(path):
 s=importlib.util.spec_from_file_location('l2formula',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def diag(M):
 S=M.snf();return [abs(int(S[i,i])) for i in range(min(S.nrows(),S.ncols())) if S[i,i]]
def main():
 p=argparse.ArgumentParser();p.add_argument('--formula',required=True);p.add_argument('--cutoff',type=int,default=12);p.add_argument('--output',required=True);a=p.parse_args();m=load_formula(a.formula);Q=m.Q
 one={(0,0,0):Q(1)};u={(1,0,0):Q(1)};aa={(0,1,0):Q(1)};b={(0,0,1):Q(1)}
 l1=m.add(m.add(b,one),m.scale(u,-1));l2m=m.add(aa,m.scale(u,Q(-1,2)));l2p=m.add(aa,m.scale(u,Q(1,2)))
 a2=m.power(aa,2);k=m.add(m.power(aa,4),m.add(m.mul(u,a2),m.scale(m.mul(m.mul(u,a2),m.power(b,2)),-1)))
 base=[(i,j) for s in range(a.cutoff+1) for i in range(1,s+1,2) for j in [s-i]];pos={x:i for i,x in enumerate(base)};v0=[];v1=[]
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  for s in range(a.cutoff+1):
   for i in range(s+1):
    f={(0,i,s-i):Q(1)}
    for plus in (False,True):
     for isq in (False,True):
      col=m.exact(sa,sb,f,isq,plus,k,l1,l2m,l2p)
      if not col or any(x+y>a.cutoff for _,x,y in col):continue
      x=[0]*len(base);y=[0]*len(base)
      for (uu,aa0,bb0),c in col.items():
       if aa0%2==0:continue
       if uu==0:x[pos[(aa0,bb0)]]=int(c)
       else:
        z=2*c;assert z.denominator==1;y[pos[(aa0,bb0)]]=int(z)
      v0.append(x);v1.append(y)
 A=fmpz_mat(list(map(list,zip(*v0))));B=fmpz_mat(list(map(list,zip(*v1))))
 # Row-HNF of the paired lattice {(Ax,Bx)} avoids constructing the huge
 # transformation matrix. Rows whose A block vanishes are exactly
 # {0} x B(ker_Z A), since HNF pivot order makes the intersection explicit.
 paired=fmpz_mat([[A[i,j] for i in range(A.nrows())]+[B[i,j] for i in range(B.nrows())]
                  for j in range(A.ncols())])
 H=paired.hnf()
 relation_rows=[i for i in range(H.nrows())
                if any(H[i,j]!=0 for j in range(H.ncols()))
                and all(H[i,j]==0 for j in range(A.nrows()))]
 C=fmpz_mat([[H[i,A.nrows()+j] for i in relation_rows] for j in range(B.nrows())])
 nullity=A.ncols()-A.rank()
 old=diag(A)
 Aug=fmpz_mat([[A[i,j] for j in range(A.ncols())]+[C[i,j] for j in range(C.ncols())] for i in range(A.nrows())])
 aug=diag(Aug)
 transition=[0]*len(base);transition[pos[(3,0)]]=3;transition[pos[(3,1)]]=3
 HA,TA=A.hnf(transform=True)
 left_rows=[i for i in range(HA.nrows()) if all(HA[i,j]==0 for j in range(HA.ncols()))]
 transition_detector_values=[sum(int(TA[i,j])*transition[j] for j in range(A.nrows())) for i in left_rows]
 transition_detector_gcd=math.gcd(*transition_detector_values)
 detected=[(abs(v),i,v) for i,v in zip(left_rows,transition_detector_values) if v]
 minabs,detector_row,detector_value=min(detected)
 detector_sign=1 if detector_value>0 else -1
 sparse_detector=[{'monomial':list(base[j]),'coefficient':detector_sign*int(TA[detector_row,j])}
                  for j in range(A.nrows()) if TA[detector_row,j]]
 canonical=[]
 for j in range(a.cutoff-4):
  v=[0]*len(base);v[pos[(3,j)]]=1;v[pos[(3,j+2)]]=-1;canonical.append(v)
 for j in (0,1):
  if (11,j) in pos:
   v=[0]*len(base);v[pos[(11,j)]]=1;canonical.append(v)
 Canon=fmpz_mat([[A[i,j] for j in range(A.ncols())]+[v[i] for v in canonical] for i in range(A.nrows())])
 CanonL2=fmpz_mat([[Canon[i,j] for j in range(Canon.ncols())]+[transition[i]] for i in range(Canon.nrows())])
 canonical_smith=diag(Canon);canonical_l2_smith=diag(CanonL2)
 Sum=fmpz_mat([[Aug[i,j] for j in range(Aug.ncols())]+[CanonL2[i,j] for j in range(CanonL2.ncols())]
               for i in range(Aug.nrows())])
 sum_smith=diag(Sum)
 With=fmpz_mat([[Aug[i,j] for j in range(Aug.ncols())]+[transition[i]] for i in range(Aug.nrows())])
 with_transition=diag(With)
 divided_transition=[z//3 for z in transition]
 WithDivided=fmpz_mat([[Aug[i,j] for j in range(Aug.ncols())]+[divided_transition[i]] for i in range(Aug.nrows())])
 with_divided_transition=diag(WithDivided)
 aug_index=math.prod(aug);transition_index=math.prod(with_transition)
 out={'schema':'marici.nima.L2-bockstein-relation-smith.v1','status':'passed','D':a.cutoff,
  'odd_target_rank':len(base),'labelled_columns':len(v0),'relation_nullity':nullity,
  'image_rank':len(old),'image_plus_bockstein_rank':len(aug),'bockstein_rank_gain':len(aug)-len(old),
  'image_smith_nonunits':[x for x in old if x!=1],
  'augmented_smith_nonunits':[x for x in aug if x!=1],
  'left_annihilator_rank':len(left_rows),
  'distinguished_transition_left_detector_gcd':abs(transition_detector_gcd),
  'primitive_transition_detector_exists':abs(transition_detector_gcd)==1,
  'minimal_basis_detector_value':minabs,
  'normalized_sparse_transition_detector':sparse_detector,
  'canonical_rank_gain':len(canonical_smith)-len(old),
  'canonical_plus_L2_rank_gain':len(canonical_l2_smith)-len(old),
  'canonical_nonunits':[x for x in canonical_smith if x!=1],
  'canonical_plus_L2_nonunits':[x for x in canonical_l2_smith if x!=1],
  'canonical_plus_L2_reaches_full_bockstein_rank':len(canonical_l2_smith)==len(aug),
  'sum_lattice_nonunits':[x for x in sum_smith if x!=1],
  'sum_lattice_rank':len(sum_smith),
  'sum_over_canonical_plus_L2_index':math.prod(canonical_l2_smith)//math.prod(sum_smith),
  'sum_over_full_bockstein_index':math.prod(aug)//math.prod(sum_smith),
  'canonical_plus_L2_contained_in_full_bockstein':math.prod(aug)==math.prod(sum_smith),
  'full_bockstein_contained_in_canonical_plus_L2':math.prod(canonical_l2_smith)==math.prod(sum_smith),
  'distinguished_transition':'3*a^3+3*a^3*b',
  'rank_with_distinguished_transition':len(with_transition),
  'transition_torsion_index_ratio':aug_index//transition_index if len(with_transition)==len(aug) else None,
  'smith_with_transition_nonunits':[x for x in with_transition if x!=1],
  'rank_with_divided_transition':len(with_divided_transition),
  'divided_transition_torsion_index_ratio':aug_index//math.prod(with_divided_transition) if len(with_divided_transition)==len(aug) else None,
  'smith_with_divided_transition_nonunits':[x for x in with_divided_transition if x!=1],
  'lattice':'u0 original; u1 generator u/2','scope':'exact cutoff integral relation-kernel presentation'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
