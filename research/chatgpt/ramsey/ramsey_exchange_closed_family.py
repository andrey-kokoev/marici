"""Find maximal exchange-closed families of maximum blue sets. Standard library."""
from collections import defaultdict
from pathlib import Path
from pauli_realization_audit import decode_graph6


def audit(rows, k):
    blocks = []
    def visit(pool, chosen):
        if chosen.bit_count() == k:
            blocks.append(chosen); return
        while pool.bit_count() >= k - chosen.bit_count():
            bit = pool & -pool; pool ^= bit
            visit(pool & ~rows[bit.bit_length()-1], chosen | bit)
    visit((1 << len(rows))-1, 0)
    faces = defaultdict(list)
    for s in blocks:
        for i in range(len(rows)):
            if s >> i & 1: faces[s ^ (1 << i)].append(s)
    assert faces and max(map(len, faces.values())) <= 2
    adj = defaultdict(set); boundary = set()
    for f, pair in faces.items():
        if len(pair) == 1: boundary.add(pair[0]); continue
        a,b = pair; x=(a^f).bit_length()-1; y=(b^f).bit_length()-1
        assert rows[x] >> y & 1
        adj[a].add(b); adj[b].add(a)
    unseen=set(blocks); closed=[]
    while unseen:
        stack=[unseen.pop()]; component=set(stack)
        while stack:
            for v in adj[stack.pop()] & unseen:
                unseen.remove(v); component.add(v); stack.append(v)
        if component.isdisjoint(boundary): closed.append(len(component))
    return len(blocks),len(boundary),sorted(closed)

if __name__=='__main__':
    root=Path(__file__).parent/'pauli-realization-catalogues'
    for k,n in [(2,5),(3,8),(4,13),(5,17),(6,22)]:
        lines=(root/f'r3{k+1}_{n}.g6').read_text().splitlines() if k!=2 else []
        graphs=[decode_graph6(s) for s in lines] if lines else [[(1<<((i+1)%5)) | (1<<((i-1)%5)) for i in range(5)]]
        results=[audit(g,k) for g in graphs];print(n,len(graphs),sum(bool(r[2]) for r in results),'first',results[0])
