"""Exact counterexample to full-domain coverage by the fixed count attachment."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/strominger/contracts/route-count-elastic-coverage-probe.v1.json'


def main():
    frozen=(ROOT/CONTRACT).read_bytes()
    a,b,g=s.symbols('a b gain',positive=True,real=True)
    M=a*a+b*b
    plus=s.Matrix([1,1])/s.sqrt(2)
    minus=s.Matrix([1,-1])/s.sqrt(2)
    O=s.Matrix([a,b])/s.sqrt(M)*plus.T+s.Matrix([b,-a])/s.sqrt(M)*minus.T
    B=s.diag(a,b)*O
    simp=lambda x:x.applyfunc(s.simplify)
    assert s.simplify(B.det())==a*b
    p=simp(B*g*s.Matrix([1,-1]))
    assert simp(p-s.sqrt(2/M)*a*b*g*s.Matrix([1,-1]))==s.zeros(2,1)
    assert s.simplify(sum(p))==0
    kinetic=s.simplify((p.T*s.diag(1/a**2,1/b**2)*p)[0]/2)
    assert kinetic==g*g
    preimage=simp(B.inv()*p/g)
    assert preimage==s.Matrix([1,-1])
    # Codomain Nat x Nat supplies the impossibility, not a bounded search.
    assert preimage[1].is_negative is True
    # Original successful source observer fixture remains represented and swaps.
    C=s.Matrix([[a*a-b*b,2*a*a],[2*b*b,b*b-a*a]])/M
    assert simp(C*B*g*s.Matrix([1,2])-B*g*s.Matrix([2,1]))==s.zeros(2,1)
    assert (ROOT/CONTRACT).read_bytes()==frozen
    paths=[CONTRACT,'research/nima/agda/NativeFeedbackRouteReadout.agda',
           'research/nima/exchange-to-mechanical-recoil.md',
           'research/strominger/native-feedback-elastic-binding-v1.md',
           str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','claim':'route-count-elastic-full-domain-coverage',
            'outcome_semantics':'proof-attempt-outcomes-v1','intent':'reject','outcome':'-+',
            'counterexample':[str(x) for x in p], 'unique_required_counts':[1,-1],
            'total_momentum':'0','kinetic_energy':str(kinetic),
            'unit_mass_unit_gain_counterexample':[1,-1],
            'previous_intertwining_control_preserved':True,
            'proof_kind':'written range obstruction plus exact symbolic inverse and admissibility checks',
            'kernel_verified_analytic_theorem':False,
            'scope':'Fixed count attachment is not onto the full real momentum plane; its action binding survives. No general WG nonexistence theorem.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/route-count-elastic-coverage/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
