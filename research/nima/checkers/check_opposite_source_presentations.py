"""Expansion/regrouping equivalence, not a sum/product duality.

P/Q path coordinates versus P/H product coordinates, H=Q-P.
Actual ordered source products and Fox records anchor both presentations.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import importlib.util,json
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('roles',ROOT/'checkers/check_four_residual_coherence_roles.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)


def leaf(kind,i):return (kind,i)
def scale(c,x):return ('scale',str(c),x)
def plus(*xs):return ('sum',xs)
def times(x,y):return ('product',x,y)


def span(x):
    if x[0] in ('P','Q','H'):return x[1],x[1]+1
    if x[0]=='scale':return span(x[2])
    if x[0]=='sum':
        spans=[span(y) for y in x[1]]
        if not spans or len(set(spans))!=1:raise ValueError('sum corners')
        return spans[0]
    if x[0]=='product':
        p,q=span(x[1]),span(x[2])
        if p[1]!=q[0]:raise ValueError('product endpoints/order')
        return p[0],q[1]
    raise ValueError('node')


def add_sources(xs):
    out={}
    for source in xs:
        for p,c in source.items():out[p]=out.get(p,Q(0))+c
    return {p:c for p,c in out.items() if c}


def expand(x):
    span(x)
    kind=x[0]
    if kind in ('P','Q','H'):
        return a.paths({'P':[Q(1),Q(0)],'Q':[Q(0),Q(1)],'H':[Q(-1),Q(1)]}[kind],x[1],1)
    if kind=='scale':return {p:Q(x[1])*c for p,c in expand(x[2]).items() if Q(x[1])*c}
    if kind=='sum':return add_sources([expand(y) for y in x[1]])
    return a.f['multiply'](expand(x[1]),expand(x[2]))


def interaction_eval(x):
    """Independent evaluation in the factored interaction coordinates."""
    span(x);kind=x[0]
    if kind in ('P','Q','H'):return {'P':[Q(1),Q(0)],'Q':[Q(1),Q(1)],'H':[Q(0),Q(1)]}[kind]
    if kind=='scale':return [Q(x[1])*v for v in interaction_eval(x[2])]
    if kind=='sum':return [sum(v,Q(0)) for v in zip(*(interaction_eval(y) for y in x[1]))]
    return a.tensor(interaction_eval(x[1]),interaction_eval(x[2]))


def expression(coefficients,n,offset,second):
    terms=[]
    for bits,c in enumerate(coefficients):
        if not c:continue
        leaves=[leaf(second if bits&(1<<i) else 'P',offset+i) for i in range(n)]
        term=leaves[0]
        for nxt in leaves[1:]:term=times(term,nxt)
        terms.append(scale(c,term))
    if not terms:return scale(0,expression([Q(1)]+[Q(0)]*((1<<n)-1),n,offset,second))
    return plus(*terms)


def clean_record_sum(weighted):
    result={}
    for coefficient,record in weighted:
        for key,value in record.items():result[key]=result.get(key,Q(0))+coefficient*value
    return {key:value for key,value in result.items() if value}


def main():
    checks={'inverse_and_typed_presentations':0,'full_fox_record_squares':0,
            'source_product_squares':0,'residual_depth_roundtrips':0,'distributive_routes':0}
    for n in (1,2,3):
        for offset in range(4-n):
            samples=a.basis(1<<n)+[a.inverse(v) for v in a.basis(1<<n)]+[[Q(i-2,i+1) for i in range(1<<n)]]
            start=(1<<(2*offset))-1;end=(1<<(2*(offset+n)))-1
            modes=[a.paths(a.inverse(v),offset,n) for v in a.basis(1<<n)]
            for coefficients in samples:
                m=a.moments(coefficients)
                assert a.inverse(m)==coefficients and a.moments(a.inverse(m))==m
                factored=expression(m,n,offset,'H');summed=expression(coefficients,n,offset,'Q')
                assert expand(factored)==expand(summed)==a.paths(coefficients,offset,n)
                assert interaction_eval(factored)==interaction_eval(summed)==m
                checks['inverse_and_typed_presentations']+=1
                for r in range(n+1):
                    lhs=a.f['vacuum_rows'](start,end,expand(summed),r)
                    rhs=clean_record_sum((c,a.f['vacuum_rows'](start,end,mode,r)) for c,mode in zip(m,modes))
                    assert lhs==rhs
                    checks['full_fox_record_squares']+=1
                    envelope=a.encode_m(m,offset,n,r)
                    assert a.decode(a.wire(envelope))==expand(summed)
                    checks['residual_depth_roundtrips']+=1
    for n,k in ((1,1),(1,2),(2,1)):
        for u,v in product(a.basis(1<<n),a.basis(1<<k)):
            factored=times(expression(u,n,0,'H'),expression(v,k,n,'H'))
            source=a.f['multiply'](a.paths(a.inverse(u),0,n),a.paths(a.inverse(v),n,k))
            assert expand(factored)==source==a.paths(a.inverse(a.tensor(u,v)),0,n+k)
            assert a.moments(a.tensor(a.inverse(u),a.inverse(v)))==a.tensor(u,v)
            checks['source_product_squares']+=1
    # Distributivity/reassociation without exchanging the order of any factors.
    for u,v,w in product(('P','Q','H'),repeat=3):
        x=plus(leaf(u,0),scale(Q(-2,3),leaf('P',0)))
        y=plus(leaf(v,1),scale(2,leaf('Q',1)));z=leaf(w,2)
        routes=[times(times(x,y),z),times(x,times(y,z)),
                plus(*(times(times(first,second),z) for first in x[1] for second in y[1]))]
        assert all(expand(route)==expand(routes[0]) for route in routes)
        assert all(interaction_eval(route)==interaction_eval(routes[0]) for route in routes)
        checks['distributive_routes']+=1
    # Coarse jets identify these two different presentations of source values.
    hidden_m=[Q(i==7) for i in range(8)];hidden_a=a.inverse(hidden_m)
    hidden_source=a.paths(hidden_a,0,3)
    assert hidden_source
    assert all(not a.f['vacuum_rows'](0,63,hidden_source,r) for r in (0,1,2))
    bad=a.encode_m(hidden_m,0,3,2);bad['residuals']=[]
    try:a.decode(bad)
    except ValueError:pass
    else:raise AssertionError('discarded residual silently reconstructed')
    # Opposite presentation direction does NOT reverse source multiplication.
    try:expand(times(leaf('P',1),leaf('Q',0)))
    except ValueError:pass
    else:raise AssertionError('reversed incompatible product accepted')
    # A normalized source value cannot recover its original expression history.
    x=times(plus(leaf('P',0),leaf('Q',0)),leaf('H',1))
    y=plus(times(leaf('P',0),leaf('H',1)),times(leaf('Q',0),leaf('H',1)))
    assert x!=y and expand(x)==expand(y)
    # Historical evidence in both coordinate presentations.
    E=[a.inverse(v) for v in a.basis(2)]
    E=list(map(list,zip(*E))) # m -> a
    tail=[Q(1),Q(-1)];T1=a.action(tail,1);T2=a.action(tail,2)
    T=a.pull(T2,T1)
    vacuum=a.basis(8)[0]
    past_path=a.pull([vacuum],T)[0]
    past_interaction=a.pull([past_path],E)[0]
    assert past_path==[1,0] and past_interaction==[1,-1]
    for reading in (Q(0),Q(1),Q(2,3)):
        path_fiber=a.solve([[1,1],past_path],[1,reading],2)
        interaction_fiber=a.solve([[1,0],past_interaction],[1,reading],2)
        assert a.canonical(path_fiber,2)==a.canonical(a.image(E,interaction_fiber),2)
    # The general final vacuum covector becomes alternating interaction signs.
    Em=list(map(list,zip(*(a.inverse(v) for v in a.basis(8)))))
    assert a.pull([vacuum],Em)[0]==[Q((-1)**t.bit_count()) for t in range(8)]
    report={'schema':'opposite-source-presentations-v1','passed':True,'checks':checks,
        'bridge':{'forward':'expand P/H product-basis coefficients m to P/Q path coefficients a',
                  'backward':'regroup a into m by the Boolean zeta transform',
                  'H_convention':'H=Q-P; the forgotten ideal relation is P-Q=-H',
                  'expansion_matrix':[[str(x) for x in row] for row in Em],
                  'regrouping_matrix':[[str(int(b&t==t)) for b in range(8)] for t in range(8)]},
        'history_evidence':{'past_terminal_path_row':[1,1],'past_terminal_interaction_row':[1,0],
                            'future_vacuum_path_row':[1,0],'future_vacuum_interaction_row':[1,-1],
                            'whole_affine_fiber_comparisons':3,'recorded_reading_changed':False},
        'negative_controls':{'jets_through_order_two_miss_nonzero_cubic_source':True,
                             'missing_residual_rejected':True,'incompatible_reversed_product_rejected':True,
                             'different_expression_histories_can_have_same_source_value':True},
        'meaning':'Inverse, oppositely directed coordinate presentations of one typed source. They intertwine ordered products, complete finite Fox records and evidence pullback.',
        'limits':'Not an exchange of sum and product operations, a recovered factorization history, or a proved categorical-opposite identification. Truncated jets alone remain lossy; no general rank-one factorization of arbitrary sources is asserted.',
        'scope':'Finite rational forgotten packets with fixed labelled P/Q and P/H bases, admitted ordered concatenations and exact synthetic historical evidence.'}
    (ROOT/'results/opposite-source-presentations.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('passed','checks','history_evidence','negative_controls','limits')},indent=2))


if __name__=='__main__':main()
