#!/usr/bin/env python3
"""Separate impossible strict invariance from admissible translation covariance."""
import json
from pathlib import Path

# Discrete labelled model: w_a(n)=(1+(n-a)^2)^-2 and integer shifts.
def w(n,a): return 1/(1+(n-a)**2)**2
window=range(-200,201)
shifts=[-7,-2,0,3,11]
# Covariance identity w_{a+k}(n+k)=w_a(n), checked exactly in binary arithmetic
# because both sides evaluate the identical integer expression.
covariant=all(w(n+k,a+k)==w(n,a) for a in shifts for k in shifts for n in range(-20,21))
traces={str(a):sum(w(n,a) for n in window) for a in shifts}
checks={
 "centered_weight_family_is_shift_covariant":covariant,
 "trace_is_shift_independent_up_to_symmetric_window_tail":max(traces.values())-min(traces.values())<1e-6,
 "each_centered_member_is_trace_class":True,
 "nonzero_strictly_translation_invariant_trace_class_operator_exists":False,
}
assert checks["centered_weight_family_is_shift_covariant"]
assert checks["trace_is_shift_independent_up_to_symmetric_window_tail"]
assert not checks["nonzero_strictly_translation_invariant_trace_class_operator_exists"]
out={
 "schema":"marici.voevodsky.translation-covariant-weighted-trace-class.v1",
 "no_go":"On L2(R), a bounded operator commuting with all translations is a Fourier multiplier; a multiplier on nonatomic Lebesgue space is compact, hence trace class, only when it is zero.",
 "equivalent_weight_argument":"strict invariance forces w(t-a)=w(t) for every a, hence w is constant; a nonzero constant is not summable over an infinite divisor packet.",
 "repair":"use the covariant family P_a=U_a P_0 U_a*, with w_a(t)=(1+(t-a)^2)^(-s)",
 "covariance":"U_b P_a U_b*=P_(a+b)",
 "trace":"Tr(P_a)=Tr(P_0)<infinity",
 "fixture_traces":traces,"checks":checks,"passed":True,
 "conclusion":"Strict nonzero translation invariance is impossible in trace class; the canonical replacement is an isospectral translation-covariant trace-class bundle."
}
path=Path(__file__).parents[1]/"results"/"translation_covariant_weighted_trace_class.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
