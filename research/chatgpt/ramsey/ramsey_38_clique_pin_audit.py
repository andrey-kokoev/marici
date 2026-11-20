"""Erase one pair at a time; test both colors against singleton and six-set pins."""
from ast import literal_eval
from collections import Counter
from itertools import combinations
from pathlib import Path
from ramsey_38_cube_inversion import sign

def audit(n,red):
    V=range(n);N=[sum(1<<j for j in V if i!=j and red(i,j)) for i in V];ind=[0]
    for i in V:ind += [s|1<<i for s in ind if not s&N[i]]
    assert max(s.bit_count() for s in ind)==7
    six=[s for s in ind if s.bit_count()==6];counts=Counter();examples={}
    for i,j in combinations(V,2):
        r=(N[i]&N[j]).bit_count(); exclude=N[i]|N[j]|(1<<i)|(1<<j);b=sum(not s&exclude for s in six)
        assert not (r if red(i,j) else b)
        key=('red' if red(i,j) else 'blue',bool(r or b));counts[key]+=1;examples.setdefault(key,(i,j,r,b))
    print(n,counts,examples)
if __name__=='__main__':
    rows=literal_eval(Path(__file__).with_name('ramsey_38_blind_frontier_run.txt').read_text().split('witness_masks=')[1]);audit(len(rows),lambda i,j:rows[max(i,j)]>>min(i,j)&1);audit(27,sign)
