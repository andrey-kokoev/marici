"""Passive joint certification. Compare a same-witness join with two independent existential requests."""
from itertools import permutations,product
from pathlib import Path
import json

# The named addresses r0,r1,b0,b1 are neutral on minus requests. Each has
# exactly one incident positive certificate. Two immutable witnesses each
# serve one red and one blue address; they are not consumed by a read.
slots=('r0','r1','b0','b1');witnesses=('w','v')
def accepts(address,sign):
    def resolve(net):
        if address in slots:return net[address] if sign=='+' else frozenset()
        native='+' if address.startswith('r') else '-'
        return frozenset([address]) if sign==native else frozenset()
    return resolve

def tet(net):
    r=['r'+str(i) for i in range(3)];b=['b'+str(i) for i in range(7)]
    no_rm=not any(accepts(i,'-')(net) for i in r);all_rp=all(accepts(i,'+')(net) for i in r);no_bp=not any(accepts(i,'+')(net) for i in b);all_bm=all(accepts(i,'-')(net) for i in b)
    return (no_rm,all_rp,no_bp,all_bm,no_rm or no_bp)

def joint(a,b):
    # Request one positive certificate valid at both endpoints. A single
    # participant satisfies both incidences in one realization, not two calls.
    return lambda net:bool(accepts(a,'+')(net)&accepts(b,'+')(net))

def audit():
    cases=[]
    for red,blue in product(permutations(witnesses),repeat=2):
        net={s:frozenset([w]) for s,w in zip(slots,red+blue)};values=tet(net);assert values==(True,True,False,False,True)
        table=[[joint(a,b)(net) for b in slots[2:]] for a in slots[:2]]
        for p in permutations(witnesses):
            rename=dict(zip(witnesses,p));other={s:frozenset(rename[x] for x in xs) for s,xs in net.items()};assert table==[[joint(a,b)(other) for b in slots[2:]] for a in slots[:2]]
        assert all(map(any,table)) and sum(map(sum,table))==2
        cases.append(dict(witness_at_each_address=red+blue,vertices_and_or=values,joint_matrix=table))
    assert len({str(c['joint_matrix']) for c in cases})==2
    out=dict(address_order=slots,scope='Added exterior rule: a common positive witness, not independent witnesses or equality of Boolean values. Degree-preserving synthetic bindings; no source positive-transfer law.',cases=cases);print([(c['witness_at_each_address'],c['joint_matrix'][0][0]) for c in cases]);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_common_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
