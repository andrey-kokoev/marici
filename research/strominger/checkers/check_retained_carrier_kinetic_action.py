"""A common occupied-sector action on the metric sphere of each native return.

H = -hbar²/(2F²) Delta_S. Retain the whole sphere, not just a phase circle.
A degree-l harmonic has energy l(l+d-2)/2; internal phase weight k=1 first
occurs at l=1, giving energy (d-1)/2 and r complex holomorphic coordinates.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib
from assemble_metric_coefficient_protocol import ROOT,A,ONE,ZERO,read_operator,product,sharp,integer_trace


def inner(v,w,metric):return sum((x.flip(8)*y*A(g) for x,y,g in zip(v,w,metric)),ZERO)
def monomials(degree,dimension):
    if dimension==1:
        yield (degree,);return
    for k in range(degree+1):
        for rest in monomials(degree-k,dimension-1):yield (k,)+rest

def coefficient_rank(matrix):
    rows=[[F(x) for x in row] for row in matrix];r=0
    if not rows:return 0
    for c in range(len(rows[0])):
        p=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r];pivot=rows[r][c];rows[r]=[v/pivot for v in rows[r]]
        for i in range(r+1,len(rows)):
            if rows[i][c]:
                a=rows[i][c];rows[i]=[x-a*y for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r


def harmonic_charge_dimension(r,p,q):
    # Homogeneous complex polynomials of bidegree (p,q), phase charge p-q.
    # Euclidean Laplacian is 4 sum_i partial_z_i partial_zbar_i.
    columns=[a+b for a in monomials(p,r) for b in monomials(q,r)]
    if not p or not q:return len(columns)
    targets=[a+b for a in monomials(p-1,r) for b in monomials(q-1,r)]
    ids={x:i for i,x in enumerate(targets)};M=[[0]*len(columns) for _ in targets]
    for j,exponents in enumerate(columns):
        for i in range(r):
            factor=4*exponents[i]*exponents[r+i]
            if factor:
                e=list(exponents);e[i]-=1;e[r+i]-=1;M[ids[tuple(e)]][j]+=factor
    return len(columns)-coefficient_rank(M)


def main():
    specpath=ROOT/'research/strominger/contracts/retained-carrier-kinetic-action.json';spec=json.loads(specpath.read_text())
    root=ROOT/'research/strominger/results/common-three-carrier-protocol';verification=root/'verification.json';old=json.loads(verification.read_text())
    assert old['status']=='passed'
    for p,h in {**old['source_hashes'],**old['packet_hashes']}.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    rows={};checks={};paths=[specpath,verification,Path(__file__).resolve(),Path(__file__).with_name('assemble_metric_coefficient_protocol.py')]
    for name in ('proton','neutron','electron'):
        path=root/(name+'.json');packet=json.loads(path.read_text());paths.append(path)
        metric=tuple(map(F,packet['source']['metric']));n=len(metric);N=read_operator(packet['operators']['N'],n)
        assert all(g>0 for g in metric) and sharp(N,metric)==N and product(N,N)==N
        r=integer_trace(N);assert r>0
        # Each nonzero column and their complex combinations live on the
        # actual native return. A scalar rescaling must not alter the metric
        # readout on its normalized ray/phase orbit.
        vectors=[tuple(N.get((i,j),ZERO) for i in range(n)) for j in range(n)]
        vectors=[v for v in vectors if any(x!=ZERO for x in v)]
        for v in vectors:
            squared=inner(v,v,metric);assert squared!=ZERO and squared.flip(8)==squared
            normalized_pairing=inner(v,v,metric)/squared;assert normalized_pairing==ONE
            scaled=tuple(3*x for x in v);assert inner(scaled,scaled,metric)==9*squared
            assert inner(scaled,scaled,metric)/inner(scaled,scaled,metric)==normalized_pairing
        d=2*r
        # Polar Laplacian identity for a homogeneous harmonic polynomial:
        # 0=Delta_R(rho^l Y)=rho^(l-2)[l(l+d-2)Y+Delta_S Y].
        # Fixed phase charge +1 has p=q+1 and l=2q+1; degree one is
        # therefore the lowest possible nonempty harmonic sector.
        energies=[]
        for q in range(5):
            p=q+1;l=p+q;multiplicity=harmonic_charge_dimension(r,p,q)
            if multiplicity:
                energies.append({'degree':l,'multiplicity':multiplicity,'energy':str(F(l*(l+d-2),2))})
        assert energies[0]['degree']==1 and energies[0]['multiplicity']==r
        assert harmonic_charge_dimension(r,1,0)==harmonic_charge_dimension(r,0,1)==r
        # l(l+d-2) increases for all l>=1, d>=2, so higher degrees
        # cannot undercut the charged first harmonics. No spectral cutoff.
        assert d>=2 and all(F(e['energy'])>=F(d-1,2) for e in energies)
        rows[name]={'source_return_rank':r,'real_sphere_dimension':d-1,'internal_charge':1,
                    'external_charge':spec['external_charge_multipliers'][name],
                    'occupied_sector_ground_energy':str(F(d-1,2)),'occupied_ground_multiplicity':r,
                    'first_nonempty_charge_one_harmonic_blocks':energies,
                    'retained_phase_only_circle_would_give':'1/2; incorrect for full rank-two sphere because it deletes transverse dynamics'}
        checks[name+'_native_metric_and_return_verified']=True
        checks[name+'_normalization_not_arrow_multiplicity']=True
        checks[name+'_occupied_charge_sector_and_ground_dimension']=True
    ratios={'proton_per_electron':str(F(rows['proton']['occupied_sector_ground_energy'])/F(rows['electron']['occupied_sector_ground_energy'])),
            'neutron_minus_proton_per_electron':str((F(rows['neutron']['occupied_sector_ground_energy'])-F(rows['proton']['occupied_sector_ground_energy']))/F(rows['electron']['occupied_sector_ground_energy']))}
    assert ratios=={'proton_per_electron':'1/3','neutron_minus_proton_per_electron':'0'}
    # Reference is inspected after the action/spectrum has been constructed.
    refspecpath=ROOT/spec['held_out_reference_contract'];refspec=json.loads(refspecpath.read_text());ref=refspec['held_out_reference'];refpath=ROOT/ref['path']
    assert hashlib.sha256(refpath.read_bytes()).hexdigest()==ref['sha256']
    reference=json.loads(refpath.read_text())['inputs']
    checks['joint_mass_comparison_failed']=F(ratios['proton_per_electron'])!=F(reference['proton_me']) and F(reference['neutron_me'])!=F(reference['proton_me'])
    checks['common_positive_occupied_energy_and_zero_vacuum']=all(F(x['occupied_sector_ground_energy'])>0 for x in rows.values())
    paths += [refspecpath,refpath,ROOT/'research/nima/comparison-kinetic-readout.md']
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,'carriers':rows,'ratios':ratios,
            'construction':'Full unit-sphere kinetic action of each native retained carrier; common Laplace-Beltrami quantization and conserved internal phase charge +1',
            'disposition':'Positive occupied sectors and the correct retained ground dimensions, but wrong hierarchy: proton and neutron 1/2, electron 3/2.',
            'residual':'A source rule must distinguish the occupied action beyond a normalized return space. Fixed charge sector and Laplace-Beltrami ordering are supplied, not derived from N.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/retained-carrier-kinetic-action.json';out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
