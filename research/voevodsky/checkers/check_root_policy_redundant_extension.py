"""Finite row-root selection square under exact redundant-row extension."""
from fractions import Fraction as Q
from pathlib import Path
import json
old_roots=('x-low','x-high','y-low','y-high')
new_roots=old_roots+('z-diagonal',)
p=(Q(0),Q(1),Q(0),Q(1));ip=p+(Q(0),);q=(Q(0),)*4+(Q(1),)
def retract(v):return (v[0],v[1]+v[4],v[2],v[3]+v[4])
def pick(candidates,roots):return min(candidates,key=lambda v:tuple(v[roots.index(k)] for k in sorted(roots)))
def root_image(v,rs):
 rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1),((1,1),2))[:len(rs)]
 return tuple(sum(rows[i][0][j]*v[i] for i in range(len(v))) for j in (0,1)),sum(rows[i][1]*v[i] for i in range(len(v)))
assert root_image(p,old_roots)==root_image(ip,new_roots)==root_image(q,new_roots)==((1,1),Q(2))
assert retract(ip)==retract(q)==p
assert pick((p,),old_roots)==p
assert pick((ip,q),new_roots)==q # z-root sorts AFTER x-high, so smaller x-high wins
assert pick((ip,q),new_roots)!=ip
assert retract(pick((ip,q),new_roots))==pick((p,),old_roots)
# An inclusion-natural finite selector can prioritize zero *new* row multiplier.
relative=lambda v:(v[4],tuple(v[old_roots.index(k)] for k in sorted(old_roots)))
assert min((ip,q),key=relative)==ip
report={'passed':True,'same_target_and_bound':True,'new_proof_retracts_to_old':True,'root_lex_extension_selects_new_row':True,'root_lex_inclusion_naturality_fails':True,'retraction_selection_square_passes_in_this_finite_example':True,'zero_fresh_row_priority_repairs_inclusion_for_this_finite_example':True,'scope':'Frozen two-element candidate set; no general impossibility, no canonical global selection, no source-owner grant or analytic role functor.'}
out=Path(__file__).resolve().parents[1]/'results/root-policy-redundant-extension.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
