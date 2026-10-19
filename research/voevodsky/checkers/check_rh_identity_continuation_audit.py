# /// script
# dependencies = ["sympy"]
# ///
"""RH task-relative identity audit. --replay constructs exact witnesses.
Default validates the retained result and source hashes without symbolic imports.
"""
import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[3]
DICT='research/conjecture_net/contracts/rh-stage-dictionary.v1.json'
NOTE='research/voevodsky/rh-identity-continuation-audit-v1.md'
OUT='research/voevodsky/results/rh-identity-continuation-audit-v1.json'
SOURCE_RECEIPTS={
 'carrier':'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json',
 'endpoint':'research/voevodsky/results/full-endpoint-fourier-bridge-v1.json',
 'riemann':'research/voevodsky/results/riemann-comb-specialization-v1.json'}
REPLAY={'endpoint':'check_full_endpoint_fourier_bridge.py','riemann':'check_riemann_comb_specialization.py'}
CELLS={
 'hidden-reconstruction':dict(disposition='constructed_for_fixed_coefficient_tasks',equivalence='P x=P y for generic analytic readout; r12 x=r12 y for unshifted readout. Neither identifies complete retained source states.',licensed_operations=['C12','D12 and its finite-dimensional flow'],witness='P C12=C4 P; P D12=D4 P; r12 C12=r12; r12 D12=0. Complete state reconstructed as E P x+N x.'),
 'history-retention':dict(disposition='constructed_for_fixed_history_tasks',equivalence='O_n x=O_n y for full endpoint/generic analytic task; complete source identity also compares endpoint-invisible histories and provenance.',licensed_operations=['native step_n at audited stages','existing lifted L_n and its flow'],witness='O_next step=M O_n; O_n L_n=A_endpoint O_n; N_next step=step N_n; x=Efull Pfull x+Nfull x.'),
 'riemann-quotient':dict(disposition='unsafe_scalar_identity_rejected_and_safe_task_reader_constructed',equivalence='For endpoint recurrence with scalar observation ell, equality of Z x, Z=[ell;ell M], is future-safe. Equality of ell x alone is not.',licensed_operations=['native endpoint M','declared A_endpoint drift'],witness='ell=[2,2,0,0], ell M=[2,2,2,2], Z M=[[0,1],[1,1]] Z, Z A_endpoint=0. Equal scalar readouts 2 can have next readouts 2 and 4.')}


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def validate_cells(cells):
    d=load(DICT)
    required={c['id'] for c in d['cells'] if c['owner']=='rh-identity-continuation-transport' and c['required_for_interface']}
    require(set(cells)==required and cells==CELLS,'changed/missing identity cell or licensed-operation scope')
    require({c['id'] for c in d['cells'] if c['owner']=='rh-identity-continuation-transport' and not c['required_for_interface']}=={'one-dimensional-binding'},'source-selection boundary changed')


