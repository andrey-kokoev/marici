# Reciprocal seam determinant ratios are identically trivial

## 1. Reflected seams

Let \(R\) be reflection,

\[
  (Rf)(u)=f(-u).
\]

For an even completed source, the Friedrichs diffusion commutes with
reflection:

\[
  RA_\Phi=A_\Phi R.
\]

Let \(C_a^+\) be the oriented seam interval on one side and define the
reciprocal seam by

\[
  C_a^-=RC_a^+R.
\]

Their heat compressions satisfy

\[
  C_{a,t}^-
  =
  e^{-tA_\Phi/2}C_a^-e^{-tA_\Phi/2}
  =
  RC_{a,t}^+R.
\]

## 2. Exact determinant equality

Unitary conjugacy preserves Fredholm determinants. Therefore, whenever the
heat-sandwiched operators are trace class,

\[
  \det(I+\lambda C_{a,t}^-)
  =
  \det(I+\lambda C_{a,t}^+).
\]

The most obvious reciprocal relative determinant is consequently

\[
  \boxed{
  \frac{\det(I+\lambda C_{a,t}^+)}
       {\det(I+\lambda C_{a,t}^-)}
  =1.}
\]

It is independent of heat time, seam displacement, and spectral parameter
because it contains no relative information beyond unitary equivalence.

## 3. Consequence

The completed theta scalar cannot be obtained by assigning an independent
determinant to each reciprocal sector and dividing them. Reflection makes
those separate determinants identical.

Any nontrivial transition section must instead involve a coupled block:

\[
  \mathcal C_{a,t}(z)
  =
  \begin{pmatrix}
    C_{a,t}^+ & K_{+-}(z)\\
    K_{-+}(z) & C_{a,t}^-
  \end{pmatrix},
\]

where the off-diagonal maps compare the two polarization charts. The
determinant can then depend on their relative angle or failure of
transversality.

This is another exact form of the two-sector principle:

\[
\boxed{
\text{separate sector data are symmetric and trivial;}
\quad
\text{meaning lives in the coupling}.}
\]

## 4. Typing of the coupling

The off-diagonal block cannot be chosen to reproduce \(X\). It must descend
from operations that actually cross between the sectors:

1. Fourier quarter-turn;
2. rational Poisson sewing;
3. the moving-endpoint cocycle; and
4. the completed vacuum.

The earlier mixed right--left Green denominator problem is precisely the
typing problem for \(K_{+-}(z)\). A successful construction must convert its
natural sum parameter \(z+\bar w\) into the de Branges difference parameter
\(\bar w-z\) through an independently derived orientation law.

## 5. New minimal target

Construct the off-diagonal seam holonomy

\[
  K_{+-}(z)
  =
  \Pi_+\,e^{-tA_\Phi/2}
  (\text{Poisson/Fourier crossing at }z)
  e^{-tA_\Phi/2}\Pi_-,
\]

with every map defined before scalar compression. Then determine:

1. whether it is Hilbert--Schmidt;
2. whether the Schur products
   \(K_{+-}K_{-+}\) are trace class;
3. whether the block determinant is heat-time independent after the diagonal
   cancellation; and
4. whether its first variation is the exact completed theta seam current.

## 6. Falsifier

If Fourier/reflection covariance makes the coupled block unitarily reducible
to two identical diagonal pieces, its determinant is still universal. If the
off-diagonal block requires inserting \(X\), the construction is circular.
Only a nontrivial source-derived relative-angle operator can survive.

## 7. Scope

Reflection conjugacy and equality of the separate Fredholm determinants are
exact. They eliminate the simplest regulator-independent determinant ratio.
No off-diagonal crossing operator, nontrivial block determinant, identity
with \(X\), or RH theorem is constructed.
