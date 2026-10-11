"""Exact constraint dynamics, reversible records and coordinate-invariant energy.

Uses the actual proton coefficient store and the belt's weighted intrinsic
coordinates. The Hamiltonian is a declared common constraint rule; no physical
mass, rate, or target splitting is used to choose coefficients.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from check_reversed_coefficient_attachment import SOURCE, verify, weight
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale
from check_belt_three_by_twelve import decode

BASE = Path(__file__).resolve().parents[1]


def clean(a):
    return {k:v for k,v in a.items() if v != Z}


def plus(*terms):
    out = {}
    for a in terms:
        for k,v in a.items():
            out[k] = add(out.get(k,Z),v)
    return clean(out)


def times(q,a):
    return clean({k:scale(q,v) for k,v in a.items()})


def compose(a,b):
    rows = {}
    for (k,j),v in b.items():
        rows.setdefault(k,[]).append((j,v))
    out = {}
    for (i,k),u in a.items():
        for j,v in rows.get(k,[]):
            out[i,j] = add(out.get((i,j),Z),mul(u,v))
    return clean(out)


def identity(n):
    return {(i,i):ONE for i in range(n)}


def adjoint(a,metric):
    # Inner product x* D^-1 y. Intrinsic numerator coordinates have D=diag(d).
    return {(j,i):scale(metric[j]/metric[i],conj(v)) for (i,j),v in a.items()}


def trace(a,n):
    value = Z
    for i in range(n):
        value = add(value,a.get((i,i),Z))
    assert value[1] == 0 and value[0].b == 0
    return value[0].a


def polynomial_product(a,b):
    # Exact universal algebra of two commuting idempotents, checked below
    # against the concrete coefficient stores before this algebra is applied.
    out = {}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            key = (max(i,k),max(j,l))
            out[key] = out.get(key,F(0))+u*v
    return {k:v for k,v in out.items() if v}


def main():
    p_raw = SOURCE.read_bytes()
    packet = json.loads(p_raw)
    certified,rows = verify(packet)
    assert certified['verified']
    ports = sorted({tuple(row['source'][1:]) for row in rows})
    ix = {p:i for i,p in enumerate(ports)}
    proton = {s:{} for s in ('L','G','N')}
    stages = {'raw':'L','local':'G','aligned':'N'}
    for row in rows:
        value = weight(row)
        proton[stages[row['source'][0]]][ix[tuple(row['target'][1:])],ix[tuple(row['source'][1:])]] = (R(value[0]),R(value[1]))
    path = BASE/'results/belt_three_by_twelve_store.json'
    b_raw = path.read_bytes()
    belt_store = json.loads(b_raw)
    d = tuple(F(c['d']) for c in belt_store['coordinates'])
    belt = {s:{} for s in ('L','G','N')}
    for row in belt_store['arrows']:
        # Similarity to physical orthonormal coordinates removes square roots:
        # physical entry=num/sqrt(d_i*d_j), numerator-coordinate entry=num/d_j.
        belt[row['stage']][row['target'],row['source']] = scale(1/d[row['source']],decode(row['numerator']))
    I = identity(36)
    spectral = {}
    matrices = {}
    for name,operators,metric in [('proton',proton,(F(1),)*36),('belt',belt,d)]:
        L,G,N = (operators[s] for s in ('L','G','N'))
        assert all(adjoint(a,metric)==a for a in (L,G,N))
        assert compose(L,L)==L and compose(G,G)==G
        assert compose(L,G)==compose(G,L)==N
        assert compose(N,N)==N
        joint = {'both':N,'selection_only':plus(L,times(-1,N)),
                 'alignment_only':plus(G,times(-1,N)),
                 'neither':plus(I,times(-1,L),times(-1,G),N)}
        assert plus(*joint.values()) == I
        ranks = {k:int(trace(a,36)) for k,a in joint.items()}
        assert ranks == ({'both':1,'selection_only':11,'alignment_only':2,'neither':22} if name=='proton'
                         else {'both':1,'selection_only':2,'alignment_only':11,'neither':22})
        # Independent rational tests of a(I-L)+b(I-G) in the joint decomposition.
        trials = []
        for a,b in [(F(2),F(3)),(F(3),F(2)),(F(1),F(1))]:
            H = plus(times(a+b,I),times(-a,L),times(-b,G))
            resolved = plus(times(b,joint['selection_only']),times(a,joint['alignment_only']),times(a+b,joint['neither']))
            assert H == resolved
            assert compose(H,N) == {}
            trials.append({'selection_penalty':str(a),'alignment_penalty':str(b),'trace':str(trace(H,36)),'ground_energy':'0','ground_rank':1})
        spectral[name] = {'multiplicities':ranks,'energies':{'both':'0','selection_only':'b','alignment_only':'a','neither':'a+b'},'trials':trials}
        matrices[name] = (joint,plus(times(5,I),times(-2,L),times(-3,G)))
    # Certificate for the four syndrome blocks and a reversible XOR record:
    # P_ij P_kl = delta_ik delta_jl P_ij. This establishes U^2=I and [U,H]=0
    # for U=sum P_ij tensor X^i tensor X^j, with degenerate record energies.
    polynomials = [{(1,1):F(1)}, {(1,0):F(1),(1,1):F(-1)},
                   {(0,1):F(1),(1,1):F(-1)},
                   {(0,0):F(1),(1,0):F(-1),(0,1):F(-1),(1,1):F(1)}]
    for i,j in product(range(4),repeat=2):
        assert polynomial_product(polynomials[i],polynomials[j]) == (polynomials[i] if i==j else {})
    h = {(0,0):F(5),(1,0):F(-2),(0,1):F(-3)}
    for p in polynomials:
        assert polynomial_product(h,p) == polynomial_product(p,h)

    # Actual 36 -> 54 plane embedding and its metric adjoint/decoder.
    W,D = {},{}
    for e in belt_store['embedding_entries']:
        a,i = e['ambient_target'],e['intrinsic_source']
        v = (R(*map(F,e['numerator'])),R())
        W[a,i] = scale(1/d[i],v)
        D[i,a] = v
    assert compose(D,W)==I
    Q = compose(W,D)
    assert adjoint(Q,(F(1),)*54)==Q and trace(Q,54)==36
    assert compose(Q,Q)==Q
    H = matrices['belt'][1]
    transported = compose(compose(W,H),D)
    assert adjoint(transported,(F(1),)*54)==transported
    assert compose(compose(D,transported),W)==H
    assert compose(transported,W)==compose(W,H)
    normal = plus(identity(54),times(-1,Q))
    assert trace(normal,54)==18 and compose(normal,W)=={}
    # Distinct arbitrary normal penalties never change any intrinsic energy.
    for kappa in (F(1),F(7)):
        ambient = plus(transported,times(kappa,normal))
        assert compose(compose(D,ambient),W)==H
    # Full return matches the earlier ambient carrier; its local protocol does
    # NOT equal the transported sector-local protocol.
    old_path = BASE/'results/coupled_six_piece_belt_store.json'
    old_raw = old_path.read_bytes()
    old = json.loads(old_raw)['record']
    ambient_ops = {s:{} for s in ('L','G','N')}
    for row in old['arrows']:
        i = 3*row['target'][1]+'xyz'.index(row['target'][2])
        j = 3*row['source'][1]+'xyz'.index(row['source'][2])
        ambient_ops[row['stage']][i,j] = decode(row['coefficient'])
    assert compose(compose(W,belt['N']),D)==ambient_ops['N']
    carried_L = compose(compose(W,belt['L']),D)
    assert trace(carried_L,54)==3 and trace(ambient_ops['L'],54)==18
    assert carried_L != ambient_ops['L']
    # Generic reversible re-encoding/redecoding adds no intrinsic dynamics.
    permutation = {(i,(i+1)%36):ONE for i in range(36)}
    inverse = adjoint(permutation,(F(1),)*36)
    assert compose(inverse,permutation)==I
    Hp = matrices['proton'][1]
    recoded = compose(compose(permutation,Hp),inverse)
    assert compose(compose(inverse,recoded),permutation)==Hp
    result = {
        'verification_passed':True,
        'hamiltonian':'H=a(I-L)+b(I-G), a,b>0; candidate constraint energy, not assumed rest energy',
        'spectrum':spectral,
        'ground_return':'unique common zero-energy subspace im(N)',
        'imaginary_time_limit':'exp(-t H) -> N; normalized relaxation is not automatically deterministic physical preparation',
        'reversible_record':{'syndrome_bits':2,'raw_zero_syndrome_effect':'N','unitary_square':'I','commutes_with_H':True,'record_energy_assumption':'degenerate records; preparation/control/erasure not assigned zero cost'},
        'coordinate_transport':{'intrinsic_dimension':36,'ambient_dimension':54,'image_rank':36,'normal_dimension':18,'energy_intertwining':True,'normal_penalties_checked':['1','7']},
        'old_ambient_local_rank':18,'transported_intrinsic_local_rank':3,
        'old_ambient_protocol_is_only_a_coordinate_change':False,
        'reversible_encoding_added_support':72,'reversible_encoding_energy_change':'0',
        'constraint_ground_energy_splitting':'0',
        'constraint_trace_difference':'9*(a-b)',
        'rest_energy_offset_selected':False,
        'next_gate':'Derive a physical retained-record Hamiltonian and its sector offset, or couple a specified reservoir to the syndrome dynamics. Recording alone does not set Delta_L or Delta_G.',
        'source_sha256':{'proton':sha256(p_raw).hexdigest(),'intrinsic_belt':sha256(b_raw).hexdigest(),'ambient_belt':sha256(old_raw).hexdigest()}
    }
    out = BASE/'results/constraint_energy_accounting.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
