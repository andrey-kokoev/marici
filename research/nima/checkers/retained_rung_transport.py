"""Pinned exact-domain SOFTWARE transport; physical identification is separate.

Reuses the original fixture's incoming promotion and indexing functions. No
cross-target connector admission is performed by this module.
"""
from dataclasses import dataclass
from record_context_transport import T9_exact_domain
from branch_response_summary import summarize, combine, read

CONTRACT_ID = 'nima.T9.exact-domain.software.v1'


@dataclass(frozen=True)
class TransportResult:
    contract_id: str
    original: tuple
    final: tuple
    summary: object

    def source_view(self, fixture):
        return fixture['indexed'](self.final, 'source')

    def target_view(self, fixture):
        return fixture['indexed'](self.final, 'target')

    def observe(self, fixture):
        return read(self.summary, fixture['physical_reference'].value, fixture['m'])


def transport(rows, fixture):
    rows = tuple(rows)
    if not rows:
        raise ValueError('Transport needs a nonempty carrier-index table')
    if len({row.label for row in rows}) != len(rows):
        raise ValueError('Original labels must be unique')
    if len({(row.source, row.target) for row in rows}) != len(rows):
        raise ValueError('Pinned source table requires unique endpoint pairs')
    for row in rows:
        if (len(row.source) != 3 or len(row.target) != 3
                or row.source[0] not in ('a', 's')
                or row.target[0] != row.source[0]):
            raise ValueError('Expected tagged carrier-index endpoints, not common assembly roles')
        if row.members or row.mass <= 0:
            raise ValueError('Expected original positive-mass leaves, not promoted inputs')
    final = T9_exact_domain(rows, fixture)
    restored = fixture['leaves'](final)
    if restored != tuple(sorted(rows, key=lambda row: row.label)):
        raise ValueError('Transport did not recover original labelled leaves')

    old_to_new = {}
    new_to_old = {}
    summaries = []
    algebra = fixture['m']
    for family in final:
        child_summaries = []
        for child in family.members:
            leaves = fixture['leaves']((child,))
            if child.mass != sum(row.mass for row in leaves) or child.value != fixture['mean'](leaves):
                raise ValueError('Intermediate family response or mass is corrupt')
            child_summaries.append(summarize(leaves, lambda row: row.source[0], algebra))
        summary = combine(child_summaries, algebra)
        summaries.append(summary)
        if family.mass != sum(summary.masses) or family.value != fixture['mean'](family.members):
            raise ValueError('Final family response or mass is corrupt')
        for leaf in fixture['leaves']((family,)):
            old, new = leaf.target, family.target
            if old in old_to_new and old_to_new[old] != new:
                raise ValueError('Original context split')
            if new in new_to_old and new_to_old[new] != old:
                raise ValueError('Original contexts merged')
            old_to_new[old] = new
            new_to_old[new] = old
    summary = combine(summaries, algebra)
    if summary != summarize(rows, lambda row: row.source[0], algebra):
        raise ValueError('Branch summary failed staged/direct agreement')
    return TransportResult(CONTRACT_ID, rows, final, summary)


def T9(rows, fixture):
    """Public entrypoint for the pinned SOFTWARE T9 contract."""
    return transport(rows, fixture)


def T8(source_view, fixture):
    return transport(fixture['unindex'](source_view), fixture).source_view(fixture)


def T7(target_view, fixture):
    return transport(fixture['unindex'](target_view), fixture).target_view(fixture)
