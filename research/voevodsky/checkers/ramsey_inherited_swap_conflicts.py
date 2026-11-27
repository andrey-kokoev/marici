"""Minimal old-swap collections excluded by every candidate pentagon."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from ramsey_inherited_swap_selector import run


def main():
    hist=Counter();all_sizes=Counter();examples={};mix=Counter();causes=Counter();pair_examples=[]
    def inspect(sq,path,viable,children):
        if not children or any(viable<=v for _,v in children):return
        marks=sorted(viable);allc=(1<<len(children))-1;cover=[sum(1<<j for j,(_,v) in enumerate(children) if m not in v) for m in marks];minimal=[]
        # Every inclusion-minimal cover has a distinct private cycle per mark.
        for n in range(1,min(len(children),len(marks))+1):
            for ids in combinations(range(len(marks)),n):
                u=0
                for i in ids:u|=cover[i]
                if u==allc and not any(g.issubset(ids) for g in minimal):minimal.append(frozenset(ids))
        sizes=sorted({len(g) for g in minimal});hist[sizes[0]]+=1;mix[tuple(sizes)]+=1
        U=set().union(*sq)
        for g in minimal:
            all_sizes[len(g)]+=1
            if len(g)==1:
                s,t=marks[next(iter(g))];e,f=[tuple(sorted(set(v)-U)) for v in (s,t)];both=any(e not in c and f not in c for c,_ in children);each=all(any(z not in c for c,_ in children) for z in (e,f));causes['joint obstruction' if both else 'outside pairs incompatible' if each else 'one row impossible']+=1
            elif len(g)==2:
                ids=sorted(g);pair_examples.append(dict(square=sq,old_path=path,marks=[marks[i] for i in ids],candidates=[dict(edges=sorted(c),accepts=[marks[i] in v for i in ids]) for c,v in children]))
        if sizes[0] not in examples or len(marks)<examples[sizes[0]]['total_marks']:
            ids=sorted(minimal[0]);examples[sizes[0]]=dict(square=sq,old_path=path,total_marks=len(marks),conflict=[marks[i] for i in ids],candidates=[dict(edges=sorted(c),accepts=[marks[i] in v for i in ids]) for c,v in children])
    run(inspect);assert sum(hist.values())==67;out=dict(singleton_causes=causes,pair_examples=pair_examples,by_min_size=hist,minimal_sets_by_size=all_sizes,by_all_sizes={str(k):v for k,v in mix.items()},examples=examples);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_inherited_swap_conflicts.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
