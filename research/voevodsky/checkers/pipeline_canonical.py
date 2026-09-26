"""Read-only pipeline equivalence: ordered output roots, optional proof stages."""
from copy import copy
from forest_canonical import canonical

def key(net,proof=True):
 assert len(set(net.outputs))==len(net.outputs)
 positions={n:i for i,n in enumerate(net.outputs)}
 view=copy(net)
 view.tags={n:(net.stage[n] if proof else 0,positions.get(n,-1)) for n in net.types}
 graph=canonical(view,tagged=True)
 return (net.stage_ops,graph) if proof else graph
