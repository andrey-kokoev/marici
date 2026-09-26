"""Reduce the complete parity tensor to its actual single-flavor span."""
from pathlib import Path
import itertools,json
import sympy as s
root=Path(__file__).resolve().parents[1]
source=json.loads((root/'results/seven-point-full-parity-tensor.json').read_text());results=[]
for witness in source['witnesses']:
 terms=witness['direct_terms']+witness['Fourier_transformed_parity_terms']
 V=s.Matrix.hstack(*(s.Matrix(list(map(s.Rational,t['vector']))) for t in terms))
 _,columns=V.rref();basis=V[:,list(columns)];rank=len(columns)
 _,rows=basis.T.rref();square=basis[list(rows),:];coords=square.inv()*V[list(rows),:]
 assert basis*coords==V
 weights=[s.Rational(t['weight'])*(1 if i<6 else -1) for i,t in enumerate(terms)]
 monomials=list(itertools.combinations_with_replacement(range(rank),4));identities=[]
 for indices in monomials:
  value=s.factor(sum(weights[j]*s.prod(coords[i,j] for i in indices) for j in range(12)))
  assert value==0
  identities.append({'indices':indices,'difference':str(value)})
 results.append({'input_index':witness['input_index'],'single_flavor_span_rank':rank,'basis_term_columns':columns,'pivot_component_rows':rows,'symmetric_quartic_checks':len(identities),'identities':identities,'coordinates':[[str(x) for x in row] for row in coords.tolist()]})
report={'passed':True,'witnesses':results,'scope':'Exact rank reduction and all symmetric quartic identities at the two saved rational inputs. Basis embedding checked on all35 components; not yet a symbolic bosonic identity.'}
(root/'results/seven-point-parity-reduction.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'ranks':[r['single_flavor_span_rank'] for r in results],'quartic_checks':[r['symmetric_quartic_checks'] for r in results],'pivots':[r['pivot_component_rows'] for r in results]}))
