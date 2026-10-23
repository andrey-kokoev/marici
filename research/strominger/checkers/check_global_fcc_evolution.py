"""Execute a declared whole-FCC evolution; measure, do not fit, its native E match."""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import copy
import hashlib
import json
from global_fcc_evolution import GlobalFCCEvolution
from check_fcc_gaussian_boundary import action as prior_gaussian_action

ROOT=Path(__file__).resolve().parents[3]
CENSUS='research/voevodsky/results/esd7_explicit_analytical_census.json'
COARSE='research/strominger/results/fcc-first-transport.json'
FLAGS='research/strominger/results/esd7-seven-stage-handoff.json'
NATIVE='research/strominger/results/native-fcc-end-to-end.json'

def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def norm(v):return sum(abs(z)**2 for z in v)
def distance(a,b):return norm([x-y for x,y in zip(a,b)])**0.5
def encode(v):return [[z.real,z.imag] for z in v]
def sums(terms):
    d=defaultdict(int)
    for k,v in terms:d[k]+=v
    return {k:v for k,v in d.items() if v}


def main():
    census,coarse,flags,native=[json.loads((ROOT/p).read_text(encoding='utf-8')) for p in [CENSUS,COARSE,FLAGS,NATIVE]]
    checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    check('geometry and native readout fixtures pin the live census',coarse['source_sha256'][CENSUS]==flags['source_sha256']==native['sourceSha256'][CENSUS]==sha(CENSUS))
    flag=flags['central_flag_bridges'][0]['ascending_flag']
    engine=GlobalFCCEvolution(census,coarse,flag,tau=1)
    n=len(engine.vertex_ids)
    check('complete microscopic FCC kernel on120 shared vertices',n==120 and len(coarse['coarse_cells'])==175 and all(engine.A[i][j]==engine.A[j][i] for i in range(n) for j in range(n)))
    check('all1807 original annotated cells retained',len(engine.cells)==1807 and engine.payload==census)
    def fcc(p):return (p[0]+p[1],p[0]+p[2],p[1]+p[2])
    prior_kernel=prior_gaussian_action([tuple(fcc(p) for p in c['vertices']) for c in coarse['coarse_cells']],
                                       [fcc(engine.bary[v]) for v in engine.vertex_ids])
    check('assembled kernel exactly reproduces the existing Gaussian action implementation',all(28*prior_kernel[i][j]==engine.A[i][j] for i in range(n) for j in range(n)))
    # Exact integer symmetry, independent of the numerical integrator.
    for p in permutations(range(4)):
        ix=[engine.index[engine.by_point[tuple(engine.bary[v][j] for j in p)]] for v in engine.vertex_ids]
        assert all(engine.A[ix[i]][ix[j]]==engine.A[i][j] for i in range(n) for j in range(n))
    checks.append('FCC kernel is exactly covariant under all24 coordinate permutations')
    for id in engine.cells:
        assert not sums((g,a*b) for f,a in engine.boundary[id] for g,b in engine.boundary[f])
        assert sums((f,engine.rho_sign[id]*a) for f,a in engine.boundary[engine.rho[id]])==sums((engine.rho[f],a*engine.rho_sign[f]) for f,a in engine.boundary[id])
    checks.append('all original triangular and tetrahedral boundaries remain signed-chain natural')
    fixture=native['fixture'];slots=['C0','M0','C1','M1','C2']
    def embedded_packet(packet):
        out=[0j]*n
        for name,z in zip(slots,packet['coefficients']):
            point=tuple(2-int(x) for x in packet['chart']['aliases'][name].split(','))
            out[engine.index[engine.by_point[point]]]=complex(*z)
        return out
    initial=embedded_packet(fixture['packets'][0]);target=embedded_packet(fixture['packets'][-1])
    check('native P and E targets have distinct equal-norm full retained fields',norm(initial)==norm(target)>0 and initial!=target)
    probe=[complex((i%11)-5,(i%7)-3) for i in range(n)]
    moved=engine.linear_step(probe)
    check('full-field Cayley forward inverse roundtrip',distance(engine.linear_step(moved,inverse=True),probe)<1e-10)
    qix=[engine.index[engine.rho[v]] for v in engine.vertex_ids]
    def qfield(v):
        out=[0j]*n
        for i,j in enumerate(qix):out[j]=v[i]
        return out
    check('coefficient update commutes numerically with the whole chart turn',distance(engine.linear_step(qfield(probe)),qfield(moved))<1e-10)
    state=engine.initial(initial);trace=[];events=[];errors=[];residuals=[]
    initial_norm=norm(initial);initial_support={i for i,z in enumerate(initial) if z}
    for tick in range(29):
        views=[engine.presentation(state,b) for b in range(4)]
        for view in views:
            assert engine.restore(view)==tuple(sorted(engine.cells))
            assert engine.restrictions_agree(engine.cell_readouts(state,view['frame']))
        # Field and entire cell/witness payload are shared, not copied as four physical systems.
        assert engine.payload==census
        fidelity=abs(sum(a.conjugate()*b for a,b in zip(target,state['field'])))**2/(norm(target)*norm(state['field']))
        relative_error=distance(state['field'],target)/(norm(target)**0.5)
        trace.append({'tick':tick,'depth':len(engine.cells[state['cursor']]),'frame':state['frame'],
                      'formal_grade':state['formal_grade'],'windows':[v['window'] for v in views],
                      'fiber_counts':[len(v['groups']) for v in views],
                      'field':encode(state['field']),'norm_squared':norm(state['field']),
                      'native_E_fidelity':fidelity,'native_E_relative_error':relative_error,
                      'outside_initial_support_norm_squared':sum(abs(z)**2 for i,z in enumerate(state['field']) if i not in initial_support)})
        errors.append(abs(norm(state['field'])-initial_norm)/initial_norm)
        if tick==28:break
        before=state;state=engine.step(state)
        events.append(state['history'][-1]['action'])
        # The equation actually solved, not just a norm diagnostic.
        left=[z+1j*sum(a*w for a,w in zip(row,state['field']))/56 for z,row in zip(state['field'],engine.A)]
        right=[z-1j*sum(a*w for a,w in zip(row,before['field']))/56 for z,row in zip(before['field'],engine.A)]
        residuals.append(distance(left,right))
        assert distance(engine.linear_step(state['field'],inverse=True),before['field'])<1e-10
    check('all29 whole presentations reconstruct every cell in all four views',len(trace)==29)
    check('shared-face restrictions agree throughout the whole evolution',len(events)==28)
    check('nontrivial dynamics changes values beyond the initial native packet',trace[1]['outside_initial_support_norm_squared']>1e-6 and distance(state['field'],initial)>1e-6)
    check('norm and update-equation numerical residuals remain controlled',max(errors)<1e-11 and max(residuals)<1e-10)
    handoffs=[i+1 for i,event in enumerate(events) if event=='handoff']
    check('flag zipper generates seven visits without a stage-index branch',handoffs==[7,14,21,28] and [r['depth'] for r in trace[:7]]==[1,2,3,4,3,2,1])
    check('one shared controller drives four views and records a formal grade wrap',state['frame']==0 and state['formal_grade']==1 and len(state['history'])==28)
    check('four chart returns do not reset the evolving field or execution history',trace[0]['windows']==trace[28]['windows'] and distance(state['field'],initial)>1e-6)
    # No E label is manufactured from a phase or grade.
    matched=trace[-1]['native_E_relative_error']<1e-9
    # A wrong marked group and a mismatched shared-face value are detectable.
    bad=copy.deepcopy(engine.presentation(state));key=next(iter(bad['groups']));bad['groups'][key].pop()
    try:engine.restore(bad)
    except ValueError:pass
    else:raise AssertionError('dropped row accepted')
    bad=engine.cell_readouts(state);triangle=next(id for id,vs in engine.cells.items() if len(vs)==3)
    v=engine.cells[triangle][0];bad[triangle][v]+=1
    check('hostile isolated face-value edit breaks global compatibility',not engine.restrictions_agree(bad))
    checks.append('hostile dropped row breaks full fibration recovery')
    # Controller dependence on marking is tested separately from the field law.
    saved=engine.flag
    for b in flags['central_flag_bridges']:
        engine.flag=tuple(b['ascending_flag']);s=engine.initial([0j]*n);profile=[]
        while not s['history'] or s['history'][-1]['action']!='handoff':
            profile.append(len(engine.cells[s['cursor']]));s=engine.step(s)
            assert len(profile)<=2*len(engine.flag)
        assert profile==[1,2,3,4,3,2,1]
    engine.flag=saved
    checks.append('the structural controller has the same visit profile on all24 central flags')
    inputs=[CENSUS,COARSE,FLAGS,NATIVE,'research/strominger/checkers/global_fcc_evolution.py',
            'research/strominger/checkers/check_global_fcc_evolution.py',
            'research/strominger/fcc-gaussian-boundary-v1.md','research/strominger/checkers/check_fcc_gaussian_boundary.py','research/nima/table-fibration.md',
            'research/nima/arrow-history-window.md','research/nima/full-esd7-graded-tate-torus-realization.md']
    report={'status':'passed','candidate_outcome':'native E endpoint matched under the declared embedding' if matched else 'rejected as the native28-step P/E exchange under the declared embedding','check_count':len(checks),'checks':checks,'source_sha256':{p:sha(p) for p in inputs},
      'candidate':'U=(I+iK/2)^(-1)(I-iK/2), K=sum_c(I_V(c)/14+L_E(c)/4); field step plus one structural flag-zipper action',
      'assumptions':['native five-slot values embedded at their actual reference vertices; all other initial vertex amplitudes zero',
                     'scalar complex vertex field with counting inner product; Gaussian kernel promoted to a Hamiltonian candidate',
                     'dimensionless Cayley interval tau=1; no tuning to the E target or stage count',
                     'one field update per flag visit; return-view convention uses rho; handoff occurs at exhausted parent stack',
                     'formal grade records four chart wraps; no analytic Fourier or physical suspension is computed'],
      'handoff_ticks':handoffs,'maximum_relative_norm_error':max(errors),'maximum_equation_residual':max(residuals),
      'native_E_match_at28':matched,'native_E_fidelity_at28':trace[-1]['native_E_fidelity'],
      'native_E_relative_error_at28':trace[-1]['native_E_relative_error'],
      'native_E_target':encode(target),'vertex_ids':engine.vertex_ids,'trace':trace,'history':state['history'],
      'disposition':'Executable nontrivial whole-field candidate with retained presentations. Seven visits follow the declared structural controller, not a discovered native clock. Native E comparison is measured independently of the controller.',
      'scope':'Exact integer kernel/symmetry and incidence checks; floating-point complex evolution with residuals. All source annotations retained, but their native analytical transfer equations and 36-component field binding are not asserted. Shared scalar restrictions are the implemented coherence realization. No whole-object physical P/E equivalence or28-stage theorem follows.'}
    dest=ROOT/'research/strominger/results/global-fcc-evolution.json';dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','handoff_ticks','maximum_relative_norm_error','maximum_equation_residual','native_E_match_at28','native_E_fidelity_at28','native_E_relative_error_at28']}))


if __name__=='__main__':main()
