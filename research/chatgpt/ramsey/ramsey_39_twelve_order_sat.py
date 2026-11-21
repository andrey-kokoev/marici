"""Order-independent feasibility test on sampled 12-weight sets. Relax Hamilton cycle to 2-factor."""
from itertools import combinations
from collections import Counter,defaultdict
from random import Random
from time import monotonic
from pathlib import Path
import json,sys
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from ramsey_mutual_repair_conjecture import sevens

def test(W, audit=None, degree_budget=False, chord=None, pair_only=False, degree_floors=None, connected_ramsey=False, seconds=None, on_connected=None):
    M=39;es=list(combinations(W,2));inc=defaultdict(list);ids={};clauses=[];top=len(es)
    for i,(a,b) in enumerate(es,1):
        for t in W:inc[tuple(sorted(((a+t)%M,(b+t)%M)))].append(i)
    if len({(a+b)%M for a in W for b in W})!=39:return 'not covering'
    for e,lits in inc.items():
        top+=1;ids[e]=top;clauses.append([-top,*lits]);clauses.extend([-l,top] for l in lits)
    if chord is not None:clauses.append([es.index(chord)+1])
    for a in W:
        enc=CardEnc.equals([i for i,e in enumerate(es,1) if a in e],2+int(chord is not None and a in chord),top_id=top,encoding=EncType.seqcounter);top=enc.nv;clauses.extend(enc.clauses)
    if degree_budget:
        for p in range(M):
            incp=[k for e,k in ids.items() if p in e];enc=CardEnc.atmost(incp,9,top_id=top,encoding=EncType.seqcounter);top=enc.nv;clauses.extend(enc.clauses)
            if degree_floors:
                enc=CardEnc.atleast(incp,degree_floors[p],top_id=top,encoding=EncType.seqcounter);top=enc.nv;clauses.extend(enc.clauses)
    for a,b,c in combinations(range(M),3):
        tri=((a,b),(a,c),(b,c))
        if not all(e in ids for e in tri):continue
        if not pair_only:clauses.append([-ids[e] for e in tri]);continue
        for j,e in enumerate(tri):
            for move in set(inc[tri[(j+1)%3]]) & set(inc[tri[(j+2)%3]]):
                clauses.extend([[-move,-k] for k in inc[e]])
    with Solver(name='cadical195',bootstrap_with=clauses) as s:
        seen_tri=False;seen_budget=False
        deadline=monotonic()+seconds if seconds is not None else None
        passed=0
        while True:
            if deadline is None:ok=s.solve()
            elif monotonic()>=deadline:return f'open:{passed}'
            else:
                s.conf_budget(2000);ok=s.solve_limited()
                if ok is None:continue
            if not ok:break
            seen_tri=True;pos=set(s.get_model());chosen=[e for e,k in ids.items() if k in pos];rim=[i for i in range(1,len(es)+1) if i in pos]
            if len(chosen)<136:s.add_clause([-i for i in rim]);continue
            if connected_ramsey:
                N={a:set() for a in W}
                for i in rim:
                    a,b=es[i-1];N[a].add(b);N[b].add(a)
                component={W[0]};stack=[W[0]]
                while stack:
                    nxt=N[stack.pop()]-component;stack.extend(nxt);component.update(nxt)
                if len(component)!=len(W):
                    s.add_clause([j for j,(a,b) in enumerate(es,1) if (a in component)!=(b in component)]);continue
                passed+=1
            if degree_budget and not connected_ramsey:return 'candidate degree-budget factor: '+str(rim)
            seen_budget=True;A=[0]*39
            for a,b in chosen:A[a]|=1<<b;A[b]|=1<<a
            if on_connected is not None:on_connected([es[i-1] for i in rim],A)
            if audit is not None:
                N={a:[] for a in W}
                for i in rim:
                    a,b=es[i-1];N[a].append(b);N[b].append(a)
                remaining=set(W);cycles=[]
                while remaining:
                    v=min(remaining);cycle=[]
                    while v in remaining:
                        remaining.remove(v);cycle.append(v);v=next((u for u in N[v] if u in remaining),cycle[0])
                    cycles.append(cycle)
                audit(cycles,len(chosen),A)
                s.add_clause([-i for i in rim]);continue
            I=next(sevens(A,k=10),None)
            if I is None:return ('witness: ' if connected_ramsey else 'candidate 2-factor: ')+str(rim)
            s.add_clause([k for (a,b),k in ids.items() if I>>a&I>>b&1])
        if connected_ramsey:return f'excluded:{passed}'
        return 'ten obstruction' if seen_budget else 'budget obstruction' if seen_tri else 'triangle obstruction'
if __name__=='__main__':
    rng=Random(2026);stats=Counter();examples={};end=monotonic()+float(sys.argv[1]);samples=set()
    while monotonic()<end:
        W=tuple(sorted([0,1]+rng.sample(range(2,39),10)))
        if W in samples:continue
        samples.add(W);s=test(W);stats[s]+=1;examples.setdefault(s,W)
        if s.startswith('candidate'):break
    print(stats,examples);Path(__file__).with_suffix('.json').write_text(json.dumps({'seed':2026,'samples':len(samples),'stats':dict(stats),'examples':examples},indent=2)+'\n')
