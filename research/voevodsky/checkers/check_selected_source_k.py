"""Fresh exact verification of the explicitly selected K; not umbrella admission."""
from pathlib import Path
from hashlib import sha256
import json,sys
from check_sector_theorem_progress import audit,occupation_bounds,ROOT,BASE
from check_native_spinor_pair_adapter import matrix,transport_matrix
from check_typed_spin_channels import decode,eye,kron,conjugate_matrix
from check_pentachoron_spin_interfaces import A,mm,adj,scale,add
from check_rival_defect_record_rule import vacuum_extend
from sector_theorem import SOURCE_K,MODULE,validate_source_k

def verify():
    selection=validate_source_k(ROOT)
    progress=audit()  # Fresh source closure; never overwrite the historical checkpoint.
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    def load(name):return json.loads((ROOT/(BASE+name)).read_text())
    source=load('results/pentachoron_cycle_transport.json');spin=load('results/pentachoron_spin_interfaces.json')
    typed=load('results/typed_spin_channels.json');Ps=matrix(typed['input_scalar_projector'])
    check('all_source_cases_verified',all(v is True for v in progress['checks'].values()))
    reports=[]
    for row in source['chirality_results']:
        chirality=row['chirality'];extension=row['conditional_cycle_defect_extension']
        Ws=[matrix(extension[k]['cell_isometry']) for k in ('attachment_encoding','opposite_lift_attachment_encoding')]
        low=add(*(mm(W,adj(W)) for W in Ws));lo=decode(row['low_energy'])
        hi=decode(next(r for r in spin['chirality_results'] if r['chirality']==chirality)['higher_energy'])
        L=add(scale(lo,low),scale(hi,add(eye(10),scale(A(-1),low))))
        T=transport_matrix(matrix(row['spin_lift']));H=add(L,add(scale(A(2),eye(10)),scale(A(-1),add(T,adj(T)))))
        pair=add(kron(H,eye(10)),kron(eye(10),conjugate_matrix(H)));K=vacuum_extend(pair)
        check('self_adjoint_'+str(chirality),adj(K)==K)
        check('zero_vacuum_and_carrier_commutation_'+str(chirality),len(K)==101 and all(K[100][j]==K[j][100]==A(0) for j in range(101)))
        for option,W in enumerate(Ws):
            label=f'{chirality}_{option}';J=kron(W,conjugate_matrix(W));Pi=mm(mm(J,Ps),adj(J))
            energy=next(c['scalar_pair_energy'] for c in progress['cases'] if c['source_choice']=='optional_cycle_defect' and c['chirality']==chirality and c['doublet_option']==option)
            epsilon=decode(energy);KJ=mm(pair,J);KPi=mm(mm(KJ,Ps),adj(J))
            check('selected_pair_compression_'+label,KJ==scale(epsilon,J))
            check('selected_scalar_commutation_'+label,KPi==adj(KPi) and KPi==scale(epsilon,Pi))
            reports.append({'chirality':chirality,'doublet_option':option,'scalar_pair_energy':energy})
    check('all_four_selected_cases',sorted((r['chirality'],r['doublet_option']) for r in reports)==sorted(map(tuple,selection['native_cases'])))
    lower,upper=occupation_bounds()
    check('selected_readout_separation',0<lower<upper<1)
    sources=dict(progress['source_hashes'])
    for p in (SOURCE_K,MODULE,BASE+'checkers/check_selected_source_k.py'):
        sources[p]=sha256((ROOT/p).read_bytes()).hexdigest()
    return {'schema':'marici.voevodsky.selected-source-k-check.v1','status':'pass','scientific_outcome':None,
        'physical_admission':False,'kernel_verified_analytic_theorem':False,
        'selection':selection['selection'],'matter_operator':selection['matter_operator'],'vacuum_energy':'0',
        'checks':checks,'selected_cases':reports,
        'record_occupation':{'primary_exact':'(1-cos(sqrt(2)))/4','lower':str(lower),'upper':str(upper),'rival':'0'},
        'resolved_input_blockers':['source K explicitly selected','zero K vacuum reference explicitly selected','no additional orbital or sector-mixing terms in this version'],
        'remaining_obligations':['complete joint-energy and retained post-readout accounting','variable-phase contract and typed sector classification','reviewed nonce-bound conclusion receipts'],
        'interpretation':'Input selection and exact K checks only; no automatic consumer, umbrella or physical admission.',
        'source_hashes':sources}

if __name__=='__main__':Path(sys.argv[1]).write_text(json.dumps(verify(),indent=2)+'\n')
