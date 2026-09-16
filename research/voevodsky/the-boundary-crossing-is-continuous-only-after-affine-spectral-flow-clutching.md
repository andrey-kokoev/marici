# The boundary crossing is continuous only after affine spectral-flow clutching

## Correction

The strong Schwartz dual retains both one-sided limits of a boundary crossing, but it does not identify them.

For the symmetry-completed family, define

\[
A_\gamma
=
\delta_\gamma+
\delta_{-\gamma}
\]

and normalize the phase current by

\[
\nu_{a,\gamma}
=
\frac1{2\pi i}
\partial_t
\log
\Theta_{a,\gamma}(t).
\]

With the established orientation,

\[
\lim_{a\uparrow0}
\nu_{a,\gamma}
=
+A_\gamma,
\]

whereas

\[
\lim_{a\downarrow0}
\nu_{a,\gamma}
=
-A_\gamma.
\]

Therefore no value at \(a=0\) makes

\[
a
\longmapsto
\nu_{a,\gamma}
\]

continuous as a map into the Hausdorff vector space

\[
\mathcal S'(\mathbb R)_\beta.
\]

The unsigned Poisson profile has a common delta limit; the signed phase current does not.

## Crossing cycle

Let

\[
I_{a,\gamma}
=
\begin{cases}
0,&a<0,\\
A_\gamma,&a>0.
\end{cases}
\]

This is the cumulative oriented spectral-flow cycle. Its total multiplicity is

\[
\langle I_{a,\gamma},1\rangle
=
\begin{cases}
0,&a<0,\\
2,&a>0,
\end{cases}
\]

formally, or after pairing with a cutoff equal to one near \(\pm\gamma\).

The jump equals the Krein--Langer negative-index jump:

\[
\Delta
\operatorname{ind}_-
=
2.
\]

## Augmented current

Define

\[
\widehat\nu_{a,\gamma}
=
\nu_{a,\gamma}
+
2I_{a,\gamma}.
\]

Then

\[
\lim_{a\uparrow0}
\widehat\nu_{a,\gamma}
=
A_\gamma
\]

and

\[
\lim_{a\downarrow0}
\widehat\nu_{a,\gamma}
=
-A_\gamma+2A_\gamma
=
A_\gamma.
\]

Thus the augmented current has a unique strong-dual crossing limit.

The coefficient two is forced by the difference of the two oriented one-sided currents:

\[
(+A_\gamma)-(-A_\gamma)
=
2A_\gamma.
\]

## Affine, not linear, gluing

The raw pair

\[
(
\nu,
I
)
\]

is not a continuous path in the product of a vector space with a discrete cycle lattice: \(I\) jumps.

The correct object is an affine current bundle. Across the crossing, local representatives obey

\[
(
\nu_-,
I_-
)
\sim
(
\nu_- -2A_\gamma,
I_-+A_\gamma
).
\]

The combination

\[
\widehat\nu
=
\nu+2I
\]

is invariant under this transition.

Equivalently, the current coordinate is a torsor under the integral atomic-cycle lattice rather than a globally trivial vector coordinate.

## Scalar index convention

For a compactly supported cutoff \(\chi\) satisfying

\[
\chi(\gamma)
=
\chi(-\gamma)
=
1,
\]

define the localized current number

\[
b_\chi(a)
=
\langle
\nu_{a,\gamma},
\chi
\rangle.
\]

Its one-sided limits are

\[
b_\chi(0^-)=2,
\qquad
b_\chi(0^+)=-2.
\]

Let

\[
\kappa(a)
=
\operatorname{ind}_-(k_{a,\gamma})
=
\begin{cases}
0,&a<0,\\
2,&a>0.
\end{cases}
\]

Then

\[
\widehat b_\chi(a)
=
b_\chi(a)
+
2\kappa(a)
\]

has the common crossing limit

\[
2.
\]

This scalar formula is only the total-mass shadow of the stronger cycle-valued identity

\[
\widehat\nu
=
\nu+2I.
\]

The cycle-valued form is required when several crossings occur at different spectral locations.

## General finite crossing

Let

\[
A
=
\sum_{j=1}^m
n_j
\delta_{t_j}
\]

be an oriented atomic crossing cycle. Suppose

\[
\nu_{0^-}
=
+A,
\qquad
\nu_{0^+}
=
-A.
\]

Set

