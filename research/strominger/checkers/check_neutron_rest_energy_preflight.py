"""Rest-energy preflight on the existing source-bound neutron closure.

Compute stationarity and common stationary subspace without choosing a new
Hamiltonian, physical clock, charging law or particle mass normalization.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,difference,rank,inverse,scale,columns,mv,inner,encoded


def nullspace(rows,n):
    a=[list(r) for r in rows];pivots=[];r=0
    for c in range(n):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][c];a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        pivots.append(c);r+=1
    out=[]
    for c in range(n):
        if c in pivots:continue
        v=[F(0)]*n;v[c]=1
        for i,p in enumerate(pivots):v[p]=-a[i][c]
        out.append(v)
    return out


def main():
    paths={k:ROOT/p for k,p in {
        'closure':'research/strominger/results/neutron-canonical-occupied-closure.json',
        'binding':'research/strominger/results/neutron-canonical-record-binding.json',
        'occupation':'research/voevodsky/results/seam_occupation_energy.json',
        'occupation_checker':'research/voevodsky/checkers/check_seam_occupation_energy.py',
        'clock_note':'research/nima/recovered-source-to-qp-clock-chain.md'}.items()}
    packet=json.loads(paths['closure'].read_text());binding=json.loads(paths['binding'].read_text());checks={}
    assert packet['status']=='passed'
    for p,h in packet['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_closure_receipt_valid']=True
    closed=packet['minimal_closure'];n=closed['complex_dimension'];g=[list(map(F,r)) for r in closed['metric']]
    x0=mv([list(map(F,r)) for r in closed['metric_left_inverse']],list(map(F,packet['envelope']['initial_coordinates'])))
    budget=inner(x0,g,x0);expected=F(binding['unit_coherent_neutron_empty_record_bank']['each_port_energy'])
    generators={k:[list(map(F,r)) for r in a] for k,a in closed['generators'].items()}
    projectors={k:scale(F(1,2),difference(eye(n),E)) for k,E in generators.items() if k!='native_rotation'}
    rows=[];profiles={}
    for name,P in projectors.items():
        assert mm(P,P)==P and rank(P)==1
        y=mv(P,x0);h=inner(x0,g,y)/budget
        residual=[a-h*b for a,b in zip(y,x0)]
        residual_norm=inner(residual,g,residual)/budget
        assert h==expected and residual_norm==h*(1-h)>0
        rows.extend(P)
        profiles[name]={'expectation':str(h),'generator_eigenstate_residual_squared':str(residual_norm),
                        'generator_eigenvalues':{'0':n-1,'1':1},'is_stationary_ray':False}
    checks['all_18_prepared_pulse_expectations_not_stationary_energies']=True
    fixed_basis=nullspace(rows,n);assert len(fixed_basis)==1
    k=fixed_basis[0];assert mv(generators['native_rotation'],k)==k
    coefficient=inner(k,g,x0)/inner(k,g,k);fixed=[coefficient*v for v in k]
    fixed_weight=inner(fixed,g,fixed)/budget
    assert fixed_weight==F(closed['initial_fixed_weight'])
    assert all(mv(P,fixed)==[F(0)]*n for P in projectors.values())
    checks['one_common_zero_generator_state_retained']=True
    # A common eigenvector with eigenvalue 1 for any rank-one P must lie on
    # its image. Find another projector for which that image is neither a
    # zero nor a one eigenvector. Thus no additional shared stationary ray.
    witnesses={}
    for name,P in projectors.items():
        column=next([P[i][j] for i in range(n)] for j in range(n) if any(P[i][j] for i in range(n)))
        for other,Q in projectors.items():
            y=mv(Q,column)
            if y!=[F(0)]*n and y!=column:
                witnesses[name]=other;break
        assert name in witnesses
    checks['no_common_positive_energy_eigenstate_for_the_pulse_family']=True
    # Inspect record occupation as an operator, not as a new energy law.
    # The natural bank projector in the exact 13D envelope need not preserve
    # the 11D source-pulse closure. A charging term cannot just be inserted
    # into the reduced matrices without checking this enlargement.
    B=[list(map(F,r)) for r in closed['basis_columns']]
    bank=[[F(i==j and 6<=i<12) for j in range(13)] for i in range(13)]
    bankB=mm(bank,B);enlarged=rank([a+b for a,b in zip(B,bankB)])
    assert enlarged>n
    checks['bank_occupation_operator_requires_larger_state_space']=True
    # Prior seam energy is a supplied neutral-register model. Read its live
    # receipt and check the source lift digest; do not relabel its registers
    # as the sixteen source-bank coordinates in this binding.
    old=json.loads(paths['occupation'].read_text());assert old['verification_passed']
    lift=ROOT/'research/voevodsky/results/native_operation_energy_lift_store.json'
    assert hashlib.sha256(lift.read_bytes()).hexdigest()==old['source_sha256']
    zero=next(t for t in old['exact_trials'] if t['g']=='0')
    assert F(zero['epsilon'])==F(1,4) and old['source_seams']==21
    assert zero['twenty_one_seam_increment']=={'0':'21/4'}
    assert old['physical_neutron_mass_predicted'] is False
    checks['prior_21_over_4_identified_as_separate_supplied_model']=True
    result={'status':'passed','checks':checks,'pulse_stationarity':profiles,
            'common_stationary_subspace':{'complex_dimension':1,'energy_for_each_existing_pulse':'0',
                'prepared_state_projection_weight':str(fixed_weight),'basis_vector':list(map(str,k)),
                'positive_common_eigenvector_exclusion_witnesses':witnesses,
                'scope':'Shared stationary rays of this addressed generator family, not a ground state theorem for an unspecified neutron rest Hamiltonian.'},
            'bank_occupation_diagnostic':{'source_pulse_closure_dimension':n,'dimension_after_adjoining_bank_projector_images':enlarged,
                'energy_term_added':False},
            'prior_seam_occupation':{'increment_at_supplied_zero_mixing_parameters':'21/4',
                'coupling':old['coupling'],'parameters':{k:zero[k] for k in ('epsilon','J','kappa','g')},
                'same_registers_as_canonical_binding':False,'source_lift_hash_verified':True,
                'old_checker_freshly_rerun':False},
            'rest_energy_disposition':'Not determined by the bound pulse family: the prepared neutron is not stationary, the common stationary ray has zero pulse energy, and no occupied-sector autonomous charging law or physical pulse-angle conversion has been selected.',
            'next_executable_test':'Transport the actual 21 seam controls into the full retained neutron/bank representation and test their invariant closure before importing any supplied neutral-register energy model.'}
    bound=list(paths.values())+[Path(__file__).resolve(),Path(__file__).with_name('check_neutron_canonical_occupied_closure.py'),lift]
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-rest-energy-preflight.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'pulse_expectation':str(expected),
        'stationarity_residual_squared':next(iter(profiles.values()))['generator_eigenstate_residual_squared'],
        'common_stationary_dimension':1,'common_pulse_energy':'0','bank_occupation_enlargement':enlarged,
        'rest_energy':'not yet determined'},indent=2))

if __name__=='__main__':main()
