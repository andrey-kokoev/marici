"""H7 partial certificate audit; exact controls are not a source resolvent proof."""
import argparse
import io
import json
from fractions import Fraction as F
from pathlib import Path
from zipfile import ZipFile
import numpy as np
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_full_response128_packet_bundle.zip'
PROOF=HOME/'FULL-RESOLVENT-CERTIFICATE.md'
RESULT=HOME/'results/resolvent-certificate-attempt.v1.json'


def audit():
    historical_validate()
    note=(HOME/'omitted_mode_estimate_note.md').read_text(encoding='utf-8')
    assert 'not interval arithmetic' in note and '12,250' in note
    with ZipFile(ARCHIVE) as z:
        with np.load(io.BytesIO(z.read('results/response128/metadata.npz')),allow_pickle=False) as m:
            K=[F(str(float(x))) for x in m['K']];e0=float(m['e0']);cpose=float(m['cpose']);down_shape=[int(v) for v in m['base_shape']]
            massless=int(np.count_nonzero(m['mass']==0))
    assert len(K)==17 and all(a<b for a,b in zip(K,K[1:]))
    assert massless>0
    midpoint=(K[8]+K[9])/2
    assert K[0]<midpoint<K[-1] and all(k!=midpoint for k in K)
    # Exact gap-only counterexample: positive diagonal blocks, singular coupled matrix.
    B,D,C=F(1),F(9),F(3)
    assert B*D-C*C==0 and D>0 and B!=0
    # A valid sufficient certificate example, independent of the source matrices.
    B,D,C=F(2),F(9),F(1)
    gamma,delta,eta=1/B,1/D,C
    rho=gamma*eta*eta*delta;assert rho<1
    full_bound=delta+gamma/(1-rho)*(1+(eta*delta)**2)
    determinant=B*D-C*C
    inverse=[[D/determinant,-C/determinant],[-C/determinant,B/determinant]]
    # Its exact Frobenius norm bounds its spectral norm and lies below C_full.
    frobenius_squared=sum(v*v for row in inverse for v in row)
    assert frobenius_squared<=full_bound*full_bound
    # Projected-zero residual does not imply the full residual vanishes.
    residual=(F(0),F(1));assert residual[0]==0 and sum(x*x for x in residual)==1
    sources=[HOME/'RADIAL-RESOLVENT-ENVELOPE.md',HOME/'results/radial-envelope.v1.json',HOME/'results/corrected-matching-residual.v1.json',ARCHIVE,PROOF,Path(__file__),HOME/'omitted_mode_estimate_note.md',HOME/'closed_mode_feedback_note.md',HOME/'response128_packet_note.md']
    return {'schema':'marici.scattering.resolvent-certificate-attempt.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},
            'H7_disposition':'open; sufficient certificate derived, source bounds not certified',
            'packet_nodes':len(K),'packet_K_band':[str(K[0]),str(K[-1])],'source_e0_float':e0,
            'source_common_pose_shift':cpose,
            'reported_gap_candidate_float':16-(e0+float(K[-1])+cpose),
            'reported_gap_candidate_is_certified':False,'downstream_matrix_shape':down_shape,
            'massless_boundary_unknowns':massless,'physical_mass_is_positive_solver_norm':False,
            'raw_internal_dimension_per_body':12250,'retained_internal_directions':548,
            'exact_controls':{'gap_only_singular_matrix':[[1,3],[3,9]],
                              'unsampled_singular_energy':str(midpoint),
                              'valid_example_rho':str(rho),'valid_example_full_bound':str(full_bound),
                              'valid_example_inverse_Frobenius_squared':str(frobenius_squared),
                              'projected_zero_full_residual_norm_squared':'1'},
            'positive_solver_norm_specified':True,
            'central_matching_residual_audited':True,
            'missing_source_inputs':['certified raw functional-calculus and spectral-frame reconstruction','certified omitted gap','certified coupling and general matching-system inverse bounds over the whole band'],
            'source_solvers_replayed':False,'uniform_source_inverse_certified':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale H7 attempt receipt'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: exact sufficient-certificate controls and source-gap audit. H7 remains open.')


if __name__=='__main__':main()
