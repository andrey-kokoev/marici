"""Eight-role patch. Select one internal edge by maximal transfer support; test a relative, rather than unary, edge reader. No Ramsey graph input."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json
HOME=Path(__file__).resolve().parents[1]

def run():
    d=json.loads((HOME/'results/esd7_explicit_analytical_census.json').read_text()); t=next(q for q in d['tetrahedra'] if q['id']=='T184');v=set(t['vertices']);u=set(v)
    for f in combinations(v,3):
        across=[set(q['vertices']) for q in d['tetrahedra'] if q!=t and set(f)<=set(q['vertices'])];assert len(across)==1;u|=across[0]
    assert len(u)==8
    labels={frozenset(e['vertices']):set(e['transfer_mask']) for e in d['edges'] if set(e['vertices'])<=u};internal=[e for e in labels if e<=v];maxima=[e for e in internal if not any(labels[e]<labels[q] for q in internal)];assert len(maxima)==1;selected,=maxima
    def edges(s):return {frozenset(t) for t in combinations(s,2)}
    def trial(c):
        leaves=u-c;touch={w:{a for a in c if frozenset((a,w)) in labels} for w in leaves};legal=[]
        for private,shared in product((False,True),repeat=2):
            red={c}|{frozenset((a,w)) for w,z in touch.items() for a in z if private and len(z)==1 or shared and len(z)==2};blue=edges(u)-red
            def has(s,r,E):return any(edges(f)<=E for f in combinations(s,r))
            if has(u,3,red) or has(u,7,blue):continue
            verdict=lambda s:('−' if has(s,2,red) else '+')+('−' if has(u-s,6,blue) else '+')
            states={key:verdict(s) for key,s in [('six',leaves),('eight',u),('empty',set()),('pair',c)]};assert states==dict(six='++',eight='−+',empty='+−',pair='−−');legal.append(dict(private=private,shared=shared,red=sorted(sorted(e) for e in red),states=states))
        assert len(legal)==1;return dict(pair=sorted(c),contacts=dict(sorted((w,sorted(z)) for w,z in touch.items())),eligible=legal)
    chosen=trial(selected);controls=[trial(e) for e in internal if e!=selected];return dict(selected=chosen,transfer=''.join(sorted(labels[selected])),alternative_pairs_with_square=len(controls),central_vertices=sorted(v))
if __name__=='__main__':
    res=run();print(json.dumps(res,indent=2));(HOME/'results/ramsey_t184_relative_link_reader.json').write_text(json.dumps(res,indent=2)+'\n')
