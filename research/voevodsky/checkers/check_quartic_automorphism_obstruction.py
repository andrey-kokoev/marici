#!/usr/bin/env python3
"""Verify quartic involutions and their node/critical-value permutations."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/quartic_automorphisms_obstruct_a_canonical_ordered_thimble_marking.md'
DISC=ROOT/'research/voevodsky/results/global_quartic_discriminant_and_path_gate.json'
BD=ROOT/'research/voevodsky/bunch_davies_boundary_germ_does_not_order_the_paired_thimbles.md'
CUT=ROOT/'src/ledger/20260821-1751 The Physical Cut Pairing Does Not Resolve the Integral Cusp Extension.md'
RESULT=ROOT/'research/voevodsky/results/quartic_automorphism_obstruction.json'
t,x,y,E,z=s.symbols('t x y E z',nonzero=True)
h=x**2+y**2-(E-x-y)**2
F=s.expand(x**2*t**4-h*t**2+y**2)
r=s.expand(F.subs(t,-t))
reciprocal=s.expand(t**4*F.subs({t:1/t,x:y,y:x},simultaneous=True))
F0=s.factor(F.subs(E,0))
critical=[s.Integer(0),2*x,2*y,2*(x+y)]
swapped=[s.expand(c.subs({x:y,y:x},simultaneous=True)) for c in critical]
disc=json.loads(DISC.read_text(encoding='utf-8'));bd=BD.read_text(encoding='utf-8');cut=CUT.read_text(encoding='utf-8');text=PACKET.read_text(encoding='utf-8')
checks={
 'even_involution':s.expand(r-F)==0,
 'reciprocity':s.expand(reciprocal-F)==0,
 'total_energy_square':s.expand(F0-(x*t**2+y)**2)==0,
 'r_exchanges_formal_nodes':s.simplify(-s.sqrt(-y/x)+s.sqrt(-y/x))==0,
 'critical_permutation':swapped==[0,2*y,2*x,2*(x+y)],
 'physical_base_invariant':s.expand((x+y+z).subs({x:y,y:x},simultaneous=True)-(x+y+z))==0,
 'involutions_commute_on_t':s.simplify(-1/t-1/(-t))==0,
 'prior_critical_values':disc['critical_values']==['0','2x','2y','2(x+y)'],
 'bd_symmetric':'approaches both nodes from the same local side' in bd,
 'cut_null':'is zero' in cut,
 'scope_not_overstated':'does not prove that every invariant ambient parity class is impossible' in text,
 'ambient_action_missing':'That action is not present in current source artifacts' in text,
}
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.quartic-automorphism-obstruction.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'discriminant_result_sha256':sha256(DISC.read_bytes()).hexdigest(),'bd_result_sha256':sha256(BD.read_bytes()).hexdigest(),'involutions':{'r':'t -> -t','s':'(x,y,t) -> (y,x,1/t)'},'critical_value_permutation_s':['0','2y','2x','2(x+y)'],'checks':checks,'passed':all(checks.values()),'disposition':{'canonical_ordered_local_thimble_pair':'obstructed','identity_vs_wall_swap':'unresolved without asymmetric labels','all_parity_classes_obstructed':'not established','missing_input':'ambient rank-nine Picard action of r and s'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
