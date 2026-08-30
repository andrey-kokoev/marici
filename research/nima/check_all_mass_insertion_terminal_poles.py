"""Audit the all-chain terminal-pole incidence formula.

For a path x1--w1--...--wr--x2, enumerate connected vertex intervals that
contain the terminal white site wr and convert them to their cosmological
subgraph energies (site sum plus energies of cut boundary edges).
"""


def interval_energy_shift(start, end, white_count):
    vertices = ["x1"] + [f"w{i}" for i in range(1, white_count + 1)] + ["x2"]
    terminal_label = f"w{white_count}"
    terms = [
        vertex for vertex in vertices[start : end + 1]
        if vertex != terminal_label
    ]
    cut_edges = int(start > 0) + int(end < len(vertices) - 1)
    if cut_edges:
        terms = terms + (["y"] if cut_edges == 1 else ["2y"])
    return tuple(terms)


def terminal_interval_energies(white_count):
    terminal = white_count
    last_vertex = white_count + 1
    return {
        interval_energy_shift(start, end, white_count)
        for start in range(terminal + 1)
        for end in range(terminal, last_vertex + 1)
        if end >= terminal
    }


def formula_energies(white_count):
    result = set()
    for first_white in range(white_count, 0, -1):
        suffix = tuple(f"w{i}" for i in range(first_white, white_count))
        result.add(suffix + ("2y",))
        result.add(suffix + ("x2", "y"))
    all_but_terminal = tuple(f"w{i}" for i in range(1, white_count))
    result.add(("x1",) + all_but_terminal + ("y",))
    result.add(("x1",) + all_but_terminal + ("x2",))
    return result


def main():
    for white_count in range(1, 101):
        intervals = terminal_interval_energies(white_count)
        formula = formula_energies(white_count)
        assert intervals == formula
        assert len(formula) == 2 * white_count + 2

    derived_counts = {1: 4, 2: 6, 3: 8}
    for white_count, expected_count in derived_counts.items():
        assert len(formula_energies(white_count)) == expected_count

    print("all-chain terminal interval formula: PASS")
    print("verified white-site counts: 1..100")
    print("terminal pole count: 2r+2")


if __name__ == "__main__":
    main()
