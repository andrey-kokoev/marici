"""Predict exact gained row IDs, before querying shellable fillings. See protocol in freeze artifact."""
import sys,json,gzip
from itertools import combinations
from functools import lru_cache
from ramsey38_cycle_direction_trial import graph,candidates,cycle,make,prev,shell_scan,P as prior
from ramsey38_novel_array_trial import perm_table
from ramsey38_release_census import templates,bits
from ramsey38_ring_budget_screen import screen
from ramsey38_alternating_boundary_paths import find
P=prev.out/'ramsey38_named_gain_predictions.json';R=prev.out/'ramsey38_named_gain_comparison.json'
protocol='First eight canonically distinct unchanged-root marked transitions from record 12 onward, excluding previous cycle trial. Seven columns, forest -> unique six-cycle, marked triangle -> tetrahedron. Predict exact newly sole-hidden rows. Baseline: all other edges of the old triangle occurring as rows. Stronger: red shell screen possible with old triangle interior, minus blue shell screen possible. Seven original labels only. No fillings in freeze.'
def inputs(e):
    u,v=e['u'],e['v'];g=graph(e['word']);b=make(g,u,v,e['A'],e['B']);a=make(g,u,v,e['A'],e['C']);x,=set(e['C'])-set(e['B']);labs=sorted(b[u]);mask=lambda s:sum(1<<i for i,w in enumerate(labs) if w in s);rows={j:mask(s) for j,s in b.items() if j not in b[u]|{u}};return b,a,x,rows,mask({v})
def key(e):
    _,_,x,rs,v=inputs(e);prefix=bytes([rs[x],v]);rest=bytes(sorted(s for j,s in rs.items() if j!=x));return min(prefix.translate(t)+bytes(sorted(rest.translate(t))) for t in perm_table())
@lru_cache(None)
def face(f):return bits(f)
def possible(rs,buried):
    ss=set(map(face,rs.values()));short={j:s for j,s in rs.items() if s.bit_count()<4};wins=set();p=frozenset(range(7))
    for fs,cl in templates():
        if buried in cl:continue
        hidden=[j for j,s in short.items() if s not in cl]
        if len(hidden)!=1 or hidden[0] in wins:continue
        bd=frozenset(map(face,fs))
        if screen(p,ss,bd)=='pass' and not find(ss|bd,bd):wins.add(hidden[0])
    return wins
if __name__=='__main__' and sys.argv[1]=='freeze':
    es=[];seen={key(e) for e in json.loads(prior.read_text())['cases'] if len(e['A'])==6}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<12:continue
            word=line.strip();g=graph(word)
            for u,v in combinations(sorted(g),2):
                if v not in g[u]:continue
                abc=candidates(g,u,v)
                if not abc:continue
                a,b,c=abc
                if len(a)!=6 or cycle(g,a,b):continue
                cy=cycle(g,a,c)
                if len(cy)!=6 or any(len(s)!=2 for s in cy.values()):continue
                e=dict(record=i,word=word,u=u,v=v,A=a,B=b,C=c);_,_,x,rs,col=inputs(e);s=rs[x]
                if s.bit_count()!=3 or max(t.bit_count() for t in rs.values())>4:continue
                k=key(e)
                if k in seen:continue
                seen.add(k);rs1={**rs,x:s|col};simple=sorted(j for j,q in rs.items() if q.bit_count()==2 and q&s==q);blue=possible(rs,None);red=possible(rs1,s);es.append(dict(e,optional=x,old_triangle=[w for j,w in enumerate(sorted(set(e['A'])|{v})) if s>>j&1],edge_baseline=simple,predicted=sorted(red-blue-{x}),blue_shortlist=sorted(blue),red_buried_shortlist=sorted(red),canonical=k.hex()));print(i,u,v,simple,es[-1]['predicted'],flush=True)
                if len(es)==8:break
            if len(es)==8:break
    assert len(es)==8;prev.save(P,dict(protocol=protocol,cases=es));print('frozen',prev.sha(P.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    data=json.loads(P.read_text());assert data['protocol']==protocol;results=[]
    for e in data['cases']:
        b,a,x,rs,col=inputs(e);u=e['u'];sc=[shell_scan(g,u) for g in (b,a)];wins=[{q[0] for q in cs if len(q)==1} for cs in sc];gain=sorted(wins[1]-wins[0]-{x});results.append(dict(actual=gain,certificates=[{str(list(q)):o for q,o in cs.items()} for cs in sc]));print(e['record'],u,e['v'],'predicted',e['predicted'],'actual',gain,'edge baseline',e['edge_baseline'],flush=True)
    prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),results=results))
