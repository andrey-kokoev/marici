"""Binary readings on an addressed cube. A square agrees if its edge XOR is zero.
Compare two cubes at matching corners, with the comparison transported along edges.
"""
from itertools import combinations


def edges(d):
    return [(v,v^(1<<i)) for v in range(1<<d) for i in range(d) if not v&(1<<i)]

def gradient(p,E):
    return sum((((p>>v)^(p>>w))&1)<<i for i,(v,w) in enumerate(E))

def main():
    for d in range(4):
        E=edges(d); index={tuple(sorted(e)):i for i,e in enumerate(E)};faces=[]
        for i,j in combinations(range(d),2):
            for v in range(1<<d):
                if v&((1<<i)|(1<<j)):continue
                a,b=v^(1<<i),v^(1<<j);c=a^(1<<j)
                faces.append(sum(1<<index[tuple(sorted(e))] for e in [(v,a),(a,c),(v,b),(b,c)]))
        flat={x for x in range(1<<len(E)) if all((x&f).bit_count()%2==0 for f in faces)}
        roots={gradient(p,E):p for p in range(0,1<<(1<<d),2)}
        assert set(roots)==flat
        print(d,1<<d,d*(d-1)//2,len(faces),len(flat))
    full=(1<<8)-1;constant=0
    for a in flat:
        for b in flat:
            p=roots[a^b];assert gradient(p^full,E)==a^b
            constant+=p==0
    print('pairs',len(flat)**2,'constant comparison possible',constant)

if __name__=='__main__':main()
