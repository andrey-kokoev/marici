"""Select third-swap destination before constructing its row, width ten."""
from ramsey_shared_hub_generator import ALL,D,independent,cap,safe,combinations,Counter,json
from functools import lru_cache

@lru_cache(None)
def single_gate(C,B,v,fixed):
    if not safe((C,B,v)):return frozenset()
    allowed=set(ALL)
    for n in range(4):
        for q in combinations((C,B,v),n):
            free=ALL.difference(fixed,*q);a=cap(free);limit=5-n # one incomplete corner and n ports; allow at most six total
            if a>limit+1:return frozenset()
            if a==limit+1:
                # Mandatory sites of a maximum independent path set: alternate sites of odd runs only.
                must=set();run=[]
                for i in range(1,12):
                    if i in free:run.append(i)
                    else:
                        if len(run)%2:must.update(run[::2])
                        run=[]
                allowed&=must
    return frozenset(allowed)

def main():
    counts=Counter();ex={};wins=set()
    for x in range(1,10):
        pair={x,x+1}
        for W in map(frozenset,combinations(sorted(ALL-pair),3)):
            if not all(independent(W|{i}) for i in pair):continue
            rem=ALL-W-pair
            for M in map(frozenset,combinations(sorted(rem),2)):
                T=rem-M
                if not independent(T) or not all(independent(M|{i}) for i in pair):continue
                for c,d in ((x,x+1),(x+1,x)):
                    C=M|{c};B=M|{d}
                    for S in map(frozenset,combinations(sorted(rem),3)):
                        if not independent(S) or not S&M or not S&T:continue
                        zset=M-S;neighbors=lambda z:{z-1,z+1}&W
                        for y in M:
                            fixed=(M-{y})|{c};legal=single_gate(C,B,S,fixed)&single_gate(C,B,T,fixed)
                            residual=W if all(len(neighbors(z))>=1+(z==y) for z in zset) else set();choices=[]
                            for Y in (y-1,y+1):
                                if Y not in ALL-(M|pair) or not all(independent((M-{y})|{Y,j}) for j in pair):continue
                                E=fixed|{Y}
                                if E in (T,S):continue
                                counts['candidates']+=1;ok1=Y in legal;ok2=Y in residual
                                assert ok1==(safe((C,B,E,T)) and safe((C,B,E,S)))
                                assert ok2==(cap(ALL-S-T)<5 and cap(ALL-S-T-E)<4)
                                if ok1:choices.append((Y,ok2))
                                if ok1 and ok2:
                                    counts['pass']+=1;wins.add((C,frozenset((B,E)),frozenset((S,T))))
                                elif ok1:counts['residual_reject']+=1
                                else:counts['single_reject']+=1
                            for dest,ok in choices:
                                ex.setdefault(str(ok),dict(C=sorted(C),B=sorted(B),S=sorted(S),T=sorted(T),W=sorted(W),y=y,Y=dest))
    assert len(wins)==counts['pass']==456;result=dict(counts=counts,example=ex);print(result);(D/'ramsey_shared_hub_third_corner.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
