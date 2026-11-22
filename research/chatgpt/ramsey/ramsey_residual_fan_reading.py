"""Decode the nonconstant residual flags on the six closed strip paths in fixed corner labels. Test each member separately against the previously computed compatibility outcomes."""
from ramsey_folded_entry_handoff import X,P,T,D,json
from ramsey_row_quotient_constructor import R

def decode(i,j):
    centres=[set(X[a])&set(X[b]) for a,b in T[j-15]];f=sum(bool(s) for s in centres);a,b=P[i];apex,=set(X[a])&set(X[b]);missing=sorted(set(range(1,5))-set.union(*centres));answer='neither' if f!=3 else ('handoff' if apex==1 or missing==[4] else 'retain');return dict(flag=[i,j],fans=f,apex=apex,missing=missing,reading=answer)
def run():
    out=[]
    for q in json.loads((D/'ramsey_route_fill_decagon_test.json').read_text()):
        r,=q['results'];z=set(map(tuple,r['fill']))-{(9,26),(14,15)};u,v=sorted(z);assert tuple(R[x] for x in u)==v;d=[decode(*e) for e in (u,v)];choices=[name for k,name in [('10','retain'),('13','handoff')] if r['controls'][k][-1]];assert all(x['reading']==next(iter(choices),'neither') for x in d) and len(choices)<=1;out.append(dict(path=q['path'],extra=d))
    return out
if __name__=='__main__':
    out=run();print([q['extra'][0] for q in out]);(D/'ramsey_residual_fan_reading.json').write_text(json.dumps(out)+'\n')
