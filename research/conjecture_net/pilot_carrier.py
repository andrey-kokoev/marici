"""Finite retained relational carrier fragment for the native Bool pilot.

Not a universal Carrier or physical model. Paths retain their operation words;
matching endpoints do not identify them. TickFragment uses only the existing
fixed-source Bool Tick classification, not a classification of arbitrary paths.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product

Label = tuple[bool, bool]
LABELS: tuple[Label, ...] = tuple(product((False, True), repeat=2))
NAMESPACE = 'programme.native-bool-retained-fragment.v1'


class Operation(Enum):
    LEFT = 'left'
    RIGHT = 'right'


class Schedule(Enum):
    LEFT_FIRST = 'leftFirst'
    RIGHT_FIRST = 'rightFirst'


def require_label(label):
    if not isinstance(label, tuple) or len(label) != 2 or any(type(value) is not bool for value in label):
        raise ValueError('expected a Bool x Bool source label')


def apply(operation: Operation, source: Label) -> Label:
    require_label(source)
    if operation is Operation.LEFT:
        return not source[0], source[1]
    if operation is Operation.RIGHT:
        return source[0], not source[1]
    raise ValueError('unknown native operation')


def schedule_word(schedule: Schedule) -> tuple[Operation, ...]:
    if schedule is Schedule.LEFT_FIRST:
        return Operation.LEFT, Operation.RIGHT
    if schedule is Schedule.RIGHT_FIRST:
        return Operation.RIGHT, Operation.LEFT
    raise ValueError('unknown retained schedule')


@dataclass(frozen=True)
class PathRecord:
    source: Label
    operations: tuple[Operation, ...]

    def __post_init__(self):
        require_label(self.source)
        if not isinstance(self.operations, tuple) or any(type(op) is not Operation for op in self.operations):
            raise ValueError('invalid operation word')

    @property
    def trace(self) -> tuple[Label, ...]:
        labels = [self.source]
        for operation in self.operations:
            labels.append(apply(operation, labels[-1]))
        return tuple(labels)

    @property
    def target(self) -> Label:
        return self.trace[-1]

    @property
    def structural_id(self):
        return NAMESPACE, self.source, tuple(op.value for op in self.operations)

    def then(self, following: 'PathRecord') -> 'PathRecord':
        if self.target != following.source:
            raise ValueError('noncomposable source attachment')
        return PathRecord(self.source, self.operations + following.operations)


@dataclass(frozen=True)
class TickFragment:
    source: Label
    first: Schedule
    second: Schedule

    def __post_init__(self):
        require_label(self.source)
        if type(self.first) is not Schedule or type(self.second) is not Schedule:
            raise ValueError('invalid schedule tags')

    @property
    def routes(self):
        return tuple(PathRecord(self.source, schedule_word(schedule)) for schedule in (self.first, self.second))

    @property
    def tags(self):
        return self.first, self.second

    @property
    def seam_labels(self):
        # Accepted return starts at both-flipped source and executes the
        # positive-phase legs in reversed order, not inverse-phase reversal.
        target = self.routes[0].target
        return tuple(apply(schedule_word(schedule)[1], target) for schedule in self.tags)

    @classmethod
    def rebuild(cls, source, tags):
        if not isinstance(tags, tuple) or len(tags) != 2:
            raise ValueError('expected ordered schedule pair')
        return cls(source, *tags)

    def swap(self):
        return TickFragment(self.source, self.second, self.first)


@dataclass(frozen=True)
class Occurrence:
    occurrence_id: str
    record: PathRecord

    def __post_init__(self):
        if not isinstance(self.occurrence_id, str) or not self.occurrence_id:
            raise ValueError('missing occurrence identity')
        if type(self.record) is not PathRecord:
            raise ValueError('invalid retained record')


@dataclass(frozen=True)
class Family:
    family_id: tuple
    grouping_key: str
    key_value: Label
    members: tuple[Occurrence, ...]


def promote(occurrences: tuple[Occurrence, ...], grouping_key: str, batch_id: str) -> tuple[Family, ...]:
    """Retaining grouping only. No all-pairs product is implied or created."""
    if grouping_key not in ('source', 'target'):
        raise ValueError('grouping key must be explicitly source or target')
    if not isinstance(batch_id, str) or not batch_id:
        raise ValueError('promotion requires an explicit batch namespace')
    ids = [occurrence.occurrence_id for occurrence in occurrences]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate occurrence identity')
    grouped = {}
    for occurrence in occurrences:
        value = getattr(occurrence.record, grouping_key)
        grouped.setdefault(value, []).append(occurrence)
    return tuple(Family((NAMESPACE, batch_id, 'family', grouping_key, value), grouping_key, value, tuple(members))
                 for value, members in sorted(grouped.items()))


def label_index(label: Label) -> int:
    require_label(label)
    return 2 * int(label[0]) + int(label[1])


def basis(label: Label):
    index = label_index(label)
    return tuple(int(i == index) for i in range(4))


def native_permutation(operation: Operation):
    # Columns are source images; row order is the contract's 00,01,10,11.
    images = [label_index(apply(operation, source)) for source in LABELS]
    return tuple(tuple(int(row == images[column]) for column in range(4)) for row in range(4))


def intensity(vector):
    """Mathematical coordinate intensities, not a Born probability assertion."""
    if len(vector) != 4:
        raise ValueError('expected four complex coordinates')
    return tuple(abs(value) ** 2 for value in vector)
