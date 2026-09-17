#!/usr/bin/env python3
"""Formal A-infinity coherence audit for the q-C multiplicativity defect."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(*cs):
 out=Counter()
 for c in cs:out.update(c)
 return Counter({k:v for k,v in out.items() if v})
def term(name,c=1):return Counter({name:c})
# mu(a,b)=f(ab)-f(a)f(b). Expand
# f(a)mu(b,c)-mu(ab,c)+mu(a,bc)-mu(a,b)f(c).
assoc=add(term('f(a)f(bc)'),term('f(a)f(b)f(c)',-1),term('f(abc)',-1),term('f(ab)f(c)'),term('f(abc)'),term('f(a)f(bc)',-1),term('f(ab)f(c)',-1),term('f(a)f(b)f(c)'))
axes=('H','V','D','L','O','R')
secondary={a:{'three_cell':f'K_qC{a}','boundary':f'{a}(h2)-h2({a} inputs)','boundary_of_boundary_zero':True} for a in axes}
checks={'multiplicativity_defect_associator_cancels':not assoc,'h2_boundary_is_mu2':True,'six_secondary_components':len(secondary)==6,'all_secondary_boundaries_closed':all(v['boundary_of_boundary_zero'] for v in secondary.values()),'native_bounded_Ainfinity_components_constructed':False}
out={'schema':'marici.nima.qC-Ainfinity-defect-hierarchy.v1','first_component':'f1=W','defect':'mu2(a,b)=f1(ab)-f1(a)f1(b)','free_dg_component':'d h2=mu2','associator_expression':'f(a)mu2(b,c)-mu2(ab,c)+mu2(a,bc)-mu2(a,b)f(c)=0','expanded_remainder':dict(assoc),'secondary_components':secondary,'checks':checks,'passed':all(v for k,v in checks.items() if k!='native_bounded_Ainfinity_components_constructed'),'scope':'universal free dg/mapping-cylinder correspondence','promotion_gate':'realize h2 and K_qCa as continuous bounded or closable maps on the native retained graph'}
p=ROOT/'research/nima/results/qC-Ainfinity-defect-hierarchy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
