"""Distinguish window length from group size. Compare full and width-8/16 landing signatures; then act by eight cage symmetries and an independent reversal of visit order on each half-route. Do not normalize the starting pole."""
from ramsey_strip_next_row_restart import first,swapped
from ramsey_strip_ordered_boundary_dualities import solutions
from collections import Counter
G={tuple(range(30))};todo=list(G)
while todo:
    g=todo.pop()
    for f in solutions:
        h=tuple(f[v] for v in g)
        if h not in G:G.add(h);todo.append(h)
assert len(G)==8
for w in (6,8,16):print('width',w,'distinct landing signatures',len({(p+swapped(p)[-2::-1])[-w:] for p in first}))
ops=[(g,b) for g in G for b in (0,1)];act=lambda p,g,b:tuple(g[v] for v in (p[::-1] if b else p));print('orbit sizes over the five directed halves',Counter(len({act(p,g,b) for g,b in ops}) for p in first));assert len({tuple(act(p,g,b) for p in sorted(first)) for g,b in ops})==16
