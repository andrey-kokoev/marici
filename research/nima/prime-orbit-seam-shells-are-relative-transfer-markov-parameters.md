# Prime-orbit seam shells are relative-transfer Markov parameters

## Source realization on one prime orbit

Fix a prime length \(L=\log p\). Partition the completed source into seam
shells

\[
\beta_j(z)
=
\int_{jL}^{(j+1)L}\phi(v)e^{zv}\,dv,
\qquad j\geq0.
\]

These are not fitted coefficients. They are the successive interval
innovations swept out by repeated multiplication by \(p\).

Let the boundary state be the innovation sequence space with unilateral shift
\(A e_j=e_{j+1}\), incidence \(b=e_0\), and return functional

\[
c_z e_j=\beta_j(z).
\]

Then the mixed return moments are exactly

\[
c_zA^jb=\beta_j(z).
\]

The cumulative moving window after \(k\) prime transports is

\[
B_{p^k}(z)=\sum_{j=0}^{k-1}\beta_j(z).
\]

Thus the moving-seam source already determines the complete local Markov
sequence of the Euler–boundary attachment.

## Relative transfer is forced

The local transfer function is

\[
h_p(t,z)
=
c_z(I-tA)^{-1}b
=
\sum_{j\geq0}\beta_j(z)t^j.
\]

Unless every source shell vanishes, this transfer is nonzero. Since the
incidence pair \((A,b)\) is cyclic at every finite cutoff, the preceding
minimality theorem applies: a faithful return produces a relative determinant.

The relative factor is therefore not an arbitrary correction added to the
Euler product. Its Taylor coefficients are the labelled moving-seam shells.

## Seam-boundedness

On the centered seam, \(z=it\), the exponential has unit modulus.
Cauchy–Schwarz gives

\[
|\beta_j(it)|^2
\leq
L\int_{jL}^{(j+1)L}|\phi(v)|^2\,dv.
\]

Summing over disjoint shells yields

\[
\sum_{j\geq0}|\beta_j(it)|^2
\leq L\lVert\phi\rVert_2^2.
\]

Hence \(c_{it}\) is a bounded return functional on the innovation space.
This supplies local completion control on the critical seam directly from the
source norm.

Away from the seam, \(e^{zv}\) changes shell size exponentially. Plain
\(L^2\) control of \(\phi\) no longer implies \((\beta_j(z))\in\ell^2\).
For example, an exponentially decaying \(L^2\) source can be exactly canceled
by the growing Mellin weight, leaving a constant non-square-summable Markov
sequence.

This is a boundedness boundary, not a zero-location argument.

## Reciprocal typing

The positive sector controls one sign of the exponential displacement; the
reciprocal sector controls the other. Their doubled colligation is required
before comparing off-seam continuations. Seam boundedness alone does not prove
that the global relative determinant is nonzero or that zeros are confined.

## DPC verdict

Resolved for each fixed prime orbit:

- the source-derived realization \((A,b,c_z)\);
- exact identification of seam shells with Markov parameters;
- inevitability of a nontrivial local relative transfer;
- boundedness of the return functional on the centered seam.

Withheld:

- simultaneous all-prime summability;
- reciprocal gluing away from the seam;
- determinant-class regularization of the global transfer;
- the zero-state-to-flux bridge.

The finite falsifier is a claimed source return whose \(j\)-th Markov
parameter differs from the corresponding labelled shell integral.

## Verification

The checker `check_prime_orbit_shell_markov_realization.py` verifies exact
Markov recovery, cumulative-window reconstruction, the seam Cauchy bound, and
an off-seam family with bounded source norm but divergent return norm.
