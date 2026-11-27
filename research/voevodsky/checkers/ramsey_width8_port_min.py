"""Fixed (3,7). All matched parents of the specified two-support family."""
from ramsey_forward_path_insertion import graph,check,D,combinations,Counter,sha256,json

def run():
    U=range(8);rows=[s for s in combinations(U,3) if min(s[1]-s[0],s[2]-s[1])>=2];counts=Counter();examples={}
    for A,B in combinations(rows,2):
        if set(A)&set(B):continue
        counts['support_pairs']+=1;h,l=sorted(set(U)-set(A+B))
        for m in range(1,4):
            ss=[A]*m+[B]*(4-m);cols=(0,1<<list(combinations(range(4),2)).index((0,m)))
            if not all(check(graph(8,ss,c),4095,3,7) for c in cols):continue
            counts['legal_parent_pairs']+=1
            for gap in range(9):
                new=[tuple(x+(x>=gap) for x in s) for s in ss];a,b=(graph(9,new,c) for c in cols);p,q=(check(g,8191,3,7) for g in (a,b));assert not(p and not q)
                compatible=l-h>1 and not({h,l}&{gap-1,gap});cl=[h+(h>=gap),l+(l>=gap),gap,9,10,11,12];assert compatible==all(not(a[i]>>j&1) for i,j in combinations(cl,2))
                split=p!=q;assert not split or compatible;key=('compatible' if compatible else 'incompatible')+('_split' if split else '_same');counts[key]+=1
                if 0<gap<8:examples.setdefault(key,dict(supports=[[x+1 for x in s] for s in ss],uncovered=[h+1,l+1],after_old_site=gap,red_pair_1based=[1,m+1],child_legal=[p,q]))
    assert 'compatible_split' in examples;out=dict(protocol_sha=sha256((D.parent/'ramsey_width8_port_protocol.md').read_bytes()).hexdigest(),counts=counts,interior_examples=examples);print(out);text=json.dumps(out,indent=2)+'\n';dest=D.parent/'ramsey_width8_port_min.json';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
