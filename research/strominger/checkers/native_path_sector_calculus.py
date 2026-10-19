"""Endpoint normal forms and retained algebraic comparison traces.

Words denote left-to-right matrix products, hence rightmost-first execution on
column states. A normal form NEVER replaces a retained execution word.
No matrices or supplied chart operations are used by the symbolic reducer.
"""
from itertools import product

Q_ONE = (0, 0, 0)
Q_A = (0, 1, 0)
Q_B = (0, 0, 1)
Q_C = (0, 1, 1)
ONE = (*Q_ONE, 0)
CENTRAL = (1, 0, 0, 0)
A = (*Q_A, 0)
B = (*Q_B, 0)
C = (*Q_C, 0)
T = (0, 0, 0, 1)
NORMAL_FORMS = tuple(product(range(2), range(2), range(2), range(3)))


def qmul(q, r):
    """z^e a^i b^j times z^f a^u b^v, with a²=b²=z, ba=zab."""
    e, i, j = q
    f, u, v = r
    return ((e + f + j*u + (i+u)//2 + (j+v)//2) % 2,
            (i+u) % 2, (j+v) % 2)


def phi(q):
    """Conjugation by t: a -> b, b -> ab, z -> z."""
    e, i, j = q
    out = (e, 0, 0)
    if i:
        out = qmul(out, Q_B)
    if j:
        out = qmul(out, Q_C)
    return out


def multiply(x, y):
    if x not in NORMAL_FORMS or y not in NORMAL_FORMS:
        raise ValueError('normal form domain')
    q, r = x[:3], y[:3]
    for _ in range(x[3]):
        r = phi(r)
    return (*qmul(q, r), (x[3]+y[3]) % 3)


def power(x, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('nonnegative exponent')
    out = ONE
    for _ in range(n):
        out = multiply(out, x)
    return out


def signed_axis(axis, sign):
    if axis not in range(3) or sign not in (-1, 1):
        raise ValueError('signed axis domain')
    q = (A, B, C)[axis]
    return q if sign == 1 else multiply(CENTRAL, q)


def word_normal_form(word):
    out = ONE
    for axis, sign in word:
        out = multiply(out, signed_axis(axis, sign))
    return out


def sector_certificate(omitted_axis, signs):
    if omitted_axis not in range(3) or len(signs) != 2 or any(s not in (-1, 1) for s in signs):
        raise ValueError('sector domain')
    axes = tuple(a for a in range(3) if a != omitted_axis)
    orbit_power = next(r for r in range(3)
                       if set((r, (r+1) % 3)) == set(axes))
    orbit_pair = (orbit_power, (orbit_power+1) % 3)
    sign_map = dict(zip(axes, signs))
    left = tuple(zip(axes, signs))
    return {
        'omitted_axis': omitted_axis,
        'signs': tuple(signs),
        'seed': 'ab=zba',
        'cyclic_conjugation_power': orbit_power,
        'orbit_pair': orbit_pair,
        'inverted_seed_positions': tuple(i for i, a in enumerate(orbit_pair) if sign_map[a] == -1),
        'exchange_route_order': orbit_pair != axes,
        'left': left,
        'right': tuple(reversed(left)),
        'phase_bit': 1,
    }


def verify_sector(certificate):
    expected = sector_certificate(certificate['omitted_axis'], certificate['signs'])
    if certificate != expected:
        raise ValueError('forged sector derivation')
    left = word_normal_form(certificate['left'])
    right = word_normal_form(certificate['right'])
    if left != multiply(CENTRAL, right):
        raise ValueError('sector relation residual')
    return True


def swap_trace(word, positions):
    """Each distinct-axis adjacent exchange contributes the central z."""
    current = tuple(word)
    word_normal_form(current)  # Validate signed tokens, including untouched ones.
    steps = []
    for position in positions:
        if not isinstance(position, int) or not 0 <= position < len(current)-1:
            raise ValueError('swap position')
        if current[position][0] == current[position+1][0]:
            raise ValueError('distinct axes required')
        updated = list(current)
        updated[position], updated[position+1] = updated[position+1], updated[position]
        updated = tuple(updated)
        steps.append({'position': position, 'before': current,
                      'after': updated, 'phase_bit': 1})
        current = updated
    return {'input': tuple(word), 'output': current, 'steps': tuple(steps),
            'phase_bit': len(steps) % 2}


def verify_trace(trace):
    positions = tuple(step['position'] for step in trace['steps'])
    expected = swap_trace(trace['input'], positions)
    if trace != expected:
        raise ValueError('forged swap trace')
    correction = CENTRAL if trace['phase_bit'] else ONE
    if word_normal_form(trace['input']) != multiply(correction, word_normal_form(trace['output'])):
        raise ValueError('trace relation residual')
    return True
