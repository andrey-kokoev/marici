"""Realize the saved mixed history as constraints on one labelled source.

Uses the independent numerical history verifier, never a solver or producer.
The finite columns include two distinct tail endpoints; the final column
pattern extends to every A>=5, with monotone moment weights.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
vp=ROOT/'research/nima/certificates/verify_refinement_history.py'
spec=importlib.util.spec_from_file_location('numerical_history',vp)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
path=ROOT/'research/nima/results/mixed-refinement-history.json'
bundle=h.v.strict_load(path);report=h.verify_history(bundle)
nodes={n['id']:n for n in bundle['nodes']}
assert set(nodes)==set('RABCFDE')
# Columns are ACTUAL distinct labelled source directions, not a tail module:
# retained v0 at A=2; forgotten k2,k3,k4,k5,k6.
labels=['v0@2','k@2','k@3','k@4','k@5','k@6']
weights=[F(32)]+[8*F(A,2)**12 for A in range(2,7)]
specs={'R':(1,[[0],[1],[2,3,4,5]],3),
 'B':(2,[[0],[1],[2,3,4,5]],3),
 'A':(1,[[0],[1],[2],[3,4,5]],4),
 'C':(2,[[0],[1],[2],[3,4,5]],4),
 'F':(1,[[0],[1],[2],[3],[4,5]],5),
 'D':(2,[[0],[1],[2],[3],[4,5]],5),
 'E':(1,[[0],[1],[2],[3],[4,5]],5)}
def mat(g,groups):return tuple(tuple(F(g)*int(j in group) for j in range(6)) for group in groups)
def mm(a,b):return tuple(tuple(sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)) for row in a)
def enc(a):return [[str(v) for v in row] for row in a]
def require(ok,msg):
    if not ok:raise ValueError(msg)
# Reconstruct marked path products, including the 32-term retained source.
def source_column(kinds):
    factors=[]
    for pair,kind in zip(((2,3),(5,7),(11,13)),kinds):
        terms=[]
        for order,sign in ((pair,1),(pair[::-1],-1)):
            for marks in (((0,0),) if kind==0 else ((1,0),(0,1))):terms.append((order,marks,sign))
        factors.append(terms)
    return [(sum((x[0] for x in terms),()),sum((x[1] for x in terms),()),
             terms[0][2]*terms[1][2]*terms[2][2]) for terms in product(*factors)]
def row_value(A,B,col,kinds):
    if A!=B:return 0
    wanted=((B,2*B,kinds[0]),(6*B,30*B,kinds[1]),(210*B,2310*B,kinds[2]))
    result=0
    for word,marks,c in col:
        states=[A]
        for p in word:states.append(states[-1]*p)
        assert states[-1]==30030*A
        for cuts in combinations(range(6),3):
            if any(mark and j not in cuts for j,mark in enumerate(marks)):continue
            if tuple((states[j],states[j+1],marks[j]) for j in cuts)==wanted:result+=c
    return result
vac=source_column((0,0,0));ret=source_column((1,1,0))
assert len(vac)==8 and len(ret)==32
assert len({(w,m) for w,m,c in ret})==32
assert row_value(2,2,ret,(1,1,0))==1 and row_value(2,2,ret,(0,0,0))==0
for A in range(2,7):
    assert row_value(A,2,vac,(1,1,0))==0
    assert [row_value(A,B,vac,(0,0,0)) for B in range(2,7)]==[int(A==B) for B in range(2,7)]
charts={};roles={}
for name,(gain,groups,tail_start) in specs.items():
    p=nodes[name]['problem'];assert F(p['budget'])==40 and F(p['target']['threshold'])==0
    assert len(p['rows'])==len(groups)
    C=mat(gain,groups);charts[name]=C
    for j,(group,row) in enumerate(zip(groups,p['rows'])):
        assert F(row['weight'])*gain==min(weights[k] for k in group)
        assert F(p['target']['coefficients'][j])*gain==int(j!=0)
        if j:assert row['calibration']==['1','1']
    last=p['rows'][-1]
    assert list(map(F,last['data']))==[-F(40)/F(last['weight']),F(40)/F(last['weight'])]
    roles[name]=['acquired-retained-reading']+['acquired-vacuum-reading']*(len(groups)-2)+['prior-bounded-unacquired-tail']
    # Every A>=5 is still distinct in the source. Its chart column has this
    # same last-row pattern, and w_A>=w_5; no endpoint identification follows.
    assert all(row[4]==row[5] for row in C)
# Observation maps are polynomial matrices Z(E)=Z0+E*Z1. E is the SAME
# actual retained response at every node; vacuum rows have unit calibration.
def observation_parts(C):
    return (tuple(tuple(x if j!=0 else F(0) for j,x in enumerate(row)) for row in C),
            tuple(tuple(x if j==0 else F(0) for j,x in enumerate(row)) for row in C))
edge_checks=[];parents={key:set() for key in nodes}
for edge in bundle['edges']:
    a,b=edge['from'],edge['to'];parents[b].add(a)
    S,O,g=h.maps(nodes[a]['problem'],nodes[b]['problem'],edge['certificate'])
    require(mm(S,charts[b])==charts[a],'source chart does not commute')
    for old,new in zip(observation_parts(charts[a]),observation_parts(charts[b])):
        require(mm(O,new)==old,'observation chart does not commute for the fixed actual E')
    ta=(tuple(map(F,nodes[a]['problem']['target']['coefficients'])),)
    tb=(tuple(map(F,nodes[b]['problem']['target']['coefficients'])),)
    require(mm(tb,charts[b])==tuple(tuple(g*x for x in row) for row in mm(ta,charts[a])),'target chart')
    edge_checks.append({'from':a,'to':b,'same_source_evaluation':True,'symbolic_fixed_E_observation':True})
# Projection cost never exceeds the actual labelled-source cost. Equality
# holds for the finite section placing each tail at its first allowed A.
for name,C in charts.items():
    w=list(map(lambda r:F(r['weight']),nodes[name]['problem']['rows']))
    for k in range(6):assert sum(wj*abs(row[k]) for wj,row in zip(w,C))<=weights[k]

def ancestors(key):
    out=set(parents[key])
    for p in parents[key]:out.update(ancestors(p))
    return out

def lift(name,values):
    gain,groups,_=specs[name];out=[[F(0)] for _ in range(6)]
    for group,value in zip(groups,values):out[min(group)][0]=F(value)/gain
    source=tuple(tuple(r) for r in out)
    assert mm(charts[name],source)==tuple((F(x),) for x in values)
    source_cost=sum(w*abs(x[0]) for w,x in zip(weights,source))
    numerical_cost=sum(F(row['weight'])*abs(F(x)) for row,x in zip(nodes[name]['problem']['rows'],values))
    assert source_cost==numerical_cost<=40
    return source

def feasible(name,source,E_interval):
    p=nodes[name]['problem'];u=mm(charts[name],source)
    assert sum(w*abs(x[0]) for w,x in zip(weights,source))<=F(p['budget'])
    lo,hi=map(F,p['rows'][0]['calibration'])
    assert lo<=E_interval[0]<=E_interval[1]<=hi
    for j,(row,coef) in enumerate(zip(p['rows'],u)):
        dlo,dhi=map(F,row['data'])
        for E in E_interval:
            value=coef[0]*(E if j==0 else 1)
            assert dlo<=value<=dhi

witnesses=[];pullbacks=0
for name in nodes:
    cert=nodes[name]['certificate'];assert cert['version']==1
    E_interval=tuple(map(F,nodes[name]['problem']['rows'][0]['calibration']))
    for kind in ('witness','false_witness','true_witness'):
        if kind not in cert:continue
        src=lift(name,cert[kind]);feasible(name,src,E_interval)
        for old in ancestors(name):feasible(old,src,E_interval);pullbacks+=1
        witnesses.append({'node':name,'kind':kind,'finite_source_coefficients':enc(src),
                          'ancestor_nodes':sorted(ancestors(name))})
# These are literally identical canonical terminal constraints, not just
# targets of the same sign. D has the same constraints in units twice as large.
assert nodes['F']['problem']==nodes['E']['problem']
assert charts['F']==charts['E']
assert tuple(tuple(x/2 for x in row) for row in charts['D'])==charts['F']
for gained,canonical in zip(nodes['D']['problem']['rows'],nodes['F']['problem']['rows']):
    assert [F(x)/2 for x in gained['data']]==list(map(F,canonical['data']))
    assert gained['calibration']==canonical['calibration']
    assert 2*F(gained['weight'])==F(canonical['weight'])
assert [2*F(x) for x in nodes['D']['problem']['target']['coefficients']]==list(map(F,nodes['F']['problem']['target']['coefficients']))
# A concrete missing-label corruption violates the endpoint-resolved square.
bad=[list(row) for row in charts['F']];bad[-1][-1]=0
edge=next(e for e in bundle['edges'] if e['from']=='A' and e['to']=='F')
S,O,g=h.maps(nodes['A']['problem'],nodes['F']['problem'],edge['certificate'])
assert mm(S,tuple(map(tuple,bad)))!=charts['A']
result={'passed':True,'history_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'nodes':report['nodes'],'edges':report['edges'],'alternative_route_comparisons':report['alternative_route_comparisons'],
 'endpoint_resolved_columns':labels,'source_chart_matrices':{k:enc(c) for k,c in charts.items()},
 'tail_column_rule':'For each distinct A>=5 use the k@5 chart column; retain its actual endpoint (A,30030*A) and actual weight 8*(A/2)^12.',
 'row_roles':roles,'edge_checks':edge_checks,'finite_witness_lifts':witnesses,
 'ancestor_feasibility_checks':pullbacks,'missing_endpoint_corruption_rejected':True,
 'scope':'Same-source evaluation and constraint pullback, not equivariance of scalar aggregation or transport of a filtered extension. Actual retained calibration and acquisition remain external inputs.'}
(ROOT/'research/voevodsky/results/endpoint-resolved-mixed-history.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','nodes','edges','alternative_route_comparisons','ancestor_feasibility_checks','scope')},indent=2))
