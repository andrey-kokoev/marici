#!/usr/bin/env python3
"""Exact dual-rail matrix audit for the optical commutator benchmark."""
from __future__ import annotations
import cmath
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "optical-logical-commutator-benchmark.v1.json"
RESULT = ASPECT / "results" / "optical_logical_commutator_benchmark.json"

I = ((1+0j,0j),(0j,1+0j))
X = ((0j,1+0j),(1+0j,0j))
Z = ((1+0j,0j),(0j,-1+0j))

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def dagger(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))

def scale(c,a):
    return tuple(tuple(c*x for x in row) for row in a)

def close(a,b,tol=1e-12):
    return all(abs(a[i][j]-b[i][j]) < tol for i in range(2) for j in range(2))

def commutator(z,x,zinv,xinv):
    return mm(mm(mm(z,x),zinv),xinv)

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    ideal = commutator(Z,X,dagger(Z),dagger(X))
    odd_ok = close(ideal, scale(-1,I))
    even = commutator(Z,Z,dagger(Z),dagger(Z))
    even_ok = close(even,I)

    alpha, beta = 0.37, -0.61
    zt, xt = scale(cmath.exp(1j*alpha),Z), scale(cmath.exp(1j*beta),X)
    phased = commutator(zt,xt,dagger(zt),dagger(xt))
    phase_cancelled = close(phased,ideal)

    wrong_inverse = commutator(zt,xt,Z,X)
    wrong_inverse_detected = not close(wrong_inverse,ideal)
    states = ((1+0j,0j),(0j,1+0j),(2**-0.5,2**-0.5),(2**-0.5,1j*2**-0.5))
    target_records = []
    for psi in states:
        cpsi = tuple(sum(ideal[i][j]*psi[j] for j in range(2)) for i in range(2))
        overlap = sum(psi[i].conjugate()*cpsi[i] for i in range(2))
        target_records.append((overlap.real,overlap.imag,abs(overlap)))
    target_independent = all(abs(x+1)<1e-12 and abs(y)<1e-12 and abs(m-1)<1e-12 for x,y,m in target_records)
    hostiles = {
        "odd_commutator_is_minus_identity": odd_ok,
        "even_control_is_identity": even_ok,
        "primitive_rephasing_cancels_with_actual_inverses": phase_cancelled,
        "wrong_inverse_detected": wrong_inverse_detected,
        "target_state_independence": target_independent,
        "interaction_net_promotion_rejected": not contract["claim_boundary"]["instantiates_interaction_net_O_or_K"],
        "execution_not_fabricated": not contract["claim_boundary"]["physical_execution_completed"]
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.optical-logical-commutator-benchmark-result.v1",
        "passed": passed,
        "ideal_commutator": [[str(x) for x in row] for row in ideal],
        "target_records": target_records,
        "hostiles": hostiles,
        "physical_status": "not_run",
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__":
    main()
