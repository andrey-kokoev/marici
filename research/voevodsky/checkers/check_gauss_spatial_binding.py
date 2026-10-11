"""3D Gauss-field branch: exact integer variational binding certificate.
SciPy proposes a Dirichlet Green function; integer inequalities certify a
lower bound independently of solver accuracy. --replay needs only NumPy.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import permutations, product
import argparse
import json
import numpy as np

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
SCALE=2**40
RADII=(12,20,28,36,44,52,60,72,88)


def laplacian(a):
    out=6*a.copy()
    for axis in range(3):
        left=[slice(None)]*3;right=[slice(None)]*3
        left[axis]=slice(1,None);right[axis]=slice(None,-1)
        out[tuple(left)]-=a[tuple(right)]
        out[tuple(right)]-=a[tuple(left)]
    return out


def reflect_octant(o):
    half=o.shape[0]-1;side=2*half+1
    y=np.abs(np.arange(-half,half+1,dtype=np.int64))[:,None]
    z=y.T
    out=np.empty((side,)*3,dtype=np.int64)
    for ix in range(side):
        x=abs(ix-half)
        lo=np.minimum(np.minimum(x,y),z)
        hi=np.maximum(np.maximum(x,y),z)
        mid=x+y+z-lo-hi
        out[ix]=o[lo,mid,hi]
    return out


def propose(half):
    from scipy.fft import dstn,idstn
    side=2*half+1
    delta=np.zeros((side,)*3,dtype=np.float64);delta[half,half,half]=1
    ev=2-2*np.cos(np.pi*np.arange(1,side+1)/(side+1))
    denominator=ev[:,None,None]+ev[None,:,None]+ev[None,None,:]
    proposal=idstn(dstn(delta,type=1,norm='ortho')/denominator,type=1,norm='ortho')
    assert np.isfinite(proposal).all() and float(np.max(np.abs(proposal)))<1
    octant=np.floor(proposal[half:,half:,half:]*SCALE).astype(np.int64)
    del proposal,denominator,delta
    integer=reflect_octant(octant)
    assert int(np.max(np.abs(integer)))<=SCALE
    residual=laplacian(integer);residual[half,half,half]-=SCALE
    error=max(0,int(residual.max()))
    # b=3(L+1)^2-|x|^2 has L_D b>=6, also at grounded boundary sites.
    x=np.arange(-half,half+1,dtype=np.int64)
    barrier=3*(half+1)**2-x[:,None,None]**2-x[None,:,None]**2-x[None,None,:]**2
    assert int(laplacian(barrier).min())>=6
    correction=(error+5)//6
    assert correction*int(barrier.max())+SCALE < (2**63)//12
    lower=np.maximum(integer-correction*barrier,0)
    certify(lower)
    return lower,dict(proposal_max_residual=error,barrier_correction=correction)


def certify(h):
    assert h.dtype==np.int64 and h.ndim==3
    side=h.shape[0];half=(side-1)//2
    assert 16<=half<=128 and h.shape==(2*half+1,)*3
    assert int(h.min())>=0 and int(h.max())<=SCALE
    residual=laplacian(h);residual[half,half,half]-=SCALE
    assert int(residual.max())<=0
    return int(residual.max())


def save_witness(path,h):
    half=(h.shape[0]-1)//2
    packed=np.array([h[half+i,half+j,half+k] for k in range(half+1)
                     for j in range(k+1) for i in range(j+1)],dtype=np.int64)
    np.savez_compressed(path,half=np.array(half),scale=np.array(SCALE),values=packed)


def load_witness(path):
    with np.load(path,allow_pickle=False) as data:
        half=int(data['half']);assert int(data['scale'])==SCALE and 16<=half<=128
        packed=data['values'];assert packed.dtype==np.int64
        assert packed.shape==((half+1)*(half+2)*(half+3)//6,)
        o=np.empty((half+1,)*3,dtype=np.int64);index=0
        for k in range(half+1):
            for j in range(k+1):
                for i in range(j+1):
                    for coordinates in permutations((i,j,k)):o[coordinates]=packed[index]
                    index+=1
    h=reflect_octant(o);certify(h);return h


def tent_energy(h,radius,t,beta):
    half=(h.shape[0]-1)//2
    line=np.maximum(radius-np.abs(np.arange(-half,half+1,dtype=np.int64)),0)
    weights=line*line;total=int(weights.sum())
    assert total==radius*(2*radius*radius+1)//3
    assert int(h.max())*total < 2**63
    first=np.tensordot(weights,h,axes=(0,0))
    second=first.astype(object) @ weights.astype(object)
    numerator=sum(int(weights[i])*int(second[i]) for i in range(len(weights)))
    potential=F(numerator,SCALE*total**3)
    kinetic=F(18)*t/(2*radius*radius+1)
    return dict(radius=radius,kinetic=str(kinetic),attraction_lower=str(beta*potential),
                energy_upper=str(kinetic-beta*potential),decimal_upper=float(kinetic-beta*potential))


def local_law_checks():
    # Three supplied translations -> the existing positive-defect constructor.
    sites=list(product(range(3),repeat=3))
    index={p:i for i,p in enumerate(sites)};ident=np.eye(27,dtype=np.int64)
    kinetic=np.zeros_like(ident)
    for axis in range(3):
        shift=np.zeros_like(ident)
        for i,p in enumerate(sites):
            q=list(p);q[axis]=(q[axis]+1)%3;shift[index[tuple(q)],i]=1
        assert np.array_equal(shift.T@shift,ident)
        defect=shift-ident
        assert np.array_equal(defect.T@defect,2*ident-shift-shift.T)
        kinetic+=defect.T@defect
    assert np.array_equal(kinetic@np.ones(27,dtype=np.int64),np.zeros(27,dtype=np.int64))
    # A grounded local graph keeps all boundary flux edges in its field energy.
    columns=[]
    for i,p in enumerate(sites):
        for axis in range(3):
            if p[axis]<2:
                q=list(p);q[axis]+=1
                col=[0]*27;col[i]=1;col[index[tuple(q)]]=-1;columns.append(col)
            for boundary in (0,2):
                if p[axis]==boundary:
                    col=[0]*27;col[i]=1;columns.append(col)
    incidence=np.array(columns,dtype=np.int64).T
    lap=incidence@incidence.T
    assert np.all(np.diag(lap)==6)
    addresses=[index[(1,1,1)],index[(2,1,1)]]
    rows=[[F(int(lap[i,j])) for j in range(27)]+[F(i==a) for a in addresses] for i in range(27)]
    for k in range(27):
        pivot=rows[k][k];assert pivot>0
        rows[k]=[x/pivot for x in rows[k]]
        for i in range(27):
            if i!=k:
                weight=rows[i][k]
                if weight:rows[i]=[x-weight*y for x,y in zip(rows[i],rows[k])]
    potentials=[np.array([row[27+j] for row in rows],dtype=object) for j in range(2)]
    fields=[incidence.T@phi for phi in potentials]
    for j in range(2):
        charge=np.array([F(i==addresses[j]) for i in range(27)],dtype=object)
        assert np.array_equal(incidence@fields[j],charge)
        assert sum(x*x for x in fields[j])==potentials[j][addresses[j]]
    cross=sum(a*b for a,b in zip(*fields))
    assert cross==potentials[0][addresses[1]]==potentials[1][addresses[0]] and cross>0
    for sign in (-1,1):
        pair=fields[0]+sign*fields[1]
        connected=(sum(x*x for x in pair)-sum(x*x for x in fields[0])-sum(x*x for x in fields[1]))/2
        assert connected==sign*cross
    return dict(translation_defect_laplacian=True,gauss_and_boundary_field_norm=True,
                exact_cross_green=str(cross),opposite_charge_attraction_same_charge_repulsion=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--half-width',type=int,default=96)
    parser.add_argument('--replay',type=Path)
    args=parser.parse_args()
    t,beta=F(1),F(1)  # fixed before trial/box enlargement; no experimental input
    law_checks=local_law_checks()
    if args.replay:
        h=load_witness(args.replay);half=(h.shape[0]-1)//2
        trials=[tent_energy(h,r,t,beta) for r in RADII if r<=half]
        replay=dict(exact_replay_passed=True,maximum_residual=certify(h),
            negative_trial=any(F(r['energy_upper'])<0 for r in trials),trials=trials,
            witness_sha256=sha256(args.replay.read_bytes()).hexdigest(),
            checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
            local_law_checks=law_checks,solver_used=False)
        (BASE/'results/gauss_spatial_binding_replay.json').write_text(json.dumps(replay,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(replay,indent=2))
        return
    half=args.half_width;assert 16<=half<=128
    h,proposal_info=propose(half)
    trials=[tent_energy(h,r,t,beta) for r in RADII if r<=half]
    best=min(trials,key=lambda row:F(row['energy_upper']))
    negative=F(best['energy_upper'])<0
    suffix='' if half==96 else f'_box{half}'
    data_path=BASE/f'results/gauss_spatial_green_lower{suffix}.npz'
    save_witness(data_path,h)
    reloaded=load_witness(data_path)
    assert np.array_equal(reloaded,h)
    assert tent_energy(reloaded,best['radius'],t,beta)==best
    residual=laplacian(reloaded);residual[half,half,half]-=SCALE
    location=np.unravel_index(int(np.argmax(residual)),residual.shape)
    bad=reloaded.copy();bad[location]+=1
    assert int(residual[location])+6>0
    try:
        certify(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError('One-unit witness corruption was accepted')
    del bad,residual
    for a,b,c in [(F(2),F(3),F(1)),(F(1),F(1),F(1,4))]:
        assert a*b>c*c
        for qp,qe in [(F(1),F(-1)),(F(1),F(1))]:
            pair=beta*(qp*qp*a+qe*qe*b+2*qp*qe*c)/2
            single=beta*(qp*qp*a+qe*qe*b)/2
            assert pair-single==beta*qp*qe*c
    contact_path=BASE/'results/proton_electron_contact_binding.json'
    contact=json.loads(contact_path.read_text(encoding='utf-8'))
    assert contact['verification_passed']
    for name,digest in contact['source_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    report=dict(verification_passed=True,local_law_checks=law_checks,model=dict(spatial_dimension=3,t=str(t),beta=str(beta),
        lattice_and_charge_assignment_supplied=True,charges=['+1','-1'],
        architecture='instantaneous longitudinal Gauss field; replaces the gapped onsite mediator'),
        field_elimination='min (beta/2)||E||^2 subject to BE=rho = (beta/2)<rho,L^-1 rho>',
        common_reference='same infinite field; both single-source self-energies retained',
        relative_hamiltonian='t L - beta G(x), G=L^-1 delta_0',
        certificate=dict(box_half_width=half,scale=SCALE,**proposal_info,
            certified_max_residual=certify(h),file=str(data_path.relative_to(ROOT)).replace('\\','/'),
            sha256=sha256(data_path.read_bytes()).hexdigest(),integer_max=int(h.max()),
            solver_accuracy_required_for_validity=False,one_unit_witness_corruption_rejected=True),
        trials=trials,best_trial=best,negative_level_certified=negative,
        nonnegative_trials_do_not_prove_nonbinding=True,
        bound_state_energy_is_exact_value=False,spin_selective=False,
        physical_hydrogen_binding_derived=False,physical_length_or_mass_calibrated=False,
        scope='Conditional reduced electrostatic lattice model; not full quantized gauge-field dynamics.',
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            [Path(__file__),BASE/'open-flux-common-vacuum.md',BASE/'weighted-matter-link-adapter.md',
             BASE/'results/proton_electron_contact_binding.json']})
    (BASE/f'results/gauss_spatial_binding{suffix}.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
