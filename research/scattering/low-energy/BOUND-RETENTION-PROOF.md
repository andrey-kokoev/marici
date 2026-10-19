# C5 — ordered-limit bound retention for the named preparations

## Exact claim and normalizations

Use C2's fixed full Hilbert space and five normalized full-tail eigenmodes phi_a with distinct energies E_a. Let P_b be their orthogonal projection and let P_R retain the eleven central coordinates and the first R sites of each of the three leads.

The named normalized central preparations are the belt port e0/sqrt(h0), the carrier sum (e1+e2)/sqrt(40), the carrier difference (e1-e2)/sqrt(40), and the individual carrier ports e1/sqrt(20), e2/sqrt(20), with h0=1196/15. The source's proton/electron labels here identify mathematical port vectors, not independent physical particle identifications.

## Large-region, long-time-averaged identity

Write psi=psi_b+psi_ac using C2 and C9. Completeness gives an outgoing free state f for psi_ac with

    ||exp(-itH)psi_ac-J exp(-itH_D)f|| -> 0.

For each fixed R, the free packet has vanishing norm in P_R as t->infinity. Indeed each finite-site amplitude is a sine-transform integral with an L1 energy density after the monotone change E=2-2cos(k); Riemann–Lebesgue applies. The statement extends to arbitrary free L2 inputs since the sine kernel times an L2 function is L1 on the finite k interval. The central component of J is zero. Thus ||P_R exp(-itH)psi_ac||->0. Its time-averaged square and its cross term with the uniformly bounded bound component also tend to zero.

Expand psi_b=sum_a c_a phi_a. For fixed R,

    lim_(T->infinity) (1/T) integral_0^T ||P_R exp(-itH)psi||² dt
      = sum_a |c_a|² ||P_R phi_a||².

Distinct bound energies make every off-diagonal time average vanish. Taking R->infinity afterward gives ||P_R phi_a||->1 and therefore

    lim_(R->infinity) lim_(T->infinity) (1/T) integral_0^T
      ||P_R exp(-itH)psi||² dt = sum_a |c_a|² = ||P_b psi||².

The order of limits matters. Taking R->infinity first would give the full conserved norm at every time. For normalized psi the escaping **squared norm** is 1-||P_b psi||², while the outgoing state's norm is its square root. No claim that instantaneous central occupation converges is made; bound-state beating can persist.

## Fresh nonzero-overlap certification

Reconstruct the exact H-orthogonal invariant preparation sectors from the source core: a dimension-five sector seeded by e0 and e1+e2, and a dimension-six sector seeded by e1-e2. Verify invariance under the actual K and the port projector P, not only the names of the seeds. The sectors exhaust the eleven coordinates and their active port ranks are two and one.

For each of the five source rational decay brackets, freshly evaluate the corresponding restricted secular matrix and the principal minor obtained by removing each active port coordinate. The full block has one simple root in the bracket. The minor has identical nonsingular endpoint inertias. Its positive derivative in E implies its inertia cannot change inside without an eigenvalue crossing zero; equal endpoint counts therefore prove it remains nonsingular at the full root.

The nonzero diagonal cofactor at a simple Hermitian root implies that the kernel vector has nonzero amplitude at the removed active port coordinate. Thus the belt and carrier sum overlap both symmetric-sector modes; the carrier difference overlaps all three antisymmetric-sector modes. Each individual carrier is half the sum plus or minus half the difference. Orthogonality of the two spectral sectors prevents cancellation, giving overlap with all five modes.

Every listed nonzero normalized preparation therefore has ||P_b psi||²>0. This certifies positivity, not the magnitude of the retained fraction or an assertion that all its norm is bound.

## Verification boundary

`check_bound_retention.py` replays C2, rebuilds the two reducing sectors, checks actual K/P invariance and recomputes all fourteen active-port minor endpoint inertias in exact Q(sqrt(151)) arithmetic. It does not trust source overlap flags or assign a numerical retained fraction. The ordered-limit argument above is analytic and applies to the full lead tails; no finite lead truncation is used.