def exact_witnesses():
    import sympy as S
    def rows(x):return [[str(v) for v in x.row(i)] for i in range(x.rows)]
    sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
    from source_arrow_hamiltonian import construct
    prior=load('research/strominger/results/source-arrow-hamiltonian-descent.json')
    src,C,edges=construct(tuple('ABCD'),prior['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    E=S.eye(12)[:,:4];P=(E.T*src.G*E).inv()*E.T*src.G;N=S.eye(12)-E*P
    C4=P*C*E;D4=P*src.D*E
    require(P*C==C4*P and P*src.D==D4*P,'carrier quotient not future-safe')
    require(N*C==C*N and N*src.D==src.D*N,'carrier hidden continuation')
    require(E*P+N==S.eye(12),'carrier reconstruction')
    top=S.Matrix(load(SOURCE_RECEIPTS['carrier'])['projection_then_attachment']);r12=S.ones(1,4)*top
    require(r12*C==r12 and r12*src.D==S.zeros(1,12),'carrier Riemann quotient not safe')
    h=next(N[:,j] for j in range(12) if N[:,j]!=S.zeros(12,1))
    require(P*h==S.zeros(4,1) and E*P*h+N*h==h,'hidden source lost')
    endpoint=load(SOURCE_RECEIPTS['endpoint']);M=S.Matrix(endpoint['endpoint_matrix']);J=S.Matrix(endpoint['full_analytic_attachment']);Q=S.Matrix(endpoint['endpoint_basis']);Qi=Q.inv()
    ell=S.simplify(S.ones(1,4)*J);Z=ell.col_join(ell*M);T=S.Matrix([[0,1],[1,1]])
    require(ell==S.Matrix([[2,2,0,0]]) and ell*M==S.Matrix([[2,2,2,2]]),'changed native readout convention')
    require(Z.rank()==2 and Z*M==T*Z,'safe predictive quotient')
    a=S.eye(4)[:,0];b=a+S.eye(4)[:,2]
    require(ell*a==ell*b==S.Matrix([2]),'equal-present hostile')
    require(ell*M*a==S.Matrix([2]) and ell*M*b==S.Matrix([4]),'different-next hostile')
    A0=S.Matrix([[0,S.Rational(2,3)],[-2,0]]);Aep0=Q*S.diag(A0,S.zeros(2))*Qi
    require(Z*Aep0==S.zeros(2,4),'predictive reader drift changed')
    for k in range(12):require(ell*M**k==(S.Matrix([[1,0]])*T**k)*Z,'all-future recurrence control')
    # Derive the smallest rowspace stable under M, rather than assume Z is minimal.
    observability=S.Matrix.vstack(*(ell*M**k for k in range(4)))
    require(observability.rank()==2 and observability.col_join(Z).rank()==2,'minimal predictive rank')
    sys.path.insert(0,str(ROOT/'research/nima/checkers'))
    from retained_path_successor import RetainedSuccessorLedger
    from check_natural_tower_return import PACKETS
    import photon_native_spatial_step as rotor
    rb=S.Matrix(rotor.target_reader())*S.Matrix.hstack(S.Matrix(rotor.U),S.Matrix(rotor.W));pa=(rb.T*rb).inv()*rb.T
    complement=Q[:,2:];Sfull=Qi*M*Q
    ledger=RetainedSuccessorLedger(PACKETS);frame=ledger.root;weights=[S.Rational(1)]*len(frame.paths);old=None;stages=[]
    for tick in range(4):
        child=ledger.successor(frame);counts=[child.parent_slots.count(i) for i in range(len(frame.paths))]
        weights=[weights[i]/counts[i] for i in child.parent_slots];frame=child;n=len(frame.paths)
        step=S.Matrix(frame.step_lift);G=S.diag(*weights)
        O=S.Matrix([[int(path[-1][1]==a) for path in frame.paths] for a in 'ABCD']);Pf=Qi*O;Pactive=pa*O
        if old is None:
            Ea=G.inv()*Pactive.T*(Pactive*G.inv()*Pactive.T).inv()
            Ec=G.inv()*O.T*(O*G.inv()*O.T).inv()*complement
            Ef=Ea.row_join(Ec)
        else:Ef=step*old['Ef']*Sfull.inv();Ea=Ef[:,:2]
        Nh=S.eye(n)-Ef*Pf;L0=Ea*A0*Pactive
        require(Pf*Ef==S.eye(4) and Ef*Pf+Nh==S.eye(n),'history reconstruction')
        require(O*L0==Aep0*O,'endpoint drift transport')
        require(Z*O*L0==S.zeros(2,n),'history predictive task drift')
        x=S.eye(n)[:,next(i for i,path in enumerate(frame.paths) if path[-1][1]=='A')]
        hc=S.eye(n)[:,next(i for i,path in enumerate(frame.paths) if path[-1][1]=='C')];y=x+hc
        require(O*x==a and O*y==b,'hostile not in actual history space')
        require(ell*O*x==ell*O*y==S.Matrix([2]),'history same present readout')
        require(Ef*Pf*x+Nh*x==x and Ef*Pf*y+Nh*y==y,'hostile archive reconstruction')
        kernel_witness=next(Nh[:,j] for j in range(n) if Nh[:,j]!=S.zeros(n,1))
        require(O*kernel_witness==S.zeros(4,1) and kernel_witness!=S.zeros(n,1),'endpoint equality erases full history')
        item=dict(dimension=n,reader_rank=(Z*O).rank(),full_endpoint_rank=O.rank(),hidden_dimension=n-4,
                  hostile_parent_x=rows(x),hostile_parent_y=rows(y),present_readouts=['2','2'],endpoint_predicted_next=['2','4'],reconstruction=True)
        if old is not None:
            require(O*step==M*old['O'] and Nh*step==step*old['N'],'native continuation lost')
            require(L0*step==step*old['L0'],'generator/extension overlap')
            require(Z*O*step==T*Z*old['O'],'predictive task/history square')
            require(ell*O*step*old['x']==S.Matrix([2]) and ell*O*step*old['y']==S.Matrix([4]),'actual next-readout hostile fails')
            # A formerly endpoint-invisible difference remains endpoint-invisible.
            require(O*step*old['hidden']==S.zeros(4,1),'kernel equivalence not respected')
            item['actual_previous_hostile_next_readouts']=['2','4']
        stages.append(item);old=dict(Ef=Ef,O=O,N=Nh,L0=L0,x=x,y=y,hidden=kernel_witness)
    require([r['dimension'] for r in stages]==[10,16,26,42],'audited stage set')
    return dict(carrier_hidden_witness=rows(h),carrier_riemann_row=rows(r12),
      endpoint_readout=rows(ell),predictive_reader=rows(Z),predictive_update=rows(T),
      endpoint_pair=[rows(a),rows(b)],minimum_future_safe_linear_reader_rank=2,
      history_stages=stages,
      theoretical_future_scope='All powers of the declared endpoint recurrence by ell(M^2-M-I)=0; four actual history stages and three extension squares freshly constructed.',
      complete_state_identity_inferred_from_task_readout=False)


def source_paths():
    d=load(DICT);paths=[DICT,NOTE,Path(__file__).relative_to(ROOT).as_posix(),
      'research/voevodsky/rh-operation-composition-audit-v1.md',
      'research/voevodsky/results/rh-operation-composition-audit-v1.json',
      'research/strominger/results/source-arrow-hamiltonian-descent.json',
      'research/strominger/checkers/source_arrow_hamiltonian.py',
      'research/nima/checkers/retained_path_successor.py',
      'research/nima/checkers/check_natural_tower_return.py',
      'research/nima/checkers/photon_native_spatial_step.py']
    paths+=list(SOURCE_RECEIPTS.values())
    paths+=['research/voevodsky/checkers/'+s for s in REPLAY.values()]
    paths+=list(d['evidence_sources'].values())
    return sorted(set(paths))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--replay',action='store_true');args=parser.parse_args()
    validate_cells(CELLS);controls=[]
    for mode in ('missing-cell','scalar-promoted-to-full-identity','unbound-operation-added','source-selection-promoted'):
        bad=copy.deepcopy(CELLS)
        if mode=='missing-cell':bad.pop('history-retention')
        elif mode=='scalar-promoted-to-full-identity':bad['riemann-quotient']['equivalence']='Equal scalar readout identifies full history.'
        elif mode=='unbound-operation-added':bad['history-retention']['licensed_operations'].append('arbitrary independently writable memory')
        else:bad['one-dimensional-binding']=bad['riemann-quotient']
        try:validate_cells(bad)
        except ValueError:controls.append(mode)
        else:raise AssertionError('hostile accepted '+mode)
    if args.replay:
        executions=[]
        for key,script in REPLAY.items():
            p='research/voevodsky/checkers/'+script;old=sha(SOURCE_RECEIPTS[key])
            r=subprocess.run([sys.executable,str(ROOT/p)],cwd=ROOT,capture_output=True,text=True,timeout=240)
            require(r.returncode==0,'source replay failed '+key+'\n'+r.stderr+'\n'+r.stdout[-3000:])
            require(sha(SOURCE_RECEIPTS[key])==old,'pinned upstream receipt changed '+key)
            executions.append(dict(id=key,checker=p,returncode=0,receipt_unchanged=True))
        witnesses=exact_witnesses()
        result=dict(schema='marici.rh-identity-continuation-audit.v1',passed=True,cells=CELLS,
          required_cells_covered=3,witnesses=witnesses,source_suites_freshly_replayed=executions,
          analytic_completion_gate_closed=False,stagewise_assembly_closed=False,
          physical_detector_or_control_admitted=False,corruptions_rejected=controls,
          source_sha256={p:sha(p) for p in source_paths()})
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    else:
        result=load(OUT);require(result['passed'] and result['cells']==CELLS,'changed identity receipt')
        require(result['source_sha256']=={p:sha(p) for p in source_paths()},'identity source drift')
        require(result['witnesses']['minimum_future_safe_linear_reader_rank']==2 and not result['witnesses']['complete_state_identity_inferred_from_task_readout'],'identity promotion')
        require(not result['analytic_completion_gate_closed'] and not result['stagewise_assembly_closed'],'assembly promotion')
    print(json.dumps(dict(passed=True,required_cells_covered=3,fresh_replay_this_run=args.replay,
      endpoint_readout=result['witnesses']['endpoint_readout'],predictive_reader=result['witnesses']['predictive_reader'],
      predictive_update=result['witnesses']['predictive_update'],next_hostile_readouts=[2,4],
      corruptions_rejected=controls),indent=2))


if __name__=='__main__':main()
