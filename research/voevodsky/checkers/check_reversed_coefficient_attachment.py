"""Test two declared reversals of the actual retained L/G/N protocol.

Transpose is linear dualization; adjoint additionally uses the standard
Hermitian coordinate pairing. Neither is inferred from flag reversal alone.
No host-side fold construction is used.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json
from itertools import permutations

from check_proton_merkle_reassembly import verify, weight, plus, times, ZERO, ONE, POINTS

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / 'results/proton_merkle_store.json'

def neg(a): return (-a[0], -a[1])
def sub(a,b): return plus(a,neg(b))
def conj(a): return (a[0],-a[1])
def div(a,b):
    d = b[0]*b[0]+3*b[1]*b[1]
    if not d: raise ZeroDivisionError
    x = times(a,conj(b))
    return (x[0]/d,x[1]/d)
def transpose(a): return [list(row) for row in zip(*a)]
def adjoint(a): return [[conj(x) for x in row] for row in transpose(a)]
def identity(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def multiply(a,b):
    out = [[ZERO for _ in b[0]] for _ in a]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x == ZERO: continue
            for j,y in enumerate(b[k]):
                if y != ZERO: out[i][j] = plus(out[i][j],times(x,y))
    return out

def rank(a):
    a = [row[:] for row in a]; pivot = 0
    for j in range(len(a[0])):
        k = next((i for i in range(pivot,len(a)) if a[i][j] != ZERO),None)
        if k is None: continue
        a[pivot],a[k] = a[k],a[pivot]
        d = a[pivot][j]; a[pivot] = [div(x,d) for x in a[pivot]]
        for i in range(pivot+1,len(a)):
            d = a[i][j]
            if d != ZERO:
                a[i] = [sub(x,times(d,y)) for x,y in zip(a[i],a[pivot])]
        pivot += 1
        if pivot == len(a): break
    return pivot

def encode(a):
    if isinstance(a,tuple): return [str(x) for x in a]
    return [encode(x) for x in a]

def trace(a):
    out = ZERO
    for i in range(len(a)): out = plus(out,a[i][i])
    return out

def calculate(source):
    evidence,rows = verify(source)
    labels = sorted({tuple(r['source'][1:]) for r in rows})
    index = {p:i for i,p in enumerate(labels)}; size = len(labels)
    matrices = {stage:[[ZERO for _ in labels] for _ in labels]
                for stage in ('raw','local','aligned')}
    for r in rows:
        matrices[r['source'][0]][index[tuple(r['target'][1:])]][index[tuple(r['source'][1:])]] = weight(r)
    L,G,N = (matrices[s] for s in ('raw','local','aligned'))
    I = identity(size)
    forward = multiply(N,multiply(G,L))
    transposed = multiply(transpose(L),multiply(transpose(G),transpose(N)))
    hermitian = multiply(adjoint(L),multiply(adjoint(G),adjoint(N)))
    residual = [[sub(I[i][j],N[i][j]) for j in range(size)] for i in range(size)]
    # A nonzero retained raw state with zero complete proton readout.
    kernel = [ZERO]*size
    kernel[0] = neg(div(N[0][1],N[0][0])); kernel[1] = ONE
    kernel_column = [[x] for x in kernel]
    # Every entry of the source rank-one N is nonzero. The first column
    # supplies a concrete invertible diagonal intertwiner, not extra nodes.
    diagonal = [div(N[i][0],conj(N[i][0])) for i in range(size)]
    # Audit all rigid vertex alignments rather than treating an arbitrary
    # complex diagonal map as a geometric orientation of the tetrahedron.
    alignments = []
    for perm in permutations('ABCD'):
        rename = dict(zip('ABCD',perm))
        R = [[sum(Q(POINTS[rename[v]][i]*POINTS[v][j],4) for v in 'ABCD')
              for j in range(3)] for i in range(3)]
        assert all(sum(x != 0 for x in row) == 1 for row in R)
        mapping = []
        for edge,axis in labels:
            j = 'xyz'.index(axis)
            i = next(i for i in range(3) if R[i][j] != 0)
            target = (''.join(rename[v] for v in edge),'xyz'[i])
            mapping.append((index[target],R[i][j]))
        matches = all(N[di][dj] == times((si*sj,Q(0)),transposed[i][j])
            for i,(di,si) in enumerate(mapping) for j,(dj,sj) in enumerate(mapping))
        alignments.append({'vertices':''.join(perm),'matches_transpose_return':matches})
    fixed_frame_roundtrip = multiply(transposed,N)
    scalar = trace(fixed_frame_roundtrip)
    ranks = {name:rank(a) for name,a in [('L',L),('G',G),('N',N),
                ('transpose_return',transposed),('adjoint_return',hermitian),('residual',residual)]}
    # Reversal has separately dual-typed endpoints; equal coordinate labels
    # do not silently identify the original and dual spaces.
    reversed_rows = [(tuple(r['target']),tuple(r['source']),weight(r)) for r in rows]
    checks = {
        'source_reverified': evidence['verified'],
        'all_1836_arrows_reversed_bijectively': len(set(reversed_rows)) == len(rows) == 1836,
        'source_GL_equals_N': multiply(G,L) == N,
        'complete_forward_return_is_N': forward == N,
        'transpose_reverses_full_composition': transposed == transpose(forward),
        'adjoint_reverses_full_composition': hermitian == adjoint(forward),
        'transpose_is_involutive_on_each_stage': all(transpose(transpose(a)) == a for a in (L,G,N)),
        'adjoint_is_involutive_on_each_stage': all(adjoint(adjoint(a)) == a for a in (L,G,N)),
        'adjoint_return_matches_forward_return': hermitian == N,
        'adjoint_direct_attachment_closes_on_retained_image': multiply(hermitian,N) == N,
        'transpose_closes_on_its_own_image': multiply(transposed,transposed) == transposed,
        'diagonal_alignment_has_unit_norm_entries': all(times(x,conj(x)) == ONE for x in diagonal),
        'diagonal_alignment_intertwines_directly': all(
            times(N[i][j],diagonal[j]) == times(diagonal[i],transposed[i][j])
            for i in range(size) for j in range(size)),
        'aligned_transpose_attachment_returns_retained_state': all(
            times(times(diagonal[i],transposed[i][j]),conj(diagonal[j])) == N[i][j]
            for i in range(size) for j in range(size)),
        'full_state_inverse_obstructed_by_explicit_nonzero_kernel': any(x != ZERO for x in kernel)
            and multiply(N,kernel_column) == [[ZERO] for _ in labels],
        'lossless_split_reconstructs_every_state': all(plus(N[i][j],residual[i][j]) == I[i][j]
            for i in range(size) for j in range(size)),
        'lost_state_survives_in_complement': multiply(residual,kernel_column) == kernel_column,
        'residual_is_complementary_projector': multiply(residual,residual) == residual
            and multiply(N,residual) == [[ZERO]*size for _ in labels],
        'full_state_residual_has_rank_35': ranks['N'] == 1 and ranks['residual'] == 35,
        'identity_intermediate_removable_in_direct_attachment': multiply(hermitian,multiply(I,N)) == multiply(hermitian,N),
        'wrong_identity_inverse_rejected': multiply(N,I) != I,
        'all_24_rigid_vertex_alignments_audited': len(alignments) == 24,
        'removing_phase_alignment_breaks_fixed_frame_matching': transposed != N,
        'phase_alignment_not_a_fixed_proton_frame_symmetry': any(
            times(N[i][j],diagonal[j]) != times(diagonal[i],N[i][j])
            for i in range(size) for j in range(size)),
        'mutated_alignment_rejected': any(
            times(N[0][j],diagonal[j]) != times(neg(diagonal[0]),transposed[0][j])
            for j in range(1,size)), 
    }
    return {
        'passed':all(checks.values()), 'checks':checks,
        'source_root':source['root'], 'coordinate_labels':[list(p) for p in labels],
        'ranks':ranks,
        'contracts':{
            'linear_dual':'reverse typed arrows with unchanged weights; L^T G^T N^T',
            'hermitian_adjoint':'reverse typed arrows with conjugated weights; L* G* N*',
            'direct_adjoint':'identify raw-coordinate copies by the declared Hermitian frame',
            'direct_transpose':'explicit diagonal frame identification D, with N D = D N^T',
            'retained_observable':'complete return N; distinguish from identity on all 36 inputs'},
        'fixed_frame_transpose':{
            'same_as_forward':transposed == N,
            'roundtrip_equals_forward':fixed_frame_roundtrip == N,
            'roundtrip_trace':encode(scalar),
            'roundtrip_rank':rank(fixed_frame_roundtrip)},
        'rigid_vertex_alignments':alignments,
        'diagonal_alignment':encode(diagonal),
        'nonzero_kernel_witness':encode(kernel),
        'conclusion':'Adjoint reversal closes directly on the retained image. Unchanged-weight transpose '
          'requires alignment: the explicit diagonal map works, and its removal breaks fixed-frame '
          'matching. Whether that map is allowed as the electron frame identification or must be '
          'realized by extra structure is not specified by incidence reversal. Full-state recovery '
          'additionally requires information lost by N.',
        'scope':'Two coefficient-reversal candidates on the full source protocol; '
          'not a derivation of either candidate from the 24 geometric flags.'}

if __name__ == '__main__':
    original = SOURCE.read_bytes()
    result = calculate(json.loads(original))
    result['source_sha256'] = sha256(original).hexdigest()
    result['checker_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    assert SOURCE.read_bytes() == original, 'source was modified'
    destination = BASE/'results/reversed_coefficient_attachment.json'
    destination.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in
        ('coordinate_labels','diagonal_alignment','nonzero_kernel_witness')},indent=2))
    if not result['passed']: raise SystemExit(1)
