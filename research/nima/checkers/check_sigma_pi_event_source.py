"""Exhaust all reachable labelled states and all event ideals for bounded words.
This checks a source-derived schedule presentation, not arbitrary source paths.
"""
from collections import deque,Counter
from itertools import product
from pathlib import Path
import json,random
from sigma_pi_event_source import (Event,event_poset,initial,enabled,redexes,step,
    primitive,signature,sample_value,value_step,linear_extension,compare_schedules,
    valid_schedule,cubical_cells,contract_cells)

ROOT=Path(__file__).resolve().parents[3]
rng=random.Random(419)
counts=Counter();cube_dimensions=Counter();maxima={'events':0,'states':0,'schedules':0}
examples=[]

for length in range(7):
  for letters in product('SP',repeat=length):
    word=''.join(letters);poset=event_poset(word)
    a,b=signature(word)
    assert len(poset)==a-word.count('S')
    maxima['events']=max(maxima['events'],len(poset))
    start=frozenset();states={start:initial(word)}
    values={start:tuple(sample_value(word,salt) for salt in (0,1))}
    paths={start:1};queue=deque([start]);actual_edges=set()
    while queue:
      done=queue.popleft();state=states[done]
      assert signature(primitive(state))==(a,b)
      # This rank strictly decreases for every rewrite and bounds all routes.
      assert a-primitive(state).count('S')==len(poset)-len(done)
      actual=tuple(e for e,_ in redexes(state))
      predicted=enabled(poset,done)
      assert set(actual)==set(predicted), ('enabled mismatch',word,done)
      for e in actual:
        after=step(state,e);target=done|{e}
        v=tuple(value_step(state,e,x) for x in values[done])
        assert all(value_step(state,e,y,inverse=True)==x for x,y in zip(values[done],v))
        if target in states:
          assert states[target]==after and values[target]==v
        else:
          states[target]=after;values[target]=v;queue.append(target);paths[target]=0
        paths[target]+=paths[done]
        actual_edges.add((done,e));counts['edges']+=1
      # Full independent-event cube: check ALL its vertex subsets and all
      # orders to each subset by recursively adding its initial events.
      if len(actual)>=2:
        cube={frozenset():(state,values[done])};todo=deque([frozenset()])
        while todo:
          used=todo.popleft();corner,cv=cube[used]
          for e in actual:
            if e in used:continue
            nxt=used|{e};ns=step(corner,e)
            nv=tuple(value_step(corner,e,x) for x in cv)
            if nxt in cube:assert cube[nxt]==(ns,nv)
            else:cube[nxt]=(ns,nv);todo.append(nxt)
        assert len(cube)==2**len(actual)
        cube_dimensions[len(actual)]+=1
        counts['cube_vertices_checked']+=len(cube)
    assert len(states)<20000, 'frozen state budget exceeded'
    terminal=frozenset(poset)
    assert primitive(states[terminal])=='P'*b+'S'*a
    assert all(done==terminal or redexes(state) for done,state in states.items())
    # Independent ideal enumeration from the poset, not from rewrite states.
    ideals={start};iq=deque([start]);model_edges=set()
    while iq:
      ideal=iq.popleft()
      for e in enabled(poset,ideal):
        target=ideal|{e};model_edges.add((ideal,e))
        if target not in ideals:ideals.add(target);iq.append(target)
    assert ideals==set(states) and model_edges==actual_edges
    cells=cubical_cells(poset,ideals)
    prisms,contraction=contract_cells(poset,cells)
    counts['cubical_cells']+=len(cells)
    counts['verified_contraction_prisms']+=prisms
    counts['contraction_stages']+=len(contraction)
    first=linear_extension(poset)
    schedules={first,linear_extension(poset,key=lambda e:(-e.product_origin,-e.sum_origin,e.residual))}
    for _ in range(8):
      keys={e:rng.random() for e in poset}
      schedules.add(linear_extension(poset,key=keys.get))
    for schedule in schedules:
      comparison=compare_schedules(poset,first,schedule)
      counts['schedule_comparisons']+=1
      counts['retained_swap_steps']+=len(comparison)-1
      for route in comparison:
        current=initial(word);v=values[start][0]
        for e in route:
          v=value_step(current,e,v);current=step(current,e)
        assert current==states[terminal] and v==values[terminal][0]
    counts['source_words']+=1;counts['states']+=len(states)
    maxima['states']=max(maxima['states'],len(states))
    maxima['schedules']=max(maxima['schedules'],paths[terminal])
    if word in ('SPP','SPSP','SSPP','SPPPP','SSPPPP'):
      examples.append({'word':word,'events':len(poset),'states':len(states),
        'complete_schedules':paths[terminal],
        'event_predecessors':[
          {'event':[e.sum_origin,e.product_origin,e.residual],
           'requires':[[p.sum_origin,p.product_origin,p.residual] for p in sorted(ps)]}
          for e,ps in poset.items()]})

