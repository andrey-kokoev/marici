#!/usr/bin/env python3
"""Exact source-conformance checks for the four-point one-loop MHV integrand."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
fixture=json.loads((ROOT/'research/nima/fixtures/four-point-one-loop-mhv-source.v1.json').read_text())
# Exponent bookkeeping for <1234>^2/(<AB12><AB23><AB34><AB41>).
external={i:2 for i in range(1,5)}
denoms=((1,2),(2,3),(3,4),(4,1))
for i,j in denoms:
 external[i]-=1;external[j]-=1
loop_basis={'A':-len(denoms),'B':-len(denoms)}
# Every denominator is a distinct linear Pluecker divisor and occurs once.
poles=fixture['object']['physical_poles'];dlogs=fixture['object']['dlog_coordinates']
checks={
 'source_formula_exact':fixture['object']['rational_integrand']=='<1234>^2/(<AB12><AB23><AB34><AB41>)',
 'external_projective_weight_zero':all(v==0 for v in external.values()),
 'loop_basis_rational_weight_minus_four':loop_basis=={'A':-4,'B':-4},
 'four_simple_physical_poles':len(poles)==4 and len(set(poles))==4,
 'no_spurious_poles':fixture['object']['spurious_poles']==[],
 'four_dlog_coordinates':len(dlogs)==4 and len(set(dlogs))==4,
 'preintegration_scope_explicit':'Pre-integration' in fixture['claim_boundary']
}
out={
 'schema':'marici.nima.four-point-one-loop-mhv-integrand.v1',
 'source_fixture':'research/nima/fixtures/four-point-one-loop-mhv-source.v1.json',
 'integrand':fixture['object']['rational_integrand'],
 'external_projective_weights':{str(k):v for k,v in external.items()},
 'loop_basis_rational_weights':loop_basis,
 'physical_poles':poles,
 'checks':checks,
 'passed':all(checks.values()),
 'scope':'Exact weight and denominator conformance for the sourced pre-integration four-point one-loop MHV rational integrand.'
}
p=ROOT/'research/nima/results/four-point-one-loop-mhv-integrand.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
