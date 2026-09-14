#!/usr/bin/env python3
"""Classify physical basepoint chambers by triangle inequalities."""
from hashlib import sha256
from pathlib import Path
import itertools,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/physical_basepoint_chamber_is_equivalent_to_triangle_inequalities.md';DISC=ROOT/'research/voevodsky/results/global_quartic_discriminant_and_path_gate.json';CM=ROOT/'research/benincasa/cayley-menger-contour-family-gate.json';RESULT=ROOT/'research/voevodsky/results/physical_basepoint_triangle_chambers.json';x,y,z=s.symbols('x y z',positive=True);Ep=x+y+z;diffs=[s.expand(Ep-2*x),s.expand(Ep-2*y),s.expand(Ep-2*(x+y))];samples={'triangle':(3,4,5),'x_dominant':(6,2,1),'y_dominant':(2,6,1),'z_dominant':(2,1,6)}
def classify(v):
 xv,yv,zv=v;e=xv+yv+zv
 if xv>=yv+zv:return 'x_dominant'
 if yv>=xv+zv:return 'y_dominant'
 if zv>=xv+yv:return 'z_dominant'
 return 'triangle'
# Exhaustively verify at most one strict failure for a bounded positive grid.
grid=list(itertools.product(range(1,8),repeat=3));at_most_one=all(sum([a>b+c,b>a+c,c>a+b])<=1 for a,b,c in grid);cm=json.loads(CM.read_text(encoding='utf-8'));disc=json.loads(DISC.read_text(encoding='utf-8'));text=PACKET.read_text(encoding='utf-8');checks={'difference_identities':diffs==[-x+y+z,x-y+z,-x-y+z],'sample_chambers':all(classify(v)==k for k,v in samples.items()),'at_most_one_failure_grid':at_most_one,'four_critical_values_prior':disc['critical_values']==['0','2x','2y','2(x+y)'],'cm_parameters_distinct_labels':cm['three_site_cycle']['external_parameters']==['P1','P2','P3'],'parameter_map_absent':'do not identify those parameters with the quartic variables' in text,'triangle_equivalence_stated':'holds exactly when' in text,'path_gate_retained':'does not choose a based path homotopy' in text};checks={k:bool(v) for k,v in checks.items()};result={'schema':'marici.voevodsky.physical-basepoint-triangle-chambers.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'discriminant_result_sha256':sha256(DISC.read_bytes()).hexdigest(),'cayley_menger_source_sha256':sha256(CM.read_bytes()).hexdigest(),'differences':[str(v) for v in diffs],'chambers':list(samples),'checks':checks,'passed':all(checks.values()),'disposition':{'basepoint_ambiguity':'four open chambers plus singular walls','triangle_chamber_interval':'max(2x,2y)<Ephys<2(x+y)','source_chamber':'unselected without P-to-xyz map','based_path':'still missing'}};RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':checks,'disposition':result['disposition']}));raise SystemExit(0 if result['passed'] else 1)
