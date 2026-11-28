"""Width-ten reflection templates: planning uses no candidate pentagon or verdict."""
import json
from itertools import combinations
from ramsey_two_moves_flank_rule import block_word,rule
from ramsey_inherited_swap_selector import D,evaluate
from ramsey_two_repairs_opposite import run
from ramsey_pentagon_selector import charts


def flip(rows):return tuple(sorted(tuple(sorted(11-i for i in r)) for r in rows))

def signature(sq):
    f,=set.intersection(*map(set,sq));mov=set().union(*sq)-{f};return (f,*sorted(i for i in mov if i+1 in mov and not any({i,i+1}<=set(r) for r in sq)))

def plan(sq,templates):
    if block_word(sq) in {'fBBh','hBBf','fhBB','BBhf','BfhB','BhfB'}:
        p=rule(sq);return dict(probe=p['first'],yes=dict(quartet=tuple(sorted(p['yes'][0]+p['yes'][1]))),no=dict(probe=p['second'],yes=dict(quartet=tuple(sorted(p['second_yes'][0]+p['second_yes'][1]))),no=dict(none=True)))
    rev=flip(sq)<sq;key=signature(flip(sq) if rev else sq);t=templates.get(str(key))
    if not t:return dict(none=True)
    def rows(rs):return flip(rs) if rev else tuple(map(tuple,rs))
    def leaf(g):return dict(quartet=rows(g)) if g else dict(none=True)
    return dict(probe=rows([t['probe']])[0],yes=leaf(t['yes']),no=leaf(t['no'])) if t.get('probe') else leaf(t['yes'])


def audit():
    keys=run();templates=json.loads((D/'ramsey_square_label_templates.json').read_text());records=[];minimum={tuple(map(tuple,r['square'])):{'none':0,'common':0,'first row':1,'no first-row plan':2}[r['outcome']] for r in json.loads((D/'ramsey_square_first_move.json').read_text())['records'] if not r['promise']}
    for sq,_,cs in charts():
        p=plan(sq,templates);depths=[]
        for c in cs:
            node=p;kept=[];n=0
            while 'probe' in node:
                r=tuple(node['probe']);assert not kept;ok=bool(evaluate(10,sq,c,[(r,)]));n+=1
                if ok:kept.append(r)
                node=node['yes' if ok else 'no']
            depths.append(n)
            if 'quartet' in node:
                g=node['quartet'];assert set(kept)<=set(g) and (sq,tuple(sorted(c)),g) in keys
                opts=[e for e in combinations(g,2) if set(e[0]).isdisjoint(e[1]) and all(set(r)&set(e[0]+e[1]) for r in sq)]
                m,=[(a,b) for a,b in combinations(opts,2) if set(a).isdisjoint(b)];node['repairs']=m
            else:assert not any(s==sq and k==tuple(sorted(c)) for s,k,_ in keys)
        assert max(depths)==minimum[sq];records.append(dict(square=sq,plan=p))
    (D/'ramsey_square_label_plans.json').write_text(json.dumps(records,indent=2)+'\n');print('verified',len(records),'plans')
if __name__=='__main__':audit()
