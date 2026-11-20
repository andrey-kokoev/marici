"""Input: named five-blocks and the compressed 8D decoder (represented as 25 PAP). No marked root or midpoint bijection. Test descent of the target matching under blockwise relabelings. Target midpoint equality is used only to assess recovery."""
from ramsey_pentagon_contrast_transport import L,orbits,neighborhood_tests,contrast,blocks
from itertools import permutations
import json,hashlib
from pathlib import Path

def main():
    mid=[3*sum(x)%5 for x in L];truth=frozenset((i,j) for i in blocks[0] for j in blocks[1] if mid[i]==mid[j]);out={}
    for mask in range(1<<len(orbits)):
        E=set().union(*(o for i,o in enumerate(orbits) if mask>>i&1));S=neighborhood_tests(E)
        if S is None:continue
        C=contrast(E);by_orbit=set();root_orbit=set();count=0
        for a in permutations(blocks[0]):
            for b in permutations(blocks[1]):
                p=a+b
                if not all(C[p[i]][p[j]]==C[i][j] for i in range(10) for j in range(i,10)):continue
                count+=1;by_orbit.add(frozenset((p[i],p[j]) for i,j in truth));root_orbit.add(p[0])
        predicted={(i,j) for i in blocks[0] for j in blocks[1] if C[i][j]>0};recover=predicted==truth
        assert (recover and len(by_orbit)==1) or len(by_orbit)>1;assert len(root_orbit)==5
        out[mask]=dict(block_preserving_symmetries=count,distinct_indistinguishable_matchings=len(by_orbit),positive_cross_entries_recover_pairing=recover,possible_root_images=len(root_orbit),attachments=len(S))
    assert len(out)==4;res=dict(decoders=out,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_unmarked_pairing.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':main()
