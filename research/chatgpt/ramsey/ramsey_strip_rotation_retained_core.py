"""Find the links common to all four rotated matchings. Compare preservation of whole row residue, maximal common core, and feasibility of accumulating all rotated residues."""
from collections import Counter
from ramsey_strip_rotating_boundary import f,image,leaves,allms
from ramsey_strip_boundary_binary_search import target
from ramsey_strip_matching_restart import turn
stats=Counter();cores={}
for m in leaves:
    orbit=[m]
    for _ in range(3):orbit.append(image(orbit[-1],f))
    core=frozenset.intersection(*orbit);res=m&turn(m);assert image(core,f)==core;assert core==res&image(res,f)
    union=res|image(res,f);compatible=len({x for e in union for x in e})==2*len(union)
    ext=sum(union<=n for n in allms) if compatible else 0
    stats[len(res),len(core),compatible,ext]+=1;cores[m]=core
print('residue size, retained core size, union compatible, union completions:',dict(sorted(stats.items())))
print('target residue',sorted(target&turn(target)),'rotation core',sorted(cores[target]));mx=max(map(len,cores.values()));best=[m for m,c in cores.items() if len(c)==mx];print('largest retained core',mx,'candidates',len(best),'target included',target in best)
print('largest core candidates by first branch',Counter(leaves[m][0] for m in best))