# Hostile 1: deleting a genuine predecessor admits an impossible event.
p=event_poset('SPP');root=Event(0,1,'');child=Event(0,2,'R')
assert root in p[child]
broken=dict(p);broken[child]=p[child]-{root}
assert child in enabled(broken,frozenset())
try:step(initial('SPP'),child)
except ValueError:pass
else:raise AssertionError('impossible residual event was accepted')
# Hostile 2: a dependent event exchange is not an order comparison.
route=list(linear_extension(p));route[0],route[1]=route[1],route[0]
assert not valid_schedule(p,route)
try:compare_schedules(p,linear_extension(p),route)
except ValueError:pass
else:raise AssertionError('dependent swap accepted')
# The independent square is necessary: same endpoint, distinct retained routes.
p=event_poset('SPSP');left=linear_extension(p)
right=linear_extension(p,key=lambda e:(-e.product_origin,e.sum_origin,e.residual))
assert left!=right
full=compare_schedules(p,left,right)
assert full[0]==left and full[-1]==right and len(full)>1
example_comparison=[[[e.sum_origin,e.product_origin,e.residual] for e in route] for route in full]
# Hostile 3: removing higher cubes while retaining their lower faces breaks
# the supplied contraction. Pairwise squares alone are not this certificate.
p=event_poset('SPSPSP');ideals={frozenset()};queue=deque(ideals)
while queue:
    ideal=queue.popleft()
    for e in enabled(p,ideal):
        target=ideal|{e}
        if target not in ideals:ideals.add(target);queue.append(target)
cells=cubical_cells(p,ideals)
assert any(len(c)==3 for _,c in cells)
try:contract_cells(p,{(i,c) for i,c in cells if len(c)<3})
except AssertionError as exc:
    assert str(exc) in ('missing contraction prism','projected cell complex is incomplete')
else:raise AssertionError('missing higher cubes were accepted')
report={'schema':'marici.nima.sigma-pi-event-source.v1','passed':True,
 'classification':'exhaustive_bounded_source_event_poset_and_independence_coherence',
 'max_primitive_word_length':6,'counts':dict(counts),'maxima':maxima,
 'independent_cube_dimensions':dict(cube_dimensions),
 'hostiles':{'deleted_predecessor_exposes_illegal_event':True,
             'dependent_swap_refused':True,'distinct_routes_retained':True,
             'missing_higher_cube_certificate_refused':True},
 'examples':examples,'retained_SPSP_comparison':example_comparison,
 'scope':{'state_graph_and_ideal_graph':'exhaustive for every one of 127 words through length six',
          'complete_schedule_comparisons':'deterministic and sampled schedules; constructive general algorithm supplied',
          'value_checks':'two labelled source values per word on every state edge and independent cube',
          'unbounded_argument':'written event-poset, adjacent-swap and maximal-event cubical contraction proofs; not proof-assistant-certified',
          'arbitrary_dependent_indices_or_atomic_higher_paths':'not covered'}}
path=ROOT/'research/nima/results/sigma-pi-event-source.json'
path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('examples','retained_SPSP_comparison')},indent=2))
