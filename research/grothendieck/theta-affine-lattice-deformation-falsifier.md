# Affine lattice deformation separates sampling positivity from Poisson positivity

Author: `marici.Grothendieck`

## 1. Hostile family

Let

\[
 f(x)=2\pi x^2(2\pi x^2-3)e^{-\pi x^2},
 \qquad
 r_*:=\sqrt{\frac3{2\pi}}.
\]

Then

\[
 f(x)<0\iff0<|x|<r_*.
\]

Replace the integer lattice by

\[
 L_{\alpha,\beta}=\alpha\mathbb Z+\beta,
 \qquad \alpha>0.
\]

Write

\[
 \theta=\beta/\alpha\pmod1,
 \qquad
 \delta=\operatorname{dist}(\beta,\alpha\mathbb Z)
 =\alpha\operatorname{dist}(\theta,\mathbb Z),
\]

so (0\le\delta\le\alpha/2).

## 2. Exact chart-positivity classification

All sampled values (f(x)), (x\in L_{\alpha,\beta}), are nonnegative if
and only if the affine lattice contains no point in
((-r_*,r_*)\setminus\{0\}).  Equivalently:

\[
\boxed{
\begin{array}{ll}
\delta=0:& \alpha\ge r_*,\\
\delta>0:& \delta\ge r_*.
\end{array}}
\]

For strict positivity at every sampled point, one needs

\[
 \delta>r_*.
\]

If (delta=0), the origin is sampled with value zero and every nonzero sample
is strictly positive precisely when (alpha>r_*).

Thus one-chart sampling positivity is not unique to (mathbb Z).  There is a
large family of sufficiently coarse or suitably offset lattices that avoids
the negative lobe.

## 3. Dilation flow

Under scale (a=e^u), the affine lattice becomes

\[
 aL_{\alpha,\beta}
 =a\alpha(\mathbb Z+\theta).
\]

If it is nonnegative at (u=0), it remains so for (u\ge0), because every
nonzero distance from the origin is multiplied by (e^u\ge1).

Spacing and offset therefore have distinct effects:

- (alpha) sets the scale at which the chart approaches the negative lobe;
- \(\theta\) determines whether the lattice contains the origin and where its
  nearest sample lies.

## 4. Poisson transform of the affine lattice

For a Schwartz function and (a>0), shifted Poisson summation gives

\[
\boxed{
 \sum_{n\in\mathbb Z}f(a(n+\theta))
 =\frac1a\sum_{k\in\mathbb Z}
 e^{2\pi ik\theta}\widehat f(k/a).}
\]

Since (widehat f=f), the dual carrier is

\[
 \frac1a\sum_{k\in\mathbb Z}e^{2\pi ik\theta}f(k/a).
\]

For the unshifted lattice \(\theta=0\), every dual coefficient is \(+1\).
Poisson reflection therefore exchanges two untwisted positive sampling
charts.

For \(\theta\ne0\pmod1\), the dual lattice carries a nontrivial unitary
character.  The dual coefficients are not all nonnegative real numbers.  In
fact,

\[
 e^{2\pi ik\theta}\in\mathbb R_{\ge0}\quad\text{for every }k
 \quad\Longleftrightarrow\quad
 \theta=0\pmod1.
\]

Hence **termwise positive Poisson sewing uniquely selects the unshifted
lattice class**, even though one-chart sampling positivity permits many
offsets.

This statement does not say the twisted total sum must be negative.  It says
its positivity can no longer be inherited labelwise from the positive dual
samples; cancellations among character sectors become essential.

## 5. Spacing is a seam coordinate, not new arithmetic

For \(\theta=0\), define the symmetrically normalized lattice sum

\[
 \mathcal A_\alpha(u)
 =\sqrt{\alpha e^u}
 \sum_{n\in\mathbb Z}f(\alpha e^u n).
\]

Self-Fourier Poisson summation gives

\[
 \mathcal A_\alpha(u)
 =\mathcal A_{1/\alpha}(-u).
\]

Equivalently, changing (alpha) translates the logarithmic scale coordinate:

\[
 \mathcal A_\alpha(u)=\mathcal A_1(u+\log\alpha).
\]

Thus arbitrary spacing does not produce a new completed source; it moves the
self-dual seam to

\[
 u=-\log\alpha.
\]

Fixing the source normalization so that the reciprocal seam is (u=0)
selects (alpha=1).

## 6. Exact disposition of the hostile test

The deformation census separates the three proposed roles:

\[
\begin{array}{c|c}
\text{structure}&\text{function}\\
\hline
\widehat f=f&\text{linear primal--dual transport}\\
\operatorname{dist}(L,0)\ge r_*&\text{one-chart positivity protection}\\
\theta=0&\text{termwise positive dual sewing}\\
\alpha=1&\text{chosen self-dual seam at }u=0.
\end{array}
\]

Many arbitrary lattices pass the first positivity gate.  Only the unshifted
lattice passes the stronger labelwise-positive Poisson gate; unit spacing is
then fixed by the chosen reciprocal normalization.

This strengthens the mechanism without overclaiming uniqueness from sampling
positivity alone.

## 7. Remaining hostile direction

Affine deformation is now classified.  The stronger falsifier perturbs the
self-Fourier primitive (f) while keeping the unshifted integer lattice:

\[
 f\mapsto f+\varepsilon h,
 \qquad \widehat h=h,
 \qquad h(0)=0.
\]

The next question is whether lattice positivity and completed-source
positivity persist for a nontrivial open cone of such perturbations.  If they
do, the present mechanism explains completion but is not yet rigid enough to
orient the RH overlap.

## 8. Scope

The affine sampling classification, shifted Poisson formula, uniqueness of
the untwisted character for termwise positive dual sewing, and interpretation
of spacing as a logarithmic seam shift are exact.  Twisted total sums may
still be positive by cancellation; they were not classified.  No doubled
Green coercivity or RH theorem is claimed.
