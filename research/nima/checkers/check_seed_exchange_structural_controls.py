"""Does the exchange diagnostic require the two-triangle seed?
Fixed S4 probe dictionary and same AB preparation; topology changes admission,
not feature values. This is the implemented conditional model's contract.
"""
from fractions import Fraction as F
import check_carrier_probe_adapter as probe
from check_natural_tower_return import PACKETS

registry={label:(s,t) for label,s,t in PACKETS}
labels=tuple(registry);index={label:i for i,label in enumerate(labels)}
controls={'full':frozenset(labels),'seam-only':frozenset(('AB','BA'))}
controls.update({f'delete-{e}':frozenset(set(labels)-{e}) for e in ('BC','CA','AD','DB')})

def admitted(word,edges):
    return all(e in edges for e in word) and all(registry[a][1]==registry[b][0] for a,b in zip(word,word[1:]))

def simple_paths(start,end,edges):
    out=[]
    def visit(v,seen,path):
        if v==end: out.append(path);return
        for e in labels:
            s,t=registry[e]
            if e in edges and s==v and t not in seen: visit(t,seen|{t},path+(e,))
    visit(start,{start},())
    return tuple(out)

x0=('AB',);x1=('AD','DB');y0=('BA',);y1=('BC','CA')
rectangle=(x1+y1,x1+y0,x0+y1,x0+y0)
for name,edges in controls.items():
    f=simple_paths('A','B',edges);r=simple_paths('B','A',edges)
    assert admitted(x0+y0,edges)
    if name=='full': assert len(f)==len(r)==2 and all(admitted(w,edges) for w in rectangle)
    else: assert len(f)*len(r)<4 and not all(admitted(w,edges) for w in rectangle)
    print(name,'forward/return simple paths',len(f),len(r),'full rectangle admitted',all(admitted(w,edges) for w in rectangle))

for name,features,norm in (('endpoint-fixing',probe.fixed,F(2)),('directed-transition',probe.transition,F(6))):
    U={e:tuple(features[probe.edges.index(('ABCD'.index(s),'ABCD'.index(t)))].get(k,F(0))
               for k in range(24)) for e,(s,t) in registry.items()}
    initial=(F(0),)*24+tuple(F(e=='AB') for e in labels)
    def run(word,edges,prepared=None):
        if not admitted(word,edges): raise ValueError('Unavailable or noncomposable source word')
        state=initial if prepared is None else prepared
        for e in word:
            q,w=state[:24],state[24:];i=index[e];u=U[e]
            delta=w[i]-sum(a*b for a,b in zip(u,q))/norm
            state=tuple(a+b*delta for a,b in zip(q,u))+tuple(z-delta if j==i else z for j,z in enumerate(w))
        return state
    # Removed record ports remain idle bookkeeping coordinates, so states share
    # one comparison space. Dropping those zero coordinates gives the same result.
    reference=run(('AB','BA'),controls['full'])
    for control,edges in controls.items():
        assert run(('AB','BA'),edges)==reference
        for e in set(labels)-set(edges): assert reference[24+index[e]]==0
        if control!='full':
            try:
                for word in rectangle: run(word,edges)
            except ValueError: pass
            else: raise AssertionError('Missing rectangle silently executed')
    # All primitive transfer diagnostics depend only on the two used features.
    # Deleting any unused edge cannot change an admitted word's response.
    for i,(a,(s,t)) in enumerate(registry.items()):
        for b,(u,v) in registry.items():
            if t!=u: continue
            used=frozenset((a,b))
            assert run((a,b),used)==run((a,b),controls['full'])
    print(name,'AB->BA output identical even on seam-only graph:',reference[24+index['BA']])
    # NEW PREPARATION HYPOTHESIS: coherent unit displacement along each retained
    # primitive feature. Contributions sum; records start zero. Not derived
    # from incidence or from the exchange law, and not rescaled after deletion.
    prepared_predictions={}
    for control,edges in controls.items():
        prepared=tuple(sum(U[e][k] for e in edges) for k in range(24))+(F(0),)*6
        result=run(('AB','BA'),edges,prepared)
        prepared_predictions[control]=result[24+index['BA']]
        sAB=sum(U['AB'][k]*prepared[k] for k in range(24))/norm
        sBA=sum(U['BA'][k]*prepared[k] for k in range(24))/norm
        overlap=sum(U['AB'][k]*U['BA'][k] for k in range(24))/norm
        assert result[24+index['BA']]==sBA-overlap*sAB
        def energy(state):
            return sum(v*v for v in state[:24])/norm+sum(v*v for v in state[24:])
        assert energy(result)==energy(prepared)
    # Interaction control: preparation contributions add independently.
    # Delete one forward indirect leg and one return indirect leg; compare
    # the same surviving experiment in the four graph environments.
    environments=(frozenset(labels),frozenset(set(labels)-{'AD'}),
                  frozenset(set(labels)-{'BC'}),frozenset(set(labels)-{'AD','BC'}))
    outputs=[]
    for edges in environments:
        prepared=tuple(sum(U[e][k] for e in edges) for k in range(24))+(F(0),)*6
        outputs.append(run(('AB','BA'),edges,prepared))
    structural_mixed=tuple(outputs[0][k]-outputs[1][k]-outputs[2][k]+outputs[3][k]
                           for k in range(30))
    assert not any(structural_mixed)
    print('Structural two-leg deletion mixed response: zero in every output coordinate.')
    if name=='endpoint-fixing':
        assert all(value==0 for value in prepared_predictions.values())
    else:
        assert prepared_predictions=={'full':F(4,3),'seam-only':F(8,9),
            'delete-BC':F(13,9),'delete-CA':F(13,9),
            'delete-AD':F(1),'delete-DB':F(1)}
    print('NEW conditional coherent-sum preparation predictions:',prepared_predictions)
print('PASS: probe-choice discriminator is not specific to the two-triangle seed.')
print('PASS: full mixed protocol requires all six edges, but deletion makes it unavailable, not numerically zero.')
print('BOUNDARY: fixed preparation gives no environmental dependence; coherent-sum preparation introduces it as a new assumption.')
