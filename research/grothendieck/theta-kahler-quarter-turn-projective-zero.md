# The Laplace--Fourier quarter-turn is a universal Kähler orbit

## 1. Source orbit

Let

\[
  \Omega(u)=\Phi(u)^{1/2}\in L^2(\mathbb R),
\]

and let \(Q\) be multiplication by \(u\). The complex character orbit is

\[
  \Omega_z=e^{izQ}\Omega.
\]

For real \(x\), \(e^{ixQ}\) is unitary. For imaginary displacement
\(z=-iy\), it is positive exponential tilt. Super-exponential theta tails
make the orbit analytic on a common rigged core.

The completed scalar is the vacuum overlap

\[
  X(z)=\langle\Omega,\Omega_z\rangle
\]

with the appropriate bilinear/analytic convention.

## 2. Kähler geometry

The squared norm of the complexified orbit is

\[
  \|\Omega_z\|^2
  =
  \int_{\mathbb R}\Phi(u)e^{-2\operatorname{Im}(z)u}\,du.
\]

Its projective Kähler potential is

\[
  \mathcal K(z,\bar z)
  =
  \log\|\Omega_z\|^2.
\]

Differentiation gives the Fubini--Study metric

\[
  g_{z\bar z}
  =
  \partial_z\partial_{\bar z}\mathcal K
  =
  \operatorname{Var}_{z}(Q),
\]

up to the harmless normalization determined by whether \(z\) or \(z/2\) is
used in the orbit. Positivity is automatic.

The complex structure acts by

\[
  J(\partial_x)=\partial_y,
  \qquad
  J(\partial_y)=-\partial_x.
\]

Thus the operator's proposed ninety-degree rotation is exact:

\[
\boxed{
\text{unitary Fourier direction}
\xleftrightarrow{\ J\ }
\text{positive Laplace/Fisher direction}.}
\]

The Fisher metric and the unitary phase geometry are the real and imaginary
faces of one projective Kähler tensor.

## 3. Meaning of a zero

The affine chart based at the vacuum uses the transition coordinate

\[
  \langle\Omega,\Omega_z\rangle.
\]

When \(X(z)=0\), that chart fails because the transported line is orthogonal
to the vacuum line. The projective state \([\Omega_z]\) itself remains
perfectly well defined and its Kähler metric need not degenerate.

Therefore:

\[
\boxed{
\text{a theta zero is loss of one overlap chart's meaning,
not automatically loss of the underlying state}.}
\]

This refines the operator's intuition. To interpret the zero as a genuine
physical or categorical loss of meaning, the vacuum overlap must be proved
to be the transition unit between two *complete source-authorized
localizations*. Otherwise it is merely one projective coordinate vanishing.

## 4. Why the geometry is insufficient

Every positive source with adequate tails produces the same Kähler
construction. Hostile Fourier-stable sources with off-critical zeros still
have:

1. a positive Fubini--Study metric;
2. a complex structure rotating tilt into phase;
3. a unitary real orbit; and
4. projective overlap zeros.

Hence Kähler compatibility alone cannot imply RH.

The arithmetic theorem must constrain the overlap divisor relative to the
two modular localizations. In geometric language, one needs a
source-selected real structure or positive line bundle whose authorized
transition section is \(X\), and whose divisor is forced onto the fixed locus
of the reciprocal anti-involution.

## 5. Sharpened target

Construct two adelic polarization charts \(\mathcal U_+\) and
\(\mathcal U_-\) on the projective source orbit such that:

1. their transition line is derived from Poisson/rational descent;
2. its transition section is \(X(z)\) up to a nowhere-zero unit;
3. reciprocal conjugation exchanges the charts;
4. chart failure away from the fixed seam contradicts positivity or
   maximality of the descended Hermitian line; and
5. a hostile Fourier-stable vacuum fails to admit the same atlas.

This turns “loss of meaning” into a typed statement: failure of an authorized
descent chart, not mere scalar orthogonality.

## 6. Scope

The projective Kähler orbit, Fisher metric, complex quarter-turn, and
orthogonality interpretation are exact. They are universal and do not
constrain the zero divisor. No arithmetic line bundle, two-chart descent,
off-seam exclusion theorem, or RH result is constructed.
