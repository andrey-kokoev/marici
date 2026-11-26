"""Out-of-sample test: record 2, all degree-seven roots with intact supports of size <=4.
Run freeze before compare. Release means permission, not a demand to hide the row.
"""
import gzip,json,sys,hashlib
from collections import Counter
from pathlib import Path
from unittest.mock import patch
import ramsey38_rotation_transfer as rule
from ramsey38_support_shell import catalogue

base=Path(__file__).resolve().parents[1]/'results';pred=base/'ramsey38_record2_frozen.json';result=base/'ramsey38_record2_comparison.json'
def digest(b):return hashlib.sha256(b).hexdigest()
with gzip.open(catalogue,'rt') as f:first=next(f).strip();word=next(f).strip()
g={v:set() for v in range(1,28)};assert ord(word[0])-63==27
bits=''.join(f'{ord(c)-63:06b}' for c in word[1:]);
for b,(v,w) in zip(bits,((i,j) for j in g for i in range(1,j))):
    if b=='1':g[v].add(w);g[w].add(v)
roots=[r for r,n in g.items() if len(n)==7 and all(len(n&m)<=4 for v,m in g.items() if v not in n|{r})]
checks=('ramsey38_rotation_transfer.py','ramsey38_root15_link_rotation.py')
meta={'record':2,'graph_sha256':digest(word.encode()),'rule_pins':{n:digest(Path(__file__).with_name(n).read_bytes()) for n in checks},'positive':'shellable ball on original seven labels, every nonreleased short row exposed; released support retained','selection':'all degree-seven roots without a support of size five or more; include no-release control 0'}
def save(path,data):
    text=json.dumps(data,indent=2)+'\n'
    if path.exists():assert path.read_text()==text,'artifact drift'
    else:path.write_text(text)
if __name__=='__main__' and sys.argv[1]=='freeze':
    predictions={}
    with patch.object(rule,'N',g):
        for r in roots:
            predictions[r]={v:rule.classify(r,v) for v in [0]+[v for v,n in g.items() if v not in g[r]|{r} and len(g[r]&n)<4]}
    save(pred,dict(meta=meta,predictions=predictions));print('frozen',len(roots),digest(pred.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    import ramsey38_release_census as census
    frozen=json.loads(pred.read_text());assert frozen['meta']==meta;out={};counts=Counter();exceptions=[]
    with patch.object(census,'N',g):
        for r in roots:
            labels,rows,buckets=census.predict(r);cases=frozen['predictions'][str(r)];win={};cert={}
            for d,bs in buckets.items():
                for bd in sorted(bs,key=sorted):
                    order=census.first_ball(bd,set(rows.values()))
                    if order:
                        cert[d]=[sorted(labels[i] for i in t) for t in order];break
            for v,p in cases.items():
                d=int(v);ok=(d in cert or 0 in cert);counts[('release' if d else 'control',p,str(ok))]+=1
                if (p=='pass')!=ok:exceptions.append((r,d,p,ok))
            out[r]={'certificates_by_actual_hidden_row':cert,'boundary_counts':{d:len(bs) for d,bs in buckets.items() if bs}}
    save(result,dict(prediction_sha256=digest(pred.read_bytes()),counts={'/'.join(k):n for k,n in sorted(counts.items())},exceptions=exceptions,roots=out));print(counts,exceptions)
