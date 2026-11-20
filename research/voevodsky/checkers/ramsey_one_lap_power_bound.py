"""Sharpness certificates for the one-lap bounded monotone bridge reader. General proof in ../ramsey-one-lap-power-bound.md. No catalogue or successful boundary input."""
import json
from pathlib import Path

def accepts(word,k):
    for flip in (0,(1<<k)-1):
        for sign in (-1,1):
            for j in range(k):
                cur={0}
                for mask in word:
                    m=mask^flip;new=set()
                    for a in cur:
                        for h in range(min(k-1,k-a)+1):
                            if not m & (1<<((j+sign*(a+h))%k)):break
                            new.add(a+h)
                    cur=new
                    if not cur:break
                if k in cur:return True
    return False
out=[]
for k in range(3,13):
    all_sites=(1<<k)-1;x=[]
    for j in reversed(range(k)):
        x.extend([all_sites^(1<<j),all_sites])
    verdict=[accepts(x*i+[all_sites],k) for i in (k-1,k,k+1)];assert verdict==[True,False,False];out.append(dict(k=k,word=x,suffix=[all_sites],verdict=verdict))
D=Path(__file__).resolve().parents[1]/'results';(D/'ramsey_one_lap_power_bound.json').write_text(json.dumps(out,indent=2)+'\n');print('Verified separating contexts for k=3..12.')
