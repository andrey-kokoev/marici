# Port-level XOR net prototype exposes only parity at closed boundary

Fresh `check_port_chain_xor_net.py` represents an ACC agent with principal output joined to the principal input of a BIT agent; BIT has an auxiliary next-wire. The local active-pair rewrite replaces ACC(p)--BIT(b) with ACC(p xor b) and reconnects its principal output to BIT.next. Each step checks unique port labels, connected acyclic remaining chain, and absence of dangling internal next references. Exhaustive words of length 0..8 yield the expected parity, consuming each labelled bit exactly once. A closed chain exposes only its final parity bit, so the two-state summary is sufficient for its specified observations.

An indexed READ(i) operation is not available on this closed interface. To admit it one must retain labelled side ports or equivalent access; the previously established 2^n distinguishability then applies. This is a typed port-graph fragment, not a complete interaction-net semantics or a model of Nima's E/E_B operations.

Next test compositionality at the boundary: joining two closed segments must preserve parity under either evaluation order without duplicating/losing port wires. Specify the interface operation and prove its summary congruence for arbitrary finite segment lengths.
