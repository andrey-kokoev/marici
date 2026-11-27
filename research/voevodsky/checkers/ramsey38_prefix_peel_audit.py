"""Distinguish caching prefix-free legal moves from caching a prefix-specific answer."""
from ramsey38_three_route_novelty import P,R,json,prev
from ramsey38_shared_peel_trial import Peeler
from ramsey38_append_holdout import attaches,faces
from functools import lru_cache
from collections import Counter

def run():
    data=json.loads(P.read_text());ver=json.loads(R.read_text());assert ver['prediction_sha']==prev.sha(P.read_bytes());out=[];tot=Counter()
    for e,z in zip(data['cases'],ver['cases'],strict=True):
        for p in e['plans']:
            if p['goal'] not in z['verified']:continue
            cells=sorted(map(frozenset,p['stages'][-1]['cells']),key=sorted);B=(1<<len(cells))-1;solver=Peeler(True);cnt=Counter();examples={};as_set=lambda m:frozenset(t for i,t in enumerate(cells) if m>>i&1)
            @lru_cache(None)
            def legal(m):return tuple(1<<i for i,t in enumerate(cells) if m>>i&1 and attaches(as_set(m^(1<<i)),t))
            @lru_cache(None)
            def reverse(m,prefix):
                if m==prefix:return ()
                for bit in legal(m):
                    if bit&prefix:continue
                    tail=reverse(m^bit,prefix)
                    if tail is not None:return (bit,)+tail
                return None
            # Independent forward powerset traversal: all reachable supersets, never remove a cell.
            @lru_cache(None)
            def forward(m):
                if m==B:return True
                s=as_set(m);return any(forward(m|1<<i) for i,t in enumerate(cells) if not m>>i&1 and attaches(s,t))
            unmarked=solver(as_set(B));first=cells.index(unmarked[-1]);
            @lru_cache(None)
            def ball(m):return bool(solver(as_set(m)))
            for prefix in range(1,B):
                A=as_set(prefix)
                if not ball(prefix):continue
                cnt['shellable_prefixes']+=1;order=reverse(B,prefix);assert (order is not None)==forward(prefix)
                if order is None:
                    cnt['no_relative_order']+=1;examples.setdefault('nonextendible',faces(A));continue
                cnt['extendible']+=1;reuse=tuple(1<<cells.index(t) for t in reversed(unmarked[len(A):]));
                if any(prefix&b for b in reuse):cnt['invalid_unmarked_suffix']+=1
                if prefix>>first&1:
                    cnt['first_move_protected']+=1
                    if len(A)==len(cells)-1:examples.setdefault('first_move_conflict',dict(protected=faces(A),naive_first=sorted(cells[first]),correct_first=sorted(cells[order[0].bit_length()-1])))
                m=B
                while m!=prefix:
                    b=next((b for b in legal(m) if not b&prefix),None)
                    if b is None:break
                    m^=b
                if m!=prefix:cnt['greedy_stuck']+=1;examples.setdefault('greedy_stuck',faces(A))
                m=B
                while m!=prefix:
                    b=next((b for b in legal(m) if not b&prefix and ball(m^b)),None)
                    if b is None:break
                    m^=b
                if m!=prefix:cnt['ball_checked_greedy_stuck']+=1;examples.setdefault('ball_checked_stuck',faces(A))
            print(e['record'],p['goal'],cnt,flush=True);tot.update(cnt);out.append(dict(record=e['record'],goal=p['goal'],cells=faces(cells),counts=dict(cnt),examples=examples,legal_cache=str(legal.cache_info()),relative_cache=str(reverse.cache_info())))
    print(tot);prev.save(prev.out/'ramsey38_prefix_peel_controls.json',dict(source_sha=prev.sha(P.read_bytes()),totals=dict(tot),plans=out))
if __name__=='__main__':run()
