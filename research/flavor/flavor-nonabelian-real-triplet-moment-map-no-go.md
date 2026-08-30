# Non-Abelian real-triplet moment-map no-go: WP717

## Question

Can one unified non-Abelian moment map improve WP716 by fixing the gauge
metric and generating the angular stiffness required by the faithful flavor
frame?

## Descent calculation

The admitted fields are real triplets of diagonal \(SO(3)\). In the complex
adjoint representation the standard gauge moment map is

\[
\mu(\phi)=-i\phi^*\mathbin\times\phi.
\]

Its cross term obeys the generator-completeness identity

\[
\mu(n)\mathbin\cdot\mu(m)
=(n^*\mathbin\cdot m)(n\mathbin\cdot m^*)
-(n^*\mathbin\cdot m^*)(n\mathbin\cdot m).
\]

On the real-triplet slice, \(n^*=n\) and \(m^*=m\), so

\[
\mu(n)=\mu(m)=0.
\]

The apparent non-Abelian angular operator therefore vanishes when pulled back
to the actual state domain. A real singlet portal boson has no non-Abelian
moment map; a real adjoint portal boson has the same zero pullback. Neither
choice produces the required asymmetric portal.

## Smallest hostile pair

Take

\[
n=(1,0,0),\qquad m_\parallel=(1,0,0),\qquad
m_\perp=(0,1,0).
\]

The physical angular invariant differs:

\[
(n\mathbin\cdot m_\parallel)^2=1,
\qquad
(n\mathbin\cdot m_\perp)^2=0.
\]

Both configurations nevertheless have the same non-Abelian moment-map
readout, zero. Thus this source operation is not faithful on the real flavor
domain and cannot rigidify its frame.

## Reference-extension boundary

A nonzero adjoint moment map requires an independent complex-conjugate or
cotangent direction. For example, independent vectors \(e_1\) and \(e_2\)
give \(-i e_1\mathbin\times e_2\ne0\). Such a direction is an added phase or
momentum port. It enlarges the state space and changes the physical groupoid;
it is not recovery of an operator already present on `physical16`.

## Claim boundary and disposition

WP717 rules out the direct simple non-Abelian D-term repair on the admitted
two-real-triplet domain. The failure precedes anomaly, RG, threshold, and
instrument questions: the source map itself collapses the faithful angular
coordinate and produces no portal.

The next viable class must act directly on real triplets. A tensor auxiliary
field or an F-term constraint could generate \((n\mathbin\cdot m)^2\), but it
is progressive only if its representation and source algebra also force the
asymmetric portal coefficient and its normalization. Introducing a complex
reference field merely to make the moment map nonzero must be typed as a new
relational experiment.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp717_nonabelian_real_triplet_moment_map_no_go.py`

Generated result: `results/wp717_nonabelian_real_triplet_moment_map_no_go.json`.
