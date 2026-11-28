"""Independent restricted counterexample searches: frozen forward rule, free port rows, exact two-addition cost."""
from ramsey_double_cross_blind_veto import audit as generate
from ramsey_cross_residual_propagation import audit as finish
from ramsey_centered_family_envelope import enumerate_all,D,json,G,induced,Counter,CAT,gzip,decode
from itertools import islice

def transfer(idx):
    src=generate(idx=idx,score_cube=False);res=finish(src);return dict(record=idx,starts=res['start_count'],cases=res['case_counts'],survivors=res['survivors'],proposals=src['counts']['proposals'])

def pack(a):
    # Necessary only: two port rows cannot both miss an old blue seven.
    I=[0]
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
    seven=[q for q in I if q.bit_count()==7];assert max(q.bit_count() for q in I)==7
    rows=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];miss=[sum(1<<j for j,q in enumerate(seven) if not q&s) for s in rows];
    if 0 in miss:return True  # repeated maximal row may pass this relaxation
    def search(options,needed):
        if needed==1:return bool(options)
        for i,m in enumerate(options):
            if len(options)-i<needed:break
            if search([v for v in options[i+1:] if not v&m],needed-1):return True
        return False
    return search(sorted(set(miss),key=int.bit_count),8)

def run():
    T=D.parent;V=json.loads((T/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,V);assert pack(a);prev=json.loads((T/'ramsey_double_cross_blind_veto.json').read_text());idx=prev['record'];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,idx,None)).strip())
    passed=[]
    for n,r in enumerate(prev['candidates']):
        h=b[:]
        for i,j in r['pair']+r['forced']:h[i]^=1<<j;h[j]^=1<<i
        if pack(induced(h,[v for v in range(27) if v!=r['z']])):passed.append(n)
    rows=json.loads((T/'ramsey_cube_cut_location.json').read_text())['cases'];hist=Counter()
    for r in rows:
        es,models=enumerate_all(a,r);hist.update(2+m.bit_count() for m in models)
    result=dict(two_addition_signatures=len(rows),two_addition_cost=hist,port_tested=len(prev['candidates']),passed_port_indices=passed,transfer=transfer(99148));print('C2',len(passed),'C3',hist);(T/'ramsey_three_claim_attack.json').write_text(json.dumps(result,indent=1)+'\n')
if __name__=='__main__':run()
