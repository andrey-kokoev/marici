"""Saturate the stored 39-parent after at most one valid red-edge deletion.
Counts are for labeled matrices, not isomorphism classes.
"""
from collections import Counter
from ramsey310_six_set_parent_test import base, full, independent, six

pairs = [(i,j) for i in range(39) for j in range(i)]
def addable(A,i,j):
    return not ((A[i] >> j & 1) or A[i] & A[j])
def toggle(A,i,j):
    A[i] ^= 1 << j; A[j] ^= 1 << i

def completions(A):
    opts = [(i,j) for i,j in pairs if addable(A,i,j)]
    def visit(k):
        if k == len(opts):
            if not any(addable(A,i,j) for i,j in opts): yield tuple(A)
            return
        i,j = opts[k]
        yield from visit(k+1)
        if addable(A,i,j):
            toggle(A,i,j); yield from visit(k+1); toggle(A,i,j)
    yield from visit(0)

if __name__ == '__main__':
    assert not independent(base,full,10)
    assert all(not(base[i]&base[j]) for i,j in pairs if base[i]>>j & 1)
    seen = set(completions(base.copy())); initial = len(seen)
    for i,j in pairs:
        if base[i]>>j & 1 and not independent(base,full & ~(base[i]|base[j]),8):
            A=base.copy(); toggle(A,i,j); seen.update(completions(A))
    hist=Counter(); misses=0
    for A in sorted(seen):
        s=six(A); misses+=s is None; hist[sum(x.bit_count() for x in A)//2]+=1
    A=max(seen,key=lambda a:(sum(x.bit_count() for x in a),a)); s=six(A)
    print('direct',initial,'all',len(seen),'edge histogram',sorted(hist.items()),'without obstruction',misses)
    print('example removed',[(i,j) for i,j in pairs if (base[i] & ~A[i])>>j&1], 'added',[(i,j) for i,j in pairs if (A[i] & ~base[i])>>j&1], 'six',s)
