"""Test the frozen source-index cut on an independently specified oscillator DAG."""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s
from check_berry_fibration_cut import canonical, fibrate, restore, cut

ROOT = Path(__file__).resolve().parents[3]


def transfer(rows, source, target):
    # Actual acyclic operation composition: multiply along a route, add routes.
    outgoing = {}
    for value, a, b in rows:
        outgoing.setdefault(a, []).append((value, b))
    def walk(a, visited):
        if a == target:
            return s.Integer(1)
        if a in visited:
            raise ValueError('Cyclic source outside this constructor')
        return sum((v*walk(b, visited | {a}) for v,b in outgoing.get(a, [])), s.Integer(0))
    return s.simplify(walk(source, set()))


def main():
    # 0 external input; 1 bath input; 2 oscillator amplitude; 3 external output.
    # g,h are real positive coupling amplitudes, rates g^2,h^2.
    g,h = s.symbols('g h', positive=True, real=True)
    delta = s.symbols('delta', real=True)
    chi = 1/((g*g+h*h)/2-s.I*delta)
    rows = canonical(((g*chi,0,2),(h*chi,1,2),(-g,2,3),(s.Integer(1),0,3)))
    grouped = fibrate(rows,1,range(4))
    assert restore(grouped) == rows
    # Apply the existing operation twice, retaining its intermediate fibers.
    # Each application groups by current source and reverses endpoint wiring,
    # exactly TableFibrationCycle.twice; two applications give its four.
    def advance(table):
        family = fibrate(table, 1, range(4))
        successor = canonical((v, b, a) for a, children in family[1] for v,b in children)
        return family, successor
    family1, stage1 = advance(rows)
    family2, stage2 = advance(stage1)
    assert stage2 == rows
    assert stage1 == canonical((v,b,a) for v,a,b in rows)
    # Read the intermediate presentation with its endpoint-exchange marker.
    oriented_stage1 = canonical((v,b,a) for v,a,b in stage1)
    assert oriented_stage1 == rows
    for source in (0,1):
        assert transfer(stage2,source,3) == transfer(rows,source,3)
        assert transfer(oriented_stage1,source,3) == transfer(rows,source,3)
    iteration = {
        'operation':'group-from then unpack-reversed; TableFibrationCycle.twice',
        'first_nonempty_fibers':[[a,len(children)] for a,children in family1[1] if children],
        'second_nonempty_fibers':[[a,len(children)] for a,children in family2[1] if children],
        'first_successor_edges':[[a,b] for _,a,b in stage1],
        'second_successor_edges':[[a,b] for _,a,b in stage2],
        'second_successor_equals_source':True,
        'marked_intermediate_response_preserved':True,
        'unmarked_intermediate_external_response':str(transfer(stage1,0,3)),
        'scope':'Two re-presentation operations, not two applications of an unspecified generative WG rule.'
    }
    r,q = transfer(rows,0,3),transfer(rows,1,3)
    assert s.simplify(r-(1-g*g*chi)) == 0
    assert s.simplify(q+g*h*chi) == 0
    weight = lambda z: s.simplify(z*s.conjugate(z))
    assert s.simplify(weight(r)+weight(q)-1) == 0
    fixture = {g:1,h:2,delta:0}
    assert r.subs(fixture) == s.Rational(3,5)
    assert q.subs(fixture) == -s.Rational(4,5)
    outcomes = []
    for selected in combinations(range(4),3):
        selected_rows = cut(grouped,selected)
        recovered = restore(fibrate(selected_rows,1,range(4)))
        assert recovered == selected_rows
        rr,qq = transfer(selected_rows,0,3),transfer(selected_rows,1,3)
        active = sorted({v for _,a,b in selected_rows for v in (a,b)})
        triangle = len(active)==3 and len(selected_rows)==3 and len({frozenset((a,b)) for _,a,b in selected_rows})==3
        faithful = s.simplify(rr-r)==0 and s.simplify(qq-q)==0
        outcomes.append({
            'selected_source_fibers':list(selected), 'active_vertices':active,
            'edges':[[a,b] for _,a,b in selected_rows],
            'literal_three_vertex_triangle':triangle, 'preserves_response_and_noise':faithful,
            'resonant_r':str(rr.subs(fixture)), 'resonant_q':str(qq.subs(fixture)),
            'resonant_commutator_weight':str(s.simplify((weight(rr)+weight(qq)).subs(fixture))),
        })
    assert not any(x['literal_three_vertex_triangle'] and x['preserves_response_and_noise'] for x in outcomes)
    literal = [x for x in outcomes if x['literal_three_vertex_triangle']]
    assert len(literal)==1 and literal[0]['resonant_commutator_weight']=='9/25'
    retained = [x for x in outcomes if x['preserves_response_and_noise']]
    assert len(retained)==1 and len(retained[0]['active_vertices'])==4
    # Exact readout of Aspect's supplied fixture, without its producer side effects.
    sources = ['research/aspect/markov-oscillator-loss-noise-identity.md',
               'research/aspect/checkers/markov_oscillator_loss_noise_identity.py',
               'research/strominger/checkers/check_berry_fibration_cut.py',
               'research/nima/agda/TableFibrationCycle.agda',
               str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result = {
        'status':'pass', 'scientific_disposition':'literal_triangle_candidate_falsified_for_this_source_presentation',
        'source':'Markov oscillator equations; no tetrahedral geometry supplied',
        'source_vertices':{'0':'external input','1':'bath input','2':'oscillator amplitude','3':'external output'},
        'source_edges':[[a,b] for _,a,b in rows], 'cuts':outcomes,
        'two_successive_applications':iteration,
        'general_loss_noise_identity':True,
        'rival_boundary':'Refutes this literal three-vertex source-index-cut interpretation, not all possible formed-triangle or structured tetrahedral presentations.',
        'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
    }
    out=ROOT/'research/strominger/results/oscillator-fibration-cut/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
