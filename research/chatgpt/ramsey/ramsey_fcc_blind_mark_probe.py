"""Stop at the first square. Geometric controls only; no reflect-on-closure operation."""
import json
from collections import Counter
from pathlib import Path

def main():
    d=json.loads((Path(__file__).resolve().parents[2]/'strominger/results/fcc-first-transport.json').read_text());site={tuple(v['barycentric']):v['id'] for v in d['vertices']};step={(r['source'],tuple(r['sector'])):r['target'] for r in d['directed_moves']};word=[(2,3),(0,1),(3,2),(1,0)]
    def run(v,w):
        for s in w:
            v=step.get((v,s));
            if v is None:break
        return v
    stats=Counter()
    for c in d['coarse_cells']:
        if not c['id'].startswith('oct-'):continue
        b=tuple(map(min,zip(*c['vertices'])));pos=lambda label:site[tuple(x+(str(i+1) in label) for i,x in enumerate(b))];source=pos('13');north=pos('12');south=pos('34')
        # Predeclared geometric reader: +1 at 12, -1 at 34, zero elsewhere.
        def read(v):return int(v==north)-int(v==south)
        assert read(north)==1 and read(south)==-1
        end=run(source,word);assert end==source and read(end)==0;stats['site_only_blind']+=1
        tag=run(north,word)
        if tag is None:stats['co_translation_guarded_out']+=1
        else:assert read(tag)==1;stats['co_translation_identity']+=1
    print(dict(stats))
if __name__=='__main__':main()
