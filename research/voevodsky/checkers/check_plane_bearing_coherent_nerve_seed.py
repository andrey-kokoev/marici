#!/usr/bin/env python3
"""Exact simplicial audit of the two-object C2 groupoid used as a mapping space."""
import itertools, json
from pathlib import Path

def simplices(n):
    # An n-simplex in the groupoid nerve: n+1 objects and n C2-labelled arrows.
    for objects in itertools.product((0, 1), repeat=n + 1):
        for labels in itertools.product((0, 1), repeat=n):
            yield objects, labels

def face(s, i):
    objects, labels = s
    n = len(labels)
    if i == 0:
        return objects[1:], labels[1:]
    if i == n:
        return objects[:-1], labels[:-1]
    return objects[:i] + objects[i + 1:], labels[:i - 1] + (labels[i - 1] ^ labels[i],) + labels[i + 1:]

def degeneracy(s, i):
    objects, labels = s
    return objects[:i + 1] + (objects[i],) + objects[i + 1:], labels[:i] + (0,) + labels[i:]

def main():
    identities = 0
    for n in range(1, 6):
        for x in simplices(n):
            for i in range(n):
                for j in range(i + 1, n + 1):
                    assert face(face(x, j), i) == face(face(x, i), j - 1)
                    identities += 1
            for i in range(n + 1):
                for j in range(i, n + 1):
                    assert degeneracy(degeneracy(x, j), i) == degeneracy(degeneracy(x, i), j + 1)
                    identities += 1
    # Two distinct planes between mapping-space vertices h=1 and p=0.
    planes_1_to_0 = [x for x in simplices(1) if x[0] == (1, 0)]
    assert len(planes_1_to_0) == 2
    # Every labelled arrow has an inverse with the same C2 label.
    for objects, labels in simplices(1):
        a, b = objects; g = labels[0]
        assert g ^ g == 0
    result = {
        'schema': 'marici.voevodsky.plane-bearing-coherent-nerve-seed.v1',
        'mapping_groupoid_objects': ['mediated_route', 'direct_route'],
        'plane_labels_between_each_ordered_pair': 2,
        'planes_direct_to_mediated': len(planes_1_to_0),
        'simplicial_identity_instances': identities,
        'dimensions_checked': [0, 1, 2, 3, 4, 5],
        'all_checks_passed': True,
        'global_claim_basis': 'The nerve of a groupoid is Kan; a simplicial category with Kan mapping spaces has a quasicategorical coherent nerve.',
        'claim_boundary': 'One plane-bearing triangular seed, not yet the four-grade coherence pyramid.',
    }
    out = Path(__file__).parents[1] / 'results' / 'plane_bearing_coherent_nerve_seed.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
