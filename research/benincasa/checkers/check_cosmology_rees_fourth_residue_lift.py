#!/usr/bin/env python3
"""Construct an exact fourth-normal-residue lift within the active DPC test sequence."""
import json
from pathlib import Path
# P=-189X5-378X4+9720X3-23328X2.
# A(X)= -2X3+6X2, so with a2=3240X:
# P-A(a2)=R0*b3, R0=X2(X-6), b3=-189X2-1512X+7128.
P={5:-189,4:-378,3:9720,2:-23328};A={3:-6480,2:19440};b={2:-189,1:-1512,0:7128}
def evalp(p,x):return sum(v*x**k for k,v in p.items())
for x in range(-5,9):
 lhs=evalp(P,x)-evalp(A,x);rhs=x*x*(x-6)*evalp(b,x);assert lhs==rhs
out={'schema':'marici.benincasa.cosmology-rees-fourth-residue-lift.v1','governing_dpc':'repeated-divisor residues separate scalarized tau','test_step':'constrained fourth normal residue','target':'-189X5-378X4+9720X3-23328X2','boundary_tangential_choice':'a2=3240X','boundary_normal_choice':'b3=-189X2-1512X+7128','identity':'P-A(a2)=X2(X-6)b3','exact_residual':0,'disposition':'fourth residue is admitted; governing DPC remains unresolved','next_test':'add s2*a2 and s3*b3 to the explicit lift, compute the full residual once, then solve all remaining normal orders jointly rather than opening one DPC case per order','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_fourth_residue_lift.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
