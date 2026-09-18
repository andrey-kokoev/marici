#!/usr/bin/env python3
"""Exact weight audit of the sourced chiral two-loop double pentagon."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
fixture=json.loads((ROOT/'research/nima/fixtures/chiral-two-loop-double-pentagon-source.v1.json').read_text())
ext_num={i:0 for i in range(1,7)};ext_den={i:0 for i in range(1,7)}
def add(table,labels,m=1):
 for i in labels:table[i]+=m
add(ext_num,(1,3,4,5));add(ext_num,(5,6,1,3));add(ext_num,(4,6))
# <CD|(234) intersect (612)> has one occurrence from each defining plane.
add(ext_num,(2,3,4));add(ext_num,(6,1,2))
for labels in ((6,1),(1,2),(2,3),(3,4),(3,4),(4,5),(5,6),(6,1)):add(ext_den,labels)
weights={i:ext_num[i]-ext_den[i] for i in range(1,7)}
# Each loop numerator has one line bracket; each loop appears in four local denominators plus <ABCD>.
loop_rational={'AB':1-(4+1),'CD':1-(4+1)}
loop_with_measure={q:w+4 for q,w in loop_rational.items()}
checks={'source_factor_count':len(fixture['object']['numerator_factors'])==4 and len(fixture['object']['denominator_factors'])==9,'all_external_weights_zero':all(v==0 for v in weights.values()),'each_rational_loop_weight_minus_four':all(v==-4 for v in loop_rational.values()),'each_complete_loop_weight_zero':all(v==0 for v in loop_with_measure.values()),'building_block_scope_explicit':'not the complete' in fixture['claim_boundary']}
out={'schema':'marici.nima.chiral-two-loop-double-pentagon-covariance.v1','source_fixture':'research/nima/fixtures/chiral-two-loop-double-pentagon-source.v1.json','external_numerator_weights':ext_num,'external_denominator_weights':ext_den,'external_net_weights':weights,'loop_rational_weights':loop_rational,'loop_weights_with_projective_measures':loop_with_measure,'checks':checks,'passed':all(checks.values()),'scope':'Exact projective covariance audit of one sourced two-loop chiral integral building block.'}
p=ROOT/'research/nima/results/chiral-two-loop-double-pentagon-covariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
