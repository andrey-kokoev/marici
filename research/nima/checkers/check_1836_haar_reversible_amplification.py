"""Exact transfer of the source-derived 1836 retained mode to a Haar core.

Reconstructs P,G,N from the existing tetrahedral source constraints. Does not
import a fitted collective vector or identify the 1836 graph with arithmetic.
All arithmetic is in Q(i*sqrt(3)); normalization by sqrt(nu) is checked through
exact Gram identities without floating square roots.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import check_lrg_1836 as native

ROOT = Path(__file__).resolve().parents[3]
ZERO, ONE = native.ZERO, native.ONE


def kron(a,b):
    return tuple(tuple(native.zmul(a[i//len(b)][j//len(b[0])], b[i%len(b)][j%len(b[0])])
                       for j in range(len(a[0])*len(b[0])))
                 for i in range(len(a)*len(b)))


def embed(w,d):
    return tuple(tuple(w[i//d] if i%d==j else ZERO for j in range(d))
                 for i in range(len(w)*d))


def norm_column(v):
    return sum((native.znorm(row[0]) for row in v),F(0))


def main():
    rows,frames,L=native.source()
    spectrum=native.spectrum(L)
    Gscalar=native.eye(12)
    for lam in spectrum:
        if lam:
            Gscalar=native.mm(Gscalar,native.add(native.eye(12),native.scale(L,-F(1,lam))))
    rotations=[row[2] for row in rows]
    G=native.lift([[native.zreal(native.scale(native.mm(r,native.transpose(s)),Gscalar[i][j]))
                    for j,s in enumerate(rotations)] for i,r in enumerate(rotations)])
    local=[native.local_ground(x,native.OMEGA) for x in frames]
    empty=tuple((ZERO,)*3 for _ in range(3))
    P=native.lift([[local[i][1] if i==j else empty for j in range(12)] for i in range(12)])
    N=native.zmm(G,P)
    assert native.zmm(P,G)==N
    assert native.zmm(N,N)==N and native.dagger(N)==N and native.ztrace(N)==1
    assert [native.count(M) for M in [P,G,N]]==[108,432,1296]
    assert sum(native.count(M) for M in [P,G,N])==1836
    # Derive the retained vector from a nonzero column of the new projector.
    j=next(j for j in range(36) if N[j][j]!=ZERO)
    w=tuple(N[i][j] for i in range(36))
    nu=sum((native.znorm(x) for x in w),F(0))
    assert nu>0
    assert native.projector(w)==N
    wcol=tuple((x,) for x in w)
    for M in [P,G,N]: assert native.zmm(M,wcol)==wcol

    # Actual relative-Haar core: e_n is the normalized indicator of
    # [n log(p),(n+1)log(p))^2 in the two logarithmic Haar coordinates.
    # The seam-normalized diagonal prime dilation sends e_n to e_(n-1).
    source_cells=[0,1,2]
    target_cells=[-1,0,1,2]
    S=native.zreal(tuple(tuple(F(a==b-1) for b in source_cells) for a in target_cells))
    assert native.zmm(native.dagger(S),S)==native.zreal(native.eye(3))
    embeddings={}
    retractions={}
    for d in [3,4]:
        J=embed(w,d)
        R=native.zs(native.dagger(J),1/nu)
        embeddings[d]=J;retractions[d]=R
        assert native.zmm(R,J)==native.zreal(native.eye(d))
        assert native.zmm(native.dagger(J),J)==native.zs(native.zreal(native.eye(d)),nu)
        assert native.zmm(J,R)==kron(N,native.zreal(native.eye(d)))
    amplified_shift=kron(native.zreal(native.eye(36)),S)
    assert native.zmm(amplified_shift,embeddings[3])==native.zmm(embeddings[4],S)
    assert native.zmm(retractions[4],amplified_shift)==native.zmm(S,retractions[3])
    # Reversal is valid on the transported subspace, not all target cells.
    assert native.zmm(native.dagger(amplified_shift),amplified_shift)==native.zreal(native.eye(108))

    # A nonzero coherence residual cannot be repaired by isometric amplification.
    residual=tuple(((F(x),F(0)),) for x in [1,-2,3])
    lifted=native.zmm(embeddings[3],residual)
    assert norm_column(lifted)/nu==norm_column(residual)==14
    assert native.zmm(retractions[3],lifted)==residual

    # A period-12 target loses a concrete nonzero Haar orbit difference.
    # This is a general periodic-transport hostile, not an identification of the
    # separate 1836 Fourier phase net with the projector construction above.
    fold=tuple(tuple(F(i==j%12) for j in range(13)) for i in range(12))
    orbit_difference=tuple(F(j==12)-F(j==0) for j in range(13))
    assert native.mv(fold,orbit_difference)==(F(0),)*12
    assert sum(x*x for x in orbit_difference)==2

    # Exercise the scalar energy defect itself, both for equal histories and
    # for two different histories. Equality here is a fixture, not an Xi zero.
    second=tuple(((F(x),F(0)),) for x in [0,1,1])
    defect_checks=[]
    for p in [2,3,5,7]:
        for sigma in [-1,0,1]:
            amplitude=F(p)**(-sigma)
            T=native.zs(S,amplitude)
            for label,minus in [('equal_histories',residual),('different_histories',second)]:
                plus=residual
                moved=native.zmm(T,minus)
                defect=norm_column(plus)-norm_column(moved)
                lifted_plus=native.zmm(embeddings[3],plus)
                lifted_moved=native.zmm(embeddings[4],moved)
                assert norm_column(lifted_plus)/nu-norm_column(lifted_moved)/nu==defect
                if label=='equal_histories':
                    assert defect==(1-amplitude*amplitude)*14
                defect_checks.append({'p':p,'Re_z':sigma,'fixture':label,'defect':str(defect)})
            # Replacing the true step by its unitary shift breaks intertwining
            # off the seam; the missing scalar cannot be normalized away.
            source_path=native.zmm(embeddings[4],native.zmm(T,residual))
            unitarized_path=native.zmm(amplified_shift,native.zmm(embeddings[3],residual))
            assert (source_path==unitarized_path)==(sigma==0)

    # Two off-seam fixtures strictly inside 0<Re(s)<1, without rounding logs:
    # sigma=-log(amplitude)/log(2), so |sigma|<1/2 iff 1/2<amplitude^2<2.
    critical_strip_controls=[]
    for amplitude in [F(4,5),F(5,4)]:
        assert F(1,2)<amplitude*amplitude<2 and amplitude!=1
        T=native.zs(S,amplitude)
        inverse_on_range=native.zs(native.dagger(S),1/amplitude)
        assert native.zmm(inverse_on_range,T)==native.zreal(native.eye(3))
        moved=native.zmm(T,residual)
        defect=14-norm_column(moved)
        assert defect!=0
        assert 14-norm_column(native.zmm(embeddings[4],moved))/nu==defect
        critical_strip_controls.append({'p':2,'amplitude':str(amplitude),
            'Re_z':'-log('+str(amplitude)+')/log(2)',
            'equal_history_energy_defect':str(defect),'inverse_recovers_state':True,
            'is_actual_Xi_zero':False})

    multipliers=[]
    for p in [2,3,5,7]:
        for twice_sigma in [-2,-1,0,1,2]:
            gain=F(p)**(-twice_sigma)
            assert gain>0 and gain*F(p)**twice_sigma==1
            assert (gain==1)==(twice_sigma==0)
            multipliers.append({'p':p,'twice_Re_z':twice_sigma,'energy_gain':str(gain),
                                'roundtrip_gain':'1','one_step_isometry':gain==1})
    out={
        'schema':'marici.nima.1836-haar-reversible-amplification.v1',
        'passed':True,
        'native_dimensions':36,
        'native_projector_ranks':[native.ztrace(P),native.ztrace(G),native.ztrace(N)],
        'native_support_counts':[108,432,1296],
        'native_total_arrows':1836,
        'source_derived_column':j,
        'unnormalized_column_norm_squared':str(nu),
        'normalized_realization':'J h=(w/sqrt(nu)) tensor h; R=J dagger; RJ=I; JR=N tensor I',
        'haar_core':{'source_cells':source_cells,'target_cells':target_cells,
                     'normalization':'indicator of log-square divided by log(p)',
                     'prime_action':'e_n -> e_(n-1); no cyclic wrapping'},
        'intertwining_and_recovery':True,
        'nonzero_residual_norm_squared_before_and_after':14,
        'periodic_collapse_hostile_norm_squared':2,
        'energy_multipliers':multipliers,
        'scalar_defect_preservation_checks':defect_checks,
        'off_seam_critical_strip_controls':critical_strip_controls,
        'unitarizing_transport_breaks_intertwining_off_seam':True,
        'claim_boundary':'Constructs reversible norm-preserving amplification retaining the Haar history factor. Does not compress the full Haar representation into a fixed finite model, change its modular multiplier, derive a proton mass, or prove Xi-state energy conservation.',
        'rh_proved':False,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'native_input_sha256':{
            str(Path(module.__file__).resolve().relative_to(ROOT)).replace('\\','/'):
                hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
            for module in [sys.modules[name] for name in [
                'check_lrg_1836', 'check_twelve_triangle_positive_geometry',
                'check_twenty_four_triangle_shared_seed', 'check_collective_four_state_identity',
                'check_triangle_half_phase',
            ]]
        },
    }
    # Projector traces are exact rationals; serialize them without coercion.
    out['native_projector_ranks']=list(map(str,out['native_projector_ranks']))
    target=ROOT/'research/nima/results/1836-haar-reversible-amplification.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__=='__main__': main()
