"""Repaired conditional Gram-norm calculation; not a derivation of the Born rule.
uv run --with sympy python research/nima/checkers/check_gram_selection_principle.py
Original bytes: quarantine/20261007-quantum-readout-evidence/checkers/.
"""
import json
from itertools import combinations
from pathlib import Path
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
CODES = [(False,False),(False,True),(True,False),(True,True)]


def code(pt):
    return (1 if pt[0] else 0)*2+(1 if pt[1] else 0)


def image_vec(f):
    return [code(f(pt)) for pt in CODES]


def dot(u,v):
    return sum(a*b for a,b in zip(u,v))


def norm2(v):
    return dot(v,v)


def identity(pt): return pt

def swap(pt): return (pt[1],pt[0])

def twist(pt): return (pt[0],not pt[1]) if pt[0] else pt

def flip_fst(pt): return (not pt[0],pt[1])

def flip_both(pt): return (not pt[0],not pt[1])

FILLERS = {'id':identity,'swap':swap,'twist':twist,'flip_fst':flip_fst,'flip_both':flip_both}


def gram_data():
    vecs = [image_vec(f) for f in FILLERS.values()]
    V = s.Matrix.hstack(*(s.Matrix(v)/s.sqrt(norm2(v)) for v in vecs))
    return vecs,V,V.H*V  # G_ij = v_i^dagger v_j, also for complex controls.


def N_slit_intensity(G,phases):
    q = s.Matrix([s.exp(s.I*p) for p in phases])
    return s.simplify((q.H*s.Matrix(G)*q)[0])


def require_equal(actual,expected,label):
    if s.simplify(actual-expected) != 0:
        raise AssertionError(label)


def balanced_packet(V,phases):
    """Supplied coherent preparation and balanced erasure, not native apparatus.

Path labels remain orthogonal until projection. P and I-P are a complete
binary path measurement; the selected port returns a record vector.
"""
    d,n = V.shape
    W = s.zeros(d*n,n)
    for j in range(n):
        W[j*d:(j+1)*d,j] = V[:,j]
    if W.H*W != s.eye(n):
        raise ValueError('Each record column must have unit norm')
    if len(phases) != n:
        raise ValueError('One phase per retained path is required')
    a = s.Matrix([s.exp(s.I*p) for p in phases])/s.sqrt(n)
    if s.simplify((a.H*a)[0]-1) != 0:
        raise ValueError('Equal-path preparation requires unit-modulus phase factors')
    K = s.kronecker_product(s.ones(1,n)/s.sqrt(n),s.eye(d))
    psi = W*a
    output = s.simplify(K*psi)
    probability = s.simplify((output.H*output)[0])
    return {'isometry':W,'input':psi,'port':K,'record_vector':output,
            'click_probability':probability,
            'record_density':None if probability == 0 else s.simplify(output*output.H/probability)}


def verify():
    vecs,V,G = gram_data()
    assert len(vecs) == 5 and V.shape == (4,5) and V.rank() == G.rank() == 4
    # All 31 principal minors, not a numerical eigensolver tolerance.
    assert all(G.extract(ix,ix).det() >= 0 for k in range(1,6) for ix in combinations(range(5),k))
    pairs = {}
    for i,j in combinations(range(5),2):
        G2 = G.extract([i,j],[i,j]); gamma = G2[0,1]
        values = []
        for phase,expected in [(0,2+2*gamma),(s.pi,2-2*gamma),(s.pi/2,2)]:
            intensity = N_slit_intensity(G2,[0,phase])
            require_equal(intensity,expected,'raw two-path norm')
            packet = balanced_packet(V[:,[i,j]],[0,phase])
            require_equal(packet['click_probability'],intensity/4,'two-path click normalization')
            assert 0 <= packet['click_probability'] <= 1
            values.append(str(intensity))
        pairs[f'{i},{j}'] = {'gamma':str(gamma),'raw_norms_at_0_pi_halfpi':values}
    packet = balanced_packet(V,[0]*5)
    require_equal(packet['click_probability'],N_slit_intensity(G,[0]*5)/25,'five-path click normalization')
    # Complex convention control: the correct synthesis is 1+i*i=0.
    CV = s.Matrix([[1,s.I]])
    require_equal(N_slit_intensity(CV.H*CV,[0,s.pi/2]),0,'complex Gram variance')
    rejected = False
    try:
        require_equal(N_slit_intensity(G.extract([0,1],[0,1]),[0,0]),1+G[0,1],'old unchecked expectation')
    except AssertionError:
        rejected = True
    assert rejected
    return {'schema':'marici.nima.gram-selection-repaired.v1','status':'pass',
            'classification':'conditional coherent norm with explicit preparation/effect normalization',
            'rank':G.rank(),'pairs':pairs,'five_path_raw_norm':str(N_slit_intensity(G,[0]*5)),
            'five_path_click_probability':str(packet['click_probability']),
            'old_expectation_rejected':rejected,
            'given_not_derived':['integer encoding and Hermitian metric','complex coherent preparation',
                                 'trace/Born pairing and balanced path effect'],
            'physical_record_map':'not established by this calculation',
            'superseding_packet':'gram-interference-and-bell-readout-comparison.md'}


def main():
    out = OWNER/'results/gram-selection-principle-repaired.json'
    out.unlink(missing_ok=True)
    result = verify()
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
