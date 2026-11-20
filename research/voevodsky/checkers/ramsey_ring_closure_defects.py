"""Even rings: minimize blue crossing edges, keeping strict pole alternation. Odd ring: enumerate every strictly red alternating simple path on 11 sites up to path reversal; test filling its closing seam by a new opposite-side vertex. No induced-cycle requirement."""
from pathlib import Path
from itertools import combinations
import json
D=Path(__file__).resolve().parents[1]/'results';out=[]
for old in json.loads((D/'ramsey_three_case_tet_ring.json').read_text()):
 t=old['t'];n=old['n'];N={7:22,8:27,9:35}[t];g=json.loads((D/(old['source']+'.json')).read_text());g=g.get('witness',g);E={tuple(sorted(e)) for e in g.get('red_edges',g.get('plus_edges'))};V=set(range(N));A=[{v for v in V if tuple(sorted((u,v))) in E} for u in V];pairs=list(combinations(range(N),2));
 if t==9:
    assert all(tuple(sorted(((u+1)%N,(v+1)%N))) in E for u,v in E);pairs=[pq for pq in pairs if pq[0]==0];
 def sides(p,q):return (A[p]-A[q]-{q},A[q]-A[p]-{p})
 if n%2==0:
    def first(cap):
        for p,q in pairs:
            L,R=sides(p,q)
            if min(len(L),len(R))<n//2:continue
            def walk(path,unused,cost):
                u=path[-1];start=path[0]
                if len(path)==n:return path if cost+int(start not in A[u])<=cap else None
                side=R if len(path)%2 else L;opts=unused&side
                # Fix the smallest chosen L site as the start.
                if side is L:opts={v for v in opts if v>start}
                for v in sorted(opts,key=lambda v:(v not in A[u],v)):
                    nc=cost+(v not in A[u]);
                    if nc<=cap:
                        found=walk(path+[v],unused-{v},nc)
                        if found:return found
            for v in sorted(L):
                ring=walk([v],(L|R)-{v},0)
                if ring:return dict(poles=[p,q],ring=ring,blue=[[u,v] for u,v in zip(ring,ring[1:]+ring[:1]) if v not in A[u]])
    for cap in range(n+1):
        ex=first(cap)
        if ex:break
    assert len(ex['blue'])==cap;row=dict(t=t,min_blue_crossings=cap,example=ex)
 else:
    count=0;filled=0;distinct=set();outside_hist={};samepole_hist={}
    for p,q in pairs:
        L,R=sides(p,q)
        for side,opp in [(L,R),(R,L)]:
            if len(side)<6 or len(opp)<5:continue
            def paths(path,free):
                if len(path)==n:
                    if path[0]<path[-1]:yield path
                else:
                    for v in sorted(free&A[path[-1]]):yield from paths(path+[v],free-{v})
            for v in side:
                for path in paths([v],(L|R)-{v}):
                    center,=A[p]&A[q];assert not (A[center]&set(path));count+=1;distinct.add((p,q));ends=A[path[0]]&A[path[-1]];outside=ends-set(path)-{p,q};f=outside&opp;filled+=bool(f);outside_hist[len(outside)]=outside_hist.get(len(outside),0)+1;samepole_hist[len(A[p]&A[q])]=samepole_hist.get(len(A[p]&A[q]),0)+1
    row=dict(t=t,paths=count,pole_pairs=len(distinct),can_fill_with_unused_opposite=filled,other_unused_common_red_counts=outside_hist,common_pole_neighbors=samepole_hist)
 out.append(row);print(row,flush=True)
(D/'ramsey_ring_closure_defects.json').write_text(json.dumps(out,indent=2)+'\n')
