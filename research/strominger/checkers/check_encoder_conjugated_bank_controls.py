"""Falsification under one bank phase family and existing discrete operations.

Exact rational orbit-span and overlap certificates, not a Lie algebra computation
or encoder compiler. A finite orbit basis does not assert a finite orbit group.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, tr, mm, inverse, blockdiag, enc, rank
from check_neutron_rest_energy_preflight import nullspace


def main():
    hashes = {}
    def load(name):
        p = BASE / 'results' / name
        raw = p.read_bytes()
        hashes[p.relative_to(ROOT).as_posix()] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw)
    source = load('neutron-seam-control-transport.json')
    memory = load('neutron-comparison-memory.json')
    assert source['status'] == memory['status'] == 'passed'
    M, B, Gamma = rat(source['metric']), rat(memory['residual_incidence']), rat(memory['memory_metric'])
    metric = blockdiag(M, Gamma)
    Mi = inverse(M)
    def mv(a, v):
        return [sum((x*y for x,y in zip(row,v) if x and y), F(0)) for row in a]
    def dot(a,b):
        return sum((x*y for x,y in zip(a,b) if x and y), F(0))
    def direction(P):
        return next(col for col in tr(P) if any(col))
    normals = []
    for i, item in enumerate(source['seam_controls']):
        P = rat(item['projector'])
        d = direction(P) + [F(0)]*21
        normals.append((f'seam:{i}', d))
    for i,row in enumerate(B):
        a = [Gamma[i][i]*x for x in mv(Mi,row)]
        d = a + [-F(j==i) for j in range(21)]
        assert dot(row,a) == 1
        normals.append((f'write:{i}',d))
    reflectors = []
    for label,d in normals:
        dual = mv(metric,d)
        norm = dot(d,dual)
        assert norm > 0
        reflectors.append((label,d,[2*x/norm for x in dual]))
    R = rat(source['native_rotation'])
    initial_item = next(x for x in source['source_pulses'] if x['frame']==0)
    initial = direction(rat(initial_item['projector'])) + [F(0)]*21
    # Every stored vector is an actual conjugate direction, not its echelon
    # residual. Echelon rows serve only for exact independence decisions.
    echelon = {}
    vectors, words = [], []
    def admit(v,word):
        row = v[:]
        for p,b in sorted(echelon.items()):
            q = row[p]
            if q:
                row = [x-q*y for x,y in zip(row,b)]
        p = next((i for i,x in enumerate(row) if x),None)
        if p is None:
            return False
        q = row[p]
        echelon[p] = [x/q for x in row]
        vectors.append(v)
        words.append(word)
        return True
    admit(initial,[])
    cursor = 0
    while cursor < len(vectors):
        v, word = vectors[cursor], words[cursor]
        for label,d,dual in reflectors:
            q = dot(dual,v)
            admit([x-q*y for x,y in zip(v,d)], word+[label])
        admit(mv(R,v[:24])+v[24:], word+['native_rotation'])
        cursor += 1
    assert rank(vectors) == len(vectors)
    gram = mm(mm(vectors,metric),tr(vectors))
    seen, queue = {0}, [0]
    tree = []
    while queue:
        i = queue.pop()
        for j in range(len(vectors)):
            if j not in seen and gram[i][j]:
                seen.add(j)
                queue.append(j)
                tree.append({'parent':i,'child':j,'metric_overlap':str(gram[i][j])})
    # Independent replay of every retained chronological conjugating word.
    lookup = {label:(d,dual) for label,d,dual in reflectors}
    for target,word in zip(vectors,words):
        v = initial[:]
        for label in word:
            if label == 'native_rotation':
                v = mv(R,v[:24])+v[24:]
            else:
                d,dual = lookup[label]
                q = dot(dual,v)
                v = [x-q*y for x,y in zip(v,d)]
        assert v == target
        assert dot(v,mv(metric,v)) == dot(initial,mv(metric,initial))
    target_survives = len(vectors)==44 and len(seen)==44
    complement = nullspace(mm(vectors,metric),45)
    polar_fixes_complement = all(not any(v[24:]) and not any(mv(B,v[:24])) for v in complement)
    assert len(complement)+len(vectors)==45
    p = Path(__file__).resolve()
    hashes[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    for p,h in hashes.items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    result = {
        'status':'pass', 'initial_bank_label':initial_item['label'],
        'initial_frame':0, 'orbit_span_dimension':len(vectors),
        'connected_nonorthogonality_graph':len(seen)==len(vectors),
        'max_conjugating_word_length':max(map(len,words)),
        'conjugating_words':words, 'directions':enc(vectors),
        'nonzero_overlap_spanning_tree':tree, 'source_hashes':hashes,
        'full_active_span_test_passed':target_survives,
        'orthogonal_complement_dimension':len(complement),
        'polar_encoder_fixes_entire_complement':polar_fixes_complement,
        'orthogonal_complement_basis':enc(complement),
        'disposition':('Full active span and connected overlaps survive with one bank phase family.' if target_survives else 'One-bank conjugation does not reproduce the 44-dimensional full active span; retain the measured restriction, not a full-family impossibility claim.'),
        'assumptions':['Permitted finite composition and inversion of these discrete software operations', 'The existing bank phase family is available as a parameterized software operation'],
        'not_established':['Encoder synthesis word', 'Full Lie algebra certificate', 'Arbitrary-accuracy compiler and bounds', 'Physical switching authority', 'Fresh replay of predecessor suites']}
    (BASE/'results/encoder-conjugated-bank-controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','orbit_span_dimension','connected_nonorthogonality_graph','max_conjugating_word_length','polar_encoder_fixes_entire_complement']}))


if __name__=='__main__':
    main()
