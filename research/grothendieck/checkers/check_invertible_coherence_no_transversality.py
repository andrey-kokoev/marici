"""Dependency-free checks for the invertible-coherence no-go."""


def ell(v):
    return v[0] + v[1]


def swap(v):
    return (v[1], v[0])


def main():
    checks = []
    v = (1, -1)
    tv = swap(v)

    checks.append(("hostile_state_nonzero", v != (0, 0)))
    checks.append(("hostile_state_scalar_null", ell(v) == 0))
    checks.append(("swap_is_involution", swap(tv) == v))
    checks.append(("readout_is_swap_invariant", ell(tv) == ell(v)))
    checks.append(("transported_state_remains_null", ell(tv) == 0))
    checks.append(("transported_state_nonzero", tv != (0, 0)))

    graph_state = (v, tv)
    checks.append(("coherent_graph_state_exists", graph_state[1] == swap(graph_state[0])))
    checks.append(("coherent_graph_state_still_null", ell(graph_state[0]) == ell(graph_state[1]) == 0))

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

