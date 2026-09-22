"""Joint uncertainty through the source-presentation/quotient/history bridge.

Uses the owning interval adapter unchanged. Retains shared parameters and the
full incoming evidence; history admission is explicit and conditional.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
import importlib.util,json
ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


g=load('interval_adapter',ROOT.parent/'grothendieck/certificates/reconstruct_uncertain_forgotten_slice.py')
t=load('matrix_tools',ROOT/'checkers/check_residual_tower_of_towers.py');a=t.a
p=load('source_presentations',ROOT/'checkers/check_opposite_source_presentations.py')
mm,mv,eye=t.mm,a.apply,t.eye

def wire_matrix(M):return [[str(x) for x in row] for row in M]
def diagonal(v):return [[x if i==j else Q(0) for j in range(len(v))] for i,x in enumerate(v)]
def plus(u,v):return [x+y for x,y in zip(u,v)]
def transpose(M):return list(map(list,zip(*M)))


def polygon(constraints):
    """Exact vertices of a bounded closed 2D polytope, including segments/points.

    Here the input ALWAYS includes finite lower/upper bounds on both variables.
    Empty results therefore certify emptiness, not an unbounded feasible set.
    """
    points=set()
    for (u,b),(v,c) in combinations(constraints,2):
        det=u[0]*v[1]-u[1]*v[0]
        if not det:continue
        point=((b*v[1]-u[1]*c)/det,(u[0]*c-b*v[0])/det)
        if all(a.dot(row,point)<=bound for row,bound in constraints):points.add(point)
    return sorted(points)


def inequalities(rows,intervals):
    return [(list(row),hi) for row,(lo,hi) in zip(rows,intervals)]+[([-x for x in row],-lo) for row,(lo,hi) in zip(rows,intervals)]


def build(payload,initial_interval,history_admission):
    bundle=g.reconstruct(payload);model=bundle['model'];A=payload['background']
    D=[[Q(x) for x in row] for row in model['inverse_matrix']]
    R=[[Q(x) for x in row] for row in model['forward_matrix']]
    Z=[[Q(x) for x in row] for row in model['interaction_matrix']]
    X=transpose([a.inverse(v) for v in a.basis(8)])
    assert mm(X,Z)==eye(8)
    intervals=[g.box(payload['readings'][name]) for name in g.IDS]
    c=[(lo+hi)/2 for lo,hi in intervals];r=[(hi-lo)/2 for lo,hi in intervals];G=diagonal(r)
    ac=mv(D,c);AG=mm(D,G);mc=mv(Z,ac);MG=mm(Z,AG)
    assert mv(X,mc)==ac and mm(X,MG)==AG
    assert list(map(Q,bundle['compatible_set']['center']))==ac
    assert [[Q(x) for x in row] for row in bundle['compatible_set']['generators']]==AG
    P=eye(7)[:2]
    residual=[[Q(x) for x in row] for row in ((0,0,1,0,0,0,0),(-1,-1,0,1,0,0,0),
                                             (0,0,0,0,1,0,0),(1,1,0,0,0,1,0),(0,0,0,0,0,0,1))]
    section=[[Q(x) for x in row] for row in ((1,0),(0,1),(0,0),(1,1),(0,0),(-1,-1),(0,0))]
    N=[[Q(i==j+2) for j in range(5)] for i in range(7)]
    joint=P+residual;inverse=[s+n for s,n in zip(section,N)]
    assert mm(inverse,joint)==mm(joint,inverse)==eye(7)
    jc=mv(joint,c);JG=mm(joint,G)
    assert mv(inverse,jc)==c and mm(inverse,JG)==G
    # Same epsilon labels on visible and residual generators: do NOT split the box.
    assert mv(D,mv(inverse,jc))==ac and mm(D,mm(inverse,JG))==AG
    affine_ast_checks=0
    for av,mv0 in zip([ac]+transpose(AG),[mc]+transpose(MG)):
        factored=p.expression(mv0,3,0,'H');expanded=p.expression(av,3,0,'Q')
        assert p.expand(factored)==p.expand(expanded)==a.paths(av,0,3)
        affine_ast_checks+=1
    vertex_checks=0
    for eps in product((Q(-1),Q(1)),repeat=7):
        y=plus(c,mv(G,eps));source=plus(ac,mv(AG,eps));mom=plus(mc,mv(MG,eps))
        assert mv(R,source)==y and mv(X,mom)==source
        v=plus(jc,mv(JG,eps));assert mv(inverse,v)==y
        vertex_checks+=1
    marginal_failure=False
    if r[0]+r[1]>0:
        fake=[center+sum(map(abs,row)) for center,row in zip(jc,JG)]
        fake_y=mv(inverse,fake)
        assert any(not lo<=value<=hi for value,(lo,hi) in zip(fake_y,intervals))
        marginal_failure=True
    if any(r):
        source_upper=[center+sum(map(abs,row)) for center,row in zip(ac,AG)]
        assert sum(source_upper)>0 # All actual source points have sum zero.
    H=[Q(1),Q(-1)];T10=a.action(H,1);append=a.action(H,2);T=mm(append,T10)
    J=mm(R,T);assert J==[list(row) for row in zip(*([Q(1),Q(0)]+[Q(0)]*5,[Q(0),Q(1)]+[Q(0)]*5))]
    for v in a.basis(2):
        assert a.paths(mv(T,v),0,3)==a.f['multiply'](a.f['multiply'](a.paths(v,0,1),a.paths(H,1,1)),a.paths(H,2,1))
    model_history={'background':A,'reading_model_sha256':payload['model_sha256'],
        'stages':[[A,6*A],[A,210*A],[A,30030*A]],
        'dynamics':'append P-Q in the second block, then P-Q in the third block',
        'T10':wire_matrix(T10),'final_source_from_initial_pair':wire_matrix(T),
        'support_and_dynamics':'external assumptions, not authenticated by this digest'}
    history_digest=g.digest(model_history)
    if history_admission is None:raise ValueError('history requires independent explicit admission')
    if history_admission!=history_digest:raise ValueError('history contract mismatch')
    prior=g.box(initial_interval)
    # Source intersection route: D(c+G eps)=T q. Reading pullback route: c+G eps=J q.
    # They have exactly the SAME parameter domain, not independently boxed marginals.
    source_equations=[row+[-x for x in tail] for row,tail in zip(AG,T)]
    reading_equations=[row+[-x for x in tail] for row,tail in zip(G,J)]
    first=a.solve(source_equations,[-x for x in ac],9)
    second=a.solve(reading_equations,[-x for x in c],9)
    assert a.canonical(first,9)==a.canonical(second,9)
    # Eliminate epsilon exactly. The bounded history polygon includes ALL seven
    # final reading intervals, including rows forced to zero by these dynamics.
    constraints=inequalities(J,intervals)+inequalities([[Q(1),Q(1)]],[prior])
    points=polygon(constraints)
    via_modes=mm(R,mm(X,mm(Z,T)))
    assert via_modes==J and polygon(inequalities(via_modes,intervals)+inequalities([[1,1]],[prior]))==points
    L=eye(2)+T10+T[1:] # correlated 13-coordinate histories, as in the exact prototype
    for q in points:
        y=mv(J,q)
        eps=[(v-mid)/rad if rad else Q(0) for v,mid,rad in zip(y,c,r)]
        assert all(-1<=e<=1 for e in eps)
        assert plus(c,mv(G,eps))==y
        assert plus(ac,mv(AG,eps))==mv(T,q)
        history=mv(L,q);assert history[:2]==list(q) and history[2:6]==mv(T10,q)
    filtration={}
    for order in range(1,5):
        if not points:filtration[str(order)]='empty_history';continue
        rows=[row for index,row in enumerate(mm(Z,T)) if index.bit_count()<order]
        bounds=[(min(a.dot(row,q) for q in points),max(a.dot(row,q) for q in points)) for row in rows]
        filtration[str(order)]=('guaranteed' if all(lo==hi==0 for lo,hi in bounds) else
                                'ruled_out_by_a_coordinate' if any(not lo<=0<=hi for lo,hi in bounds) else 'undetermined')
    result={'schema':'joint-uncertain-presentation-history-bridge-v1',
        'retained_interval_adapter_output':bundle,
        'retained_earlier_evidence':{'stage':0,'corner':[A,6*A],'row':'initial_terminal',
                                    'interval':initial_interval,'status':'synthetic exact rational bounds, externally assumed'},
        'history_model':model_history,'history_model_sha256':history_digest,
        'parameter_labels':list(g.IDS),'shared_parameter_domain':'epsilon in [-1,1]^7, not a statistical independence assertion',
        'interaction_set':{'center':list(map(str,mc)),'generators':wire_matrix(MG)},
        'joint_visible_residual_set':{'section':'pair12-and-top-filtered-linear-section-v1',
             'row_order':list(g.IDS[:2])+['r'+str(i) for i in range(5)],
             'center':list(map(str,jc)),'generators':wire_matrix(JG),
             'inverse_to_seven_readings':wire_matrix(inverse)},
        'joint_history_domain':{'variables':['epsilon_'+name for name in g.IDS]+['initial_P','initial_Q'],
             'source_intersection_equations':wire_matrix(source_equations),'source_rhs':list(map(str,[-x for x in ac])),
             'reading_pullback_equations':wire_matrix(reading_equations),'reading_rhs':list(map(str,[-x for x in c])),
             'additional_constraints':'all epsilon in [-1,1]; initial_P+initial_Q in the retained earlier interval'},
        'history_pair_constraints':[{'row':list(map(str,row)),'upper':str(bound)} for row,bound in constraints],
        'history_pair_vertices':[list(map(str,q)) for q in points],
        'full_history_map':wire_matrix(L),'full_history_vertices':[list(map(str,mv(L,q))) for q in points],
        'history_status':'compatible' if points else 'empty',
        'history_filtration_certificates':filtration,
        'audit':{'affine_ast_coefficient_checks':affine_ast_checks,'joint_box_vertex_checks':vertex_checks,
                 'parameter_equation_spaces_equal':True,'separate_marginals_failure_exhibited':marginal_failure},
        'scope':'Conditional joint inverse within the declared forgotten source support and prescribed deterministic history. No physical acquisition, support proof, stochastic model, uncertain dynamics or source-bimodule splitting.'}
    assert g.recover(bundle)==payload
    return result


def admitted_digest(payload):
    # Admission supplied by this synthetic test driver, never inferred by build().
    A=payload['background'];H=[Q(1),Q(-1)];T10=a.action(H,1);T=mm(a.action(H,2),T10)
    return g.digest({'background':A,'reading_model_sha256':payload['model_sha256'],
        'stages':[[A,6*A],[A,210*A],[A,30030*A]],
        'dynamics':'append P-Q in the second block, then P-Q in the third block',
        'T10':wire_matrix(T10),'final_source_from_initial_pair':wire_matrix(T),
        'support_and_dynamics':'external assumptions, not authenticated by this digest'})


def recover(output):
    payload=g.recover(output['retained_interval_adapter_output'])
    prior=output['retained_earlier_evidence']['interval']
    recomputed=build(payload,prior,output['history_model_sha256'])
    if g.digest(recomputed)!=g.digest(output):raise ValueError('changed evidence, correlations or derived history')
    return {'final_interval_evidence':payload,'earlier_evidence':output['retained_earlier_evidence']}


def main():
    cases=[('cubic_history',[Q(1),Q(-1)]+[Q(0)]*5,[Q(1,100)]*7,['0','0']),
           ('correlated_strip',[Q(3,5),Q(2,5),Q(1,20),Q(-1,30),Q(0),Q(1,40),Q(0)],
            [Q(1,5),Q(1,5)]+[Q(1,10)]*5,['1','1']),
           ('history_polygon',[Q(3,5),Q(2,5)]+[Q(0)]*5,[Q(1,5),Q(1,5)]+[Q(1,10)]*5,['9/10','11/10']),
           ('impossible_final_row',[Q(3,5),Q(2,5),Q(1)]+[Q(0)]*4,[Q(1,10)]*7,['1','1']),
           ('contradictory_past',[Q(3,5),Q(2,5)]+[Q(0)]*5,[Q(1,10)]*7,['2','2']),
           ('exact_history',[Q(1)]+[Q(0)]*6,[Q(0)]*7,['1','1'])]
    results=[];example=None
    for A in (2,3,4):
        for name,c,r,prior in cases:
            payload={'schema':'labelled-forgotten-ideal-interval-readings-v1','background':A,
                     'model_sha256':g.digest(g.model(A)),
                     'readings':{key:[str(mid-rad),str(mid+rad)] for key,mid,rad in zip(g.IDS,c,r)},
                     'terminal_check':['0','0'],
                     'provenance':{'kind':'synthetic','support_evidence':None,'error_contract':None}}
            frozen=json.dumps(payload,sort_keys=True)
            out=build(payload,prior,admitted_digest(payload))
            assert json.dumps(payload,sort_keys=True)==frozen
            assert recover(json.loads(json.dumps(out)))['final_interval_evidence']==payload
            if name in ('impossible_final_row','contradictory_past'):assert out['history_status']=='empty'
            else:assert out['history_status']=='compatible' and out['history_filtration_certificates']['2']=='guaranteed'
            if name=='cubic_history':assert out['history_filtration_certificates']['3']=='guaranteed'
            if name=='history_polygon':assert len(out['history_pair_vertices'])==6
            if name=='correlated_strip':
                points=[list(map(Q,q)) for q in out['history_pair_vertices']]
                fake=[max(q[j] for q in points) for j in range(2)]
                assert sum(fake)!=1 # Marginal histories cannot replace the joint strip.
                assert c[2]!=0 and payload['readings'][g.IDS[2]][0].startswith('-')
                example=out
            results.append({'background':A,'case':name,'history_status':out['history_status'],
                            'vertices':len(out['history_pair_vertices']),**out['audit']})
    rejected=[]
    for kind in ('shared_generator','historical_interval','derived_vertex','model_background'):
        bad=json.loads(json.dumps(example))
        if kind=='shared_generator':bad['joint_visible_residual_set']['generators'][0][0]='123'
        elif kind=='historical_interval':bad['retained_earlier_evidence']['interval']=['0','0']
        elif kind=='derived_vertex':bad['history_pair_vertices'][0][0]='123'
        else:bad['history_model']['background']=2
        try:recover(bad)
        except ValueError:rejected.append(kind)
        else:raise AssertionError('corrupt joint bundle accepted')
    try:build(example['retained_interval_adapter_output']['retained_input'],['1','1'],None)
    except ValueError:rejected.append('unadmitted_history')
    else:raise AssertionError('history silently imposed')
    directory=ROOT/'results/uncertain-presentation-history';directory.mkdir(exist_ok=True)
    (directory/'joint-history-example.json').write_text(json.dumps(example,indent=2)+'\n',encoding='utf-8')
    report={'schema':'joint-uncertain-presentation-history-tests-v1','passed':True,'cases':results,
        'joint_box_vertex_checks':sum(r['joint_box_vertex_checks'] for r in results),
        'affine_ast_coefficient_checks':sum(r['affine_ast_coefficient_checks'] for r in results),
        'negative_controls_rejected':rejected,
        'scope':'Finite exact rational joint sets for synthetic boxes at A=2,3,4 and the separately admitted append-P-Q-twice history. No uncertain dynamics or physical acquisition certificate.'}
    (directory/'tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
