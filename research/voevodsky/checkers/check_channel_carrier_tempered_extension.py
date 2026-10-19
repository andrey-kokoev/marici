# /// script
# dependencies = ["sympy"]
# ///
"""Exact native/archive and Gaussian-word tests for a declared additive rigging."""
import json
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from source_arrow_hamiltonian import construct
NOTE='research/voevodsky/channel-carrier-tempered-extension-v1.md'
OUT='research/voevodsky/results/channel-carrier-tempered-extension-v1.json'

def load(p): return json.loads((ROOT/p).read_text())
def require(ok,msg):
    if not ok: raise ValueError(msg)
def clean(g): return tuple(S.simplify(x) for x in g)
# g(x)=c exp(-pi A x^2+2pi B x); A>0, B complex.
def F(g):
    A,B,c=g
    return clean((1/A,-S.I*B/A,c/S.sqrt(A)*S.exp(S.pi*B**2/A)))
def T(g,b):
    A,B,c=g
    return clean((A,B+A*b,c*S.exp(-S.pi*A*b*b-2*S.pi*B*b)))
def M(g,b):
    A,B,c=g
    return clean((A,B+S.I*b,c))
def H(g,t,d=0):
    require(t>=0,'negative heat outside global multiplier domain')
    A,B,c=g
    return clean((A+t,B+t*d,c*S.exp(-S.pi*t*d*d)))
def equal(g,h): return all(S.simplify(a-b)==0 for a,b in zip(g,h))

def main():
    checks=0
    for A in (S.Rational(1),S.Rational(2)):
        for B in (S.Rational(0),S.Rational(1,3)+S.I/2):
            g=(A,B,S.Rational(1)); b=S.Rational(2,3); t=S.Rational(1,2); d=S.Rational(1,4)
            require(equal(F(T(g,b)),M(F(g),-b)),'Fourier/translation')
            require(equal(F(M(g,b)),T(F(g),b)),'Fourier/modulation')
            require(equal(F(F(g)),(A,-B,g[2])),'Fourier reflection')
            require(equal(T(H(g,t,d),b),H(T(g,b),t,d+b)),'translated heat center')
            require(equal(H(H(g,t,d),t,d),H(g,2*t,d)),'heat composition')
            require(equal(F(T(H(g,t),b)),M(F(H(g,t)),-b)),'nontrivial ordered word')
            checks+=6
    g=(S.Rational(1),S.Rational(0),S.Rational(1))
    require(not equal(T(H(g,S.Rational(1)),1),H(T(g,1),S.Rational(1))),'heat/translation hostile')
    try: H(g,S.Rational(-1))
    except ValueError: pass
    else: raise AssertionError('negative heat admitted')
    bp='research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json'
    sp='research/strominger/results/source-arrow-hamiltonian-descent.json'
    bridge=load(bp); prior=load(sp)
    for p,h in bridge['source_hashes'].items():
        require(sha256(Path(p).read_bytes()).hexdigest()==h,'upstream source drift')
    source,C,edges=construct(tuple('ABCD'),prior['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    K=S.Matrix(bridge['projection_then_attachment']); E=S.zeros(12,4)
    for i in range(4): E[i,i]=1
    section=E*K[:,:4].inv(); N=S.eye(12)-section*K; cyc=S.zeros(4)
    for i in range(4): cyc[(i+1)%4,i]=1
    require(K*C==cyc*K and N*C==C*N and K*N==S.zeros(4,12),'native/archive square')
    require(section*K+N==S.eye(12) and C**4==S.eye(12),'reconstruction/cycle')
    paths=[NOTE,bp,sp,'research/strominger/checkers/source_arrow_hamiltonian.py',
           'research/voevodsky/results/channel-carrier-operation-dictionary-v1.json',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.channel-carrier-tempered-extension.v1',passed=True,
                exact_Gaussian_word_checks=checks,native_archive_square=True,
                heat_translation_noncommutativity_retained=True,negative_heat_rejected=True,
                analytic_domain_argument='written Schwartz multiplier/dual continuity argument; not inferred from samples',
                source_extension_declared=True,full_multichannel_binding=False,
                additional_generators_natively_derived=False,physical_realization_admitted=False,
                raw_radial_combs_ordinary_log_tempered=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__': main()
