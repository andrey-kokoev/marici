"""Exact continuation trees for the six unresolved quartets. Old colors are fixed along a branch."""
from itertools import combinations
import json
from ramsey_quartet_live_probe import configs,independent_sets,decode,D,path


def tree(sq,rs,c):
    candidates=[r for r in combinations(range(1,11),3) if r not in sq+rs and all(e not in path for e in combinations(r,2))]
    def extend(supports,graph):
        n=10+len(supports);sixes=independent_sets(n,graph,6);nodes=[]
        for r in candidates:
            if r in supports:continue
            base=set(r)|{11+j for j,s in enumerate(sq) if set(s).isdisjoint(r)};opts=[11+j for j,s in enumerate(supports) if j>=4 and set(s).isdisjoint(r)]
            for k in range(len(opts)+1):
                for es in combinations(opts,k):
                    red=base|set(es);mask=sum(1<<i for i in red)
                    if any(i in red and j in red for i,j in graph) or any(not (q&mask) for q in sixes):continue
                    nodes.append(dict(row=r,optional_red=es,next=extend(supports+(r,),graph|{(i,n+1) for i in red})))
        return nodes
    result=[]
    for _,es,red,_ in configs(sq,rs,c):
        graph={tuple(i for i in range(1,19) if m>>i&1) for m in red};result.append(dict(quartet_links=es,continuations=extend(sq+rs,graph)))
    return result


def run():
    src=json.loads((D/'ramsey_quartet_live_probe.json').read_text());records=[]
    for q in src['records']:
        if q['live'] or q['joint_only']:continue
        sq=tuple(map(tuple,q['square']));rs=tuple(map(tuple,q['quartet']));tag,_,_,cs=decode(sq,rs);a,b=[tree(sq,rs,c) for c in cs];records.append(dict(square=sq,rows=rs,choice=tag,equal_colored=a==b,trees=[a,b]))
    assert len(records)==6;print([(r['choice'],r['equal_colored'],r['trees'][0]) for r in records]);(D/'ramsey_quartet_terminal.json').write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__':run()
