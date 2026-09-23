"""Match the paired carrier to the primary-source starred four-mass psi cell."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=ROOT/'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'
tex=source.read_text(encoding='utf-8')
fixture=json.loads((ROOT/'research/nima/fixtures/n2mhv-yangian-invariant-constructor-coverage.v1.json').read_text())
assert fixture['source']==str(source.relative_to(ROOT)).replace('\\','/')
psi=next(entry for entry in fixture['cyclic_classes'] if entry['id']==9)
assert psi['kind']=='four-mass-psi' and psi['formula']=='psi [A,1,2,3,4] [B,5,6,7,8]'
position=tex.index(r'\psi\,\left[A,1,2,3,4\right]')
row=tex[position-1800:position+120]
assert r'(1\,2)&(3\,4)&(5\,6)&(7\,8)' in row
assert r'\{2,5,4,7,6,9,8,11\}' in row
assert 'four-mass box' in tex[position:position+4000]
assert 'two solutions to $C(\\vec{\\alpha})\\!\\cdot\\!Z=0$' in tex[position:position+4000]
assert 'sum-over particular solutions' in tex[position:position+20000]
# Independent bounded-affine-permutation calculation by cyclic interval ranks.
# Labels are parallel-class ids; None denotes the deleted physical column.
def rank(groups):return min(2,len(set(g for g in groups if g is not None)))
def permutation(groups):
 n=len(groups);result=[]
 for i in range(n):
  if groups[i] is None:result.append(i+1);continue
  for j in range(i+1,i+2*n+1):
   interval=[groups[z%n] for z in range(i,j+1)]
   if rank(interval)==rank(interval[1:]):result.append(j+1);break
  else:raise AssertionError('permutation not found')
 return result
n8=permutation([0,0,1,1,2,2,3,3]);n9=permutation([0,0,None,1,1,2,2,3,3])
assert n8==[2,5,4,7,6,9,8,11] and n9==[2,6,3,5,8,7,10,9,13]
assert sum(x-i for i,x in enumerate(n9,start=1))==18
prior=json.loads((OUT/'nine-point-paired-cell-verification.json').read_text());assert prior['passed']
trace=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text());assert trace['passed']
result={'schema':'marici.nima.nine-point-four-mass-source-match.v1','passed':True,
 'primary_source':str(source.relative_to(ROOT)).replace('\\','/'),
 'source_table':'g2n_yangian_invariants, starred row; four_mass_explicit_solution and following discussion',
 'sourced_eight_point_psi_class':psi['formula'],
 'sourced_eight_point_parallel_classes':[[1,2],[3,4],[5,6],[7,8]],
 'sourced_eight_point_bounded_permutation':n8,
 'nine_point_zero_column_relabeling':{'old_eight_labels_to_physical_nine_labels':[1,2,4,5,6,7,8,9],
  'deleted_physical_label':3,'derived_nine_point_bounded_permutation':n9},
 'source_two_solution_statement_agrees_with_exact_fibre_degree':2,
 'claim_boundary':'The eight-point four-pair cell is source-identified as starred four-mass psi. Its nine-point zero-column embedding is geometrically established, but occurrence and normalization as a sourced nine-point generalized-R history are NOT established.'}
(OUT/'nine-point-four-mass-source-match.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':True,'sourced_cell':'starred eight-point four-mass psi',
 'eight_point_permutation':n8,'embedded_nine_point_permutation':n9,
 'nine_point_generalized_R_history_matched':False},indent=2))
