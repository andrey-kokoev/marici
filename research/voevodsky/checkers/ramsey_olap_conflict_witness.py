"""41 frozen controls. Eligible materializations: vertex->face postings, face->disjoint postings, pair-of-ports->conflict postings. Retain ONLY the first. Face ID = ordinal among sorted 16-bit face masks. Charge 16*F posting bits, no face dictionary: recover names by reading the 16 membership bits. A pair-of-ports query uses <=10 bitmap ORs plus one complement once port masks are known; no base graph reads. Six-port existence uses transient derived disjoint bitmaps and exact clique search (no latency bound)."""
import gzip, json,hashlib
from itertools import combinations_with_replacement,combinations
from pathlib import Path
from ramsey_square_index_pilot import build, DATA, OUT, PAIRS, members, six

def main():
    ctrl={e['graph6'] for e in json.loads((DATA/'ramsey_boundary_k6_witnesses.json').read_text())['records']};tot=dict(graphs=0,pair_queries=0,port_pair_queries=0,empty_conflict=0,nonempty_conflict=0,posting_bits=0,compatible_sixes=0);by={}
    for g in gzip.decompress((DATA/'r36_16.g6.gz').read_bytes()).splitlines():
        if sum((x-63).bit_count() for x in g[1:])!=33 and g.decode() not in ctrl:continue
        _,raw,R,_=build(g);F=sorted(raw);n=len(F);allf=(1<<n)-1;posts=[sum(1<<j for j,s in enumerate(F) if s>>i&1) for i in range(16)]
        def face(j):return sum(1<<v for v,p in enumerate(posts) if p>>j&1)
        # Query side: no base face masks or graph allowed after postings constructed.
        ids=[face(j) for j in range(n)];assert ids==F
        def outside(mask):
            seen=0
            for v in members(mask):seen|=posts[v]
            return allf^seen
        D=[outside(s) for s in ids];ref=[sum(1<<j for j,t in enumerate(F) if not t&s) for s in F];assert D==ref
        for a,b in PAIRS:
            assert [ids[j] for j in members(posts[a]&posts[b])]==[s for s in F if s>>a&1 and s>>b&1];tot['pair_queries']+=1
        for i,j in combinations_with_replacement(range(n),2):
            witnesses=outside(ids[i]|ids[j]);assert witnesses==ref[i]&ref[j];tot['port_pair_queries']+=1;tot['nonempty_conflict' if witnesses else 'empty_conflict']+=1
        w=six(D);assert (w is not None)==(g.decode() in ctrl)
        if w is not None:assert all(sum(not s&ids[j] for j in w)<=1 for s in F)
        tot['graphs']+=1;tot['posting_bits']+=16*n;tot['compatible_sixes']+=int(w is not None);by[len(R)]=by.get(len(R),0)+1
    assert by=={33:39,34:2};res=dict(totals=tot,by_red_edge_count=by,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(res);(OUT/'ramsey_olap_conflict_witness.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':main()