\[
I_-=0,
\qquad
I_+=A.
\]

Then

\[
\widehat\nu
=
\nu+2I
\]

has common limit \(A\), and

\[
\Delta
\operatorname{ind}_-
=
\sum_j
n_j
\]

when all crossings have the hostile orientation.

Mixed orientations are handled by signed \(n_j\). In that case the cycle-valued spectral flow is primary; the unsigned negative index alone is insufficient.

## Multiple crossing parameters

For crossings along a path \(\lambda\mapsto\Theta_\lambda\), define the cumulative cycle

\[
I_\lambda
=
\sum_{
\lambda_j<\lambda
}
A_j,
\]

with signs determined by crossing orientation. On each divisor stratum, \(\nu_\lambda\) is an ordinary strong-dual current. At a crossing \(\lambda_j\), its jump is

\[
\nu_{\lambda_j^+}
-
\nu_{\lambda_j^-}
=
-2A_j.
\]

Consequently

\[
\widehat\nu_\lambda
=
\nu_\lambda
+
2I_\lambda
\]

extends continuously across every isolated transverse crossing.

For a closed deformation loop, the obstruction to returning to the original affine chart is the total spectral-flow cycle

\[
\operatorname{SF}_{\partial}
=
\sum_j
A_j.
\]

Its total signed mass is the scalar spectral flow; its support retains where the crossings occurred.

## Relation to Maslov data

The cumulative cycle \(I\) is the boundary analogue of a Maslov crossing count. The crossing form fixes the sign of each \(A_j\).

Thus the conserved datum is not the naive unsigned sum

\[
\operatorname{ind}_-^{interior}
+
\operatorname{index}_{\partial}.
\]

It is the oriented affine invariant

\[
\boxed{
\widehat\nu
=
\nu
+
2
\operatorname{SF}_{\partial}^{cycle}
}
\]

together with its scalar pushforward when only total index is needed.

## Source pullback

For source vectors \(p,q\), define

\[
\widehat Q_a(p,q)
=
\langle
\widehat\nu_a,
\overline{m_q}m_p
\rangle.
\]

At the symmetry-completed crossing,

\[
\lim_{a\to0}
\widehat Q_a(p,q)
=
m_p(\gamma)
\overline{m_q(\gamma)}
+
m_p(-\gamma)
\overline{m_q(-\gamma)}.
\]

This is continuous on the Mellin--Schwartz source rung.

Under a convolution successor with amplitude \(m_c\), both \(\nu\) and \(I\) are pulled back by multiplication with \(|m_c|^2\), so the affine identity remains natural.

## Tetrahedral placement

The static terminal node retains a local current representative and an integral crossing cycle:

\[
C_{13,7}^{aff}
=
(
C_{13,7}^{reg},
[\nu,I],
\beta_{end}
).
\]

Here \([\nu,I]\) denotes the affine clutching class, not an orthogonal direct sum.

The deformation base must distinguish the two sides of the crossing. Locally it is the oriented blow-up

\[
[0^-,0^+]
\]

with transition

\[
(
\nu,I
)
\longmapsto
(
\nu-2A,
I+A
).
\]

Over the tetrahedral lattice, the family is therefore a stratified affine bundle over

\[
\operatorname{esd}_7(\Delta^3)
\times
\widetilde I,
\]

not a trivial vector bundle over the unmodified interval.

## Green consequence

The Green readout must use the augmented current

\[
\widehat\nu
=
\nu+2I.
\]

If it uses only the regular representative \(\nu\), it acquires a jump of \(-2A\). If it uses only the index cycle, it loses the smooth phase current. The affine sum is the deformation-stable quantity.

This remains a signed rigged-dual identity. It does not imply positivity or an ambient Hilbert adjoint.

## Open gates

The following remain:

1. derive the crossing sign directly from the Green boundary form in the full completed convention;
2. identify the affine transition with a Birman--Krein or Maslov index theorem on the physical carrier;
3. prove compatibility with nontransverse collisions and higher-order poles;
4. construct the corresponding physical trace-class clutching operator;
5. test whether positive compression annihilates the affine holonomy.

## Disposition

The boundary current itself has a genuine oriented jump. The analytically tame object is the affine-clutched current

\[
\widehat\nu
=
\nu+2I.
\]

The strong Schwartz dual supplies the correct local fibers, while spectral flow supplies the transition functions between them.
