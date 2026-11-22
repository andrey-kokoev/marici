"""Complete the observed first exit cycle without prescribing the disjoint complement. Ask whether the local record already forces the literal mate, optionally requiring the NEXT swap to be irreducible."""
from ramsey_second_cycle_ablation import final,move,trans,cycles,D,json
from ramsey_history_matching_provenance import enum
from collections import Counter

def run():
    initial,=final;base=move(initial,trans(3,2));real=move(base,trans(2,4));ec,aux=cycles(base,real);out=[]
    for m in enum():
        if ec not in cycles(base,m):continue
        nxt=move(m,trans(4,3));c=cycles(m,nxt);out.append(dict(extra=[len(q) for q in cycles(base,m) if q!=ec],next_exit_component=len(c[0]),next_components=list(map(len,c)),same_next_exit_cycle=c[0]==cycles(real,move(real,trans(4,3)))[0],difference_from_literal=sorted(m^real),common_real=len(real&m),real=m==real))
    assert sum(v['real'] for v in out)==1;return out
if __name__=='__main__':
    out=run();print(len(out),Counter((r['next_exit_component'],tuple(r['next_components'])) for r in out));(D/'ramsey_aux_completion_decoder.json').write_text(json.dumps(out)+'\n')
