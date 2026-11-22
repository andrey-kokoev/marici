"""After SAT excludes all deviations outside star 35, enumerate that star with the chart constraints and certify sharp probe count by singleton differences."""
from ramsey_exoo_root_readout import edges,Path,json
E=edges();H=[sum(1<<j for j in range(39) if tuple(sorted((i,j))) in E) for i in range(39)];anchor=H[22]|1<<22;I=[0]
for i,h in enumerate(H):
    if i!=35:I +=[s|1<<i for s in I if not s&h]
T=[s for s in I if s.bit_count()==9];G={s for s in I if not (s^H[35])&anchor and all(s&t for t in T)};F=[i for i in range(39) if any(s^(1<<i) in G for s in G)];words=sorted(''.join(str(s>>i&1) for i in F) for s in G);assert len(set(words))==len(G);r=dict(probes=F,words=words);print(len(G),F,sorted(words)[:6]);Path(__file__).with_suffix('.json').write_text(json.dumps(r)+'\n')
