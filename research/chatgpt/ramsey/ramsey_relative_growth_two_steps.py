"""Append two measured rows to the saved 20-address record; audit independent bridge cuts."""
import json
from itertools import pairwise, product
from pathlib import Path
from ramsey_common_witness_chain_20 import chain
from ramsey_relative_growth_bridge import decode
from ramsey_37_pair_rotation_rule import build


def main():
    data=json.loads(Path(__file__).with_name('ramsey_common_witness_chain_20.json').read_text())
    labels=data['address_order']; old=[tuple(sorted((labels[i],labels[j]))) for i,j in chain(len(labels))]
    internal=[(a,b,int(d)) for (a,b),d in zip(pairwise(old),data['different_from_next'],strict=True)]
    g=build(); truth={p:g[p[0]]>>p[1]&1 for p in old}; stars=[]; bridges=[]
    for n in (20,21):
        star=[(i,n) for i in labels];stars.append(star);labels=labels+[n]
        truth.update({p:g[p[0]]>>p[1]&1 for p in star})
        def record(a,b):return a,b,truth[a]^truth[b]
        internal.extend(record(a,b) for a,b in pairwise(star));bridges.append(record((0,1),star[0]))
    joined=internal+bridges
    assert all(decode(joined,{p:v})==truth for p,v in truth.items())
    for cut in ((),(0,),(1,),(0,1)):
        links=internal+[b for i,b in enumerate(bridges) if i not in cut];out=set()
        for vals in product((0,1),repeat=len(cut)):
            seeds={(0,1):truth[0,1],**{stars[i][0]:v for i,v in zip(cut,vals)}}
            result=decode(links,seeds);assert result.keys()==truth.keys();out.add(tuple(result[p] for p in truth))
        assert len(out)==2**len(cut);print('removed',cut,'compatible matrices',len(out))
    print('pair values:',len(truth),'relative readings:',len(joined),'bridges:',bridges)

if __name__=='__main__':main()
