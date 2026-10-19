"""C12 attempt 1: exact threshold-kernel criterion, not a verdict on C12.

The positive-square-root argument is documented in PENTACHORON-THRESHOLD-PROOF.md;
its finite hypotheses are freshly checked without an extended radical field.
"""
import argparse
import copy
import hashlib
import io
import json
from pathlib import Path
import zipfile
import pentachoron_exact as ex
import check_pentachoron_ground_sector as ground

HOME=Path(__file__).resolve().parent
ROOT=HOME.parents[2]
NOTE=HOME/'PENTACHORON-THRESHOLD-PROOF.md'
RESULT=HOME/'results/pentachoron-threshold-kernel.v1.json'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def decode(A):return [[ex.F(tuple(v)) for v in row] for row in A]


def rank_two(A):assert len(ex.rref(A)[1])==2,'ground/contact injection not certified'
def inverse_identity(A,B):assert ex.mm(A,B)==ex.mm(B,A)==ex.eye(len(A)),'core inverse invalid'


def build():
    certificate=ground.build()  # Fresh exact PSD, ground/dark and source checks.
    assert json.loads(ground.RESULT.read_text(encoding='utf-8'))==certificate,'stale ground receipt'
    with zipfile.ZipFile(ground.ARCHIVE) as z:
        nested=z.read('pentachoron_connected_phase_energy_bundle.zip')
    with zipfile.ZipFile(io.BytesIO(nested)) as z:raw=z.read('pentachoron_connected_phase_energy_results.json')
    assert hashlib.sha256(raw).hexdigest()==ground.SOURCE_RECEIPT_SHA
    strings=json.loads(raw)['matrices']
    matrix=lambda name:[[ex.parse(v) for v in row] for row in strings[name]]
    Ho=ex.add(matrix('L_original'),matrix('cycle_X'))
    Hc=ex.add(matrix('L_connected'),matrix('cycle_X'));P=matrix('matching_P')
    theta=ex.parse('(11-2*sqrt(6)-sqrt(5))/2')
    V=decode(certificate['ground_basis']);D=decode(certificate['dark_basis'])
    assert ex.mm(Ho,V)==[[theta*v for v in row] for row in V]
    rank_two(D)
    pivots=ex.rref(P)[1];assert len(pivots)==2
    J=[[row[j] for j in pivots] for row in P]
    assert ex.mm(P,J)==J
    C=ex.mm(ex.adjoint(V),J);rank_two(C)
    A=ex.add(Hc,[[-theta*v for v in row] for row in ex.eye(20)])
    R,pivots=ex.rref([row+unit for row,unit in zip(A,ex.eye(20))])
    assert pivots==list(range(20)),'connected core has a threshold eigenmode'
    inverse=[row[20:] for row in R];inverse_identity(A,inverse)
    controls=[]
    for name in ('dependent-ground-contact-columns','invalid-connected-core-inverse'):
        try:
            if name=='dependent-ground-contact-columns':rank_two([[row[0],row[0]] for row in C])
            else:
                bad=copy.deepcopy(inverse);bad[0][0]=bad[0][0]+1;inverse_identity(A,bad)
        except AssertionError:controls.append(name)
        else:raise AssertionError('threshold criterion hostile accepted: '+name)
    paths={NOTE,Path(__file__),Path(ex.__file__),Path(ground.__file__),ground.RESULT,ground.ARCHIVE}
    paths.update(ROOT/p for p in certificate['source_sha256'])
    return {'schema':'marici.scattering.low-energy-pentachoron-threshold-kernel.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)},
            'contact_range_dimension':2,'ground_dimension':4,'ground_to_contact_rank':2,
            'ground_adjoint_on_contact_range_injective':True,
            'contact_range_basis':ex.encoded(J),'ground_pairing_matrix':ex.encoded(C),
            'connected_core_minus_theta_rank':20,'connected_core_minus_theta_inverse':ex.encoded(inverse),
            'positive_square_root_explicitly_constructed':False,
            'square_root_free_criterion':'V*Q=0 and rank(V*|ran P)=2 force P(u-chi)=0; then Q u=0 and (H_C-theta)chi=0.',
            'full_threshold_kernel':'{(d,0):d in D}', 'full_threshold_nullity':2,
            'dark_reduced_threshold_block_invertible':True,
            'uniform_small_k_bound_reviewed':False,'C12_outcome':None,
            'new_proposition_outcomes_admitted':False,'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale threshold-kernel receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','ground_adjoint_on_contact_range_injective','connected_core_minus_theta_rank','full_threshold_nullity','dark_reduced_threshold_block_invertible','uniform_small_k_bound_reviewed','C12_outcome')}))


if __name__=='__main__':main()
