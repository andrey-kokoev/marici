"""Exact joint-kernel audit on the actual two-feature cubic source packet."""
from pathlib import Path
import importlib.util
import json

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('growth',HERE/'check_translated_cubic_observer_growth.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
f=g.f


def main():
    columns=[];seen=set()
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            factors=[f['relation'](pair,kind) for pair,kind in zip(pairs,kinds)]
            source=f['chain_product'](factors)
            assert not seen.intersection(source);seen.update(source)
            start=0;seams=[];images=[]
            for pair,kind,factor in zip(pairs,kinds,factors):
                first=pair[0]
                seams.append(('e',start,start|(1<<first),kind))
                images.append(g.one(f['derivative'](start,factor)))
                start|=sum(1<<j for j in pair)
            key=(tuple(seams),((),)*4)
            image=g.join(g.join(images[0],images[1]),images[2])
            assert image[key]==1
            columns.append((pairs,kinds,key,image))
    assert len(columns)==270
    keys={row[2]:i for i,row in enumerate(columns)}
    assert len(keys)==270
    entries=0
    for j,(_,_,_,image) in enumerate(columns):
        projected={keys[key]:value for key,value in image.items() if key in keys}
        assert projected=={j:1};entries+=len(projected)
        # Fully vacuum seams AND buffers cannot carry retained degree two.
        assert not any(all(seam[3]==0 for seam in key[0]) and
                       all(not buffer for buffer in key[1]) for key in image)
    oldkeys=[((('e',0,1,1),('e',3,7,1),('e',15,31,0)),((),)*4),
             ((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),)*4)]
    selected=[keys[key] for key in oldkeys]
    assert len(set(selected))==2
    target=next(i for i,(pairs,kinds,_,_) in enumerate(columns)
                if tuple(map(tuple,pairs))==((0,1),(2,3),(4,5)) and kinds==(1,0,1))
    assert target not in selected
    assert all(columns[target][3].get(key,0)==0 for key in oldkeys)
    result={'passed':True,'source_dimension':270,
        'old_private_coordinate_rank':2,'fully_vacuum_rank_on_this_packet':0,
        'old_plus_fully_vacuum_kernel_dimension':268,
        'expanded_private_matrix':'270 by 270 identity before nonzero actual window factors',
        'expanded_private_matrix_nonzero_entries':entries,
        'expanded_private_rank':270,'expanded_private_kernel_dimension':0,
        'explicit_old_blind_source':'mixed(2,3) forgotten(5,7) mixed(11,13)',
        'new_probe_key':columns[target][2],
        'scope':'Exact finite marked-path/record audit. Physical feature evaluations are nonzero by the cited positive residual-window bound. No uniform conditioning or infinite-source injectivity is inferred.'}
    out=HERE.parent/'results/joint-cubic-observation-kernel.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
