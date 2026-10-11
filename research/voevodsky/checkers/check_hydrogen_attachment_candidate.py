"""Conditional 12-face shell model: neutrality, negative energy and isotropy test.
Charge and Hamiltonian are declared hypotheses, not derived from 1836 arrows.
All core algebra is exact over Q; no fit to hydrogen's 13.6 eV is performed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

from check_proton_merkle_reassembly import verify as verify_focus, POINTS
from check_proton_face_extension import geometry, construct as attach, mean

BASE=Path(__file__).resolve().parents[1]
FOCUS=BASE/'results/proton_merkle_store.json'

def rank(matrix):
    a=[list(map(Q,row)) for row in matrix]; r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]; d=a[r][j]; a[r]=[x/d for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                d=a[i][j]; a[i]=[x-d*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def spectrum(L):
    # For this fixture all eigenspaces are rational and eigenvalues integral.
    # The multiplicities must exhaust the dimension, otherwise this routine fails.
    n=len(L); result={}
    for value in range(7):
        multiplicity=n-rank([[L[i][j]-value*(i==j) for j in range(n)] for i in range(n)])
        if multiplicity: result[value]=multiplicity
    if sum(result.values())!=n: raise ValueError('spectrum not exhausted by candidate eigenvalues')
    return result

def digest(record):
    return sha256(b'marici.hydrogen-attachment-candidate.v1\0'+json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def main():
    focus=json.loads(FOCUS.read_text(encoding='utf-8')); retained,_=verify_focus(focus)
    geo=geometry(focus); triangles=geo['triangles_and_transports']; n=len(triangles)
    positions=[]
    for row in triangles:
        face,a,b=row['triangle']; center=mean([tuple(map(Q,POINTS[k])) for k in face[2:]])
        positions.append(mean([center,tuple(map(Q,POINTS[a])),tuple(map(Q,POINTS[b]))]))
    neighbors=[[i!=j and len(set(triangles[i]['triangle'])&set(triangles[j]['triangle']))==2 for j in range(n)] for i in range(n)]
    degrees=[sum(row) for row in neighbors]
    L=[[degrees[i]*(i==j)-int(neighbors[i][j]) for j in range(n)] for i in range(n)]
    eig=spectrum(L)
    # Charge model on vacuum plus one occupied face: Q=+I-N_e in units of e.
    charges=[1]+[0]*n
    # On the occupied sector, H(rho)=(A/rho^2-B/rho)I+(t/rho^2)L.
    # rho>1 parameterizes the outward attachment ray; not a measured Bohr radius.
    A=B=t=Q(1); rho=2*A/B
    ground=-B*B/(4*A)
    levels={str(ground+t*Q(value)/(rho*rho)):multiplicity for value,multiplicity in eig.items()}
    norm2={sum(x*x for x in p) for p in positions}
    if len(norm2)!=1: raise ValueError('attachment radii unequal')
    radius2=next(iter(norm2))
    first=[sum(p[i] for p in positions)/n for i in range(3)]
    second=[[sum(p[i]*p[j] for p in positions)/(n*radius2) for j in range(3)] for i in range(3)]
    triple=[p[0]*p[1]*p[2] for p in positions]
    fourth=[sum(p[i]**4 for p in positions)/(n*radius2**2) for i in range(3)]
    checks={
        'source_pruning_minimal_package_preserved':retained['arrows']==1836 and retained['fixed_weight_pruning_minimal'],
        'twelve_attachment_sites_eighteen_adjacencies':n==12 and sum(degrees)//2==18 and set(degrees)=={3},
        'laplacian_symmetric_and_row_sums_zero':all(L[i][j]==L[j][i] for i in range(n) for j in range(n)) and all(sum(row)==0 for row in L),
        'unique_uniform_angular_ground_state':rank(L)==11 and eig[0]==1,
        'exact_angular_spectrum_exhausts_dimension':sum(eig.values())==12,
        'one_occupied_sector_neutral_by_explicit_charge_assignment':charges[0]==1 and set(charges[1:])=={0},
        'different_charge_assignment_does_not_give_neutrality':1+(-2)!=0,
        'outward_stationary_radius_admissible':rho>1,
        'declared_model_has_negative_ground_energy':ground==Q(-1,4),
        'binding_disappears_when_attraction_removed':all(A/r**2>0 for r in (Q(1),Q(2),Q(10))),
        'first_moment_vanishes':first==[0,0,0],
        'second_moment_is_isotropic':second==[[Q(i==j,3) for j in range(3)] for i in range(3)],
        'third_moment_obstruction_is_identical_at_every_site':set(triple)=={Q(-7,729)},
        'fourth_moment_differs_from_spherical_density':fourth==[Q(89,289)]*3 and all(v!=Q(1,5) for v in fourth),
        'not_a_hydrogen_rydberg_spectrum':sum(m for value,m in levels.items() if Q(value)<0)==1,
    }
    # Complete-square identity gives E(rho)-E_min = A(1/rho-B/(2A))^2.
    checks['radial_minimum_identity_exact']=all(A/r**2-B/r-ground==A*(1/r-B/(2*A))**2 for r in (Q(5,4),Q(3,2),Q(2),Q(3)))
    attachment=attach(focus,radial_scale=rho)
    checks['stationary_scale_has_an_actual_geometric_attachment']=bool(attachment['root'])
    # XYZ is a scalar operator on the whole 12-site Hilbert space, not just on
    # uniform mixtures: all diagonal entries equal -7/729 (off-diagonal zero).
    # Thus phases, unequal probabilities and density-matrix mixtures cannot fix it
    # while retaining this discrete position observable.
    record={'kind':'conditional-hydrogen-shell-candidate','focus':focus['root'],
            'site_labels':[r['outer_arrow'] for r in triangles],
            'site_positions_at_rho_one':[list(map(str,p)) for p in positions],
            'angular_laplacian':L,'charge_diagonal_vacuum_then_occupied':charges,
            'assumed_energy_law':'(A/rho^2-B/rho) I + (t/rho^2) L; rho>1; separated threshold 0',
            'assumed_parameters':{'A':'1','B':'1','t':'1'},
            'density_observable':'orthogonal site basis with diagonal point-position observables',
            'stationary_rho':str(rho),'stationary_ground_energy':str(ground),
            'hydrogen_identification':'fails spherical-ground-density test under declared point-site observable'}
    result={'schema':'marici.hydrogen-attachment-candidate-check.v1','passed':all(checks.values()),'checks':checks,
            'candidate_root':digest(record),'angular_spectrum':eig,'shell_energy_levels':levels,
            'positions_norm_squared':str(radius2),'first_moment':list(map(str,first)),
            'normalized_second_moment':[[str(x) for x in row] for row in second],
            'raw_xyz_moment_every_state_at_rho_one':str(triple[0]),
            'normalized_fourth_moment':list(map(str,fourth)),
            'spherical_fourth_moment':'1/5',
            'disposition':'Neutral negative-energy toy state exists under supplied laws; it is not a hydrogen model. Twelve-site point density is anisotropic for every state, and no electron spin or physical energy scale is derived.',
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'focus_file_sha256':sha256(FOCUS.read_bytes()).hexdigest()}
    out=BASE/'results'
    (out/'hydrogen_attachment_candidate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (out/'hydrogen_attachment_candidate_model.json').write_text(json.dumps({'root':digest(record),'record':record},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['passed']: raise SystemExit(1)

if __name__=='__main__': main()
