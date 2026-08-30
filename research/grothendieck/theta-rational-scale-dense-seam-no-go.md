# Rational scale covariance makes fixed point seams dense

## 1. Minimal local Green model

Split logarithmic scale at \(u=0\) and consider the first-order carrier

\[
  S=-i\partial_u
\]

on compactly supported smooth functions away from the seam. Its adjoint
admits one-sided boundary values, and integration by parts gives the local
Green form

\[
  \langle S^*f,g\rangle-\langle f,S^*g\rangle
  =
  -i\bigl(
    f(0^+)\overline{g(0^+)}
    -
    f(0^-)\overline{g(0^-)}
  \bigr),
\]

up to the chosen orientation convention. Self-adjoint extensions sew the
two boundary ports by a unitary relation.

This is the smallest exact realization of the two reciprocal sectors as two
oriented boundary charts.

## 2. Scale transport moves the seam

Multiplication by a positive rational scale \(q\) acts in logarithmic
coordinates as translation

\[
  (\tau_qf)(u)=f(u+\log q).
\]

It conjugates the seam trace at \(0\) to the seam trace at \(-\log q\).
Therefore a boundary construction covariant under the full rational scale
group must contain the orbit

\[
  \log\mathbb Q_{>0}.
\]

Because \(\mathbb Q_{>0}\) is dense in \(\mathbb R_{>0}\) and logarithm is a
homeomorphism,

\[
  \overline{\log\mathbb Q_{>0}}=\mathbb R.
\]

Thus rational covariance sends one point seam into a dense family of seams.

## 3. No locally finite point-interaction realization

A differential operator on the complement of a dense seam set has no open
interval chart on which the ordinary first-order propagation used above can
operate. In particular, the completed rational action cannot be represented
by a locally finite direct sum of point-interaction boundary ports.

\[
\boxed{
\text{full rational scale covariance}
\not\Longrightarrow
\text{a discrete point-seam Dirac extension}.}
\]

The earlier integer ingress model at \(\log N\) remains useful as a stopped
one-sided chart, but reciprocal completion and rational transport destroy
its local discreteness.

## 4. What the obstruction actually diagnoses

The density occurs after projecting rational scaling to the real logarithmic
coordinate. It therefore excludes a purely archimedean locally finite seam
model, not an adelic boundary model.

The projected transformation groupoid

\[
  \mathbb R\rtimes\log\mathbb Q_{>0}
\]

retains the moving-cut covariance but is nonproper because its orbit is
dense. The faithful replacement must restore the finite-place coordinates:
diagonal rational scaling in the full idele space is discrete, while its real
projection is dense. The seam must therefore be transported in an adelic
groupoid before archimedean compression.

This supplies a precise mathematical meaning for “two sectors secretly
pretending to be one”: the two half-line charts form a polarization atlas,
while rational scale arrows continually change which chart boundary is
called zero.

## 5. Green form as a cocycle

For a moving cut at \(a\), write \(\Gamma_a^\pm f=f(a^\pm)\). The local flux

\[
  \Omega_a(f,g)
  =
  -i\left(
  \Gamma_a^+f\,\overline{\Gamma_a^+g}
  -
  \Gamma_a^-f\,\overline{\Gamma_a^-g}
  \right)
\]

obeys the covariance law

\[
  \Omega_a(\tau_qf,\tau_qg)
  =
  \Omega_{a+\log q}(f,g).
\]

The source object is therefore not one fixed boundary form but its covariant
family over the translation groupoid. A global self-adjoint condition must
be a descent datum for this family.

## 6. New theorem-shaped target

Construct first a Hilbert module over the diagonal rational action on the
idele space, and only then derive its real moving-cut compression. It must
carry:

1. the logarithmic Dirac propagation;
2. the covariant Green cocycle \(\Omega_a\);
3. the rational-comb joint fixed distribution;
4. reciprocal Fourier rotation; and
5. a maximal isotropic descent relation.

Then test whether its primitive determinant is \(X(z)\). This formulation
retains arithmetic covariance without replacing the line by a dense array of
singularities.

## 7. Smallest falsifier

The first falsifier is failure of cocycle descent: compose two rational scale
arrows and compare the transported Green trace with the trace transported by
their product. A residual term not accounted for by the known moving-endpoint
seam current means that no groupoid boundary relation exists.

Even successful descent would not prove RH until maximal self-adjointness and
the determinant comparison are established.

## 8. Scope

Density of \(\log\mathbb Q_{>0}\), covariance of point evaluation, and the
local Green identity are exact. The locally finite *purely real* point-seam
architecture is therefore excluded. The full adelic action retains discrete
rational labels and is the required faithful source before projection. No
adelic Hilbert module, maximal descent relation, determinant identity, or RH
theorem is constructed.
