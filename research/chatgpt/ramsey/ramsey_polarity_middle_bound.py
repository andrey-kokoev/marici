"""Small carrier-only inputs for the middle-count proof: count absolute flags on polarities and measure girth, without testing pairs of matchings."""
from collections import deque,Counter
from itertools import permutations
from ramsey_antipode_extension import run as polarity
from ramsey_row_quotient_constructor import action,flags
from ramsey_folded_entry_handoff import D,json

def run():
    adj={x:set() for x in range(30)}
    for a,b in flags:adj[a].add(b);adj[b].add(a)
    girth=31
    for a,b in flags:
        q=deque([(a,0)]);seen={a}
        while q:
            x,k=q.popleft()
            if x==b:girth=min(girth,k+1);break
            for y in adj[x]-seen:
                if (x,y)==(a,b):continue
                seen.add(y);q.append((y,k+1))
    f=polarity()[0]['map'];hist=Counter()
    for p in permutations(range(6)):
        h=action(p);g=[h[f[x]] for x in range(30)]
        if all(g[g[x]]==x for x in g):hist[sum(g[a]==b for a,b in flags)]+=1
    assert girth==8 and hist=={5:36};return dict(girth=girth,polarity_absolute_flag_histogram=hist)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_polarity_middle_bound.json').write_text(json.dumps(out)+'\n')
