"""Keep predecessor, orientation, root and side endpoints; thin class-to-port red links only."""
from collections import Counter
from itertools import combinations
import json
from ramsey_excel_corner_predecessor_readout import CAT,D,decode,squares


def audit(record=None):
    hist=Counter();sing=Counter();exception=[];example=None
    for idx,line in enumerate((CAT/'r37_22.g6').read_text().splitlines(),1):
        if record is not None and idx!=record:continue
        a=decode(line);I=[0]
        for x,m in enumerate(a):I.extend([q|1<<x for q in I if not q&m])
        qs=sorted((q for q in I if q.bit_count()>=4),key=lambda q:-q.bit_count());assert qs[0].bit_count()==6
        by_site=[sum(1<<j for j,q in enumerate(qs) if q>>v&1) for v in range(22)];big={s:sum(1<<j for j,q in enumerate(qs) if q.bit_count()>=s) for s in (4,5,6)}
        for c in squares(a):
            C=sum(1<<x for x in c);base=[(1<<c[i])|(1<<c[(i+1)%4]) for i in range(4)]
            for off in (2,3):
                masks=[a[c[(i+off)%4]]&~C for i in range(4)];full=[b|m for b,m in zip(base,masks)];links=[(i,x) for i,m in enumerate(masks) for x in range(22) if m>>x&1];free=[];forced={}
                cache={}
                def miss(m):
                    if m not in cache:
                        v=0
                        for x in range(22):
                            if m>>x&1:v|=by_site[x]
                        cache[m]=~v
                    return cache[m]
                def witness(rs):
                    a,b,c1,d=map(miss,rs);pairs=(a&b)|(c1&d)|((a|b)&(c1|d));three=((a&b)&(c1|d))|((a|b)&(c1&d));hits=(pairs&big[6])|(three&big[5])|(a&b&c1&d&big[4]);return qs[(hits&-hits).bit_length()-1] if hits else None
                assert witness(full) is None
                for i,x in links:
                    r=full[:];r[i]^=1<<x;q=witness(r)
                    if q is None:free.append((i,x));continue
                    forced[i,x]=[v for v in range(22) if q>>v&1];sing[q.bit_count()]+=1
                # Only individually removable links can belong to a jointly removable set.
                best=0;solutions=[]
                for n in range(len(free),-1,-1):
                    for t in combinations(free,n):
                        r=full[:]
                        for i,x in t:r[i]^=1<<x
                        if witness(r) is None:solutions.append(t)
                    if solutions:best=n;break
                hist[len(links),len(free),best,len(solutions)]+=1
                rec=dict(record=idx,square=c,offset=off,removable=free,max_drop=best,example_drop=solutions[0],forced_witnesses={str(k):v for k,v in forced.items()})
                if idx==150:exception.append(rec)
                if best and example is None:example=rec
    out=dict(by_full_links_singly_removable_max_drop_and_minimizers={str(k):v for k,v in hist.items()},forced_by_largest_blue_clique=sing,record150=exception,first_reduction=example);print(hist,sing);print([(r['offset'],r['removable'],r['example_drop']) for r in exception]);(D.parent/('ramsey_square_minimal_contacts'+('' if record is None else f'_{record}')+'.json')).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]) if len(sys.argv)>1 else None)
