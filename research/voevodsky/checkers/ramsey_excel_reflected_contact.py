"""Does one literal half-turn supply the missing contacts, with no priority between moves?"""
from ramsey_excel_swap_contact_transfer import D,combinations,Counter,json,sys
P=D/'ramsey_excel_reflected_contact_protocol.json';R=D/'ramsey_excel_reflected_contact.json'
rule=dict(domain='Same distinct exterior rows and terminal squares as the immediate-swap audit. A new contact is one reflection of the whole literal row about the column midpoint, landing on a focal corner. Combine with direct swap by union, no priority or duplication. Reflection is not followed by a fitted shift.',score='All corners occupied with no exterior row touching two different corners. Compare all squares and count repairs of previously empty groups. A distinct single row per positive vertex is required for a size match. Control: arbitrary-length swap paths that first enter the square at a corner.')
def run():
    assert json.loads(P.read_text())==rule;base=json.loads((D/'ramsey_excel_swap_contact_transfer.json').read_text());out=[]
    for rec in base:
        w=rec['width'];rows=set(combinations(range(1,w+1),3));rows={r for r in rows if min(r[1]-r[0],r[2]-r[1])>=2};mirror=lambda r:tuple(w+1-x for x in r[::-1]);stats=Counter();cases=[]
        for case in rec['cases']:
            c=list(map(tuple,case['corners']));old=[set() for _ in c];new=[set() for _ in c];conf=[]
            for r in sorted(rows-set(c)):
                a={i for i,s in enumerate(c) if sum(abs(x-y) for x,y in zip(r,s))==1};b={i for i,s in enumerate(c) if s==mirror(r)}
                for i in a:old[i].add(r)
                for i in a|b:new[i].add(r)
                if len(a|b)>1:conf.append(dict(row=r,swap=c[next(iter(a))],mirror=mirror(r)))
            assert sorted(map(len,old))==case['sizes'];stats['total']+=1;stats['originally_empty_groups']+=sum(not s for s in old);stats['newly_occupied_groups']+=sum(not a and bool(b) for a,b in zip(old,new));stats['all_occupied']+=all(new);stats['exclusive']+=not conf;stats['both']+=all(new) and not conf;cases.append(dict(corners=c,old_sizes=list(map(len,old)),new_sizes=list(map(len,new)),conflicts=conf))
        print(w,stats,cases[0]);out.append(dict(width=w,counts=stats,cases=cases))
    text=json.dumps(out,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        text=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==text;P.write_text(text)
    else:run()
