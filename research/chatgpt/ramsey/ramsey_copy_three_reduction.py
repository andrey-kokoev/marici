"""Finite local proof obligation for both donor orientations: every outsider touching the seed receives exactly one port colour after clipping. For each omitted port, every old vertex missed by the other three avoids both its seed endpoints. They can be adjoined simultaneously."""
from itertools import permutations
from ramsey_neighbourhood_square import D,json,bits

def prove():
    E=[5,9,6,10];out=[] # 02,03,12,13
    for rot in permutations(range(4)):
        if any(e>>v&1 for e,v in zip(E,rot)):continue
        table=[]
        for neighbours in range(16):
            if neighbours&3==3 or neighbours&12==12:continue # triangle on an old edge
            colors=sum(1<<i for i,(e,x) in enumerate(zip(E,rot)) if neighbours>>x&1 and not e&neighbours);assert colors.bit_count()==bool(neighbours)
            for j,e in enumerate(E):
                if not colors&~(1<<j):assert not neighbours&e
            table.append([neighbours,colors])
        assert all(sum(e>>x&1 for e in E)==2 for x in range(4));out.append(dict(donors=rot,table=table))
    assert len(out)==2;return out
if __name__=='__main__':
    z=prove();print(z);(D/'ramsey_copy_three_reduction.json').write_text(json.dumps(z)+'\n')
