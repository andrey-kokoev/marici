"""Candidate two-route audit of retained binary ancestry, not a physical law.
Each square uses the existing Bool-factor flips; the second receipt validates
and references the first receipt and the same child records.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def route(word):
    state = [0,0]
    states = [state[:]]
    for move in word:
        state['LR'.index(move)] ^= 1
        states.append(state[:])
    return {'word':word, 'states':states}


def build(depth, address='root'):
    if depth == 0:
        return {'kind':'leaf','address':address,'occurrence':address}
    children = [build(depth-1,address+'/0'),build(depth-1,address+'/1')]
    refs = [digest(c) for c in children]
    first = {'children':refs, 'route':route('LR')}
    second = {'children':refs, 'route':route('RL'), 'first_receipt':digest(first)}
    return {'kind':'comparison','address':address,'children':children,'first':first,'second':second}


def validate(node):
    if node['kind']=='leaf':
        assert node['occurrence']==node['address']
        return
    assert node['kind']=='comparison'
    assert len(node['children'])==2
    for i,child in enumerate(node['children']):
        assert child['address']==node['address']+'/'+str(i)
        validate(child)
    refs = [digest(c) for c in node['children']]
    a,b = node['first'],node['second']
    assert a['children']==b['children']==refs
    assert a['route']==route('LR') and b['route']==route('RL')
    assert a['route']['states'][-1]==b['route']['states'][-1]==[1,1]
    assert b['first_receipt']==digest(a)


def schedule(node):
    if node['kind']=='leaf':
        return []
    out = [event for c in node['children'] for event in schedule(c)]
    for observation,receipt in [('first',node['first']),('second',node['second'])]:
        for index,move in enumerate(receipt['route']['word']):
            out.append({'node':node['address'],'observation':observation,'local_step':index+1,'move':move})
    return out


def metrics(node):
    if node['kind']=='leaf':
        return {'leaves':1,'comparisons':0,'work':0,'span_sequential_observations':0,'span_parallel_routes':0}
    a,b = [metrics(c) for c in node['children']]
    return {'leaves':a['leaves']+b['leaves'],'comparisons':a['comparisons']+b['comparisons']+1,
            'work':a['work']+b['work']+4,
            'span_sequential_observations':max(a['span_sequential_observations'],b['span_sequential_observations'])+4,
            'span_parallel_routes':max(a['span_parallel_routes'],b['span_parallel_routes'])+2}


def main():
    checks=[]
    def check(name,condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    def reject(name,mutate):
        node=deepcopy(tree);mutate(node)
        try: validate(node)
        except (AssertionError,KeyError): checks.append(name);return
        raise AssertionError('accepted corruption: '+name)
    tree=build(3);validate(tree)
    checks.append('complete nested two-route certificate validates')
    m=metrics(tree);events=schedule(tree)
    check('four-level ancestry has eight leaves and seven comparison nodes',m['leaves']==8 and m['comparisons']==7)
    check('serial primitive audit work is twenty-eight',m['work']==len(events)==28)
    check('causally sequential observations need twelve parallel rounds',m['span_sequential_observations']==12)
    check('concurrent route computation needs six move rounds excluding comparison cost',m['span_parallel_routes']==6)
    check('two routes have same endpoint but distinct intermediate states',route('LR')['states'][-1]==route('RL')['states'][-1] and route('LR')['states'][1]!=route('RL')['states'][1])
    # Serial execution validates children before a parent, first receipt before second.
    completed=set()
    for event in events:
        node=event['node'];obs=event['observation']
        if obs=='second': assert (node,'first') in completed
        if event['local_step']==2: completed.add((node,obs))
    check('every second observation follows its first',len(completed)==14)
    reject('duplicating the same observation route is rejected',lambda n:n['second'].__setitem__('route',deepcopy(n['first']['route'])))
    reject('wrong route endpoint is rejected',lambda n:n['second'].__setitem__('route',route('RR')))
    def fake_middle(n): n['second']['route']['states'][1]=[1,0]
    reject('same endpoint with false intermediate history is rejected',fake_middle)
    reject('detached second receipt is rejected',lambda n:n['second'].__setitem__('first_receipt','unrelated'))
    reject('equal-shaped replacement child is rejected',lambda n:n['children'].__setitem__(0,build(2,'different-root')))
    def corrupt_descendant(n): n['children'][0]['second']['route']['states'][1]=[1,0]
    reject('root endpoint agreement cannot hide a failed descendant',corrupt_descendant)
    reject('missing child record is rejected',lambda n:n['children'].pop())
    flip=lambda s:s^1
    swap=lambda s:((s&1)<<1)|((s&2)>>1)
    check('hostile comparison still uses two involutions',all(flip(flip(s))==s and swap(swap(s))==s for s in range(4)))
    check('two observations do not manufacture commutation',any(swap(flip(s))!=flip(swap(s)) for s in range(4)))
    census=[]
    for depth in range(5):
        t=build(depth);validate(t);m_d=metrics(t)
        assert m_d['work']==4*(2**depth-1)
        assert m_d['span_sequential_observations']==4*depth
        census.append({'branch_depth':depth,**m_d})
    checks.append('depth census follows structural work and span recurrences')
    inputs=['research/nima/nested-electron-roles.md','research/nima/nested-active-comparison.md',
            'research/nima/native-square-controlled-hamiltonian.md','research/nima/paw-half-turn-promotion.md',
            'research/strominger/checkers/check_nested_double_observation.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'certificate':tree,'serialized_events':events,'metrics':m,'depth_census':census,
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'assumptions':['one Bool square per internal binary node','both LR and RL routes required','second receipt validates first receipt and child ancestry','children complete before parent','unit cost per flip; comparison/hash costs not counted'],
            'disposition':'Twenty-eight is serial audit work for this candidate, not forced parallel depth or a proved P/E exchange. Double observation means two-route consistency here, not physical reality.',
            'scope':'Declared finite nested certificate. Hashes are implementation integrity checks, not coherence morphisms or physical observables. Both routes use the same supplied commuting operators; agreement is not independent empirical corroboration. No global sector/window binding or geometric assembly.'}
    dest=ROOT/'research/strominger/results/nested-double-observation.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'metrics':m,'result':str(dest)}))


if __name__=='__main__':main()
