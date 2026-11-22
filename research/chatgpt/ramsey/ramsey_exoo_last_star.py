"""Try to refute the sole unresolved full star (chart root 22, reader 35) by lazy exact completion. Fix chart and reader to Exoo; block Exoo itself; learn an independent-ten clause until UNSAT or a verified second wiring."""
from itertools import combinations
from ramsey_exoo_root_readout import edges,Path,json
from pysat.solvers import Solver

def run(mandatory_only=False, test_outside=False):
    E=edges();pairs=list(combinations(range(39),2));ix={p:i+1 for i,p in enumerate(pairs)};fixed={22,35}|{w for p in E if 22 in p for w in p};chart=fixed-{35};probes={tuple(e) for e in json.loads(Path(__file__).with_name('ramsey_exoo_root_readout.json').read_text())[22]['mandatory']};pin=lambda p:bool(chart.intersection(p) or (not test_outside and (p in probes if mandatory_only else 35 in p)));C=[[ix[p] if p in E else -ix[p]] for p in pairs if pin(p)];C += [[-ix[i,j],-ix[i,k],-ix[j,k]] for i,j,k in combinations(range(39),3)];C.append([(-1 if p in E else 1)*ix[p] for p in pairs if not pin(p) and (not test_outside or 35 not in p)]);learned=0
    with Solver(name='g4',bootstrap_with=C) as sat:
        sat.set_phases([ix[p] if p in E else -ix[p] for p in pairs]);
        while sat.solve():
            m=set(sat.get_model());N={p for p in pairs if ix[p] in m};h=[sum(1<<j for j in range(39) if tuple(sorted((i,j))) in N) for i in range(39)];I=[0];bad=[]
            for i in range(39):
                for s in [u|1<<i for u in I if not h[i]&u]:
                    if s.bit_count()==10:bad.append(s)
                    else:I.append(s)
            if not bad:
                assert N!=E and all(not h[i]&h[j] for i,j in N) and all(not pin(p) for p in N^E);return dict(changed=sorted(N^E),learned=learned)
            for t in bad:sat.add_clause([ix[p] for p in combinations([i for i in range(39) if t>>i&1],2)])
            learned+=len(bad)
    return dict(unique_at_Exoo=True,learned=learned)
if __name__=='__main__':
    rs={mode:run(mode=='mandatory_only',mode=='outside') for mode in ('full_star','mandatory_only','outside')};print(rs);Path(__file__).with_suffix('.json').write_text(json.dumps(rs)+'\n')
