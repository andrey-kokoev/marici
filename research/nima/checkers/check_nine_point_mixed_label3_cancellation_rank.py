"""Test chi3^4 and chi3^3 necessary cancellation constraints for all 50 histories."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_label3_history_cancellation_rank as prior
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prime=1000003

def residue(value):
 q=s.Rational(value);den=int(s.denom(q))%prime
 assert den!=0
 return int(s.numer(q))%prime*pow(den,-1,prime)%prime

def modular_rank(matrix):
 mat=[list(map(residue,row)) for row in matrix]
 count=len(mat);cols=len(mat[0]);pivot=0;pivot_columns=[]
 for col in range(cols):
  candidate=next((r for r in range(pivot,count) if mat[r][col]),None)
  if candidate is None:continue
  mat[pivot],mat[candidate]=mat[candidate],mat[pivot]
  inverse=pow(mat[pivot][col],-1,prime)
  mat[pivot]=[v*inverse%prime for v in mat[pivot]]
  for r in range(count):
   if r==pivot or not mat[r][col]:continue
   fac=mat[r][col]
   mat[r]=[(a-fac*b)%prime for a,b in zip(mat[r],mat[pivot])]
  pivot_columns.append(col);pivot+=1
  if pivot==count:break
 return pivot,pivot_columns

rays=list(prior.active)
triples=list(itertools.combinations_with_replacement(range(8),3))
independent_cubic,pivots=modular_rank([[s.prod(v[i] for i in triple) for triple in triples] for v in rays])
assert independent_cubic==17
partners=(1,2,4,5,6,7,8,9)
pairs=list(itertools.combinations(partners,2))
results=[]
for group in prior.groups:
 representative=next(ray for ray,indices in prior.active.items() if indices==group)
 ipivot=next(i for i,v in enumerate(representative) if v!=0)
 rows=[]
 for index in group:
  A,B=prior.fermionic_rows[index]
  scale=prior.pair(A,B,3,partners[ipivot])
  assert scale!=0
  rows.append([s.S.One]+[s.factor(prior.pair(A,B,p,q)/scale) for p,q in pairs])
 rank,columns=modular_rank(rows)
 results.append({'history_indices':group,'augmented_chi3_four_and_three_rank':rank,
                 'history_count':len(group),'independent':rank==len(group),
                 'pivot_conditions':['chi3^4' if j==0 else 'chi3^3 with pair '+str(pairs[j-1]) for j in columns]})
# Do NOT decouple distinct fourth-power rays in the chi3^3 sector:
# their cubic powers have rank 17, not 18. Directly build the GLOBAL
# restriction matrix across all 41 active histories and 1..4 chi3 flavors.
active_indices=sorted(i for indices in prior.active.values() for i in indices)
assert len(active_indices)==41
V=[];W=[]
for i in active_indices:
 A,B=prior.fermionic_rows[i]
 V.append([residue(prior.pair(A,B,3,p)) for p in partners])
 W.append([residue(prior.pair(A,B,p,q)) for p,q in pairs])
global_basis={};global_pivots=[];rank_by_power={}
def add_coordinate(k,vs,ws):
 column=[int(s.prod(v[t] for t in vs)*s.prod(w[t] for t in ws))%prime for v,w in zip(V,W)]
 for pivot,old in sorted(global_basis.items()):
  if column[pivot]:
   coeff=column[pivot]
   column=[(a-coeff*b)%prime for a,b in zip(column,old)]
 position=next((j for j,c in enumerate(column) if c),None)
 if position is None:return
 inv=pow(column[position],-1,prime)
 global_basis[position]=[c*inv%prime for c in column]
 global_pivots.append({'chi3_flavors':k,'other_label_indices':list(vs),'pair_indices':list(ws)})
for k in (4,3,2,1):
 for vs in itertools.combinations_with_replacement(range(8),k):
  for ws in itertools.combinations_with_replacement(range(28),4-k):
   add_coordinate(k,vs,ws)
   if len(global_basis)==len(active_indices):break
  if len(global_basis)==len(active_indices):break
 rank_by_power[str(k)]=len(global_basis)
 if len(global_basis)==len(active_indices):break
assert rank_by_power=={'4':18,'3':31,'2':41}
if prior.witness_index:
 first=json.loads((OUT/'nine-point-mixed-label3-cancellation-rank.json').read_text())
 assert first['global_chi3_restriction_rank_by_number_of_flavors']==rank_by_power
print(json.dumps({'witness_index':prior.witness_index,'cubic_ray_rank':independent_cubic,
 'global_rank_by_chi3_flavors':rank_by_power,
 'groups':[{k:row[k] for k in ('history_indices','augmented_chi3_four_and_three_rank','history_count')} for row in results]},indent=2))
report={'schema':'marici.nima.nine-point-mixed-label3-cancellation-rank.v1','passed':True,
 'witness_index':prior.witness_index,'prime':prime,
 'distinct_label3_cubic_ray_rank':independent_cubic,'cubic_monomial_pivot_columns':[list(triples[j]) for j in pivots],
 'group_augmented_ranks':results,'global_chi3_restriction_rank_by_number_of_flavors':rank_by_power,
 'global_chi3_restriction_independent_coordinate_certificate':global_pivots,
 'logical_test':'The global chi3 restriction ranks of 41 active authored fermionic fourth powers are 18 with four chi3 flavors, 31 after three, and FULL 41 after two. Each selected 41x41 modular minor is a nonzero rational determinant at the exact witness, so the restriction is injective on these 41 histories on a generic kinematic open set. No nonzero scalar-weighted combination of the 41 can be independent of chi3. Cubic-ray rank is only 17, so grouping by fourth-power rays is NOT enough for mixed-sector cancellation.',
 'consequence_with_prior':'The earlier all-eight-label projection independently excludes sums of the nine individually chi3-free histories. Together these two necessary fermionic obstructions exclude the complete starred fourmass invariant from the scalar linear span of ALL 50 standard sourced n9 NNMHV nested-R history fermion tensors, assuming the calibrated dual-momentum-twistor incidence conventions.',
 'boundary':'Two exact witnesses with modular rank certificates; bosonic R denominators are not needed for arbitrary-scalar span exclusion. No claim that the complete n9 tree amplitude vanishes, nor a theorem about arbitrary non-source Yangian histories, global form, or image coverage.'}
filename='nine-point-mixed-label3-cancellation-rank'+('-witness2' if prior.witness_index else '')+'.json'
(OUT/filename).write_text(json.dumps(report,indent=2)+'\n')
