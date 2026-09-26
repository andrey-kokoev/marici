"""Source-derived event poset for innermost-first SP -> PSS.
S residual labels L/R denote syntactic slots, not Bool values. Full labelled
states and schedules remain data; equal ideals do not erase route records.
"""
from dataclasses import dataclass
from itertools import product, combinations

@dataclass(frozen=True, order=True)
class Event:
    sum_origin: int
    product_origin: int
    residual: str

@dataclass(frozen=True)
class Token:
    kind: str
    origin: int
    residual: str = ''


def initial(word):
    if any(c not in 'SP' for c in word):raise ValueError('S/P word required')
    return tuple(Token(c,i) for i,c in enumerate(word))


def signature(word):
    a=b=0
    for c in word:
        if c=='S':a+=1
        elif c=='P':a*=2;b+=1
        else:raise ValueError('S/P word required')
    return a,b


def event_poset(word):
    initial(word)
    predecessors={}
    for s,c in enumerate(word):
        if c!='S':continue
        ps=[p for p in range(s+1,len(word)) if word[p]=='P']
        for k,p in enumerate(ps):
            for letters in product('LR',repeat=k):
                bits=''.join(letters);e=Event(s,p,bits)
                predecessors[e]=set()
                if k:predecessors[e].add(Event(s,ps[k-1],bits[:-1]))
    # One product moves monotonically left: rightmost S source first,
    # and rightmost residual of that S source first.
    for p,c in enumerate(word):
        if c!='P':continue
        line=sorted((e for e in predecessors if e.product_origin==p),
                    key=lambda e:(e.sum_origin,e.residual),reverse=True)
        for earlier,later in zip(line,line[1:]):predecessors[later].add(earlier)
    return {e:frozenset(ps) for e,ps in predecessors.items()}


def enabled(predecessors,done):
    return tuple(e for e,ps in predecessors.items() if e not in done and ps<=done)


def redexes(state):
    return tuple((Event(s.origin,p.origin,s.residual),i)
                 for i,(s,p) in enumerate(zip(state,state[1:]))
                 if s.kind=='S' and p.kind=='P')


def step(state,event):
    matches=[i for e,i in redexes(state) if e==event]
    if len(matches)!=1:raise ValueError('event is not an enabled labelled rewrite')
    i=matches[0];s,p=state[i:i+2]
    return state[:i]+(p,Token('S',s.origin,s.residual+'L'),
                       Token('S',s.origin,s.residual+'R'))+state[i+2:]


def primitive(state):return ''.join(t.kind for t in state)


def value_step(state,event,value,inverse=False):
    """Lift the local reversible map through every retained outer binder."""
    i=next((i for e,i in redexes(state) if e==event),None)
    if i is None:raise ValueError('not enabled')
    suffix=primitive(state)[i+2:]
    def local(v):
        if inverse:
            a,(b,(x,y))=v
            return ((a,x),(b,y))
        (a,x),(b,y)=v
        return a,(b,(x,y))
    def lift(outer,v):
        if not outer:return local(v)
        if outer[-1]=='P':return (lift(outer[:-1],v[0]),lift(outer[:-1],v[1]))
        tag,entry=v
        return tag,lift(outer[:-1],entry)
    return lift(suffix,value)


def sample_value(word,salt=0):
    counter=iter(range(10**9))
    def build(k):
        if k<0:return ('opaque-leaf',next(counter),salt)
        if word[k]=='P':return build(k-1),build(k-1)
        tag=(next(counter)+salt)%2
        return tag,build(k-1)
    return build(len(word)-1)


def valid_schedule(predecessors,schedule,complete=True):
    done=set()
    for e in schedule:
        if e not in predecessors or e in done or not predecessors[e]<=done:return False
        done.add(e)
    return not complete or done==set(predecessors)


def linear_extension(predecessors,key=lambda e:e):
    done=set();result=[]
    while len(done)<len(predecessors):
        options=enabled(predecessors,done)
        if not options:raise ValueError('cyclic event relation')
        e=min(options,key=key);result.append(e);done.add(e)
    return tuple(result)


def compare_schedules(predecessors,left,right):
    """Construct a retained comparison by adjacent independent swaps.
Returns every full intermediate schedule, not just equal endpoint signatures.
"""
    if not valid_schedule(predecessors,left) or not valid_schedule(predecessors,right):
        raise ValueError('complete linear extensions required')
    current=list(left);route=[tuple(current)]
    for fixed,target in enumerate(right):
        index=current.index(target)
        while index>fixed:
            before=frozenset(current[:index-1])
            a,b=current[index-1:index+1]
            if not ({a,b}<=set(enabled(predecessors,before))):
                raise AssertionError('swap would exchange dependent events')
            current[index-1:index+1]=b,a
            assert valid_schedule(predecessors,current)
            route.append(tuple(current));index-=1
    assert tuple(current)==right
    return tuple(route)


def cubical_cells(predecessors,ideals):
    """A cell is a bottom ideal and a set of independent enabled events."""
    result=set()
    for ideal in ideals:
        choices=enabled(predecessors,ideal)
        for k in range(len(choices)+1):
            for subset in combinations(choices,k):result.add((ideal,frozenset(subset)))
    return result


def contract_cells(predecessors,cells):
    """Check every prism of maximal-event deletion, retaining its witnesses.
This supplies a combinatorial strong-deformation-retraction certificate.
"""
    pred=dict(predecessors);remaining=set(cells);prisms=0;stages=[]
    for event in reversed(linear_extension(pred)):
        assert all(event not in ps for ps in pred.values()), 'event is not maximal'
        projected=set()
        for ideal,variables in remaining:
            if event in ideal:
                bottom=ideal-{event}
                prism=(bottom,variables|{event})
                if prism not in remaining:raise AssertionError('missing contraction prism')
                prisms+=1
            projected.add((ideal-{event},variables-{event}))
        del pred[event]
        assert all(ideal in {i for i,c in projected if not c} for ideal,c in projected)
        expected=cubical_cells(pred,{i for i,c in projected if not c})
        if expected!=projected:raise AssertionError('projected cell complex is incomplete')
        stages.append((event,len(remaining),len(projected)))
        remaining=projected
    assert remaining=={(frozenset(),frozenset())}
    return prisms,tuple(stages)
