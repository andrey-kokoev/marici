from collections import Counter
from itertools import combinations
from ramsey_seed_boundary_residue import D, cycles, json, move, R, sha256


def run():
    E=[''.join(t) for t in combinations('1234',2)];P=list(combinations(E,2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];fan=P.index(('24','34'));opts=[k for k,t in enumerate(T,15) if P[fan] in t];fixed,=[v for v in opts if R[v]==v];axis=P.index(('14','23'));assert (fan,opts,fixed)==(14,[15,18,21],15) and R[21]==18 and R[14]==14
    common={tuple(map(tuple,z['matching'])) for z in json.loads((D/'ramsey_seed_boundary_residue.json').read_text())['cases']};table=Counter();examples={}
    def visit(m,taken,i):
        if i==15:
            a=frozenset(enumerate(m));b=move(a,R);n=len(cycles(a,b));absent=(14,21) not in a|b;assert absent==(m[14]==fixed)==(m[14]==dict(b)[14])==(m.index(fixed)==14);assert m.index(fixed) in (14,axis);key=(tuple(sorted(a)) in common,absent,n);table[key]+=1;examples.setdefault(key,sorted(a));return
        opts=[j for j,t in enumerate(T,15) if P[i] in t and j not in taken and (i!=0 or j==16) and (i!=7 or j==29)]
        for j in opts:visit(m+[j],taken|{j},i+1)
    visit([],set(),0);assert sum(table.values())==36;encode=lambda d:{'/'.join(map(str,k)):v for k,v in sorted(d.items())};out=dict(axis=axis,neutral_fan=P[fan],partitions={k:T[k-15] for k in opts},counts=encode(table),examples=encode(examples),protocol_sha=sha256((D/'ramsey_neutral_fan_protocol.md').read_bytes()).hexdigest());print(out['axis'],out['counts']);(D/'ramsey_neutral_fan.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
