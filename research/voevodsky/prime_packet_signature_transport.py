"""Exact coordinate pullbacks for full-route signatures under packet growth.

Edges are (source_mask, added_label). Features are tuples of observed edges.
The empty feature reads total mass. Maps return integer linear combinations
of old features and never increase signature order.
"""
from collections import defaultdict


def canonical_feature(edges):
    """Return the ordered cylinder event, or None for incompatible constraints."""
    ordered = sorted(set(edges), key=lambda e: e[0].bit_count())
    previous_target = 0
    previous_level = -1
    for mask, label in ordered:
        if mask < 0 or label < 0 or mask & (1 << label):
            return None
        if mask.bit_count() <= previous_level or previous_target & ~mask:
            return None
        previous_level = mask.bit_count()
        previous_target = mask | (1 << label)
    return tuple(ordered)


def insertion_pullback(feature, old_count, slot):
    """Pull an (old_count+1)-packet feature back along insertion of the new label.

    The new label is old_count, inserted at the fixed slot 0..old_count.
    Output features live on the old labels 0..old_count-1.
    """
    if not 0 <= slot <= old_count:
        raise ValueError('Insertion slot outside the old route')
    feature = canonical_feature(feature)
    if feature is None:
        return {}
    bit = 1 << old_count
    full = (1 << old_count)-1
    old_edges = []
    cut = None
    for mask, label in feature:
        if label > old_count or mask & ~(full | bit):
            raise ValueError('Feature lies outside the target alphabet')
        if label == old_count:
            if mask & bit or mask.bit_count() != slot:
                return {}
            cut = mask
        else:
            old_mask = mask & full
            if bool(mask & bit) != (old_mask.bit_count() >= slot):
                return {}
            old_edges.append((old_mask, label))
    if cut is None or slot == old_count:
        if cut is not None and cut != full:
            return {}
        f = canonical_feature(old_edges)
        return {} if f is None else {f: 1}
    answer = defaultdict(int)
    # A vertex event at the cut is the sum of its mutually exclusive outgoing edges.
    for label in range(old_count):
        if cut & (1 << label):
            continue
        f = canonical_feature(old_edges+[(cut, label)])
        if f is not None:
            answer[f] += 1
    return dict(answer)


def deletion_pullback(feature, old_count):
    """Pull an old-packet feature back along deletion of label old_count.

    Each retained old edge has a lift before or after the deleted event.
    Incompatible combinations are removed by the endpoint constraints.
    """
    feature = canonical_feature(feature)
    if feature is None:
        return {}
    bit = 1 << old_count
    full = bit-1
    for mask, label in feature:
        if not 0 <= label < old_count or mask & ~full:
            raise ValueError('Feature lies outside the old alphabet')
    partials = [()]
    for mask, label in feature:
        next_partials = []
        for prefix in partials:
            for new_mask in (mask, mask | bit):
                f = canonical_feature(prefix+((new_mask, label),))
                if f is not None:
                    next_partials.append(f)
        partials = next_partials
    answer = defaultdict(int)
    for f in partials:
        answer[f] += 1
    return dict(answer)
