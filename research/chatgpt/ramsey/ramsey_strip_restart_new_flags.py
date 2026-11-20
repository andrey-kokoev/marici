"""Compare novelty of incidence support, an oriented matching, and the shared residue at restart."""
from ramsey_strip_unique_restart_memory import states, turn

features = {
    'two-matching support': lambda m: m | turn(m),
    'oriented matching': lambda m: m,
    'shared residue': lambda m: m & turn(m),
}
for name, feature in features.items():
    history = feature(states[2, 0]) | feature(states[3, 1])
    fresh = {q: feature(m) - history for q, m in states.items()}
    assert not fresh[2, 0]
    print(name, 'previous total', len(history), 'next 2A', sorted(fresh[2, 0]),
          'next 5A', sorted(fresh[5, 0]))
    if name == 'two-matching support':
        assert len(history) == 36 and not any(fresh.values())
    elif name == 'oriented matching':
        assert len(fresh[5, 0]) == 4
    else:
        assert fresh[5, 0] == {(10, 28), (11, 22)}
        history |= fresh[5, 0]
        assert all(feature(m) <= history for m in states.values())
