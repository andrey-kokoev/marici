#!/usr/bin/env python3
"""Exact support-growth audit for prime-circle primitive circuits."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_primitive_circuit_support_growth_audit.json"

def primes_upto(n):
    out=[]
    for p in range(2,n+1):
        if all(p%d for d in range(2,int(p**0.5)+1)): out.append(p)
    return out

def prime_power_label(n):
    for p in primes_upto(n):
        x=p; k=1
        while x<n:
            x*=p; k+=1
        if x==n: return p,k
    return None

def support(r):
    return tuple((n,prime_power_label(n)) for n in range(2,r+1) if prime_power_label(n) is not None)

rows=[]
for r in range(2,65):
    old=support(r-1); new=support(r)
    delta=len(new)-len(old)
    label=prime_power_label(r)
    rows.append({"r":r,"prime_power":label is not None,"label":list(label) if label else None,"support_size":len(new),"delta":delta})

nonpowers=[r["r"] for r in rows if not r["prime_power"]]
powers=[r["r"] for r in rows if r["prime_power"]]
# Boundary-topology audit established one new top jet at each integer grade.
# Compare that law with source-native von Mangoldt support growth.
checks={
 "support_grows_exactly_at_prime_powers":all((r["delta"]==1)==r["prime_power"] for r in rows),
 "each_growth_step_has_unique_p_k_label":all(r["label"] is not None and r["delta"]==1 for r in rows if r["prime_power"]),
 "non_prime_power_composites_add_no_primitive_circuit":all(r["delta"]==0 for r in rows if not r["prime_power"]),
 "primitive_support_growth_is_not_one_per_grade":len(nonpowers)>0,
 "square_returns_are_retained_as_k_even_not_new_primes":all(prime_power_label(p*p)==(p,2) for p in primes_upto(8)),
 "support_prefix_is_nested":all(set(support(r-1)).issubset(set(support(r))) for r in range(3,65)),
}
payload={
 "schema":"marici.strominger.rh_primitive_circuit_support_growth_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "range":[2,64],"prime_power_thresholds":powers,"no_growth_thresholds":nonpowers,
 "selected_rows":[r for r in rows if r["r"] in [4,6,8,9,10,16,25,27,32,49,64]],
 "verdict":"The minimal source-native support theorem is exact: the primitive-circuit support increases by one precisely when r is a prime power p^k, with unique label (p,k), and is unchanged at every other threshold. This falsifies the stronger route in which primitive support growth explains the boundary audit's new jet at every integer grade. Any comparison needs an additional source map from dense boundary grades to sparse prime-power support; dimensions or threshold order alone cannot supply it.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
