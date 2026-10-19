"""Three source graphs, one signed endpoint-rotor constructor, same vacuum."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
from assemble_endpoint_charging import ROOT,geometry,block_diagonal
from check_source_gauss_operator_charging import positive_definite
from check_pentachoron_spin_interfaces import A,CI,S3,add,scale,mm,adj,ZERO
from check_pentachoron_cycle_transport import eye,trace,record


def ground_interval(K,metric,diagonal,steps=65):
    lo=min(diagonal);hi=sum(m*d for m,d in zip(metric,diagonal))/sum(metric)
    # This trial uses the weighted constant kinetic ground mode.
    for _ in range(steps):
        mid=(lo+hi)/2
        form=[[metric[i]*(K[i][j]+(diagonal[i]-mid if i==j else 0)) for j in range(len(metric))] for i in range(len(metric))]
        if positive_definite(form):lo=mid
        else:hi=mid
    return lo,hi


def main():
    base=ROOT/'research/voevodsky';specpath=ROOT/'research/strominger/contracts/common-endpoint-charging.json'
    spec=json.loads(specpath.read_text());beta,eta=F(spec['beta']),F(spec['eta'])
    sourcepath=base/'results/weighted_matter_link_adapter.json';contactpath=base/'results/all_face_contact.json'
    source=json.loads(sourcepath.read_text());contacts=json.loads(contactpath.read_text())['carriers']
    assert source['verification_passed'];rows={};checks={};packets={}
    nativepath=base/'results/native_operation_energy_lift_store.json'
    assert hashlib.sha256(nativepath.read_bytes()).hexdigest()==source['source_sha256']
    for name,row in source['carriers'].items():
        metric=list(map(F,row['metric_weights']));edges=[(i,j,F(w)) for i,j,w in row['edges']];n=len(metric)
        assert row['exact_zero_field_intertwining'] and all(w>0 for _,_,w in edges)
        K=[[F(0) for _ in range(n)] for _ in range(n)]
        for i,j,w in edges:
            K[i][i]+=w/metric[i];K[i][j]-=w/metric[i];K[j][j]+=w/metric[j];K[j][i]-=w/metric[j]
        assert all(sum(r)==0 for r in K)
        assert all(metric[i]*K[i][j]==metric[j]*K[j][i] for i in range(n) for j in range(n))
        graph=geometry(n,[(i,j) for i,j,_ in edges],contacts[name]['covered_triangles']);q=spec['charges'][name]
        assert block_diagonal(graph,0,[0]*len(graph['ports']),beta,eta)==[0]*n
        checks[name+'_zero_vacuum_and_retained_K']=True
        if q==0:
            diagonal=block_diagonal(graph,q,[0]*len(graph['ports']),beta,eta)
            assert diagonal==[0]*n
            rows[name]={'signed_charge':q,'ground_interval':['0','0'],'ground_flux':'all zero','ground_rank_in_selected_modes':1,
                        'nonzero_flux_lower_bound':str(beta),'reason':'Connected positive source K has a simple zero; neutral zero-flux sector has no charging term.'}
        else:
            bounds=[];diagonals=[]
            for a in range(len(graph['ports'])):
                ell=[q*int(j==a) for j in range(len(graph['ports']))]
                diagonal=block_diagonal(graph,q,ell,beta,eta);diagonals.append(diagonal)
                assert block_diagonal(graph,-q,[-x for x in ell],beta,eta)==diagonal
                bounds.append(ground_interval(K,metric,diagonal))
            lo=min(x for x,y in bounds);hi=min(y for x,y in bounds)
            outside=3*beta/2+eta/2 # any other integer sum=+/-1 flux has norm²>=3
            assert hi<outside
            rows[name]={'signed_charge':q,'ground_interval':[str(lo),str(hi)],'unit_lead_blocks':len(bounds),
                        'all_other_flux_blocks_lower_bound':str(outside),'unit_block_bounds':[[str(x),str(y)] for x,y in bounds],
                        'method':'Exact weighted rational LDL bounds; positive internal field excludes entire remaining flux lattice'}
            checks[name+'_charge_reversal_covariant']=True
        packets[name]={'metric':list(map(str,metric)),'kinetic_operator':[[str(x) for x in r] for r in K],
                       'retained_native_complement_dimension':row['complement_retained_dimension'],'complement_field_coupling':'not supplied by this selected-sector adapter',
                       'internal_edges':graph['edges'],'exterior_ports':graph['ports'],'internal_resistance':[[str(x) for x in r] for r in graph['resistance']]}
    # Elementary source matrix and link phases are exactly those of the
    # existing endpoint parent, not a flat scalar replacement.
    qmat=scale(CI/S3,tuple(tuple(A(x) for x in r) for r in ((0,1,1,1),(-1,0,1,-1),(-1,-1,0,1),(-1,1,-1,0))))
    K=add(eye(4),scale(A(-1),qmat));assert adj(qmat)==qmat and mm(qmat,qmat)==eye(4)
    graph=geometry(4,list(combinations(range(4),2)),list(range(4)))
    assert graph['resistance']==[[F(i==j,4)-F(1,16) for j in range(4)] for i in range(4)]
    phases=[]
    for a,b,c in combinations(range(4),3):
        phase=(S3*qmat[b][a])*(S3*qmat[c][b])*(S3*qmat[a][c])
        assert phase in (CI,-CI);phases.append(phase.record())
    # Newton identities verify the complete characteristic polynomial for
    # every unit-flux block of the prior analytic solution.
    v=A(beta/4)
    for a in range(4):
        ell=[-int(j==a) for j in range(4)]
        diagonal=block_diagonal(graph,-1,ell,beta,eta)
        expected=[beta*F(x,4)+F(5,8)*beta+beta/8+eta/2 for x in ell]
        assert diagonal==expected
        B=add(K,scale(-v,tuple(tuple(A(i==j==a) for j in range(4)) for i in range(4))))
        powers=[];current=eye(4)
        for k in range(1,5):current=mm(B,current);powers.append(trace(current))
        coefficients=[A(1)]
        for k in range(1,5):coefficients.append(-sum((coefficients[k-i]*powers[i-1] for i in range(1,k+1)),ZERO)/k)
        assert coefficients==[A(1),v-4,A(4)-3*v,2*v,A(0)]
    # E=(59-sqrt(1609))/40; bound the radical by rational bisection.
    rootlo,roothi=F(40),F(41)
    for _ in range(80):
        mid=(rootlo+roothi)/2
        if mid*mid<1609:rootlo=mid
        else:roothi=mid
    elo,ehi=(59-roothi)/40,(59-rootlo)/40
    assert 0<elo<ehi<3*beta/2+eta/2
    rows['electron']={'signed_charge':-1,'ground_exact':'(59-sqrt(1609))/40','ground_interval':[str(elo),str(ehi)],
                      'ground_multiplicity':4,'unit_lead_blocks':4,'all_other_flux_blocks_lower_bound':str(3*beta/2+eta/2),
                      'source_Wilson_phases':phases}
    checks['electron_parent_recovered_exactly']=True;checks['electron_source_holonomy_retained']=True
    checks['elementary_analytic_block_spectrum_verified']=True
    packets['electron']={'metric':['1']*4,'kinetic_operator':record(K),'internal_edges':graph['edges'],'exterior_ports':graph['ports'],
                         'internal_resistance':[[str(x) for x in r] for r in graph['resistance']]}
    plo,phi=map(F,rows['proton']['ground_interval'])
    ratios={'proton_per_electron_interval':[str(plo/ehi),str(phi/elo)],
            'belt_minus_proton_per_electron_interval':[str(-phi/elo),str(-plo/ehi)]}
    # Independent reference is opened only now.
    oldspecpath=base/'contracts/source-gauss-operator-charging.v1.json';old=json.loads(oldspecpath.read_text());ref=old['held_out_reference'];refpath=ROOT/ref['path']
    assert hashlib.sha256(refpath.read_bytes()).hexdigest()==ref['sha256']
    values=json.loads(refpath.read_text())['inputs'];reference=F(values['proton_me'])
    checks['proton_ratio_mismatch_certified']=phi/elo<reference
    checks['neutral_belt_ordering_failure_certified']=F(values['neutron_me'])>reference and 0<plo
    checks['zero_flux_sector_rejects_wrong_signed_charge']=False
    try:block_diagonal(graph,-1,[0]*4,beta,eta)
    except ValueError:checks['zero_flux_sector_rejects_wrong_signed_charge']=True
    bound=[specpath,Path(__file__).resolve(),Path(__file__).with_name('assemble_endpoint_charging.py'),sourcepath,contactpath,nativepath,oldspecpath,refpath,
           base/'checkers/check_spinor_endpoint_constructor.py',base/'checkers/check_spinor_quantum_leads.py',base/'checkers/check_source_gauss_operator_charging.py',base/'checkers/check_open_flux_common_vacuum.py',base/'checkers/check_belt_interface_response.py',base/'checkers/check_pentachoron_spin_interfaces.py',base/'checkers/check_pentachoron_cycle_transport.py']
    result={'status':'passed' if all(checks.values()) else 'failed','checks':checks,'sectors':rows,'comparisons':ratios,'source_operators':packets,
            'disposition':'Common signed endpoint parent constructed. Native elementary parent recovered; electromagnetic-only extension leaves neutral belt at zero and fails rest-energy comparison.',
            'energy_bearing_next_object':'A source-backed neutral interaction or internal charge sector, distinct from external electric charge, with its common vacuum and parent.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}}
    out=ROOT/'research/strominger/results/common-endpoint-charging.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':checks,'energies':{k:[float(F(x)) for x in r['ground_interval']] for k,r in rows.items()},
                      'ratios':{k:[float(F(x)) for x in xs] for k,xs in ratios.items()}},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
