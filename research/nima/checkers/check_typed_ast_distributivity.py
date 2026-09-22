"""Explicit typed AST rewrites and bounded exhaustive distributivity diamonds.

Checks rewrite steps, not merely hand-written expressions with equal values.
No claim of unrestricted rewrite-system confluence or inversion without traces.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
from fractions import Fraction as Q
import importlib.util,json,random
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('presentations',ROOT/'checkers/check_opposite_source_presentations.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


def nodes(x,address=()):
    yield address,x
    if x[0]=='scale':yield from nodes(x[2],address+(2,))
    elif x[0]=='product':
        yield from nodes(x[1],address+(1,));yield from nodes(x[2],address+(2,))
    elif x[0]=='sum':
        for i,y in enumerate(x[1]):yield from nodes(y,address+(1,i))


def at(x,address):
    for i in address:x=x[i]
    return x


def replace(x,address,value):
    if not address:return value
    out=list(x);out[address[0]]=replace(out[address[0]],address[1:],value)
    return tuple(out)


def local_rules(x):
    kind=x[0]
    if kind=='product':
        left,right=x[1:]
        if left[0]=='sum':yield 'distribute_left',p.plus(*(p.times(y,right) for y in left[1]))
        if right[0]=='sum':yield 'distribute_right',p.plus(*(p.times(left,y) for y in right[1]))
        if left[0]=='product':yield 'associate_right',p.times(left[1],p.times(left[2],right))
        if left[0]=='scale':yield 'extract_left_scale',p.scale(left[1],p.times(left[2],right))
        if right[0]=='scale':yield 'extract_right_scale',p.scale(right[1],p.times(left,right[2]))
    if kind=='sum':
        if any(y[0]=='sum' for y in x[1]):
            yield 'flatten_sum',p.plus(*(z for y in x[1] for z in (y[1] if y[0]=='sum' else (y,))))
    if kind=='scale':
        child=x[2]
        if child[0]=='sum':yield 'distribute_scale',p.plus(*(p.scale(x[1],y) for y in child[1]))
        if child[0]=='scale':yield 'multiply_scales',p.scale(Q(x[1])*Q(child[1]),child[2])


@lru_cache(None)
def value(x):return p.expand(x)
@lru_cache(None)
def interactions(x):return tuple(p.interaction_eval(x))


def successors(x):
    for address,subtree in nodes(x):
        for rule,replacement in local_rules(subtree):
            y=replace(x,address,replacement)
            if y!=x:yield (rule,address),y


def verify_step(before,after,rule,address):
    p.span(before);p.span(after)
    permitted=[replace(before,address,y) for name,y in local_rules(at(before,address)) if name==rule]
    if after not in permitted:raise ValueError('not the declared local rewrite')
    if p.span(before)!=p.span(after):raise ValueError('changed corners')
    if value(before)!=value(after) or interactions(before)!=interactions(after):raise ValueError('changed source')


def formal_normal_form(x):
    """Terminal AST only: collect coefficients of ORDERED labelled monomials.

    This does not evaluate H=Q-P, so it cannot hide an invalid distributivity
    route behind an accidental source identity.
    """
    if list(successors(x)):raise ValueError('not rewrite-normal')
    result={}
    def monomial(y):
        if y[0] in ('P','Q','H'):return (y,)
        if y[0]=='product':return monomial(y[1])+monomial(y[2])
        raise ValueError('nonmonomial')
    for term in x[1] if x[0]=='sum' else (x,):
        coefficient=Q(1)
        if term[0]=='scale':coefficient=Q(term[1]);term=term[2]
        word=monomial(term);result[word]=result.get(word,Q(0))+coefficient
    return tuple(sorted((word,str(c)) for word,c in result.items() if c))


def explore(root,limit=30000):
    queue=deque([root]);parent={root:None};edges=0;terminals=[]
    while queue:
        x=queue.popleft();out=list(successors(x))
        if not out:terminals.append(x)
        for (rule,address),y in out:
            verify_step(x,y,rule,address);edges+=1
            if y not in parent:
                if len(parent)>=limit:raise RuntimeError('state cap reached; no completeness claim permitted')
                parent[y]=(x,rule,address);queue.append(y)
    assert terminals
    forms={formal_normal_form(x) for x in terminals}
    assert len(forms)==1
    trace=[];cursor=terminals[0]
    while parent[cursor] is not None:
        before,rule,address=parent[cursor]
        trace.append({'rule':rule,'address':address,'before':before,'after':cursor});cursor=before
    trace.reverse()
    return {'states':len(parent),'edges':edges,'terminal_asts':len(terminals),
            'formal_normal_forms':len(forms),'complete_reachable_graph':True},trace


def scheduled_route(root,seed):
    rng=random.Random(seed);cursor=root;trace=[]
    for _ in range(2000):
        candidates=list(successors(cursor))
        if not candidates:return trace
        (rule,address),nxt=rng.choice(candidates)
        verify_step(cursor,nxt,rule,address)
        trace.append({'rule':rule,'address':address,'before':cursor,'after':nxt})
        cursor=nxt
    raise RuntimeError('rewrite schedule did not finish within its declared bound')


def freeze(x):return tuple(map(freeze,x)) if isinstance(x,list) else x


def main():
    x=p.plus(p.leaf('P',0),p.leaf('Q',0))
    y=p.plus(p.leaf('P',1),p.leaf('H',1))
    z=p.plus(p.leaf('Q',2),p.leaf('H',2))
    cases={'left_right_distributivity':p.times(x,y),
           'associativity_distributivity':p.times(p.times(x,y),p.leaf('H',2)),
           'signed_rational_scalars':p.times(p.scale(Q(-2,3),x),p.scale(Q(3,5),y)),
           'cancellation':p.times(p.plus(p.leaf('P',0),p.scale(-1,p.leaf('P',0))),y)}
    audits={};traces={};jet_checks=0;routes=[]
    for name,root in cases.items():
        audit,trace=explore(root);audits[name]=audit
        routes.append((name,root,trace))
    # The unrestricted three-sum traversal exceeded the 30,000-state cap.
    # Do not relabel a bounded traversal as an exhaustive confluence check.
    three=p.times(p.times(x,y),z)
    schedules=[scheduled_route(three,seed) for seed in range(32)]
    assert len({formal_normal_form(route[-1]['after']) for route in schedules})==1
    audits['three_sum_product']={'complete_reachable_graph':False,'completed_seeded_schedules':32,
        'seeds':list(range(32)),'checked_steps':sum(map(len,schedules)),
        'formal_normal_forms':1,'reason':'bounded schedules only; full traversal exceeded the 30000-state cap'}
    routes.extend(('three_sum_schedule_'+str(seed),three,trace) for seed,trace in enumerate(schedules))
    for name,root,trace in routes:
        received=json.loads(json.dumps(trace))
        for step in received:
            verify_step(freeze(step['before']),freeze(step['after']),step['rule'],tuple(step['address']))
        # A trace can replay backwards to the original syntax; normal form alone cannot.
        cursor=freeze(received[-1]['after'])
        for step in reversed(received):
            assert cursor==freeze(step['after']);cursor=freeze(step['before'])
        assert cursor==root
        offset,end=p.span(root);start_mask=(1<<(2*offset))-1;end_mask=(1<<(2*end))-1
        for step in trace:
            for r in range(end-offset+1):
                assert p.a.f['vacuum_rows'](start_mask,end_mask,value(step['before']),r)==p.a.f['vacuum_rows'](start_mask,end_mask,value(step['after']),r)
                jet_checks+=1
        traces[name]=trace
    # Explicit competing first steps: BOTH distributivity directions are explored.
    labels={rule for (rule,address),_ in successors(cases['left_right_distributivity']) if not address}
    assert {'distribute_left','distribute_right'}<=labels
    root=cases['left_right_distributivity']
    rule,address=next(label for label,_ in successors(root) if label==('distribute_left',()))
    good=next(y for label,y in successors(root) if label==(rule,address))
    mutants={'dropped_summand':p.plus(good[1][0]),
             'wrong_sign':p.plus(good[1][0],p.scale(-1,good[1][1])),
             'reversed_factors':p.plus(*(p.times(term[2],term[1]) for term in good[1]))}
    rejected=[]
    for name,bad in mutants.items():
        try:verify_step(root,bad,rule,address)
        except ValueError:rejected.append(name)
        else:raise AssertionError('invalid distributivity step accepted')
    try:verify_step(root,good,'distribute_right',())
    except ValueError:rejected.append('wrong_rule_label')
    else:raise AssertionError('wrong rule accepted')
    # Same canonical formal sum, different construction histories.
    assert root!=good and value(root)==value(good)
    report={'schema':'typed-ast-distributivity-v1','passed':True,'cases':audits,
        'trace_fox_record_checks':jet_checks,'serialized_traces':traces,
        'negative_controls_rejected':rejected,
        'interpretation':'Four roots have exhaustive reachable-graph checks; the three-sum root has 32 completed seeded schedules, not an exhaustive traversal. Checked terminal ASTs agree as collected ordered formal monomials, independently of source evaluation. Traces preserve original syntax; normal forms alone do not.',
        'scope':'Exhaustive typed rewrite graphs for four declared roots, plus 32 bounded schedules for a three-sum root. Not a general confluence theorem or a categorical-opposite identification.'}
    out=ROOT/'results/typed-ast-distributivity.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('passed','cases','trace_fox_record_checks','negative_controls_rejected','scope')},indent=2))


if __name__=='__main__':main()
