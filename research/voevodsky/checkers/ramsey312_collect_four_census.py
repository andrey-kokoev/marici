"""Collect stress rows + disjoint complement-probe shards; repair failures and record all certified covers in compressed CSV. Arguments: paths to complement shards."""
from ramsey312_exact_four_cover import *
import collections,csv,gzip

def main():
 fix={tuple(r['d']):r['cert'] for r in json.loads((D/'ramsey312_exact_four_cover.json').read_text())};seen=set();hist=collections.Counter();rep=0;fails=[];total=0
 with gzip.open(D/'ramsey312_all_four_covers.csv.gz','wt',newline='') as fp:
    w=csv.writer(fp);w.writerow('a b c d supports repaired anchor0 ten0 anchor1 ten1 anchor2 ten2 anchor3 ten3'.split());
    for f in [D/'ramsey312_stress4_results.txt',*map(Path,sys.argv[1:])]:
      for l in f.open():
        row=l.split();d=tuple(map(int,row[:4]));assert tuple(sorted(d))==d and d not in seen and 0<=d[0]<d[1]<d[2]<d[3]<52;seen.add(d);h=F^sum(1<<v for v in d);n=int(row[4]);hist[n]+=1;total+=n;raw=row[5]=='RAW'
        if raw:
            s=list(map(int,row[6:]));assert len(s)==n;c=fix.get(d) or solve(d,s)['cert'];rep+=1
            if c is None:fails.append(d);continue
            assert all(any(x&b and not x&t for b,t in c) for x in s)
        else:c=list(zip(map(int,row[6::2]),map(int,row[7::2])))
        assert len(c)==4 and all(b.bit_count()==1 and t.bit_count()==10 and not ((b|t)&~h or b&t) and not any(adj[v]&t for v in bits(t)) for b,t in c);w.writerow([*d,n,int(raw),*itertools.chain.from_iterable(c)])
 assert len(seen)==270725
 res=dict(cores=len(seen),supports=total,nearest=len(seen)-rep,exact_fallback=rep,failures=fails,histogram=hist);(D/'ramsey312_all_four_summary.json').write_text(json.dumps(res));print({k:v for k,v in res.items() if k!='histogram'},'maximum',max(hist))
if __name__=='__main__':main()
