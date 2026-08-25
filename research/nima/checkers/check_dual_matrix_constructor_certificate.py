"""Four countermodels proving selector/contact gate independence."""


def rank_mod2(matrix):
    a = [row[:] for row in matrix]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(len(a)):
            if r != rank and a[r][column]:
                a[r] = [x ^ y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def selector_complete(matrix, required_outputs=2):
    return rank_mod2(matrix) == required_outputs


def contact_safe(matrix):
    return max(map(sum, matrix)) <= 1


full = [[1, 0], [0, 1]]
deficient = [[1], [1]]
safe = [[1, 0], [0, 1]]
unsafe = [[1, 1]]

models = {
    "complete_safe": (full, safe, True, True),
    "complete_unsafe": (full, unsafe, True, False),
    "deficient_safe": (deficient, safe, False, True),
    "deficient_unsafe": (deficient, unsafe, False, False),
}

outcomes = {}
for name, (selector, contact, expected_selector, expected_contact) in models.items():
    outcome = (selector_complete(selector), contact_safe(contact))
    assert outcome == (expected_selector, expected_contact)
    outcomes[name] = outcome

assert set(outcomes.values()) == {
    (True, True),
    (True, False),
    (False, True),
    (False, False),
}

print("four dual-matrix outcomes:", outcomes)
print("PASS: selector completeness and contact safety are logically independent")
