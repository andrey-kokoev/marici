"""Registered retained path stages with separately scoped spectral readouts.

Finite rational coefficient interface, not a physical evolution constructor.
Reuse endpoint composition and indexed-family recovery; follow SpectralLedger's
identity-bound registration pattern without changing its triangle/depth contract.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import count

import check_natural_tower_return as algebra
from check_indexed_path_synthesis import compose, source, target, recover

mm, add, scale = algebra.mm, algebra.add, algebra.scale


def identity(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def zero(n):
    return tuple((F(0),) * n for _ in range(n))


def apply(matrix, vector):
    if not matrix or len(vector) != len(matrix[0]):
        raise ValueError('Coefficient dimension mismatch')
    return tuple(sum((a * b for a, b in zip(row, vector)), F(0)) for row in matrix)


def coefficients(values, size):
    result = tuple(values)
    if len(result) != size or any(not isinstance(v, (int, F)) for v in result):
        raise ValueError('Expected exact rational coefficient vector of the registered dimension')
    return tuple(F(v) for v in result)


@dataclass(frozen=True)
class SpectralDescriptor:
    name: str
    radicand: int
    eigenvalue: tuple
    projector: tuple  # pair of rational matrices; Q(sqrt(radicand))


@dataclass(frozen=True)
class PathStage:
    label: str
    paths: tuple
    parent: str | None
    parent_slots: tuple
    step_lift: tuple
    step_decoder: tuple
    origin_lift: tuple
    origin_decoder: tuple
    summary: tuple

    @property
    def word_length(self):
        return len(self.paths[0])


@dataclass(frozen=True)
class IndexedPathFamily:
    label: str
    stage: str
    direction: str
    groups: tuple


@dataclass(frozen=True)
class InheritedMode:
    label: str
    stage: str
    origin: str
    ordered_occurrences: tuple
    descriptor: SpectralDescriptor


@dataclass(frozen=True)
class WeightedPathFamily:
    label: str
    paths: tuple
    values: tuple
    word_length: int
    operation: str
    parents: tuple
    parent_slots: tuple
    origin_stage: str | None = None


@dataclass(frozen=True)
class CompositionBlock:
    vertex: object
    left_slots: tuple
    right_slots: tuple
    matrix: tuple
    rank_at_most_one: bool


class RetainedSuccessorLedger:
    """Own records by object identity; immutable fields retain complete words.

    Path coefficients may be arbitrary at any stage. Inherited spectral reads
    have a narrower domain: im(origin_lift), explicitly checked on every call.
    Parallel primitive IDs are allowed; sink extensions are rejected rather than
    silently dropping their parents. Stage word length is not a physical clock
    or a cell degree, and these are not triangle ModeIdentity promotions.
    """

    def __init__(self, packets, descriptors=()):
        self.packets = tuple(tuple(p) for p in packets)
        if not self.packets or any(len(p) != 3 for p in self.packets):
            raise ValueError('Nonempty labelled primitive registry required')
        self.labels = tuple(p[0] for p in self.packets)
        if len(set(self.labels)) != len(self.labels):
            raise ValueError('Primitive IDs must be unique')
        self._serial = count()
        self._stages, self._families, self._modes = {}, {}, {}
        self._payloads = {}
        n = len(self.packets)
        canonical_descriptors = []
        for descriptor in descriptors:
            if (not isinstance(descriptor, SpectralDescriptor)
                    or not isinstance(descriptor.name, str)
                    or not isinstance(descriptor.radicand, int)
                    or len(descriptor.projector) != 2
                    or any(len(part) != n for part in descriptor.projector)):
                raise ValueError('Explicit quadratic descriptor of the primitive dimension required')
            canonical_descriptors.append(SpectralDescriptor(
                descriptor.name, descriptor.radicand, coefficients(descriptor.eigenvalue, 2),
                tuple(tuple(coefficients(row, n) for row in part) for part in descriptor.projector)))
        self._descriptors = tuple(canonical_descriptors)
        self.continuation = tuple(tuple(F(ta == sb) for _, _, ta in self.packets)
                                  for _, sb, _ in self.packets)
        if self._descriptors:
            self._validate_spectrum()
        paths = tuple(((s, t, label),) for label, s, t in self.packets)
        I = identity(n)
        self._root = self._register_stage(paths, None, (), I, I, I, I, I)

    @property
    def root(self):
        return self._root

    def _register_stage(self, paths, parent, slots, lift, decoder, origin_lift, origin_decoder, summary):
        out = PathStage(f'path-stage:{next(self._serial)}', paths, parent, slots,
                        lift, decoder, origin_lift, origin_decoder, summary)
        self._stages[out.label] = out
        return out

    def resolve(self, stage):
        if not isinstance(stage, PathStage) or self._stages.get(stage.label) is not stage:
            raise ValueError('Unknown, foreign or substituted path stage')
        return stage

    def successor(self, parent):
        parent = self.resolve(parent)
        paths = tuple(sorted(compose(set(parent.paths), set(self.root.paths))))
        if {p[:-1] for p in paths} != set(parent.paths):
            raise ValueError('A parent has no extension; lossless successor unavailable')
        lookup = {p: i for i, p in enumerate(parent.paths)}
        slots = tuple(lookup[p[:-1]] for p in paths)
        lift = tuple(tuple(F(slot == i) for i in range(len(parent.paths))) for slot in slots)
        sizes = tuple(slots.count(i) for i in range(len(parent.paths)))
        decoder = tuple(tuple(lift[j][i] / sizes[i] for j in range(len(paths)))
                        for i in range(len(parent.paths)))
        summary = tuple(tuple(F(p[-1][2] == label) for p in paths) for label in self.labels)
        if mm(decoder, lift) != identity(len(parent.paths)):
            raise ValueError('Extension decoder does not recover parents')
        if mm(summary, lift) != mm(self.continuation, parent.summary):
            raise ValueError('Continuation summary square failed')
        return self._register_stage(paths, parent.label, slots, lift, decoder,
                                    mm(lift, parent.origin_lift), mm(parent.origin_decoder, decoder), summary)

    def deconstruct(self, stage):
        stage = self.resolve(stage)
        if stage.parent is None:
            return self.packets
        parent = self._stages[stage.parent]
        return parent, tuple((parent.paths[i], path[-1]) for i, path in zip(stage.parent_slots, stage.paths))

    def family(self, stage, direction):
        stage = self.resolve(stage)
        if direction not in ('source', 'target'):
            raise ValueError('Explicit source or target index required')
        field = source if direction == 'source' else target
        keys = tuple(sorted({field(p) for p in stage.paths}))
        groups = tuple((key, tuple(p for p in stage.paths if field(p) == key)) for key in keys)
        family = IndexedPathFamily(f'path-family:{next(self._serial)}', stage.label, direction, groups)
        self._families[family.label] = family
        return family

    def deconstruct_family(self, family):
        if not isinstance(family, IndexedPathFamily) or self._families.get(family.label) is not family:
            raise ValueError('Unknown, foreign or substituted indexed family')
        stage = self._stages[family.stage]
        field = source if family.direction == 'source' else target
        recovered = recover({key: set(paths) for key, paths in family.groups}, field)
        if recovered != set(stage.paths):
            raise ValueError('Indexed family lost a retained word')
        # Restore the stage's order; flattening group order is not a decoder.
        return stage.paths

    def transition(self, ancestor, descendant):
        ancestor, descendant = self.resolve(ancestor), self.resolve(descendant)
        chain, current = [], descendant
        while current is not ancestor:
            if current.parent is None:
                raise ValueError('Stages do not lie on the requested ancestor chain')
            chain.append(current)
            current = self._stages[current.parent]
        lift = decoder = identity(len(ancestor.paths))
        for child in reversed(chain):
            lift = mm(child.step_lift, lift)
            decoder = mm(decoder, child.step_decoder)
        return lift, decoder

    def encode(self, ancestor, descendant, values):
        lift, _ = self.transition(ancestor, descendant)
        return apply(lift, coefficients(values, len(ancestor.paths)))

    def decode(self, ancestor, descendant, values):
        lift, decoder = self.transition(ancestor, descendant)
        values = coefficients(values, len(descendant.paths))
        decoded = apply(decoder, values)
        if apply(lift, decoded) != values:
            raise ValueError('Payload is outside the requested transition image')
        return decoded

    def _register_payload(self, paths, values, length, operation, parents=(), slots=(), origin_stage=None):
        out = WeightedPathFamily(f'weighted-family:{next(self._serial)}', paths, values,
                                 length, operation, parents, slots, origin_stage)
        self._payloads[out.label] = out
        return out

    def resolve_payload(self, payload):
        if not isinstance(payload, WeightedPathFamily) or self._payloads.get(payload.label) is not payload:
            raise ValueError('Unknown, foreign or substituted weighted path family')
        return payload

    def retain_path_payload(self, paths, values):
        """Register a nonempty homogeneous family with supplied coefficients.

        Words may be a subset of a stage. Zero coefficients retain their word
        slots. Distinct occurrence IDs sharing endpoints stay distinct.
        """
        paths = tuple(tuple(tuple(edge) for edge in path) for path in paths)
        if not paths or not paths[0] or len(set(paths)) != len(paths):
            raise ValueError('Nonempty family of distinct nonempty path words required')
        length = len(paths[0])
        registry = {(s, t, label) for label, s, t in self.packets}
        for path in paths:
            if len(path) != length or any(edge not in registry for edge in path):
                raise ValueError('Words must have one length and use registered primitive records')
            if any(a[1] != b[0] for a, b in zip(path, path[1:])):
                raise ValueError('A supplied path has an unsewn endpoint')
        values = coefficients(values, len(paths))
        return self._register_payload(paths, values, length, 'supplied')

    def retain_payload(self, stage, values):
        stage = self.resolve(stage)
        values = coefficients(values, len(stage.paths))
        return self._register_payload(stage.paths, values, stage.word_length,
                                      'supplied', origin_stage=stage.label)

    def compose_payloads(self, left, right):
        """Compose arbitrary retained homogeneous path families bilinearly.

        The fixed cut makes every resulting word determine one parent pair.
        A structurally empty product is registered as empty, not as a nonempty
        family with numerically zero coefficients. Both operands remain stored.
        """
        left, right = self.resolve_payload(left), self.resolve_payload(right)
        paths = tuple(sorted(compose(set(left.paths), set(right.paths))))
        left_index = {path: i for i, path in enumerate(left.paths)}
        right_index = {path: i for i, path in enumerate(right.paths)}
        slots = tuple((left_index[path[:left.word_length]], right_index[path[left.word_length:]])
                      for path in paths)
        values = tuple(left.values[i] * right.values[j] for i, j in slots)
        return self._register_payload(paths, values, left.word_length + right.word_length,
                                      'compose', (left.label, right.label), slots)

    def deconstruct_payload(self, payload):
        """Recover stored operands, not a nonunique factorization of the output."""
        payload = self.resolve_payload(payload)
        return tuple(self._payloads[label] for label in payload.parents), payload.parent_slots

    def assembly_history(self, payload):
        payload = self.resolve_payload(payload)
        if payload.operation == 'supplied':
            return ('supplied', payload.label, payload.origin_stage)
        left, right = (self._payloads[label] for label in payload.parents)
        return ('compose', payload.label, left.word_length,
                self.assembly_history(left), self.assembly_history(right))

    def composition_blocks(self, left, right, candidate):
        """Describe single-product constraints at a specified retained cut.

        Candidate coefficients need not equal the supplied operands' product.
        Eligibility concerns existence of SOME factors on these operand word
        domains, not recovery or replacement of registered preparation history.
        """
        left, right, candidate = (self.resolve_payload(p) for p in (left, right, candidate))
        expected = compose(set(left.paths), set(right.paths))
        if (candidate.word_length != left.word_length + right.word_length
                or set(candidate.paths) != expected):
            raise ValueError('Candidate does not have this complete composition domain')
        values = dict(zip(candidate.paths, candidate.values))
        vertices = sorted({target(p) for p in left.paths} & {source(p) for p in right.paths})
        blocks = []
        for vertex in vertices:
            rows = tuple(i for i, p in enumerate(left.paths) if target(p) == vertex)
            columns = tuple(j for j, p in enumerate(right.paths) if source(p) == vertex)
            matrix = tuple(tuple(values[left.paths[i] + right.paths[j]] for j in columns) for i in rows)
            pivot = next(((i, j) for i in range(len(rows)) for j in range(len(columns)) if matrix[i][j]), None)
            rank_one = True
            if pivot is not None:
                i0, j0 = pivot
                rank_one = all(matrix[i][j] * matrix[i0][j0] == matrix[i][j0] * matrix[i0][j]
                               for i in range(len(rows)) for j in range(len(columns)))
            blocks.append(CompositionBlock(vertex, rows, columns, matrix, rank_one))
        return tuple(blocks)

    def compose_primitive_payloads(self, stage, left, right):
        """Existing free bilinear path product on a registered first successor.

        Both inputs are supplied primitive coefficient vectors. This neither
        prepares them physically nor assumes an arbitrary path payload is one
        separable product. The endpoint rule is already enforced by stage.paths.
        """
        stage = self.resolve(stage)
        if stage.parent != self.root.label:
            raise ValueError('Primitive composition requires a direct successor of the root')
        product = self.compose_payloads(self.retain_payload(self.root, left),
                                        self.retain_payload(self.root, right))
        if product.paths != stage.paths:
            raise ValueError('Primitive product does not match the registered successor carrier')
        return product.values

    def split_payload(self, stage, values):
        """Resolve arbitrary child coefficients into parent means and detail.

        The remainder lies in ker(step_decoder). Unlike decode(), this does not
        require the input to be an unchanged-copy output, and is not a claim
        that the remainder was independently prepared by successor().
        """
        stage = self.resolve(stage)
        if stage.parent is None:
            raise ValueError('The root has no preceding extension to split')
        values = coefficients(values, len(stage.paths))
        parent_values = apply(stage.step_decoder, values)
        inherited = apply(stage.step_lift, parent_values)
        return parent_values, tuple(x - y for x, y in zip(values, inherited))

    def reassemble_payload(self, stage, parent_values, remainder):
        stage = self.resolve(stage)
        if stage.parent is None:
            raise ValueError('The root has no preceding extension to reassemble')
        parent = self._stages[stage.parent]
        parent_values = coefficients(parent_values, len(parent.paths))
        remainder = coefficients(remainder, len(stage.paths))
        if any(apply(stage.step_decoder, remainder)):
            raise ValueError('Branch remainder must have zero mean within each sibling family')
        inherited = apply(stage.step_lift, parent_values)
        return tuple(x + y for x, y in zip(inherited, remainder))

    def summarize(self, stage, values):
        stage = self.resolve(stage)
        return apply(stage.summary, coefficients(values, len(stage.paths)))

    def _validate_spectrum(self):
        n = len(self.packets)
        Z, I = zero(n), identity(n)
        if len({d.name for d in self._descriptors}) != len(self._descriptors):
            raise ValueError('Spectral names must be unique')
        sums, weighted = {}, {}
        for descriptor in self._descriptors:
            d, E, lam = descriptor.radicand, descriptor.projector, descriptor.eigenvalue
            if (len(E) != 2 or any(len(m) != n or any(len(row) != n for row in m) for m in E)
                    or len(lam) != 2):
                raise ValueError('Incorrect primitive spectral dimensions')
            if algebra.rmul(E, E, d) != E:
                raise ValueError('Non-idempotent spectral descriptor')
            weighted_E = algebra.rscale(E, *lam, d)
            if (algebra.rmul((self.continuation, Z), E, d) != weighted_E
                    or algebra.rmul(E, (self.continuation, Z), d) != weighted_E):
                raise ValueError('Descriptor does not belong to this registry operator')
            sums[d] = algebra.radd(sums.get(d, (Z, Z)), E)
            weighted[d] = algebra.radd(weighted.get(d, (Z, Z)), weighted_E)
        total, synthesized = Z, Z
        for d in sums:
            if sums[d][1] != Z or weighted[d][1] != Z:
                raise ValueError('Incomplete quadratic conjugate family')
            total, synthesized = add(total, sums[d][0]), add(synthesized, weighted[d][0])
        if total != I or synthesized != self.continuation:
            raise ValueError('Incomplete spectral reconstruction')
        for i, a in enumerate(self._descriptors):
            for j, b in enumerate(self._descriptors):
                if i == j:
                    continue
                if a.radicand == b.radicand:
                    disjoint = algebra.rmul(a.projector, b.projector, a.radicand) == (Z, Z)
                else:
                    disjoint = all(mm(p, q) == Z for p in a.projector for q in b.projector)
                if not disjoint:
                    raise ValueError('Descriptors overlap; distinct-field sectors must annihilate coefficientwise')

    def inherit(self, stage, name):
        stage = self.resolve(stage)
        descriptor = next((d for d in self._descriptors if d.name == name), None)
        if descriptor is None:
            raise ValueError('No registered origin descriptor with this name')
        mode = InheritedMode(f'inherited-mode:{next(self._serial)}', stage.label,
                             self.root.label, self.labels, descriptor)
        self._modes[mode.label] = mode
        return mode

    def resolve_mode(self, mode):
        if not isinstance(mode, InheritedMode) or self._modes.get(mode.label) is not mode:
            raise ValueError('Unknown, foreign or substituted inherited descriptor')
        return self._stages[mode.stage]

    def inherited_projector(self, mode):
        """Return L E D: sums to the IMAGE projector, not the ambient identity."""
        stage = self.resolve_mode(mode)
        return tuple(mm(stage.origin_lift, mm(part, stage.origin_decoder)) for part in mode.descriptor.projector)

    def read_mode(self, mode, values):
        """A pair of rational vectors representing the descriptor's own field."""
        stage = self.resolve_mode(mode)
        original = self.decode(self.root, stage, values)
        return tuple(apply(stage.origin_lift, apply(part, original)) for part in mode.descriptor.projector)
