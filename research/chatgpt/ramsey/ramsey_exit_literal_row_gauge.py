"""Factor the observed candidate reanchor into a row exchange and the unique nonidentity column symmetry invisible to the current literal word. Compare the full ordered pair, not just its common word."""
from itertools import permutations,combinations
from ramsey_folded_entry_handoff import D,json
def act(p,w):return ''.join(w[p.index(i)] for i in range(4))
def run():
    ps=list(permutations(range(4)));frames={p[3]+1:p for p in ps if p[0]==0 and sum(a>b for a,b in combinations(p,2))%2==0};data=json.loads((D/'ramsey_online_exit_reanchor.json').read_text());out=[]
    for orig,rec in zip([('BRNN','BNRN'),('BNRN','BRNN')],[s for s in data if s['update']]):
        for ex in rec['exits']:
            p=frames[ex['old_Q']];q=frames[ex['new_Q']];old=tuple(act(p,w) for w in orig);new=tuple(act(q,w) for w in orig);u,v=(w.index('R') for w in old);swap=tuple(v if i==u else u if i==v else i for i in range(4));nn,=[s for s in ps if act(s,old[0])==old[0] and s!=tuple(range(4))];g=tuple(q[p.index(i)] for i in range(4));assert g==tuple(nn[swap[i]] for i in range(4)) and new[1]==old[0] and new[0] not in old;assert ex['new_Q']==v+1;out.append(dict(old=old,new=new,retained_word=new[1],invisible_swap=[i+1 for i in range(4) if nn[i]!=i],external_third_word=new[0]))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_exit_literal_row_gauge.json').write_text(json.dumps(out)+'\n')
