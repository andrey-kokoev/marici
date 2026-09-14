#!/usr/bin/env python3
"""Conditional uniqueness of an odd primitive route readout."""
import json
from pathlib import Path
import sympy as sp

R=Path(__file__).resolve().parents[3]
a,b=sp.symbols("a b",integer=True)
S=sp.Matrix([[0,1],[1,0]])
q=sp.Matrix([[a,b]])
res=q*S+q
solution=sp.solve(list(res),(a,b),dict=True)
qplus=sp.Matrix([[1,-1]])
kernel=sp.Matrix([1,1])
odd=sp.Matrix([1,-1])
checks={
 "equivariance_solution":solution==[{a:-b}],
 "primitive_orientations_only":"gcd(a,-a)=abs(a)",
 "route_sum_kernel":qplus*kernel==sp.zeros(1,1),
 "route_difference_maps_to_two":qplus*odd==sp.Matrix([2]),
 "individual_routes_map_to_units":qplus*sp.Matrix([1,0])==sp.Matrix([1]) and qplus*sp.Matrix([0,1])==sp.Matrix([-1]),
}
assert checks["equivariance_solution"] and all(checks[k] for k in checks if k!="primitive_orientations_only")
out={
 "schema":"marici.voevodsky.conditional-route-swap-v-alg-covector.v1",
 "passed":True,
 "hypothesis":"the integral fixed-pencil site exchange swaps beta12 and beta13",
 "equivariant_covectors":"a*(1,-1)",
 "primitive_covectors":[[1,-1],[-1,1]],
 "forced_kernel":"Z*(beta12+beta13)",
 "odd_eigenvector_image":"plus or minus 2*v_alg",
 "warning":"do not divide beta12-beta13 by two without a separate ambient divisibility proof",
 "remaining":"construct the fixed-pencil swap and compute one route period as an integral unit",
 "checks":checks,
}
p=R/"research/voevodsky/results/conditional_route_swap_v_alg_covector.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"primitive_covector":"plus/minus (1,-1)","kernel":"route sum"}))
