"""Exact finite candidate for framed-node / elementary-arrow duality.
T = F2^2; C2 swaps the axes; S = T semidirect C2 = D8 (order eight).
This is a chosen local model, not a proof of a native or Ramsey correspondence.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json

ELEMENTS = list(product(range(2), repeat=3))
VERTICES = list(product(range(2), repeat=2))
IDENTITY = (0,0,0)
A, B, FRAME = (1,0,0), (0,1,0), (0,0,1)


def multiply(left,right):
    x,y,f = left
    u,v,g = right
    if f: u,v = v,u
    return (x^u,y^v,f^g)


def inverse(g):
    return next(h for h in ELEMENTS if multiply(g,h) == multiply(h,g) == IDENTITY)


def order(g):
    current = IDENTITY
    for n in range(1,9):
        current = multiply(current,g)
        if current == IDENTITY:return n
    raise AssertionError('No finite order found')


def act_vertex(g,vertex):
    x,y,f = g
    u,v = vertex
    if f:u,v = v,u
    return (x^u,y^v)


def to_arrow(state):
    x,y,f = state
    return ((x,y),(x^int(f == 0),y^int(f == 1)))


def to_state(arrow):
    tail,head = arrow
    if tail not in VERTICES or head not in VERTICES:
        raise ValueError('Endpoint outside square')
    delta = tuple(a^b for a,b in zip(tail,head))
    if delta not in ((1,0),(0,1)):
        raise ValueError('Not an elementary directed edge')
    return (*tail,0 if delta == (1,0) else 1)


def act_arrow(g,arrow):
    return tuple(act_vertex(g,v) for v in arrow)


def reverse(arrow):return tuple(reversed(arrow))


def main():
    arrows = [to_arrow(state) for state in ELEMENTS]
    assert len(set(arrows)) == 8
    for g in ELEMENTS:
        assert multiply(IDENTITY,g) == multiply(g,IDENTITY) == g
        assert multiply(inverse(g),g) == multiply(g,inverse(g)) == IDENTITY
        for h in ELEMENTS:
            assert multiply(g,h) in ELEMENTS
            for k in ELEMENTS:
                assert multiply(multiply(g,h),k) == multiply(g,multiply(h,k))
            for vertex in VERTICES:
                assert act_vertex(multiply(g,h),vertex) == act_vertex(g,act_vertex(h,vertex))
        for state in ELEMENTS:
            assert to_state(to_arrow(state)) == state
            assert to_arrow(multiply(g,state)) == act_arrow(g,to_arrow(state))
        for arrow in arrows:
            assert to_arrow(to_state(arrow)) == arrow
            assert reverse(reverse(arrow)) == arrow
            assert act_arrow(g,reverse(arrow)) == reverse(act_arrow(g,arrow))
        assert len({multiply(g,state) for state in ELEMENTS}) == 8
    assert multiply(A,A) == multiply(B,B) == multiply(FRAME,FRAME) == IDENTITY
    assert multiply(A,B) == multiply(B,A)
    assert multiply(multiply(FRAME,A),FRAME) == B
    rotation = multiply(A,FRAME)
    assert order(rotation) == 4
    assert multiply(rotation,rotation) == multiply(A,B)
    assert multiply(multiply(FRAME,rotation),FRAME) == inverse(rotation)
    assert Counter(order(g) for g in ELEMENTS) == {1:1,2:5,4:2}
    transport = [g for g in ELEMENTS if g[2] == 0]
    assert all(multiply(g,h) == multiply(h,g) for g in transport for h in transport)
    assert {order(g) for g in transport} == {1,2}
    assert all(multiply(multiply(g,h),inverse(g)) in transport for g in ELEMENTS for h in transport)
    color_preserving = [g for g in ELEMENTS if all(to_state(act_arrow(g,a))[2] == to_state(a)[2] for a in arrows)]
    assert color_preserving == transport
    reversals = []
    for state in ELEMENTS:
        reversed_state = to_state(reverse(to_arrow(state)))
        # Reversal is right multiplication; physical frame changes act on the left.
        assert reversed_state == multiply(state,A)
        reversals.append({'state':state,'reversed':reversed_state})
    vertex_transport_counts = Counter()
    for source in VERTICES:
        for target in VERTICES:
            vertex_transport_counts[sum(act_vertex(g,source) == target for g in ELEMENTS)] += 1
    assert vertex_transport_counts == {2:16}
    framed_transports = []
    for source in ELEMENTS:
        for target in ELEMENTS:
            solutions = [g for g in ELEMENTS if multiply(g,source) == target]
            assert len(solutions) == 1
            expected = multiply(target,inverse(source))
            assert solutions == [expected]
            framed_transports.append({'source':source,'target':target,'transport':expected})
    # All 512 composable framed-state transitions obey transport composition.
    for source,middle,target in product(ELEMENTS,repeat=3):
        first = multiply(middle,inverse(source))
        second = multiply(target,inverse(middle))
        assert multiply(second,first) == multiply(target,inverse(source))
    # Minimal countercheck: direct products do not produce the claimed group.
    xor_orders = Counter(1 if g == IDENTITY else 2 for g in ELEMENTS)
    assert xor_orders == {1:1,2:7}  # C2^3 has no order-four element.
    payload = {
        'model':'Elements (x,y,f), bits; (v,f)(w,g)=(v+swap^f(w),f+g).',
        'scope':'Chosen four-position/two-frame local square model. No native geometry or Ramsey identification.',
        'transport_subgroup':transport,'frame_exchange':FRAME,'quarter_turn':rotation,
        'element_order_histogram':dict(Counter(order(g) for g in ELEMENTS)),
        'group_table':[[multiply(g,h) for h in ELEMENTS] for g in ELEMENTS],
        'states_and_elementary_arrows':[{'state':s,'tail':to_arrow(s)[0],'head':to_arrow(s)[1],
                                        'axis_color':'red' if s[2] == 0 else 'blue'} for s in ELEMENTS],
        'arrow_reversal':reversals,'framed_state_transporters':framed_transports,
        'unframed_transport_multiplicity':2,
        'counts':{'unframed_vertices':4,'framed_states':8,'elementary_directed_square_edges':8,
                  'group_elements':8,'all_framed_state_transitions_including_identities':64,
                  'associativity_checks':512,'framed_transition_composition_checks':512},
        'checks':{'D8_presentation':True,'transport_is_V4':True,'frame_exchanges_axes':True,
                  'node_arrow_bijection':True,'bijection_is_D8_equivariant':True,
                  'reversal_is_right_multiplication_by_A':True,'framing_removes_transporter_ambiguity':True,
                  'color_preserving_subgroup_is_exactly_V4':True},
        'limits':['The bijection uses framed vertices, not the four bare vertices.',
                  'Full D8 permits exchanging red and blue; fixed-color symmetry is only V4.',
                  'Elementary square edges are not all 64 transitions of the framed-state action groupoid.',
                  'The torsor becomes a group-labeled state space only after choosing a reference state.',
                  'A model-specific equivariant bijection is not automatically categorical duality or a Ramsey law.'],
    }
    target = Path(__file__).with_name('state_transport_d8_results.json')
    target.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'counts':payload['counts'],'checks':payload['checks'],'element_orders':payload['element_order_histogram']},indent=2))
    print('Verified and saved',target)

if __name__ == '__main__':main()
