"""Exhaust the minimum two-edit deletion model without loading a successor coloring."""
import json,gzip
from itertools import combinations
from collections import Counter
from ramsey_retention_slice import CAT,D,decode


def audit():
    block=json.loads((D.parent/'ramsey_matrix_successor_block.json').read_text());S=block['S'];labels=block['core_labels'];target=sorted(8-sum(c) for c in zip(*S));goal=Counter(target);face_deg=8-max(map(sum,zip(*S)));face_n=goal[face_deg];hist=Counter();parents=[];survive=[];best=None;near=None
    weights=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)])
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for idx,line in enumerate(f,1):
            s=line.rstrip();ec=sum(s[1:].translate(weights));hist[ec]+=1
            if ec!=85:continue
            a=decode(s.decode());rec=dict(catalogue_index=idx,deletions=0,edit_pairs=0,degree_pass=0,face_degree_budget=[])
            for z,mask in enumerate(a):
                if mask.bit_count()!=7:continue
                rec['deletions']+=1;vs=[i for i in range(27) if i!=z];deg={i:(a[i]&~(1<<z)).bit_count() for i in vs};es=[(i,j) for i,j in combinations(vs,2) if a[i]>>j&1];assert len(es)==78;rec['face_degree_budget'].append(sum(max(0,v-face_deg) for v in sorted(deg.values())[:face_n]));rec['edit_pairs']+=len(es)*(len(es)-1)//2
                for e,h in combinations(es,2):
                    d=Counter(deg.values());ends=Counter(e+h)
                    for i,n in ends.items():d[deg[i]]-=1;d[deg[i]-n]+=1
                    delta=sum((goal-d).values());
                    if best is None or delta<best:best=delta;near=dict(parent=idx,delete=z,edits=[e,h],degrees=+d)
                    if not delta:rec['degree_pass']+=1;survive.append(dict(parent=idx,delete=z,edits=[e,h]))
            parents.append(rec)
    assert min(hist)==85 and hist[85]==4 and sum(hist.values())==477142
    out=dict(target_degree_histogram=goal,scope='One deleted vertex, two red-to-blue edits; indices of catalogue entries one-based, vertices zero-based.',parents=parents,survivors=survive,minimum_number_of_wrong_degree_slots=best,closest=near);print([(r['catalogue_index'],r['deletions'],r['edit_pairs'],r['degree_pass'],sorted(set(r['face_degree_budget']))) for r in parents],best,near,len(survive));(D.parent/'ramsey_matrix_two_edit_gate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
