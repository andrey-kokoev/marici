"""Interpret compatibility with next duality as preservation of the unordered matching pair, or of its shared residue. Test all four endpoint exchanges without choosing a target."""
from collections import Counter
from ramsey_strip_boundary_binary_search import leaves,target
from ramsey_strip_ordered_boundary_dualities import solutions,entry,exit
from ramsey_strip_matching_restart import turn

def image(m,f):return frozenset(tuple(sorted((f[i],f[j]))) for i,j in m)
for f in solutions:
    bits=exit.index(f[entry[0]]),entry.index(f[exit[0]])
    pairgood=[m for m in leaves if {image(m,f),image(turn(m),f)}=={m,turn(m)}];resgood=[m for m in leaves if image(m&turn(m),f)==m&turn(m)]
    print('port shifts',bits,'pair preserving',len(pairgood),'first branches',dict(Counter(leaves[m][0] for m in pairgood)),'target',target in pairgood,'residue preserving',len(resgood),'target',target in resgood)
