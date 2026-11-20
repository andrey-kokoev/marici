"""A seven-label tree forces the erased vZ sign in the joined-center example.
Input is only the projection of the partial table to these labels. No graph search.
P joins equal bits; X joins unequal bits. All other distinct pairs here are absent,
except vZ, known to be a single matching with unknown sign.
"""
from itertools import combinations

tree = [('A','a','X'), ('A','u','P'), ('u','C','X'), ('u','Z','P'),
        ('C','v','P'), ('v','B','X')]
bit = {'A':0}
for i,j,h in tree:
    assert i in bit and j not in bit
    bit[j] = bit[i] ^ (h == 'P')  # choose a nonedge on every tree link
assert len(bit)==7 and bit['v']==bit['Z']==0
predicted = 'P' if bit['v']==bit['Z'] else 'X'
print('independent selection on tree:',bit,'forced vZ:',predicted)

# Only after deriving the sign, check the partial data and prediction against
# the saved graph6 witness from ramsey_promoted_center_construction.py.
from pauli_realization_audit import decode_graph6
rows=decode_graph6('U`?IC?RGoS?h`MQLBA@H@i_@T?Ck?BQ?C?Eh?ATg')
labels='ABCabcuvdeZ';expected={frozenset((i,j)):h for i,j,h in tree}
expected[frozenset(('v','Z'))]=predicted
for i,j in combinations(bit,2):
    actual='.PX*'[(rows[2*labels.index(i)]>>(2*labels.index(j)))&3]
    assert actual==expected.get(frozenset((i,j)),'.')
print('all 21 projected entries match')
