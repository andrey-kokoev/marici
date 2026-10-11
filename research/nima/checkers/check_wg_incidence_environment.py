"""Source-incidence closure test using the retained 1836-arrow graph.

Unit squared arrow differences define a candidate stiffness. That metric is an
explicit convention, not an axiom of Layer1 WG. No inverse is fitted or added.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    path = ROOT/'results/twelve-triangle-1836-arrows.json'
    raw = path.read_bytes()
    arrows = json.loads(raw)
    pairs = [(tuple(a['source']), tuple(a['target'])) for a in arrows]
    assert len(pairs) == len(set(pairs)) == 1836
    nodes = sorted({v for edge in pairs for v in edge})
    assert len(nodes) == 108
    adjacency = defaultdict(set)
    for a,b in pairs:
        adjacency[a].add(b)
        adjacency[b].add(a)
    visited = {nodes[0]}
    queue = list(visited)
    while queue:
        v = queue.pop()
        for w in adjacency[v]-visited:
            visited.add(w)
            queue.append(w)
    assert len(visited) == 108
    counts = Counter((a[0],b[0]) for a,b in pairs)
    assert counts == {('raw','local'):108, ('local','aligned'):432, ('aligned','raw'):1296}

    def apply(x, factor=F(1)):
        out = {v:F(0) for v in nodes}
        for a,b in pairs:
            d = factor*(x[b]-x[a])
            out[b] += d
            out[a] -= d
        return out

    def pairing(a,b):
        return sum((a[v]*b[v] for v in nodes),F(0))

    ones = {v:F(1) for v in nodes}
    assert all(y == 0 for y in apply(ones).values())
    # Sum of squares and connectedness give kernel = constant vectors.
    trial = {v:F(i,108) for i,v in enumerate(nodes)}
    assert pairing(trial,apply(trial)) == sum((trial[b]-trial[a])**2 for a,b in pairs) > 0
    assert sum(apply(trial).values()) == 0

    # Uniform layer sources are the aggregate test fixture, not a claim that
    # they equal the nonuniform fine-coordinate intensity of the proton mode.
    proton = {v:F(v[0]=='raw',36) for v in nodes}
    witness = {v:F(v[0]=='aligned',36) for v in nodes}
    same_sign = {v:proton[v]+witness[v] for v in nodes}
    neutral = {v:proton[v]-witness[v] for v in nodes}
    assert sum(proton.values()) == sum(witness.values()) == 1
    assert sum(same_sign.values()) == 2
    assert sum(neutral.values()) == 0
    # Thus D x = proton, witness, or same_sign is inconsistent; neutral is
    # compatible. The following explicit solution verifies all 108 equations.
    values = {'raw':F(5,6912), 'local':F(1,6912), 'aligned':F(0)}
    x = {v:values[v[0]] for v in nodes}
    assert apply(x) == neutral
    assert apply({v:x[v]+7 for v in nodes}) == neutral
    response = pairing(neutral,x)
    assert response == F(5,6912)
    energy = pairing(x,apply(x))/2-pairing(neutral,x)
    assert energy == -F(5,13824)
    conductance = F(1296)+F(108*432,108+432)
    assert conductance == F(6912,5) and response == 1/conductance
    # Same arrows and source; two admissible metric normalizations.
    half = {v:x[v]/2 for v in nodes}
    assert apply(half,F(2)) == neutral
    assert pairing(neutral,half) == response/2
    # Doubling source strength multiplies the eliminated energy by four.
    assert pairing(neutral,{v:2*x[v] for v in nodes})*2 == 4*response
    result = dict(schema='marici.nima.wg-incidence-environment.v1',status='pass',
                  source=str(path.relative_to(ROOT.parent.parent)),
                  source_sha256=hashlib.sha256(raw).hexdigest(),
                  vertices=108,arrows=1836,connected=True,
                  layer_counts={f'{a}->{b}':n for (a,b),n in counts.items()},
                  candidate_stiffness='D=B B^T, unit metric on retained arrows',
                  kernel='constant vectors; dimension one by connectedness and sum-of-squares identity',
                  isolated_proton_source_total='1',isolated_witness_source_total='1',
                  same_sign_pair_source_total='2',neutral_pair_source_total='0',
                  neutral_fixture='uniform raw +1/36, uniform aligned -1/36, local zero',
                  effective_conductance=str(conductance),effective_response=str(response),
                  eliminated_neutral_energy=str(energy),
                  same_graph_doubled_stiffness_response=str(response/2),
                  controls=['all 108 neutral response equations', 'constant-shift invariance',
                            'nonneutral source contradicts zero row sum', 'stiffness-rescaling changes response'],
                  disposition='Incidence gives a candidate singular stiffness, not the previous positive definite environment. Neutral closure is explicit; isolated-source subtraction is unavailable without a reservoir/boundary completion.',
                  residual='Layer1 WG supplies no arrow metric, reservoir/boundary condition, or coupling strength. The unit metric and uniform layer sources are explicit test choices, not derived physical parameters.')
    out = ROOT/'results/wg-incidence-environment.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
