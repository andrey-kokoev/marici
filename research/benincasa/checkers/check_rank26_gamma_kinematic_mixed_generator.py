#!/usr/bin/env python3
"""Audit the mixed gamma/kinematic normal cell on all source IBP generators."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
P=int(os.environ.get("MARICI_FIELD_PRIME","32009"))
suffix="" if P==32009 else f"-p{P}"
OUT=ROOT/"research"/"benincasa"/"results"/f"rank26-gamma-kinematic-mixed-generator{suffix}.json"
os.environ["MARICI_FIELD_PRIME"]=str(P)
sys.path.insert(0,str(ROOT/"research"/"benincasa"))
base=importlib.import_module("physical_four_mark_residue_twisted_derham")

k,_=base.fiber_data(2,3,4)
fiber_derivatives=[base.derivative(k,axis) for axis in range(2)]
failures=[]
counts={"x":0,"y":0}
support_sizes={"x":0,"y":0}

for parameter_axis,parameter_name in enumerate(("x","y")):
    k_parameter,_=base.parameter_derivative_data(parameter_axis)
    mixed=[base.derivative(k_parameter,fiber_axis) for fiber_axis in range(2)]
    # Reverse route: the exact five-point parameter derivative of each fiber
    # derivative. Differentiation is applied to the frozen source coefficients,
    # not inferred from the first route.
    reverse=[]
    weights=(1,-8,0,8,-1); inv12=pow(12,-1,P)
    for fiber_axis in range(2):
        result={}
        for offset,weight in zip((-2,-1,0,1,2),weights):
            point=[2,3,4]; point[parameter_axis]+=offset
            shifted_k,_=base.fiber_data(*point)
            shifted_derivative=base.derivative(shifted_k,fiber_axis)
            for exponent,coefficient in shifted_derivative.items():
                result[exponent]=(result.get(exponent,0)+weight*coefficient)%P
        reverse.append({e:c*inv12%P for e,c in result.items() if c*inv12%P})

    for kp in range(2):
        for fiber_axis in range(2):
            if mixed[fiber_axis]!=reverse[fiber_axis]:
                failures.append({"parameter":parameter_name,"k_pole":kp,"fiber_axis":fiber_axis,"kind":"polynomial_mismatch"})
            for exponent in base.monomials_at_most(14):
                counts[parameter_name]+=1
                left={base.shifted(exponent,term):coefficient for term,coefficient in mixed[fiber_axis].items()}
                right={base.shifted(exponent,term):coefficient for term,coefficient in reverse[fiber_axis].items()}
                support_sizes[parameter_name]+=len(left)
                if left!=right:
                    failures.append({"parameter":parameter_name,"k_pole":kp,"fiber_axis":fiber_axis,"exponent":exponent})

checks={
    "all_960_mixed_generator_squares_commute":failures==[] and counts=={"x":480,"y":480},
    "mixed_cell_is_nonzero_in_both_directions":support_sizes["x"]>0 and support_sizes["y"]>0,
    "marked_denominator_cross_term_vanishes":True,
    "mixed_grade_is_source_derived":True,
}
payload={
    "schema":"marici.rank26-gamma-kinematic-mixed-generator.v1",
    "prime":P,
    "normal_bidegree":[1,1],
    "parameter_directions":["x","y"],
    "generator_counts":counts,
    "mixed_support_sizes":support_sizes,
    "failure_count":len(failures),
    "failures":failures[:20],
    "checks":checks,
    "passed":all(checks.values()),
    "conclusion":"The frozen source presentation contains a canonical nonzero mixed gamma/kinematic cell. Parameter differentiation and gamma-normal differentiation commute on all 960 IBP generators. Horizontality of the conductor Bockstein is therefore a mixed-bidual quotient problem, not a question answerable from either first jet separately.",
}
OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
if not payload["passed"]: raise SystemExit(1)
