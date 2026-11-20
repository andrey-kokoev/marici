"""Run a fixed residual transform for 64 stages; reverse the entire chain."""
from ramsey_residual_rewrite import transform,cost,seed


def main():
    orig=seed(7,'double')[0];order=[j for i in range(10) for j in (i,i+10)]
    for mask in range(8):
        g=orig.copy()
        for t,(i,j) in enumerate(((0,5),(1,6),(2,7))):
            for x,y in ((i,j),(j,i)):g[x]=(g[x]&~(1<<y))|((mask>>t&1)<<y)
        base=[sum((g[i]>>j&1)<<t for t,j in enumerate(order)) for i in order];r=base;cs=[];seen={tuple(r)}
        for _ in range(64):
            r=transform(r);cs.append(cost(r)[1]);seen.add(tuple(r))
        print(mask,cost(base)[1],min(cs),cs.index(min(cs))+1,cs[-1],len(seen))
        for _ in range(64):r=transform(r,inverse=True)
        assert r==base

if __name__=='__main__':main()
