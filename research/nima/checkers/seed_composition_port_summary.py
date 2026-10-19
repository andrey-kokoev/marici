"""Derived source/last-occurrence summary of registered path composition.

Not a new path law: this is a homomorphic observation of compose_payloads.
Entries retain zero coefficients to distinguish admitted coarse support from
absence. Full words and assembly provenance stay in the owning ledger.
"""
from dataclasses import dataclass
from fractions import Fraction as F


@dataclass(frozen=True)
class PortSummary:
    registry: tuple
    # (starting vertex, final primitive occurrence, summed coefficient)
    entries: tuple


def summarize(ledger, payload):
    payload = ledger.resolve_payload(payload)
    values = {}
    for path, coefficient in zip(payload.paths, payload.values):
        key = (path[0][0], path[-1][2])
        values[key] = values.get(key, F(0)) + coefficient
    return PortSummary(ledger.packets, tuple((s,e,v) for (s,e),v in sorted(values.items())))


def compose(left, right):
    """Exact coarse image of chronological left-then-right composition.

    S(left*right)[s,f] = sum_(e,u:target(e)=u) S(left)[s,e] S(right)[u,f].
    Coarse support uses existence, independently of coefficient cancellation.
    """
    if left.registry != right.registry:
        raise ValueError('Different primitive registries')
    targets = {e:t for e,s,t in left.registry}
    result = {}
    for s,e,a in left.entries:
        for u,f,b in right.entries:
            if targets[e] == u:
                key = (s,f)
                result[key] = result.get(key, F(0)) + a*b
    return PortSummary(left.registry, tuple((s,e,v) for (s,e),v in sorted(result.items())))


def final_occurrences(summary):
    """Forget starting ports to obtain the older final-occurrence summary."""
    values = {e:F(0) for e,s,t in summary.registry}
    for s,e,value in summary.entries:
        values[e] += value
    return tuple(values[e] for e,s,t in summary.registry)
