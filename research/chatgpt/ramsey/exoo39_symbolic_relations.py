"""Generate Exoo's labeled graph from pentagon offsets and four extra vertices."""
import csv
from pathlib import Path

OFFSETS = [(1,0,0,3,1,3),(2,2,1,4,4),(4,2,4,1),(1,3,4),(1,2),(3,),()]
EXTRA = {35:(27,29,33,36,37,38),36:(4,6,10,16,21,23,28,34),
         37:(2,9,13,22,24,26,32),38:(4,8,12,18,20,22,30)}

def edges():
    E=set()
    def join(a,b): E.add(tuple(sorted((a,b))))
    for i,row in enumerate(OFFSETS):
        for t in range(5):
            join(5*i+t,5*i+(t+1)%5)
            for j,h in enumerate(row,i+1): join(5*i+t,5*j+(t+h)%5)
    E.remove((4,22))
    for i,neighbors in EXTRA.items():
        for j in neighbors:join(i,j)
    return E

if __name__=='__main__':
    E=edges(); path=Path(__file__).with_name('ramsey_3_10_witness_39.csv')
    with path.open() as f: A=[[int(x) for x in row] for row in csv.reader(f)]
    assert A==[[int(tuple(sorted((i,j))) in E) for j in range(39)] for i in range(39)]
    print('All 1521 entries match;',len(E),'red edges.')
