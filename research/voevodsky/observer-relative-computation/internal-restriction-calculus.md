# First-order internal restriction calculus

`agda/ObserverInternalRestriction.agda` introduces structural restriction data: identity, discard, left/right projection, pairing, and composition. No constructor stores a host-language reply callback. Its interpreter is fixed by these constructors.

Checked results:

- Every restriction preserves the readout of the SAME history.
- It therefore induces a map on admissible images, retaining the visible reply and truncated origin membership.
- Identity and composition laws hold for these image maps.
- Any two parallel restrictions agree pointwise on admissible images.
- A restriction c→d exists exactly when rule access in d implies rule access in c. Necessity transports capabilities; sufficiency compiles the capability implication into structural syntax. This is an existence characterization, not an equivalence identifying all syntax witnesses.
- There is no restriction from result-only access to rule access.
- Left and right projections disagree on the raw pair (true,false), but agree on every admissible duplicate-rule reading.

Thus internal comparison paths can differ syntactically and on impossible raw inputs while yielding coherent restrictions of witnessed observations. This does not identify the original restriction syntax, impose physical access control, or give a resource-cost theorem.

## Scope and higher-witness boundary

The agreement proof eliminates truncated origin membership into reply equality, using the established SETNESS of these replies. It is not a theorem that comparison witnesses in arbitrary groupoid-valued observation types can be erased. The current pointwise image equalities do not manufacture a general higher-coherence theorem outside this set-valued fixture.

Next: internalize a finite comparison-witness language beyond this set-valued case and test the boundary explicitly. Distinguish a fixed-visible-reply fibre from the total dependent certificate space: distinct loops at a fixed reply need not yield distinct elements when the reply itself is allowed to move. Preserve those distinctions before asserting a richer internal-observer normalization theorem.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror check: results/agda-internal-restriction.log. The module is in the aggregate imports. A fresh check_transport_gate.py run passes local, whole ordinary, and whole -Werror checks with inventoried source bytes unchanged: results/transport-gate.json.
