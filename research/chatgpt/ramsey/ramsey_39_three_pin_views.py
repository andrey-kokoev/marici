"""Three pinned-vertex exchanges on a typed lift of an arbitrary binary 3x9 matrix."""
from itertools import combinations, permutations

def views(x):
    orders=list(permutations(range(3))); blocks={k:{} for k in orders}
    for i,row in enumerate(x):
        for p in range(9):
            for q in range(9):
                v=(i,p,q); value=row[p],row[q]
                for k in orders:
                    cols=[j for j in k if j!=0]
                    blocks[k][tuple(v[j] for j in k)]=value if cols==[1,2] else value[::-1]
    return blocks

if __name__=='__main__':
    x=[[int((i*9+p)%5<2) for p in range(9)] for i in range(3)]
    b=views(x)
    for k,block in b.items():
        for a,c in combinations(range(3),2):
            s=list(range(3));s[a],s[c]=s[c],s[a];h=tuple(k[j] for j in s)
            rev=k.index(1)<k.index(2);rev^=h.index(1)<h.index(2)
            for v,w in block.items():assert b[h][tuple(v[j] for j in s)]==(w[::-1] if rev else w)
    assert all(b[0,1,2][i,p,p]==(x[i][p],)*2 for i in range(3) for p in range(9))
    print('6 orderings x 3 exchanges x 243 entries verified; diagonal recovers X')
