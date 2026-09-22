"""Resolve actual feature windows before scalar response-norm optimization."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
import runpy,json

ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
f=g['f']

def raw_derivative(start,pair,kind):
    result=[]
    for (word,marks),c in f['relation'](pair,kind).items():
        vertices=[start]
        for p in word:vertices.append(vertices[-1]|(1<<p))
        for cut in (0,1):
            seam=('e',vertices[cut],vertices[cut+1],marks[cut])
            buffers=[]
            for indices in (range(cut),range(cut+1,2)):
                buffers.append(tuple((vertices[j],vertices[j+1]) for j in indices if marks[j]))
            result.append(((seam,),tuple(buffers),c))
    return result

def join(a,b):
    sa,ba,ca=a;sb,bb,cb=b
    return sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:],ca*cb

def expand_buffer(edges):
    out={():1}
    for x,y in edges:
        nxt=defaultdict(int)
        for prefix,c in out.items():
            nxt[prefix+(y,)]+=c
            if x:nxt[prefix+(x,)]-=c
        out=f['clean'](nxt)
    return out

columns=[];shape_rows=defaultdict(dict);all_windows=set()
for pairs in g['pairings'](tuple(range(6))):
    for kinds in ((1,1,0),(1,0,1),(0,1,1)):
        start=0;raw=[];canonical=[]
        for pair,kind in zip(pairs,kinds):
            raw.append(raw_derivative(start,pair,kind))
            canonical.append(g['one'](f['derivative'](start,f['relation'](pair,kind))))
            start|=sum(1<<p for p in pair)
        target=g['join'](g['join'](canonical[0],canonical[1]),canonical[2])
        expanded=defaultdict(int);seen=set();entries=[]
        for triple in product(*raw):
            seams,buffers,c=join(join(triple[0],triple[1]),triple[2])
            shape=(seams,tuple(map(len,buffers)))
            assert shape not in seen
            seen.add(shape)
            windows=[]
            for i,seam in enumerate(seams):
                windows.extend(buffers[i])
                if seam[3]:windows.append((seam[1],seam[2]))
            windows.extend(buffers[-1])
            assert len(windows)==2
            all_windows.update(windows)
            j=len(columns)
            shape_rows[shape][j]=(c,tuple(windows))
            entries.append((shape,c,tuple(windows)))
            for choices in product(*(expand_buffer(buf).items() for buf in buffers)):
                coeff=c
                for _,v in choices:coeff*=v
                expanded[(seams,tuple(word for word,_ in choices))]+=coeff
        assert f['clean'](expanded)==target
        assert len(entries)==256
        columns.append({'pairs':pairs,'kinds':kinds,'entries':entries})
assert len(columns)==270
result={'schema':'marici.grothendieck.cubic-analytical-shapes.v1','passed':True,
        'source_columns':len(columns),'raw_terms_per_column':256,
        'analytical_shape_blocks':len(shape_rows),'distinct_actual_event_windows':len(all_windows),
        'columns_per_shape':dict(Counter(map(len,shape_rows.values()))),
        'checks':{'all_270_columns_match_owning_terminal_recorder_exactly':True,
                  'no_within_column_shape_collisions':True,
                  'ordered_two_feature_windows_retained':True},
        'scope':'Actual unscaled seam/memory-shape carrier at one fixed spectral point. Formal potential words are expanded only to verify the owning recorder, not counted as independent analytical noise channels.'}
out=ROOT/'research/grothendieck/results/cubic-analytical-shapes.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
