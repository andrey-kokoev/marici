"""Audit residual coordinate symmetry on two unchanged copies. Run with uv run --with networkx."""
from collections import Counter
from pathlib import Path
import networkx as nx


def main():
    # The first four objects are the three coordinate functions and parity.
    masks = [1, 2, 4, 7] + list(range(1, 8))
    swap = lambda m: (m & 4) | ((m & 1) << 1) | ((m & 2) >> 1)
    fixed = 2 * sum(swap(m) == m for m in masks)
    path = Path(__file__).parent / 'pauli-realization-catalogues/r37_22.g6'
    counts = Counter(); records = 0
    for line in path.read_bytes().splitlines():
        graph = nx.from_graph6_bytes(line); records += 1
        counts.update({sum(p[v] == v for v in graph)
                       for p in nx.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter()
                       if all(p[p[v]] == v for v in graph)})
    print('records', records, 'required fixed vertices', fixed, 'record counts', sorted(counts.items()))
    assert records == 191 and fixed == 10 and not counts[fixed]

if __name__ == '__main__': main()
