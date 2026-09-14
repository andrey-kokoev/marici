# Probe residue does not canonically backreact on the prime lattice

## Question

Can incoming probe residue canonically change a source point or the ambient prime-valuation lattice using only the structures already defined?

## Claim boundary

The test addresses the evident adjoint candidate obtained from character evaluation and the shell-to-root map. It does not prohibit an additional sector from supplying a feedback law, coupling, normalization, or integral projection. Such data would be a new typed input rather than a consequence of the current probe geometry.

## Candidate response direction

Let

\[
M_T:W_n\longrightarrow k^T
\]

be character evaluation and let

\[
A:W_n\longrightarrow F_{n+1},
\qquad
A(e_i)=f_{i+1}-f_i
\]

embed shell directions as type-\(A\) roots. Using the declared coordinate pairings, a readout residue \(r\in k^T\) yields the candidate displacement

\[
\delta_T(r)=AM_T^{\mathsf T}r.
\]

This is the narrowest available route from residue back to valuation coordinates.

## Degree preservation

Every column of \(A\) has coordinate sum zero. Therefore

\[
\deg\delta_T(r)=0.
\]

If the displacement is admitted at a state, it preserves \(\Omega\). This supplies a valid tangent direction in the rational root space.

## Integrality obstruction

For rational settings such as \(5/6,3/4,7/10\), the entries of \(M_T\) contain nontrivial denominators. Consequently, integral readout basis vectors generally map to

\[
\delta_T(r)\in F_{n+1}\otimes\mathbb Q
\]

rather than the integer valuation lattice. Clearing denominators requires a scale choice and changes the displacement magnitude.

## Effectivity obstruction

Even an integral root displacement need not preserve the effective cone. The coarse character vector produces a transfer from the first coordinate to the last across the finite shell interval. It is admissible only at divisors containing the required source valuation. Hence the candidate is at most a partial state translation, not a global lattice endomorphism.

## Apparatus and pairing dependence

The adjoint depends on the chosen readout pairing. Rescaling one readout coordinate leaves the probe kernel unchanged but changes \(M_T^{\mathsf T}r\). Thus observationally equivalent presentations with the same blind directions can induce different candidate responses.

Likewise, multiplying \(\delta_T\) by any scalar preserves its direction and degree-zero property. The current structure supplies no coupling selecting one scale.

## Additivity obstruction

For fixed nonzero \(\delta\), the point update

\[
U_\delta(D)=D+\delta
\]

is affine. It does not preserve divisor addition:

\[
U_\delta(D+E)
\neq
U_\delta(D)+U_\delta(E).
\]

Therefore it is not an endomorphism of the multiplicative natural-number monoid. It moves a state when effective; it does not alter the ambient lattice, its basis, or its monoidal law.

## Strongest falsification attempt

For five shell directions and the established rational settings, compute \(AM_T^{\mathsf T}\) exactly. Test degree preservation, integrality on every readout basis vector, effectivity at the zero divisor and at suitable occupied divisors, dependence under pairing rescaling, and failure of additive monoid compatibility. A canonical backreaction survives only if all structural gates pass without adding choices.

## Disposition

The adjoint candidate gives rational degree-preserving response directions, but it fails integrality, global effectivity, pairing independence, scale selection, and monoid-endomorphism compatibility. Incoming residue therefore changes only readout accounting in the current model. A source-state response requires an explicit additional partial action

\[
\beta_T:k^T\times\operatorname{Div}_{\mathrm{eff}}(P)
\dashrightarrow
\operatorname{Div}_{\mathrm{eff}}(P)
\]

with its domain, integral normalization, and coupling declared.
