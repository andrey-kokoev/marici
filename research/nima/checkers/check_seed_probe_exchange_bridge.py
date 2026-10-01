"""Restrict existing S4 probe constructions to actual seed; conditional exchange.
Counting kernels are computed, not fit. Neither probe nor event law is physical
by virtue of this adapter alone.
"""
from fractions import Fraction as F
import check_carrier_probe_adapter as prior
from check_natural_tower_return import PACKETS

labels=tuple(label for label,_,_ in PACKETS)
edge_indices=tuple(prior.edges.index(('ABCD'.index(s),'ABCD'.index(t))) for _,s,t in PACKETS)
index={label:i for i,label in enumerate(labels)}
words=(('AD','DB','BC','CA'),('AD','DB','BA'),('AB','BC','CA'),('AB','BA'))
signs=(1,-1,-1,1)

comparisons={}
for name,all_probes,norm in (('endpoint-fixing',prior.fixed,F(2)),
                             ('directed-transition',prior.transition,F(6))):
    probes=tuple(all_probes[i] for i in edge_indices)
    gram=tuple(tuple(prior.dot(a,b)/norm for b in probes) for a in probes)
    feature_rank=prior.rank(probes)
    assert all(gram[i][i]==1 for i in range(6))
    if name=='endpoint-fixing':
        assert feature_rank==5
        assert probes[index['AB']]==probes[index['BA']]
        assert all(gram[i][j]==(1 if frozenset(PACKETS[i][1:])==frozenset(PACKETS[j][1:]) else F(1,2))
                   for i in range(6) for j in range(6))
        # Sole coefficient kernel: reverse difference, retained separately.
        x=tuple(F(i+1) for i in range(6))
        merged=x[index['AB']]+x[index['BA']]
        difference=x[index['AB']]-x[index['BA']]
        assert (merged+difference)/2==x[index['AB']]
        assert (merged-difference)/2==x[index['BA']]
    else:
        assert feature_rank==6 and probes[index['AB']]!=probes[index['BA']]
    # Use raw indicator vectors with pairing counting/norm, avoiding irrational
    # normalization. Each u is unit in this explicitly declared metric.
    features=tuple(tuple(p.get(k,F(0)) for k in range(24)) for p in probes)
    def event(state,label):
        q,w=state[:24],state[24:];i=index[label];u=features[i]
        mismatch=w[i]-sum(a*b for a,b in zip(u,q))/norm
        return tuple(a+b*mismatch for a,b in zip(q,u))+tuple(
            value-mismatch if j==i else value for j,value in enumerate(w))
    def execute(state,word):
        for label in word: state=event(state,label)
        return state
    def budget(state): return sum(x*x for x in state[:24])/norm+sum(x*x for x in state[24:])
    initial=(F(0),)*24+tuple(F(i==index['AB']) for i in range(6))
    outputs=[]
    for word in words:
        result=execute(initial,word);outputs.append(result)
        assert budget(result)==budget(initial)==1
        assert execute(result,tuple(reversed(word)))==initial
    mixed=tuple(sum(sign*row[i] for sign,row in zip(signs,outputs)) for i in range(30))
    assert any(mixed)
    # Duplicated probe values do not identify record slots or their executions.
    if name=='endpoint-fixing': assert event(initial,'AB')!=event(initial,'BA')
    print(name,'seed rank',feature_rank,'AB/BA overlap',gram[index['AB']][index['BA']],
          'mixed prepared-state output nonzero',any(mixed))
    print('normalized counting Gram:',gram)
    # Common named record readers, unchanged between the two probe geometries.
    record_outputs=tuple(tuple(out[24+i] for i in range(6)) for out in outputs)
    loop=outputs[-1]
    comparisons[name]={
        'BA_after_AB_BA':loop[24+index['BA']],
        'BA_record_squared':loop[24+index['BA']]**2,
        'carrier_budget_after_AB_BA':sum(v*v for v in loop[:24])/norm,
        'mixed_BA':mixed[24+index['BA']],
        'mixed_BC':mixed[24+index['BC']],
        'mixed_CA':mixed[24+index['CA']],
        'ABC_BC':outputs[2][24+index['BC']],
        'ABC_CA':outputs[2][24+index['CA']],
    }
    # All ten endpoint-compatible primitive pairs: prepare record i, execute
    # i then j, read the SAME named record j. This reads the computed overlap.
    tested=0
    for i,(_,s,t) in enumerate(PACKETS):
        for j,(_,u,v) in enumerate(PACKETS):
            if t!=u: continue
            prepared=(F(0),)*24+tuple(F(k==i) for k in range(6))
            response=execute(prepared,(labels[i],labels[j]))
            assert response[24+j]==gram[j][i]
            assert budget(response)==1
            tested+=1
    assert tested==10
    print('Named record predictions:',comparisons[name])
assert comparisons['endpoint-fixing']=={
    'BA_after_AB_BA':F(1),'BA_record_squared':F(1),'carrier_budget_after_AB_BA':F(0),
    'mixed_BA':F(1),'mixed_BC':F(-1,2),'mixed_CA':F(-1,4),
    'ABC_BC':F(1,2),'ABC_CA':F(1,4)}
assert comparisons['directed-transition']=={
    'BA_after_AB_BA':F(1,3),'BA_record_squared':F(1,9),'carrier_budget_after_AB_BA':F(8,9),
    'mixed_BA':F(1,3),'mixed_BC':F(-1,3),'mixed_CA':F(-2,9),
    'ABC_BC':F(1,3),'ABC_CA':F(2,9)}
print('PASS: same preparation and named record readers distinguish models after two events; all ten composable pairs checked.')
print('PASS: source -> existing probes -> computed overlap kernels -> conditional reversible exchange.')
print('BOUNDARY: distinct probe choices and their physical pairing/event interpretation remain unselected.')

# Operational query audit: g is a vertex-label permutation, not itself a
# supplied physical traversal. Stabilizing (s,t) and sending s to t are distinct.
identity=prior.group.index(tuple(range(4)))
for e in edge_indices:
    f=prior.fixed[e];t=prior.transition[e]
    assert f.get(identity,0)==1 and t.get(identity,0)==0
    assert set(f).isdisjoint(t)
    assert (len(f),len(t),24-len(set(f)|set(t)))==(2,6,16)
# Transition queries obey ordered relational composition, summing over ALL
# four intermediate vertices, including diagonal transitions absent in the seed.
for g in prior.group:
    for h in prior.group:
        hg=tuple(h[g[i]] for i in range(4))
        for e in edge_indices:
            s,t=prior.edges[e]
            assert int(hg[s]==t)==sum(int(g[s]==v)*int(h[v]==t) for v in range(4))
# A stabilizer membership query is not multiplicative under arbitrary temporal
# composition: two nonstabilizing permutations can multiply to identity.
swap_ab=(1,0,2,3)
k=prior.group.index(swap_ab)
ab=prior.fixed[prior.edges.index((0,1))]
assert not ab.get(k,0) and ab[identity]==1
assert tuple(swap_ab[swap_ab[i]] for i in range(4))==tuple(range(4))
print('QUERY AUDIT: per edge, 2 permutations stabilize endpoints, 6 realize the directed transition, and 16 do neither.')
print('PASS: the queries are disjoint and disagree at identity; no common scalar renormalization identifies them.')
print('BOUNDARY: transition composition requires the full intermediate-state domain; probe typing does not select an execution law.')
