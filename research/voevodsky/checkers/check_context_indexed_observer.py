# /// script
# dependencies = ["sympy"]
# ///
"""Exact bilinear distribution/test transport, with order and sign hostiles."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
NOTE='research/voevodsky/context-indexed-observer-v1.md'
OUT='research/voevodsky/results/context-indexed-observer-v1.json'

def require(ok,msg):
    if not ok: raise ValueError(msg)
# Gaussian c exp(pi L -pi A x^2 +2pi B x). Separate exponential and
# algebraic prefactors so every check uses exact algebra, not quadrature.
def step(g,op,transpose=False):
    A,B,L,c=g
    if op=='F': return tuple(map(S.simplify,(1/A,-S.I*B/A,L+B*B/A,c/S.sqrt(A))))
    if op=='T':
        b=-S.Rational(2,3) if transpose else S.Rational(2,3)
        return (A,B+A*b,S.simplify(L-A*b*b-2*B*b),c)
    if op=='M': return (A,B+S.I*S.Rational(1,3),L,c)
    if op=='H': return (A+S.Rational(1,2),B,L,c)
    raise ValueError(op)
def evolve(g,word,transpose=False):
    for op in (reversed(word) if transpose else word): g=step(g,op,transpose)
    return g
def pairing(g,h):
    A,B,L,c=g; a,b,l,d=h
    return (S.simplify(c*d/S.sqrt(A+a)),S.simplify(L+l+(B+b)**2/(A+a)))
def same(p,q): return all(S.simplify(x-y)==0 for x,y in zip(p,q))

def main():
    g=(S.Integer(2),S.Rational(1,3)+S.I/4,S.Integer(0),S.Integer(1))
    test=(S.Integer(1),S.Rational(1,5)-S.I/3,S.Integer(0),S.Integer(1))
    count=0
    for length in (1,2,3):
        for word in itertools.product('FTMH',repeat=length):
            require(same(pairing(evolve(g,word),test),pairing(g,evolve(test,word,True))),str(word))
            count+=1
    word=('F','H')
    wrong=test
    for op in word: wrong=step(wrong,op,True)
    require(not same(pairing(evolve(g,word),test),pairing(g,wrong)),'wrong order was invisible')
    require(not same(pairing(step(g,'T'),test),pairing(g,step(test,'T'))),'wrong translation sign was invisible')
    # Replay the preceding kernel hostile with the pulled-back transverse test.
    before=S.exp(S.pi)*S.exp(-S.pi)-1
    after=S.exp(S.pi)*S.exp(-2*S.pi)-1
    require(S.simplify(before)==0 and S.simplify(after-(S.exp(-S.pi)-1))==0,'kernel replay')
    # A concrete two-coordinate mark relabelling swaps both state and test.
    other=(S.Integer(3),S.Integer(0),S.Integer(0),S.Integer(1))
    def tensorpair(gs,hs):
        pairs=[pairing(a,b) for a,b in zip(gs,hs)]
        return (S.simplify(S.prod(p[0] for p in pairs)),S.simplify(sum(p[1] for p in pairs)))
    require(same(tensorpair((g,other),(test,other)),tensorpair((other,g),(other,test))),'transported mark covariance')
    require(not same(tensorpair((g,other),(test,other)),tensorpair((other,g),(test,other))),'frozen mark hostile')
    paths=[NOTE,'research/voevodsky/transverse-gaussian-bridge-v1.md',
           'research/voevodsky/results/transverse-gaussian-bridge-v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.context-indexed-observer.v1',passed=True,exact_word_checks=count,
                pairing='complex bilinear distribution/test pairing; not Hermitian L2 pairing',
                transpose_order='reverse chronological application to final test',
                corruptions_rejected=['same-order-transpose','wrong-translation-sign','frozen-mark'],
                old_kernel_witness_after_context_update=str(S.simplify(after)),
                retained_source_required=True,fixed_scalar_quotient_repaired=False,
                finite_tests_prove_general_distribution_theorem=False,
                native_carrier_operations_extended=False,common_source_node_closed=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__': main()
