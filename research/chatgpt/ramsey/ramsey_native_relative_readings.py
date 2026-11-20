"""Classify undirected relative-operation link readings invariant under native axis cycling.
All matrices have dyadic entries exactly representable here. No graph catalogue inputs."""
from pathlib import Path
import json
from fractions import Fraction
from collections import Counter
D=json.loads((Path(__file__).resolve().parents[2]/'strominger/results/native-path-sector-calculus-v1.json').read_text())
def matrix(m):return tuple(complex(float(Fraction(a)),float(Fraction(b))) for row in m for a,b in row)
def mul(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
forms={tuple(r['normal_form']):matrix(r['matrix']) for r in D['normal_form_dictionary']};I=forms[0,0,0,0];t=forms[0,0,0,1]

def census(project):
    rep=lambda a:forms[(0,*key[a][1:])] if project else a
    G=list(dict.fromkeys(map(rep,forms.values())));idx={v:i for i,v in enumerate(G)};n=len(G);p=[[idx[rep(mul(a,b))] for b in G] for a in G];o=idx[I];ti=idx[t];inv=[row.index(o) for row in p];cycle=lambda j:p[p[ti][j]][inv[ti]]
    # Distinct endpoint types of the sector routes and their generated orbit.
    axes=[forms[0,1,0,0],forms[0,0,1,0],forms[0,1,1,0]];moves=set()
    for s in D['sectors']:
        a=I
        for i,sgn in s['left']:a=mul(a,tuple(sgn*x for x in axes[i]))
        moves.add(idx[rep(a)])
    def reach(S):
        r={o};q=[o]
        while q:
            v=q.pop()
            for h in S:
                u=p[v][h]
                if u not in r:r.add(u);q.append(u)
        return len(r)
    orbits=[];remaining=set(range(n))-{o}
    while remaining:
        start=min(remaining);orbit={start};q=[start]
        while q:
            v=q.pop()
            for u in (cycle(v),inv[v]):
                if u not in orbit:orbit.add(u);q.append(u)
        orbits.append(sorted(orbit));remaining-=orbit
    hist=Counter();examples={}
    for m in range(1<<len(orbits)):
        S={v for i,orb in enumerate(orbits) if m>>i&1 for v in orb}
        if any(p[u][v] in S for u in S for v in S):continue
        hist[len(S),reach(S)]+=1;examples.setdefault((len(S),reach(S)),[key[G[j]] for j in sorted(S)])
    print('projective' if project else 'signed','states',n,'route endpoints',len(moves),'reachable by sectors',reach(moves),'candidate rules',1<<len(orbits),'triangle-free by (degree,component size)',dict(sorted(hist.items())))
    if not project:
        for s in sorted(hist):
            if s[1]==n:print('connected example',s,examples[s]);break
key={a:k for k,a in forms.items()}
if __name__=='__main__':census(True);census(False)
