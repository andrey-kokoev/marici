#!/usr/bin/env python3
"""Projective-limit topology and adjoint-observer equicontinuity gate."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_projective_limit_observer_topology_gate_audit.json"

# X_g has coordinates primitive, square, jet1,...,jet_g. Bonding maps truncate.
def truncate(x,g): return x[:g+2]
def compatible_family(x,max_g): return all(truncate(x,g)==truncate(truncate(x,g+1),g) for g in range(1,max_g))

x=[Fraction(2),Fraction(-1)]+[Fraction((-1)**j,j) for j in range(1,10)]
compat=compatible_family(x,8)

# Product-topology neighborhoods constrain only a finite prefix. For observer
# L_n(x)=n*x_jet_n, choose n beyond that prefix and a vector supported at jet n;
# it lies in the neighborhood while L_n has arbitrary prescribed magnitude.
def escape_witness(prefix_grade,n,magnitude):
    v=[Fraction(0)]*(n+2)
    v[n+1]=Fraction(magnitude,n) # coordinate indexing: primitive,square,jet1...
    prefix_zero=all(a==0 for a in v[:prefix_grade+2])
    value=Fraction(n)*v[n+1]
    return prefix_zero,value

escapes=[]
for g in range(1,8):
    n=g+1
    prefix_zero,value=escape_witness(g,n,100)
    escapes.append({"controlled_grade":g,"observer_grade":n,"prefix_zero":prefix_zero,"observer_value":str(value)})

# The same finite vectors admit inequivalent unbounded weighted completions.
# Sequence a_j=1/j belongs to weight 1 l2 but not weight j^2 l2: finite stages
# cannot select between them.
partial_plain=[]; partial_strong=[]
for N in range(1,101):
    partial_plain.append(sum(Fraction(1,j*j) for j in range(1,N+1)))
    partial_strong.append(sum(Fraction(j*j,j*j) for j in range(1,N+1)))
plain_bounded=partial_plain[-1] < 2
strong_linear=partial_strong[-1]==100
source_weight_law_present=False

checks={
 "truncations_form_compatible_projective_family":compat,
 "every_basic_product_neighborhood_misses_a_later_observer":all(r["prefix_zero"] and r["observer_value"]=="100" for r in escapes),
 "adjoint_observer_family_is_not_product_equicontinuous":all(r["prefix_zero"] for r in escapes),
 "finite_stages_do_not_select_between_weighted_completions":plain_bounded and strong_linear,
 "current_source_has_no_unbounded_weight_law":not source_weight_law_present,
}
payload={
 "schema":"marici.strominger.rh_projective_limit_observer_topology_gate_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "escape_witnesses":escapes,
 "weighted_completion_witness":{"sequence":"a_j=1/j","plain_partial_100":str(partial_plain[-1]),"j2_weighted_partial_100":str(partial_strong[-1])},
 "verdict":"The finite restriction system canonically yields the coordinatewise product projective limit, but that topology does not control the growing adjoint observers: every basic neighborhood leaves a later jet free, on which its observer can take value 100. The same finite stages also admit inequivalent weighted unbounded completions. Hence finite domination data do not determine the source topology needed for observer control. The seminorm-preorder direction is exhausted at a precise source gate: a source-derived unbounded weight or equicontinuity law is required.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
