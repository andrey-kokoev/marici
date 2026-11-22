"""Test whole-pentagon exchanges preserving the five distinguished connections, without assigning an orientation. Forget owner colours for the symmetry test."""
from itertools import permutations
from ramsey_polarity_receipt_quotient import check,D,json

def run():
    q=check();a=q['petersen_outer'];b=q['petersen_inner'];edges=set(map(tuple,q['core_edges']));out=[]
    for p in permutations(range(5)):
        f={a[i]:b[p[i]] for i in range(5)}|{b[i]:a[p[i]] for i in range(5)}
        if any(tuple(sorted((f[x],f[y]))) not in edges for x,y in edges):continue
        assert all(f[f[f[f[x]]]]==x for x in f);fixed=[i for i in range(5) if p[i]==i];k,=fixed;assert all(p[p[i]]==(2*k-i)%5 for i in range(5));out.append(dict(indices=p,fixed_connection=[a[k],b[k]],slope=(p[1]-p[0])%5))
    assert len(out)==10;return out
if __name__=='__main__':
    out=run();print(out[:2]);(D/'ramsey_pentagon_exchange_order.json').write_text(json.dumps(out)+'\n')
