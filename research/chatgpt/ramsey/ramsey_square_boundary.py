"""Face-first model of the chosen C--AB fill; boundary matrices over F_2."""
from itertools import combinations


def rank(columns):
    pivots = {}
    for x in columns:
        while x:
            i = x.bit_length() - 1
            if i not in pivots:
                pivots[i] = x
                break
            x ^= pivots[i]
    return len(pivots)


def main():
    old = {(r, 3+j) for j in range(7) for r in range(3) if (j+1) >> r & 1}
    e = (2, 5)  # C -- column 3 (AB)
    edges = sorted(old | {e}); ids = {p:i for i,p in enumerate(edges)}
    old_faces, fresh = [], []
    for rs in combinations(range(3), 2):
        for cs in combinations(range(3,10), 2):
            square = {(r,c) for r in rs for c in cs}
            if square <= ids.keys():
                (fresh if e in square else old_faces).append(sum(1 << ids[p] for p in square))
    d1 = [(1<<r) | (1<<c) for r,c in edges]
    assert len(edges)==13 and rank(d1)==9
    assert len(old_faces)==3 and len(fresh)==4 and rank(old_faces)==3
    for f in old_faces + fresh:
        boundary=0
        for i,column in enumerate(d1):
            if f>>i & 1:boundary ^= column
        assert boundary==0
    assert all(rank(old_faces+[f])==4 for f in fresh)
    assert all(rank(old_faces+[f^g])==3 for f,g in combinations(fresh,2))
    for name,faces in [('old faces only',old_faces),('one additional face',old_faces+fresh[:1]),('all rectangles',old_faces+fresh)]:
        b=rank(faces);print(name,'faces',len(faces),'b1',len(edges)-rank(d1)-b,'b2',len(faces)-b)

if __name__=='__main__':main()
