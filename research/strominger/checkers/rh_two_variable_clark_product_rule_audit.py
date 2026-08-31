import json
from pathlib import Path

# Exact Gaussian-integer bivariate polynomial arithmetic; keys are powers (z,u).
def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0j) + v
    return {k: v for k, v in out.items() if v != 0}

def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v != 0}

def mul(p, q):
    out = {}
    for (i,j), x in p.items():
        for (k,l), y in q.items():
            key = (i+k,j+l)
            out[key] = out.get(key, 0j) + x*y
    return {k: v for k, v in out.items() if v != 0}

def dz(p):
    return {(i-1,j): i*v for (i,j),v in p.items() if i}

def du(p):
    return {(i,j-1): j*v for (i,j),v in p.items() if j}

prefactor = {(0,1): 1j, (1,0): -1j}  # i(u-z)

def Dz(p,a): return add(p, scale(dz(p),1j*a))
def Du(p,a): return add(p, scale(du(p),-1j*a))

def trial(A,a):
    actual = Dz(Du(mul(prefactor,A),a),a)
    clark_A = add(A,scale(dz(A),1j*a),scale(du(A),-1j*a),scale(dz(du(A)),a*a))
    induced = add(scale(A,2*a),scale(add(dz(A),scale(du(A),-1)),1j*a*a))
    naive = mul(prefactor,clark_A)
    return actual == add(naive,induced), actual != naive

trials = []
for a in (1,2,3):
    for m in range(5):
        for n in range(5):
            A = {(m,n): 1+0j, (m+1,n+2): 2-1j}
            trials.append(trial(A,a))
checks = {
    "two_variable_product_rule_exact_on_75_spanning_trials": all(x for x,_ in trials),
    "omitted_induced_kernel_detected_on_all_trials": all(y for _,y in trials),
    "constant_defect_unchanged": Dz(Du({(0,0):1},2),2) == {(0,0):1},
    "induced_kernel_zero_at_a_zero": trial({(2,3):1},0) == (True,False),
}
result = {
    "schema": "marici.strominger.rh_two_variable_clark_product_rule_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "source": "research/grothendieck/theta-green-defect-descent-to-single-seam.md",
    "identity": "D_a[i(u-z)A] = i(u-z)D_a[A] + 2a A + i a^2(partial_z A-partial_u A)",
    "interpretation": "The Clark differential necessarily adds a generally infinite-rank bulk derivative kernel. Reflection can cancel the constant line, but a one-seam positivity claim still requires a sign or domination theorem for this induced kernel.",
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
out = Path(__file__).parents[1] / "results" / "rh_two_variable_clark_product_rule_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
