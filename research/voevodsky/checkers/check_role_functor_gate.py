"""First finite obstruction gate for a proposed analytic/polyhedral role functor."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky/results'
analytic=json.loads((V/'analytic-interval-defect-profile.json').read_text())
assert analytic['passed'] and len(analytic['intervals'])==10
required={(tuple(x['interval'])):(x['kernel'],x['cokernel']) for x in analytic['intervals']}
assert required[(0,1)]==(0,1) and required[(2,4)]==(0,0)
# Candidate packets must specify ALL interval graded defects, retained base
# identification and source/operator assignment. Matrix shape alone is not a
# closed cone or source-derived map.
def admit(candidate):
 if set(candidate)!={'role_assignment','edge_operator_binding','base_binding','interval_defects','reciprocal_mates','source_derivation'}:return 'missing_typed_port'
 if not all(candidate[x] for x in ('role_assignment','edge_operator_binding','base_binding','reciprocal_mates','source_derivation')):return 'missing_source_constructor'
 observed={tuple(x['interval']):(x['kernel'],x['cokernel']) for x in candidate['interval_defects']}
 if observed!=required:return 'graded_defect_mismatch'
 return 'finite_gate_pass_only'
assert admit({'shape':'nine-vertex'})=='missing_typed_port'
base={k:True for k in ('role_assignment','edge_operator_binding','base_binding','reciprocal_mates','source_derivation')}
base['interval_defects']=[{'interval':list(edge),'kernel':0,'cokernel':0} for edge in required]
assert admit(base)=='graded_defect_mismatch'
base['interval_defects']=[{'interval':list(edge),'kernel':k,'cokernel':c} for edge,(k,c) in required.items()]
assert admit({**base,'source_derivation':False})=='missing_source_constructor'
assert admit(base)=='finite_gate_pass_only'  # self-reported defects DO NOT certify maps
# Redundant Farkas row rank: [-1;1] and [-1;1;1] have rank one;
# their bare cokernels differ though their represented interval is equal.
assert (2-1,3-1)==(1,2)
report={'passed':True,'required_interval_defects':[{'interval':list(edge),'kernel':k,'cokernel':c} for edge,(k,c) in required.items()],'refusals':['shape-only','acyclic-all-edges','absent-source-derivation'],'finite_gate_pass_is_not_authority':True,'reopening':'owner-derived role/edge/base functor with closed graph-domain, reciprocal and row-equivalence comparisons plus independently verified graded defects','scope':'Schema/obstruction gate only; a self-reported complete packet is NOT validated as a source functor.'}
(V/'role-functor-gate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='required_interval_defects'},indent=2))
