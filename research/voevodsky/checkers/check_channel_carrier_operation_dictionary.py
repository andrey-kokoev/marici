# /// script
# dependencies = ["sympy"]
# ///
"""Common Fourier subdomain and obstruction to the unchanged native clock algebra."""
import json
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from source_arrow_hamiltonian import construct
NOTE='research/voevodsky/channel-carrier-operation-dictionary-v1.md'
OUT='research/voevodsky/results/channel-carrier-operation-dictionary-v1.json'

def load(p): return json.loads((ROOT/p).read_text())
def sha(p): return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok: raise ValueError(msg)
def zero(m): return S.simplify(m)==S.zeros(m.rows,m.cols)
def rows(m): return [[str(v) for v in m.row(i)] for i in range(m.rows)]

def main():
    bridge='research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json'
    b=load(bridge)
    for p,h in b['source_hashes'].items(): require(sha(p)==h,'source drift: '+p)
    src_path='research/strominger/results/source-arrow-hamiltonian-descent.json'; prior=load(src_path)
    source,C,edges=construct(tuple('ABCD'),prior['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    K=S.Matrix(b['projection_then_attachment']); F=S.zeros(4)
    for j in range(4): F[(j+1)%4,j]=1
    require(K*C==F*K and K*C**2==F**2*K and F**4==S.eye(4),'Fourier composition square')
    require(K.rank()==4,'quotient not surjective')
    z=-S.Rational(1,2)+S.I*S.sqrt(3)/2
    T=S.diag(1,z,1,S.conjugate(z))  # translate distributions by +1
    M=S.diag(z,1,S.conjugate(z),1)  # multiply by exp(2 pi i x)
    require(zero(F*T-M.inv()*F),'Fourier translation/modulation square')
    require(zero(F**2*T-T.inv()*F**2),'two-step Fourier reflection square')
    require(not zero(T*F-F*T),'missing noncommuting operation hostile')
    require(not zero(S.im(T*K)),'real carrier unexpectedly translation-closed')
    # Exhaust the candidate span of I,C,C^2,C^3 using exact linear equations.
    columns=S.Matrix.hstack(*[(K*C**j).reshape(48,1) for j in range(4)])
    target=(T*K).reshape(48,1)
    require(columns.rank()==4 and columns.row_join(target).rank()==5,'native clock algebra could lift translation')
    # Extension exists only after admitting a NEW complex operator, retained here
    # to distinguish a scoped algebra obstruction from universal impossibility.
    E=S.zeros(12,4)
    for j in range(4): E[j,j]=1
    J=K[:,:4]; section=E*J.inv(); N=S.eye(12)-section*K
    lift=S.simplify(section*T*K+N)
    require(zero(K*lift-T*K) and zero(N*lift-N),'explicit added-operator lift')
    require(not zero(lift*C-C*lift),'added operator secretly native clock polynomial')
    # Fixed mesh h=1/3: n+a=(3n+1)h, 1-a=(3n+2)h; integer character atoms use 3n.
    h=S.Rational(1,3); a=h
    for n in range(-4,5):
        require(n+a==(3*n+1)*h and n+1-a==(3*n+2)*h and n==3*n*h,'additive mesh position')
    # Heat coefficients at two same-coset atoms are unequal for every t>0.
    require((a+1)**2-a**2==S.Rational(5,3)>0,'heat escape control')
    paths=[NOTE,bridge,src_path,'research/strominger/checkers/source_arrow_hamiltonian.py',
           'research/conjecture_net/contracts/marked-channel-selection.v1.json',
           'research/voevodsky/marked-channel-selection-v1.md',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.channel-carrier-operation-dictionary.v1',passed=True,
                candidate='unchanged real carrier and complexified native clock algebra versus pointed channel translations/heat',
                Fourier_one_and_two_step_squares=True,shift='1',generic_comb_shift='1/3',mesh='1/3',
                translation=rows(T),modulation=rows(M),clock_lift_equation_rank=4,augmented_rank=5,
                unchanged_real_carrier_translation_rejected=True,unchanged_clock_algebra_translation_rejected=True,
                full_heat_leaves_four_comb_span=True,added_complex_translation_lift=rows(lift),
                added_lift_is_native=False,mark_is_supplied=True,
                transverse_charts='axis delta and constant alternate; no D-dimensional axis-comb self-Fourier claim',
                full_channel_carrier_binding_constructed=False,all_source_extensions_refuted=False,
                physical_realization_admitted=False,
                source_sha256={p:sha(p) for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','added_complex_translation_lift','translation','modulation')},indent=2))

if __name__=='__main__': main()
