"""Predict both handoff source faces from the ordered strip frame alone. Test against archived port ownership after binding; distinguish predicting face context from choosing a particular edge."""
from ramsey_strip_diagonal_frame import frame,cycle,m,r,X,D,json,pts,dot,permutations

def run():
    geo=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text());owner={q['outer_arrow']:set(q['triangle'][0][2:]) for q in geo['triangles_and_transports']};live=json.loads((D/'ramsey_live_matching_receipt.json').read_text());ds=cycle(m)[::2];out=[]
    for bind in live:
        p=bind['binding'];rows=[]
        for d,row in zip((ds,[r[i] for i in ds]),bind['rows']):
            fixed,moving=frame(d,X);faces=[set(fixed)|{i} for i in moving];maps=[{p[i-1] for i in f} for f in faces];vec=lambda a,b:tuple(y-x for x,y in zip(pts[a],pts[b]));marks=[vec(*(p[i-1] for i in t)) for t in (fixed,moving)];sig=lambda e:tuple(dot(vec(*e),s) for s in marks);legs=[]
            for e,f in zip(row['receipt'][:2],maps):
                assert owner[e]==f;all_hits=[v for v in owner if sig(v)==sig(e)];in_face=[''.join(v) for v in permutations(sorted(f),2) if sig(v)==sig(e)];assert len(all_hits)==2 and in_face==[e];legs.append(dict(port=e,same_projection=all_hits,face=''.join(sorted(f))))
            rows.append(dict(faces=[sorted(f) for f in faces],legs=legs))
        out.append(dict(binding=p,rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_handoff_source_face.json').write_text(json.dumps(out)+'\n')
