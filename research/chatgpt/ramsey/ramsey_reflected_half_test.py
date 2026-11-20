"""Test half-exchange symmetry of the local 22-vertex catalogue (networkx)."""
from pathlib import Path
import networkx as nx


def main():
    path = Path(__file__).with_name('pauli-realization-catalogues') / 'r37_22.g6'
    hits = []
    records = path.read_bytes().splitlines()
    for i, line in enumerate(records, 1):
        g = nx.from_graph6_bytes(line)
        for p in nx.isomorphism.GraphMatcher(g, g).isomorphisms_iter():
            if all(p[v] != v and p[p[v]] == v for v in g):
                hits.append(i)
                if len(hits) == 1:
                    print('First witness (1-based record, 0-based vertex pairs):', i,
                          [(v,p[v]) for v in g if v < p[v]])
                break
    print('Records with a half exchange:', len(hits), '/', len(records))


if __name__ == '__main__':
    main()
