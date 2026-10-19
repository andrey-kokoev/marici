# /// script
# dependencies = ["sympy"]
# ///
"""Separate rotation/Fourier ticks; mixed-word observer and mark regression."""
import importlib.util
import itertools
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/rotation-fourier-history-dictionary.v1.json'
NOTE='research/voevodsky/rotation-fourier-history-dictionary-v1.md'
OUT='research/voevodsky/results/rotation-fourier-history-dictionary-v1.json'
p=ROOT/'research/voevodsky/checkers/check_context_indexed_observer.py'
spec=importlib.util.spec_from_file_location('obs',p);obs=importlib.util.module_from_spec(spec);spec.loader.exec_module(obs)

def require(ok,msg):
    if not ok:raise ValueError(msg)
def apply(gs,instruction,transpose=False):
    op,axis=instruction
    if op=='R':return list(reversed(gs))
    out=list(gs)
    for i in ([axis] if op=='T' else range(2)):out[i]=obs.step(out[i],op,transpose)
    return out
def pair(gs,hs):
    ps=[obs.pairing(a,b) for a,b in zip(gs,hs)]
    return (S.simplify(S.prod(p[0] for p in ps)),S.simplify(sum(p[1] for p in ps)))
def main():
    cfg=json.loads((ROOT/DEF).read_text());require(not cfg['full_native_source_binding'],'source promotion')
    gs=[(S.Integer(2),S.Rational(1,3),S.Integer(0),S.Integer(1)),(S.Integer(1),S.I/4,S.Integer(0),S.Integer(1))]
    hs=[(S.Integer(3),S.Rational(1,5),S.Integer(0),S.Integer(1)),(S.Integer(1),S.I/3,S.Integer(0),S.Integer(1))]
    count=0
    for length in (1,2,3):
        for word in itertools.product('RFHT',repeat=length):
            forward=list(gs);mark=0;instructions=[]
            for op in word:
                instruction=(op,mark if op=='T' else None);instructions.append(instruction)
                forward=apply(forward,instruction)
                if op=='R':mark=1-mark
            back=list(hs)
            for instruction in reversed(instructions):back=apply(back,instruction,True)
            require(obs.same(pair(forward,hs),pair(gs,back)),str(word));count+=1
    for op in ('F','H'):
        require(obs.same(pair(apply(apply(gs,('R',None)),(op,None)),hs),pair(apply(apply(gs,(op,None)),('R',None)),hs)),'rotation commutation')
    # Correct R,T records axis 1 after R, not seed mark 0.
    correct=apply(apply(gs,('R',None)),('T',1))
    frozen=apply(apply(gs,('R',None)),('T',0))
    require(not obs.same(pair(correct,hs),pair(frozen,hs)),'frozen mark invisible')
    require(not obs.same(pair(apply(gs,('R',None)),hs),pair(apply(gs,('F',None)),hs)),'rotation/Fourier conflation invisible')
    # Independent atom fixture: R delta_(h,0)=delta_(0,h);
    # F delta_(h,0) is a character, integrated against Gaussian tests.
    h=S.Rational(1,3)
    rotation_value=S.exp(-2*S.pi*h*h)
    fourier_value=S.exp(-S.pi*h*h)/S.sqrt(2)
    require(S.simplify(rotation_value-fourier_value)!=0,'seed conflation hostile')
    paths=[DEF,NOTE,'research/conjecture_net/contracts/shared-quadrilateral-geometric-seed.v1.json',
           'research/voevodsky/results/shared-quadrilateral-geometric-seed-v1.json',
           'research/voevodsky/checkers/check_context_indexed_observer.py',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.rotation-fourier-history-validation.v1',passed=True,exact_mixed_word_checks=count,
                rotation_Fourier_commutation=True,rotation_is_Fourier=False,
                corruptions_rejected=['frozen-mark-translation','rotation-as-Fourier'],
                atom_rotation_query=str(rotation_value),atom_Fourier_query=str(fourier_value),
                classification='native rotation plus explicitly added analytic/channel history generators',
                full_native_source_binding=False,common_source_node_closed=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
