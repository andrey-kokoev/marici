"""Exact character controls for effects and continuation-valued states.
General function-transport statements are separately checked in Agda.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_triangle_half_phase import zmul,zconj,zadd
ROOT=Path(__file__).resolve().parents[1]
ONE=(F(1),F(0));OMEGA=(F(-1,2),F(1,2))

def power(z,n):
    if n<0:return power(zconj(z),-n)
    out=ONE
    for _ in range(n):out=zmul(out,z)
    return out

def main():
    path=ROOT/'agda/ContinuationPhaseTransport.agda'
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    receipt=json.loads((ROOT/'results/agda-ContinuationPhaseTransport.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
    assert receipt['source_sha256']==digest
    tests=0
    samples=(ONE,OMEGA,zadd(ONE,OMEGA))
    for q in range(-2,3):
        for r in range(-2,3):
            effect=r-q
            future=r-effect
            assert future==q # Exact integer character identity, not modulo three.
            for x in samples:
                for k in samples:
                    # f(x)=k*x. Effect and argument act with separate weights.
                    changed_x=zmul(power(OMEGA,q),x)
                    changed_k=zmul(power(OMEGA,effect),k)
                    assert zmul(changed_k,changed_x)==zmul(power(OMEGA,r),zmul(k,x))
                    # present(x)(k)=k*x: its natural coefficient transforms like x.
                    future_x=zmul(power(OMEGA,future),x)
                    assert future_x==changed_x
                    tests+=1
    assert power(OMEGA,1)!=power(OMEGA,-1)
    # Suppressing output neutrality changes effect weight while leaving V fixed.
    # The bare function type also permits nonlinear and antilinear functions.
    # Neutral output alone does not select a charge-one LINEAR effect sector.
    function_controls=[]
    for name,fn,weight in (
        ('linear x',lambda x:x,-1),
        ('quadratic x^2',lambda x:zmul(x,x),-2),
        ('antilinear conjugate(x)',zconj,1),
        ('norm-square',lambda x:zmul(zconj(x),x),0)):
        for x in samples:
            assert fn(zmul(zconj(OMEGA),x))==zmul(power(OMEGA,weight),fn(x))
        function_controls.append(dict(function=name,neutral_answer_character=weight))
    answer_controls=[dict(state_weight=1,answer_weight=r,effect_weight=r-1,future_weight=1) for r in (0,1,2)]
    assert [row['effect_weight'] for row in answer_controls]==[-1,0,1]
    result=dict(schema='marici.nima.continuation-charge-character.v1',status='pass',
        evaluation_controls=tests,formal_source_sha256=digest,
        source_type='Effect=V -> R; Future=(V -> R) -> R',
        forced_effect_transport='f -> h composed f composed e^-1, uniquely forced by evaluation covariance at all inputs.',
        character_formula={'state':'q','answer':'r','linear_effect':'r-q','linear_double_continuation':'q'},
        answer_representation_controls=answer_controls,
        bare_function_type_controls=function_controls,
        positive_result='For a neutral answer and a linear functional sector, the opposite phase character is derived from evaluation covariance, not assigned to an execution-status tag.',
        limit='A continuation-valued present state retains its original character. A dual effect is not thereby a newly created oppositely charged particle.',
        native_scope='The retained universe already represents function types. The Agda module checks their transport and retains input provenance, but does not prove that the seed generates a selected nonzero effect or electromagnetic coupling.',
        verification='Fresh safe Cubical closure plus independent exact character controls; not extracted code or a formal construction of U(1)/complex linear algebra.')
    (ROOT/'results/continuation-charge-character.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
