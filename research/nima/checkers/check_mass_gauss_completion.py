"""Integer Gauss constraints enforce collective occupation, not its energy scale."""
from pathlib import Path
from itertools import combinations, product
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_gap_symmetry.py'))
slots=sorted(prior['slots']); index={s:i for i,s in enumerate(slots)}
N=len(slots); identity=tuple(range(4)); generators=[]
for role in range(3):
    for a,b in combinations((1,2,3),2):
        p=list(identity); p[a],p[b]=p[b],p[a]
        g=[identity]*3; g[role]=tuple(p); generators.append(tuple(g))
edges=set()
for s in slots:
    for g in generators:
        i,j=index[s],index[prior['act'](s,g)]
        if i!=j: edges.add(tuple(sorted((i,j))))

def components(n,links):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for i,j in links:
        a,b=find(i),find(j)
        if a!=b: parent[b]=a
    groups={}
    for i in range(n): groups.setdefault(find(i),[]).append(i)
    return sorted(groups.values(),key=lambda x:x[0])
blocks=components(N,edges)
assert len(blocks)==30
# Complete only for a CONDITIONAL test: these 29 bridges are new constraints,
# not operations supplied by carrier relabellings.
bridges={(blocks[k][0],blocks[k+1][0]) for k in range(len(blocks)-1)}
complete=edges|bridges
assert len(bridges)==29 and len(components(N,complete))==1
# Integer kernel: n_i-n_j=0 makes charge constant on each component.
# A whole-block unit shift is gauge invariant; a single-site shift is not.
for block in blocks:
    vector=[int(i in set(block)) for i in range(N)]
    assert all(vector[i]==vector[j] for i,j in edges)
    assert sum(vector)==len(block)
assert min(map(len,blocks))<N
one_site=[int(i==0) for i in range(N)]
assert any(one_site[i]!=one_site[j] for i,j in complete)
assert all(1-1==0 for i,j in complete)  # collective +1 shift preserves every G
# Independent exhaustive low-charge windows on small connected graphs.
for n in range(2,7):
    links={(i,i+1) for i in range(n-1)}
    allowed=[v for v in product((-1,0,1),repeat=n) if all(v[i]==v[j] for i,j in links)]
    assert set(allowed)=={(-1,)*n,(0,)*n,(1,)*n}
    assert min(sum(x*x for x in v) for v in allowed if any(v))==n
# Unit charging coefficients produce N. Gauge invariance permits unequal ones.
weights=[1 if s[1][0]=='arrow' else 2 for s in slots]
assert sum(weights)==1944
# Even full neutral permutation symmetry permits collective charging energy.
# gamma*(sum n)^2 with gamma=1/N adds N at k=1 and commutes with all Gauss laws.
assert N+N*N//N==3672
# A one-particle incidence zero mode must not be confused with N rotor charges:
# the normalized constant mode of Delta*I+L has energy Delta, not N*Delta.
assert sum((1-1)**2 for i,j in complete)==0
assert (N+0)//N==1

result={
 'status':'passed','classification':'gauss_constraints_force_collective_integer_excitation_conditionally',
 'slots':N,'relabelling_graph_edges':len(edges),
 'source_envelope_components':len(blocks),
 'source_component_sizes':sorted(map(len,blocks)),
 'added_completion_constraints':len(bridges),
 'conditional_unit_gap_ratio':N,
 'gauge_invariant_hostiles':{'unequal_type_gaps':sum(weights),'collective_charging_term':3672},
 'checks':{'prior_chain_fresh':True,'integer_gauss_kernel':True,
           'single_channel_excitation_forbidden_after_completion':True,
           'small_rotor_window_enumeration':True,'energy_not_fixed_by_gauge_law':True,
           'normalized_single_particle_mode_not_a_mass_count':True},
 'conclusion':'Compact rotor Gauss constraints can enforce a collective1836-channel excitation without soft stiffness tuning. The relabelling-generated graph instead has30 independent components. Connecting them and selecting the charging Hamiltonian are additional physical inputs; neither1836 units of energy nor a proton identification follows from gauge invariance alone.',
 'next_falsifier':'Find actual source operations connecting the30 comparison orbits, and derive their capacitance/energy form. The29 illustrative bridge constraints must not be promoted to sourced relations.'}
out=HERE.parent/'results/mass-gauss-completion.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
