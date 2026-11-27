"""Conditional four-function tet test. No truth values assigned to vertices before full resolution."""
from collections import Counter
from itertools import product
from pathlib import Path
import json


def query(mark,kind,n_positive):
    # Each request returns a continuation on the immutable full-net binding.
    def resolve(net):
        binding=net[mark]
        if binding=='N': return False if kind=='-' else n_positive(net,mark)
        return binding==kind  # declared exclusive/exhaustive color control
    return resolve


def vertex(marks,kind,absence,n_positive):
    fs=[query(i,kind,n_positive) for i in marks]
    def resolve(net):
        values=[f(net) for f in fs]
        return not any(values) if absence else all(values)
    return resolve


def census(n_positive):
    A=range(3);B=range(3,10);vertices=[vertex(A,'+',False,n_positive),vertex(B,'+',False,n_positive),vertex(A,'-',True,n_positive),vertex(B,'+',True,n_positive)];out=Counter()
    for net in product('+-N',repeat=10):
        key=tuple(int(f(net)) for f in vertices);out[''.join(map(str,key))]+=1
    return out

def run():
    gap=census(lambda net,i:False);total=census(lambda net,i:True)
    # Role N's minus reply is identical; only its unspecified plus request differs.
    assert sum(gap.values())==sum(total.values())==3**10
    witness=lambda h:sum(n for k,n in h.items() if k[0]=='0' and k[2]=='1')
    assert witness(gap)>0 and witness(total)==0;assert len(gap)==9 and len(total)==6
    out=dict(assumptions='Domains are three A and seven B addresses; N is admitted as a responder at an address. Non-neutral signed controls are exclusive and exhaustive; B uses the same positive request for all and none. States are synthetic full-net bindings, not source frequencies.',order=['all A+','all B+','no A-','no B+'],no_A_minus_without_all_A_plus=[witness(gap),witness(total)],N_no_positive=gap,N_supplies_positive=total);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_tet_predicates.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
