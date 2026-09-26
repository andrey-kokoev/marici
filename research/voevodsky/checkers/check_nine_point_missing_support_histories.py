"""Resolve the missing mixed component into authored history contributions."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
from nine_point_source_r import Kinematics
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_cube_families_offface_chi1_chi5_independence as data
root=Path(__file__).resolve().parents[1]
hist=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
span=json.loads((root/'results/nine-point-four-cell-span.json').read_text())
pairs=((1,9),(2,8),(3,7),(4,6));rows=[]
for e,old in zip((s.Rational(1,2),s.S.One),span['witnesses']):
 p=dict(zip(data.vars,(e,1,1,1,1,1,3,2)));Y=data.cube.E['E'].subs(p)*data.Z9
 B=Y[:,:2].inv()*Y[:,2:];z=data.Z9[:,2:]-data.Z9[:,:2]*B;kin=Kinematics(z.tolist());terms=[]
 for index,record in enumerate(hist):
  a1,b1=record['outer_pair'];a,b=record['inner_pair'];A,f=kin.ordinary(a1,b1);D,g=kin.inner(a1,b1,a,b,record['branch'])
  wedges=[s.factor(A[u]*D[v]-A[v]*D[u]) for u,v in pairs]
  term=s.factor(f*g*s.prod(wedges))
  if term:terms.append({'source_ledger_index':index,'history':record,'coefficient':str(term),'pair_wedges':list(map(str,wedges))})
 total=s.factor(sum(s.Rational(t['coefficient']) for t in terms))
 assert total==s.Rational(old['tree_vector'][3]) and total!=0
 M=s.Matrix([[s.Rational(x) for x in row] for row in old['cell_matrix']]);assert M[3,:]==s.zeros(1,4)
 aug=M.row_join(s.Matrix(list(map(s.Rational,old['tree_vector']))))
 # Compact explicit nonzero minor supplementing the earlier exact rank call.
 certificate=None
 for rr in itertools.combinations(range(5),3):
  for cc in itertools.combinations(range(5),3):
   det=s.factor(aug.extract(rr,cc).det())
   if det:certificate={'rows':rr,'columns':cc,'determinant':str(det)};break
  if certificate:break
 assert certificate
 rows.append({'e':str(e),'quotient_twistors':[[str(x) for x in row] for row in z.tolist()],'nonzero_history_count':len(terms),'terms':terms,'sum':str(total),'cell_mixed_row':list(map(str,M[3,:])),'augmented_rank_lower_bound_minor':certificate})
assert [r['source_ledger_index'] for r in rows[0]['terms']]==[r['source_ledger_index'] for r in rows[1]['terms']]
report={'passed':True,'flavor_pairs':pairs,'witnesses':rows,'scope':'Exact source-history decomposition of one missing component at two common targets. Ledger indices belong to the local source contract, not the inherited history ordering. Nonzero terms are missing support sectors, not certified positive cells or a minimal completion.'}
(root/'results/nine-point-missing-support-histories.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'counts':[r['nonzero_history_count'] for r in rows],'histories':[t['history'] for t in rows[0]['terms']]},indent=2))
