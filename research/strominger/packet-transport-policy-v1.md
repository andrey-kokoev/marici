# Native transport policy and the conditional chart extension

Iteration4. Contract: `research/strominger/contracts/packet-transport-policy.v1.json`. This resolves the net's native/supplied gate by selecting its **native branch with retained -I comparison**, not by pretending the chart extension is native or primitively costed.

## Different typed tasks

The electron native task acts on its normalized logical spinor with24 binary tetrahedral matrices. For every signed distinct-axis pair A=epsilon E_a, B=eta E_b,

    AB=-BA, (AB)*(BA)=-I.

All12 signed sectors retain this comparison. Their full-amplitude reference pairings are +1 and -1, although the corresponding densities agree. An inverse recovers the image state; it does not erase either execution from the archive.

The optional chart task instead retains a fixed reference z_ref and current vertex u in {-1,0,1}³. Its value is C(u)z_ref and an edge u->v acts by T(v,u)=C(v)C(u)*. Admission requires the actual source vertex and a directed nearest-neighbor edge. Different edge words remain distinct even when their endpoint spinors agree. Validation replays the marked edge archive and checks the current spinor against its reference/chart.

Native-only chart policy admits an edge only if its matrix belongs to the24-element native group. Supplied-grid policy admits all108 declared edges as a mathematical extension. It does not imply admission of every SU(2) operation, physical control, or a primitive implementation.

## Fresh edge-level result

| Quantity | Exact count |
|---|---:|
| Grid vertices |27|
| Native vertex matrices C(u) |15|
| Nonnative vertex matrices |12|
| Directed nearest-neighbor edges |108|
| Native edge matrices T(v,u) |12|
| Edges requiring supplied nonnative matrices |96|
| Vertices reachable from origin using native grid edges |7|

Vertex membership is not edge availability: even15 native vertex matrices do not yield native transport along all coordinate edges. The7 reachable vertices are the origin and its six axis neighbors. This grid restriction does not remove the other operations from the separate24-action native task; it constrains only paths that must follow these coordinate edges.

Both supplied orders agree in all12 two-coordinate sectors. Each route enters a nonnative corner through a nonnative edge, refused by native-only policy. Native group closure independently excludes reaching that corner matrix by any finite native word. All108 edges satisfy exact unitarity, inverse-edge and encoded/raw transport squares.

## Cost ledger, not a fitted price

Every executed matrix carries a formal occurrence token c_native(U) or c_supplied(T). Numeric primitive costs and units are unassigned. The ledger retains both occurrences in a forward/inverse pair and does not simplify cost from the product matrix. Identical matrix tokens may identify operation types, but this does not authorize sharing executions or a free reset.

The existing16+64+64=144 counts the stored coefficient protocol's stage support. It is neither a per-logical-command price nor a chart-edge implementation. A supplied primitive constructor and valuation are required before numeric cost comparison. The native-only branch needs no invented flat filler: it keeps the actual -I witness as permitted by the gate's original acceptance condition.

## Verification and continuation

    python research/strominger/checkers/check_packet_transport_policy.py
    python research/aspect/scc/scc.py check packet-transport-policy-v1
    python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1

Twelve fresh exact checks pass, including source-vertex, forged-state, availability and phase-erasure hostiles. Receipt: `research/strominger/results/packet-transport-policy-v1.json`; it includes all108 directed-edge admission/cost-token records and12 sector witnesses, bound to current source/checker/contract hashes. Native producers are not run; upstream sources/stores/pins remain unchanged. No Agda recompile or primitive/physical cost certification is claimed.

Three net obligations remain: actual proton/neutron spin-coupling binding, certificate/stage cost correspondence and the bridge root. Only the first is ready. It must supply an explicit carrier/coupling enlargement, or an exact blocker, without changing the rank-one source in place.
