"""Minimal constant boundary carrier for z A + z^2 B D, with z retained."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, transpose, rank, eye, encode
from check_segmented_copy_transport import audit as segmented_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/graded-boundary-transport.v1.json'


def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in row] for row in a]


def inverse(a):
    n=len(a);rows=[list(map(F,row))+unit for row,unit in zip(a,eye(n))]
    for col in range(n):
        pivot=next(i for i in range(col,n) if rows[i][col])
        rows[col],rows[pivot]=rows[pivot],rows[col]
        divisor=rows[col][col];rows[col]=[x/divisor for x in rows[col]]
        for i in range(n):
            if i!=col:
                factor=rows[i][col];rows[i]=[x-factor*y for x,y in zip(rows[i],rows[col])]
    return [row[n:] for row in rows]


def audit():
    previous=segmented_audit();m=previous['matrices']
    A=m['one_step_boundary_A'];C=mm(m['internal_exit_B'],m['internal_entry_D'])
    K=m['macro_K'];V=m['synchronized_mode_frame']
    assert add(A,C)==K
    AV=mm(A,V);AAV=mm(A,AV)
    # Fixed reference-frame obstruction, as a polynomial coefficient identity.
    # ell compares first-pair BC with second-pair DpC, equal on the synced frame.
    ell=[[F(i==1)-F(i==7) for i in range(12)]]
    assert mm(ell,V)==[[0,0]] and mm(ell,AV)==[[-1,0]]
    assert mm(ell,mm(C,V))==[[1,0]]
    assert rank([a+b for a,b in zip(V,AV)])==3

    # Krylov closure under the two source-specified coefficient operators.
    columns=transpose(V);dimensions=[2];words=['V_s','V_t']
    while True:
        count=len(columns)
        for name,op in [('A',A),('C',C)]:
            for i in range(count):
                vector=[r[0] for r in mm(op,[[x] for x in columns[i]])]
                if rank(transpose(columns+[vector]))>len(columns):
                    columns.append(vector);words.append(name+'('+words[i]+')')
        dimensions.append(len(columns))
        if len(columns)==count:break
    assert dimensions==[2,3,4,4]
    H=transpose(columns)
    assert H==[row+[a[0],aa[0]] for row,a,aa in zip(V,AV,AAV)]
    assert rank(H)==4
    # Select independent coordinate rows; no physical metric is chosen.
    pivots=[]
    for i,row in enumerate(H):
        if rank([H[j] for j in pivots]+[row])>len(pivots):pivots.append(i)
        if len(pivots)==4:break
    select=[[F(i==j) for i in range(12)] for j in pivots]
    L=mm(inverse([H[i] for i in pivots]),select)
    assert mm(L,H)==eye(4)
    A4=mm(L,mm(A,H));C4=mm(L,mm(C,H))
    assert mm(H,A4)==mm(A,H) and mm(H,C4)==mm(C,H)
    # Polynomial identity follows from equality of each z coefficient.
    # Minimality: any constant A,C-invariant carrier containing V contains the
    # four independent generated columns, and H itself is closed under both.
    inclusion=[[1,0],[0,1],[0,0],[0,0]]
    M1=add(A4,C4)
    native_step=mm(L,mm(K,V))[:2]
    assert native_step==[[-F(1,2),F(1,2)],[-F(3,2),-F(1,2)]]
    assert mm(M1,inclusion)==mm(inclusion,native_step)
    assert mm(native_step,mm(native_step,native_step))==eye(2)
    assert rank(A4[2:])>0

    # The retained lengths are not a scalar reparametrization of the old step:
    # the reference plane leaks into extra directions at generic z.
    samples=[]
    for z in [F(0),F(1),F(-1),F(1,2),F(2)]:
        Fz=add(scale(A,z),scale(C,z*z));Tz=add(scale(A4,z),scale(C4,z*z))
        assert mm(Fz,H)==mm(H,Tz)
        assert mm(ell,mm(Fz,V))==[[z*(z-1),0]]
        leakage=Tz[2:]
        if z not in [0,1]:assert rank([row[:2] for row in leakage])>0
        samples.append({'z':z,'reference_leakage_rank':rank([row[:2] for row in leakage])})
    # The previous four-role macro carrier is a different subspace, despite
    # having the same dimension. Do not identify them by a dimension count.
    old_H=m['invariant_role_embedding_H']
    assert rank([a+b for a,b in zip(H,old_H)])==6

    dependencies=list(previous['source_sha256'])+[
        'research/scattering/seed-composition/check_graded_boundary_transport.py',
        'research/scattering/seed-composition/check_all_parse_transport.py',
        'research/scattering/seed-composition/ALL-PARSE-TRANSPORT.md']
    return {
        'schema':'marici.scattering.graded-boundary-transport.v1',
        'status':'exact_four_dimensional_constant_graded_carrier_constructed_reference_plane_leaks',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'operator':'F(z)=z A+z^2 C, C=B D; z records primitive length, not physical energy or time',
        'fixed_frame_obstruction':{'functional':'ell(y)=y_BC_first-y_DpC_second',
                                   'ell_V':[[0,0]],'ell_A_V':[[-1,0]],'ell_C_V':[[1,0]],
                                   'polynomial_defect':'ell F(z) V = [z(z-1),0]',
                                   'full_reference_plane_invariant_at_nonzero_z_only_if':'z=1',
                                   'zero_z_is_trivial_zero_operator':True},
        'minimal_constant_carrier':{'growth_dimensions':dimensions,'generated_basis':words,
                                    'rank':4,'embedding_H':H,'coordinate_rows':pivots,'left_inverse_L':L,
                                    'one_step_A4':A4,'two_step_C4':C4,
                                    'identity':'F(z) H = H (z A4+z^2 C4)',
                                    'minimality_scope':'constant linear carriers containing the original synchronized plane and invariant for every z; not minimality among z-dependent bundles'},
        'macro_specialization':{'z':1,'reference_step':native_step,'period_three_on_reference_plane':True,
                                'union_rank_with_previous_four_role_carrier':6},
        'sample_controls':samples,
        'boundary':{'z_dependent_rank_two_bundle_excluded':False,'physical_clock_or_metric_derived':False,
                    'extra_two_coordinates_are_independent_particles':False,'native_dictionary_or_preparation_derived':False,
                    'physical_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Analyze the explicit four-dimensional polynomial family: determine whether a z-dependent rank-two invariant continuation of the reference plane exists, and identify singularities or additional assumptions before calling it a clock change.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale graded-boundary receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact z(z-1) fixed-plane defect; no scalar clock substitution preserves the original plane generically.')
    print('PASS: minimal constant graded carrier has dimension 4; polynomial intertwining verified coefficientwise.')
    print('Boundary: z-dependent two-plane and physical interpretation remain open.')


if __name__=='__main__':main()
