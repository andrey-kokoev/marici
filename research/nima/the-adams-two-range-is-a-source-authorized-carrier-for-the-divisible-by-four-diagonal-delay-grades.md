# The Adams-two range is a source-authorized carrier for the divisible-by-four diagonal delay grades

## Question

Is there a source-authorized mechanism, distinct from the unsupported
common-phase Z4 action, whose range has exactly the diagonal prime orders
selected by the completed-theta shell expansion?

## Claim boundary

Yes at the carrier and coefficient levels. Applying Adams doubling to the
prime-power label on both reciprocal sheets restricts the diagonal pair to even
prime-power grades. Its weighted pair coefficients have exactly the orders
\(p^{-2},p^{-4},\ldots\). What remains unproved is that the physical diagonal
reciprocal response factors through this Adams-two range and that its endpoint
comparison has the required normalization and sign.

## Source Adams range

For labelled prime-power grades,

\[
 S_2e_{p,k}=e_{p,2k}.
\]

Its range is the closed coordinate subspace supported on even grades. This map
is already source-authorized on the projective Köthe carrier, commutes with
reciprocal reflection, and obeys cutoff naturality.

## Reciprocal pair at one grade

The Euler half-density coefficient is

\[
 w_{p,k}=\frac1k p^{-k/2}.
\]

Pair the direct and reciprocal copies at the same grade \(k\). Their delay
characters cancel, and the polarized diagonal coefficient is

\[
 w_{p,k}^2
 =\frac1{k^2}p^{-k}.
\]

Restricting to the Adams-two range, write \(k=2r\). Then

\[
 w_{p,2r}^2
 =\frac1{4r^2}p^{-2r}.
\]

Thus the algebraic prime orders are exactly

\[
 p^{-2},p^{-4},p^{-6},\ldots.
\]

In two-sheet delay grading, grade \(k=2r\) on each sheet has total grade
\(4r\). This reproduces the completed-theta divisible-by-four selection rule
without importing a Fourier phase.

## First admissible diagonal atom

At \(r=1\),

\[
 w_{p,2}^2=\frac14p^{-2}.
\]

The required leading endpoint-relative correction is

\[
 -\frac1{4\pi}p^{-2}.
\]

Therefore the remaining leading comparison is the source-normalized scalar

\[
 \mathcal T_{\rm Adams2\to diag}
 \left(w_{p,2}\otimes w_{p,2}^{\rm recip}\right)
 =-\frac1\pi
 \left(w_{p,2}\otimes w_{p,2}^{\rm recip}\right)
\]

at the response-coordinate level, subject to the actual endpoint metric and
port convention. The factor \(-1/\pi\) is a comparison target, not a derived
map.

## Exact Adams cocycle check

The one-sheet Adams-two cocycle is

\[
 \rho_2(p,k)=\frac12p^{-k/2}.
\]

On a reciprocal pair its product is

\[
 \rho_2(p,k)^2=\frac14p^{-k}.
\]

For \(k=1\), this maps the grade-one pair coefficient
\(w_{p,1}^2=p^{-1}\) to

\[
 \rho_2(p,1)^2w_{p,1}^2
 =\frac14p^{-2}
 =w_{p,2}^2.
\]

Hence the weighted pair square commutes exactly; the selected order is not an
asymptotic fit.

## Missing factorization theorem

Carrier support does not prove physical response descent. Candidate one still
needs a source arrow

\[
 \mathcal G_{\rm pair,diag}
 \longrightarrow
 \operatorname{ran}(S_2\otimes S_2)
 \longrightarrow
 \mathcal G_{\rm recip/link}
\]

that preserves:

- the common prime and grade labels;
- reciprocal analytic-transpose orientation;
- moving-shell transport;
- endpoint Green normalization;
- all Evans parameter jets.

The first arrow is especially restrictive: a projection onto even grades may
not be inserted merely because its image has the desired asymptotics.

## Relation to the formal Z4 projector

The common-phase Z4 average and the Adams-two range have the same diagonal
grade support, but different authority and action:

- the Z4 average is an unsupported phase projection on delay variables;
- Adams doubling is a source-derived irreversible grade-reindexing semigroup.

They must not be identified. Adams provides a viable carrier candidate without
supplying a group symmetry or inverse.

## Hostile

A proposed diagonal response fails this route if its finite labelled output has
a nonzero odd prime-power grade, or if its grade-two pair coefficient does not
map to \(-1/(4\pi)p^{-2}\) under the frozen endpoint normalization.

## Disposition

The source-authorized Adams-two range replaces the unsupported Z4 phase as the
leading carrier candidate for the diagonal reciprocal response. The decisive
open theorem is factorization of the physical diagonal shell map through that
range, followed by derivation of the \(-1/\pi\) grade-two endpoint comparison.
No RH conclusion is authorized.
