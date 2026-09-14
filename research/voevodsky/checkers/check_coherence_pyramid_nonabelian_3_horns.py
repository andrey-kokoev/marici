#!/usr/bin/env python3
"""Nonabelian 3-horn recovery and failures in an S3 plane-label model."""
import itertools, json
from pathlib import Path

E = (0, 1, 2)
S3 = list(itertools.permutations(E))

def mul(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in E)

def inv(p):
    out = [0] * 3
    for i, x in enumerate(p): out[x] = i
    return tuple(out)

def conj(a, x): return mul(mul(a, x), inv(a))
def name(p): return ''.join(str(i + 1) for i in p)

def main():
    # Tetrahedral equation: R(h234) h124 = L(h123) h134.
    a = (1, 0, 2)
    R = lambda x: conj(a, x)       # faithful invertible whiskering
    R_inv = lambda x: conj(inv(a), x)
    L = lambda x: x
    h123, h124, h134 = (1, 2, 0), (2, 1, 0), (0, 2, 1)
    target = mul(mul(L(h123), h134), inv(h124))
    h234 = R_inv(target)
    assert mul(R(h234), h124) == mul(L(h123), h134)
    assert [x for x in S3 if R(x) == target] == [h234]

    # Nonfaithful whiskering: every plane maps to the identity.
    R0 = lambda x: E
    no_fill_target = (1, 0, 2)
    no_fillers = [x for x in S3 if R0(x) == no_fill_target]
    many_fillers = [x for x in S3 if R0(x) == E]
    assert not no_fillers
    assert len(many_fillers) == 6

    result = {
        'schema': 'marici.voevodsky.coherence-pyramid-nonabelian-3-horns.v1',
        'plane_label_group': 'S3',
        'tetrahedral_equation': 'R(h234) h124 = L(h123) h134',
        'faithful_invertible_whiskering': {
            'forced_h234': name(h234),
            'filler_count': 1,
            'equation_passed': True,
        },
        'nonfaithful_whiskering': {
            'nonimage_target_filler_count': len(no_fillers),
            'identity_target_filler_count': len(many_fillers),
        },
        'residual': 'Horn existence is surjectivity onto the required target; horn uniqueness is injectivity of the whiskering map.',
        'claim_boundary': 'Finite nonabelian plane-label model; not construction of the full coherence-pyramid 2-category.',
    }
    out = Path(__file__).parents[1] / 'results' / 'coherence_pyramid_nonabelian_3_horns.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
