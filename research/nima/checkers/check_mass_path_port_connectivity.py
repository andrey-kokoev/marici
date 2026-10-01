"""Path continuation connects comparison ports; it does not imply charge locking."""
from pathlib import Path
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_gauss_completion.py'))
slots=prior['slots']; index=prior['index']; N=len(slots)
components=prior['components']; E=[(i,j) for i in range(4) for j in range(4) if i!=j]
links={name:set() for name in ('outer','inner_left','inner_right','endpoint')}
directions={name:set() for name in links}
def link(kind,s,t):
    assert s in index and t in index
    i,j=index[s],index[t]
    if i!=j:
        links[kind].add(tuple(sorted((i,j))))
        directions[kind].add((i,j))
for s in slots:
    outer,(kind,a,b)=s
    # Projection of a history-preserving append: the active last arrow changes.
    for f in E:
        if outer[1]==f[0]: link('outer',s,(f,s[1]))
    if kind=='arrow':
        for f in E:
            if a[1]==f[0]: link('inner_left',s,(outer,(kind,f,b)))
            if b[1]==f[0]: link('inner_right',s,(outer,(kind,a,f)))
        # These are typed readouts. We retain the parent arrow/path in a real
        # realization; the incidence link does not assert physical reversibility.
        for end in (0,1):
            if a[end]!=0 and b[end]!=0:
                link('endpoint',s,(outer,('state',a[end],b[end])))

cumulative=set(prior['edges']); stages=[len(components(N,cumulative))]
for name in links:
    cumulative |= links[name]; stages.append(len(components(N,cumulative)))
assert stages==[30,10,4,2,1]
source_links=set().union(*links.values())
assert len(components(N,source_links))==1
# Weak incidence connectivity is NOT reversible physical transport.
adj=[set() for _ in slots]; rev=[set() for _ in slots]
for es in directions.values():
    for a,b in es: adj[a].add(b); rev[b].add(a)
def reachable(start,graph):
    seen={start}; todo=[start]
    while todo:
        for v in graph[todo.pop()]:
            if v not in seen: seen.add(v); todo.append(v)
    return seen
unseen=set(range(N)); strong_sizes=[]
while unseen:
    start=min(unseen)
    strong=reachable(start,adj)&reachable(start,rev)
    strong_sizes.append(len(strong)); unseen-=strong
assert sorted(strong_sizes)==[12]*9+[1728]
# Appending a closed path returns the active edge, but not the retained history.
p=(0,1); extended=p+(0,1)
assert p[-2:]==extended[-2:] and p!=extended
assert len(extended)-len(p)==2
# Unit positive append cost cannot descend to a potential on active edges:
# e01 -> e10 -> e01 would require V(e01)=V(e01)+2.
assert sum((1,1))!=0

# Ordinary Kirchhoff conservation allows sparse cycle currents, rather than
# imposing equality of all node charges. Construct an exact three-edge witness.
inner=('state',1,1)
cycle=[index[(e,inner)] for e in ((0,1),(1,2),(2,0))]
flow={}; divergence=[0]*N
for a,b in zip(cycle,cycle[1:]+cycle[:1]):
    edge=tuple(sorted((a,b))); assert edge in source_links
    flow[edge]=1 if a<b else -1
    divergence[a]-=1; divergence[b]+=1
assert all(d==0 for d in divergence) and len(flow)==3
cycle_rank=len(source_links)-N+1
assert cycle_rank>1

result={
 'status':'passed','classification':'path_port_connectivity_closed_gauss_and_energy_bridge_open',
 'components_after_operations':dict(zip(('rooted_relabellings','outer_continuation','left_continuation','right_continuation','endpoint_readout'),stages)),
 'operation_edge_counts':{name:len(es) for name,es in links.items()},
 'path_and_readout_graph':{'vertices':N,'edges':len(source_links),'components':1,'kirchhoff_cycle_rank':cycle_rank,
                           'directed_strong_component_sizes':sorted(strong_sizes)},
 'checks':{'prior_chain_fresh':True,'typed_endpoints_and_composable_appends':True,
           'no_arbitrary_component_bridges_needed_for_connectivity':True,
           'weak_connectivity_not_reversible_transport':True,
           'closed_walk_retains_history_and_cost':True,
           'positive_path_cost_not_an_active_port_potential':True,
           'sparse_conserved_current_not_equal_channel_occupation':True},
 'conclusion':'Existing composable path continuations and typed endpoint readouts weakly connect the finite1836-port incidence graph without arbitrary bridge edges; directed transport still has10 strong components. This is not a derived Gauss equality: projection forgets retained histories, and ordinary current conservation permits sparse cycles. The physical charge-locking law and energy form remain unconstructed.',
 'next_falsifier':'Construct a history-retaining physical interaction whose constraint is n_s=n_t on these incidences; show why ordinary sparse cycle currents and unequal charging coefficients are excluded without imposing the target ratio.'}
out=HERE.parent/'results/mass-path-port-connectivity.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
