"""Can a cyclic relabelling reconcile source and literal reflections?"""

import json


ROAD = (2, 1, 0, 2, 1, 0)


def source_reflection(sector):
    return (1 - sector) % 6


def literal_reflection(sector):
    return (5 - sector) % 6


def main():
    conjugating_translations = []
    road_preserving = []
    road_shifts = {}
    for shift in range(6):
        intertwines = all(
            (source_reflection(i) + shift) % 6
            == literal_reflection((i + shift) % 6)
            for i in range(6)
        )
        if not intertwines:
            continue
        conjugating_translations.append(shift)
        shifts = {
            (ROAD[(i + shift) % 6] - ROAD[i]) % 3
            for i in range(6)
        }
        assert len(shifts) == 1
        road_shift = shifts.pop()
        road_shifts[str(shift)] = road_shift
        if road_shift == 0:
            road_preserving.append(shift)

    assert conjugating_translations == [2, 5]
    assert road_shifts == {"2": 1, "5": 1}
    assert road_preserving == []

    print(json.dumps({
        "status": "falsified_scoped_road_preserving_reflection_conjugacy",
        "source_reflection": "i -> 1-i mod 6",
        "literal_vertex_star_reflection": "i -> 5-i mod 6",
        "cyclic_conjugating_translations": conjugating_translations,
        "road_shift_by_translation": road_shifts,
        "road_preserving_conjugacies": road_preserving,
        "scalar_character_can_repair": False,
        "conclusion": (
            "The reflections are abstractly conjugate, but every conjugacy "
            "rotates the independently fixed complementary road by +1.  A "
            "line character changes coefficients only and cannot repair the "
            "support permutation."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
