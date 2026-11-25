"""Merge complete --sweep shards. Verify coverage of deletion sets; write compact replay receipts and an input list for every direct clique test."""
import csv,gzip,hashlib,json,sys,itertools,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
def main():
 seen=set();counts=collections.Counter();supports=0;maxima={};hist=collections.Counter();hits=[];special=[];digests=[];presam=[]
 for f in map(Path,sys.argv[1:]):
    dig=hashlib.sha256();n=0
    with f.open('rb') as stream:
        for line in stream:
            dig.update(line);ls=line.split();assert len(ls)>=3;d,m=map(int,ls[:2]);tag=ls[2].decode();cert=list(map(int,ls[3:]));assert d.bit_count()==5 and d.bit_length()<=52 and d not in seen;seen.add(d);counts[tag]+=1;supports+=m;n+=1;hist[m]+=1
            if maxima.get(tag,(0,None))[0]<m:maxima[tag]=(m,d)
            if tag in ('near','greedy'):
                assert len(cert)==10 and all(b.bit_count()==1 and t.bit_count()==10 and not (b&t or (b|t)&d) for b,t in zip(cert[::2],cert[1::2]));
                if n%2003==1:presam.append((d,m,tag,cert))
            elif tag in ('noK6','K6'):
                special.append(d)
                if tag=='K6':hits.append(dict(d=d,s=cert))
            else:raise ValueError(tag)
    digests.append(dict(shard=f.name,rows=n,sha256=dig.hexdigest()))
 assert len(seen)==2598960;res=dict(cores=len(seen),counts=counts,supports=supports,maximum=maxima,hits=hits,shards=digests);print({k:v for k,v in res.items() if k not in ('shards','hits')},'hits',len(hits));(D/'ramsey312_five_exhaustive_summary.json').write_text(json.dumps(res,indent=1));(D/'ramsey312_five_clique_inputs.txt').write_text(''.join(' '.join(str(i) for i in range(52) if d>>i&1)+'\n' for d in sorted(special)));(D/'ramsey312_five_sweep_cover_samples.json').write_text(json.dumps(presam))
if __name__=='__main__':main()
