"""Route-only comparison on the frozen endpoint-certified, release-marked pairs."""
from collections import Counter
from statistics import median
from time import perf_counter_ns
import gc
from ramsey38_nested_ball_obstruction_trial import P,prev,json,extend,attaches,shelling


def greedy(a,b):
    """Only for certified marked contained pairs. Not a general feasibility test."""
    order=[]
    for _ in range(len(b)-len(a)):
        for t in sorted(b-a,key=sorted):
            if attaches(a,t):
                order.append(t);a=a|{t};break
        else:raise AssertionError('certified route stranded')
    assert a==b
    return tuple(order)


def run():
    pairs=[]
    for entry in json.loads(P.read_text())['entries']:
        for endpoint in entry['ends']:
            cells=list(map(frozenset,endpoint['cells']));b=frozenset(cells)
            for mask in endpoint['marked']:
                a=frozenset(t for i,t in enumerate(cells) if mask>>i&1);assert a<b and shelling(a) and shelling(b);pairs.append((a,b))
    expected=[extend(a,b) for a,b in pairs];assert all(o is not None for o in expected)
    methods={'reference':extend,'greedy':greedy};rounds=[]
    for i in range(20):
        times={}
        for k in (list(methods) if i%2==0 else list(methods)[::-1]):
            gc.collect();start=perf_counter_ns();outputs=[methods[k](a,b) for a,b in pairs];times[k]=(perf_counter_ns()-start)/1e6
            assert outputs==expected
            for (a,b),order in zip(pairs,outputs):
                for t in order:
                    assert t in b-a and attaches(a,t);a=a|{t}
                assert a==b
        rounds.append(times)
    out=dict(source_sha=prev.sha(P.read_bytes()),pairs=len(pairs),distinct_labelled_pairs=len(set(pairs)),gaps=dict(Counter(len(b-a) for a,b in pairs)),median_ms={k:median(r[k] for r in rounds) for k in methods},paired_greedy_wins=sum(r['greedy']<r['reference'] for r in rounds),rounds_ms=rounds);print({k:v for k,v in out.items() if k!='rounds_ms'});prev.save(prev.out/'ramsey38_marked_greedy_bench.json',out)
if __name__=='__main__':run()
