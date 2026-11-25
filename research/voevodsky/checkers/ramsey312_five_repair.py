"""Repair a deterministic shard of five-deletion cover attempts; record negative instances for separate investigation."""
from ramsey312_exact_four_cover import *
def main():
 path,part,parts=sys.argv[1:4];part=int(part);parts=int(parts);prefix=sys.argv[4] if len(sys.argv)>4 else 'ramsey312_five_repair'
 with open(path) as f,(D/f'{prefix}_{part}.jsonl').open('w') as out:
    for i,l in enumerate(f):
        if i%parts!=part:continue
        row=l.split();d=list(map(int,row[:5]));n=int(row[5]);raw=row[6]=='RAW';vals=list(map(int,row[7:]));r=solve(d,vals) if raw else dict(cert=list(zip(vals[::2],vals[1::2])));out.write(json.dumps(dict(d=d,n=n,raw=raw,**r))+'\n');out.flush()
if __name__=='__main__':main()
