"""Exact additive outer summaries for a declared two-branch response task.

Branch selectors, reference, member masses and matrix operations are explicit
inputs. This interface does not select endpoints or admit new compositions.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class BranchSummary:
    masses: tuple
    sums: tuple


def summarize(rows, branch, algebra):
    masses = [0, 0]
    sums = [algebra['Z'], algebra['Z']]
    for row in rows:
        tag = branch(row)
        if tag not in ('a', 's') or row.mass <= 0:
            raise ValueError('Expected positive member masses and an explicit a/s branch')
        i = 0 if tag == 'a' else 1
        masses[i] += row.mass
        sums[i] = algebra['add'](sums[i], algebra['scale'](row.mass, row.value))
    return BranchSummary(tuple(masses), tuple(sums))


def combine(summaries, algebra):
    masses = [0, 0]
    sums = [algebra['Z'], algebra['Z']]
    for summary in summaries:
        for i in range(2):
            masses[i] += summary.masses[i]
            sums[i] = algebra['add'](sums[i], summary.sums[i])
    return BranchSummary(tuple(masses), tuple(sums))


def read(summary, reference, algebra):
    if any(m <= 0 for m in summary.masses):
        raise ValueError('Both branch means require nonempty positive-mass branches')
    a, s = [algebra['scale'](Fraction(1, m), value)
            for m, value in zip(summary.masses, summary.sums)]
    total = sum(summary.masses)
    raw = algebra['scale'](Fraction(1, total),
                           algebra['add'](*summary.sums))
    return {
        'masses': summary.masses,
        'J4': algebra['add'](raw, algebra['scale'](-1, reference)),
        'contrast': algebra['add'](a, algebra['scale'](-1, s)),
        'branch_residuals': (algebra['add'](a, algebra['scale'](-1, reference)),
                             algebra['add'](s, algebra['scale'](-1, reference))),
    }


def recover(J4, contrast, masses, algebra):
    if any(m <= 0 for m in masses):
        raise ValueError('Both branch means require positive branch masses')
    total = sum(masses)
    return (algebra['add'](J4, algebra['scale'](Fraction(masses[1], total), contrast)),
            algebra['add'](J4, algebra['scale'](-Fraction(masses[0], total), contrast)))
