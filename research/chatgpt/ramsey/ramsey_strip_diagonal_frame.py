"""Extract an ordered opposite-edge frame from strip incidences alone, then count the directed ports it distinguishes with and without source-face information."""
from ramsey_oriented_overlap_reader import cycle,m,r,X,orient,D,json,P
from ramsey_crossing_axis_scramble import pts,dot
from itertools import permutations
from collections import Counter

def frame(d,x):
    a,b=[set(x[k]) for k in P[d[0]]];entry,=a&b;last=orient(d,x)[-1];a,b=map(set,last['companions']);comp,=a&b;return ((entry,comp),tuple(last['arrow']))

def run():
    ds=cycle(m)[::2];fs=[]
    for d in (ds,[r[i] for i in ds]):
        f=frame(d,X);fs.append(f)
        for p in permutations((1,2,3,4)):
            g=lambda i:p[i-1];assert frame(d,[tuple(map(g,e)) for e in X])==tuple(tuple(map(g,e)) for e in f)
    assert fs==[((1,4),(2,3)),((1,4),(3,2))];vec=lambda e:tuple(v-u for u,v in zip(pts[e[0]],pts[e[1]]));geo=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text());ports=[(q['triangle'][0],q['outer_arrow']) for q in geo['triangles_and_transports']];records=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        for f in fs:
            marks=[''.join(p[i-1] for i in e) for e in f];sig=lambda e:tuple(dot(vec(e),vec(s)) for s in marks);hist=Counter(sig(e) for _,e in ports);tagged={(face,sig(e)) for face,e in ports};assert len(tagged)==12;records.append(dict(binding=''.join(p),marks=marks,unframed_classes=len(hist),class_sizes=sorted(hist.values()),face_tagged_classes=len(tagged)))
    return dict(column_frames=fs,records=records)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_strip_diagonal_frame.json').write_text(json.dumps(out)+'\n')
