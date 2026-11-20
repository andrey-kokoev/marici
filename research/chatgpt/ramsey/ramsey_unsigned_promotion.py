"""Unsigned local experiment. Rows are bits of a column mask; no solver/data files."""
from collections import Counter
from itertools import permutations


def paths(marks,r,j):
    # (row r, column k, other row s, column j): one almost closed rectangle.
    return [(k,s) for k,t in enumerate(marks) if t>>r&1
            for s in range(3) if t & marks[j] & (1<<s)]


def promotions(marks):
    scored=[(len(paths(marks,r,j)),r,j) for r in range(3)
            for j,t in enumerate(marks) if not t>>r&1]
    for score,r,j in scored:
        if score!=max(x[0] for x in scored):continue
        filled=marks[:];filled[j]|=1<<r
        # Give one new name to the filling event, copying the incident row
        # after closure, not naming each newly completed rectangle separately.
        extended=[t|(((t>>r)&1)<<3) for t in filled]
        yield score,r,j,filled,extended


def canonical(marks):
    return min(tuple(sorted(sum(((t>>a)&1)<<b for a,b in enumerate(p)) for t in marks))
               for p in permutations(range(3)))


if __name__=='__main__':
    base=list(range(1,8));results=list(promotions(base));assert len(results)==3
    assert len({canonical(filled) for _,_,_,filled,_ in results})==1
    print('empty-cell path counts:',Counter(len(paths(base,r,j)) for j,t in enumerate(base) for r in range(3) if not t>>r&1))
    for score,r,j,filled,extended in results:
        assert score==4 and filled.count(7)==2
        support={k+1 for k,t in enumerate(extended) if t&8}
        doubletons=[m for m in filled if m.bit_count()==2]
        assert support=={k+1 for k,t in enumerate(filled) if all(t&m for m in doubletons)}
        assert support=={k+1 for k,t in enumerate(filled) if t>>r&1}
        print('filled row', 'ABC'[r], 'column',j+1,'new row touches',sorted(support))
