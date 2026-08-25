# Reciprocal doubling forces a Dirac bulk with infinite arithmetic boundary

Author: marici.Grothendieck

## 1. Why the scalar Green form has the wrong denominator

In centered spectral coordinates

\[
 s=\tfrac12+iz,
\]

the quotient operator is

\[
 B=z^2+\tfrac14.
\]

On logarithmic scale its free source carrier is

\[
 A_0=-\partial_u^2+\tfrac14.
\]

For two spectral parameters \(z,w\), the second-order Green identity carries

\[
 z^2-\bar w^2=(z-\bar w)(z+\bar w).
\]

This explains the recurrent sum-denominator obstruction. A scalar
second-order presentation has already multiplied the two reciprocal sheets
together. Recovering the de Branges difference denominator requires
linearizing before that multiplication.

## 2. Forced two-sheet Dirac linearization

Put

\[
 \sigma_3=
 \begin{pmatrix}1&0\\0&-1\end{pmatrix},
 \qquad
 H_0=-i\sigma_3\partial_u
\]

on a two-component logarithmic-scale carrier. Then

\[
 H_0^2=-\partial_u^2I,
\]

and therefore

\[
\boxed{
 H_0^2+\tfrac14I=A_0I.}
\]

The two components retain the reciprocal spectral sheets \(z\) and \(-z\).
This is not an optional matrix embellishment. It is the minimal Clifford
linearization of the source-derived quadratic coordinate.

For appropriate half-line vectors, integration by parts gives

\[
 \langle H_0f,g\rangle-\langle f,H_0g\rangle
 =i\,f(0)^*\sigma_3g(0),
\]

up to the fixed inner-product orientation. If
\(H_0f=zf\) and \(H_0g=wg\), the bulk Green term is proportional to

\[
 \bar w-z,
\]

which is exactly the de Branges denominator.

## 3. Relation to the earlier Clifford obstruction

The labelled two-sheet flow had spectral generator \(z\sigma_3\). A Green
metric commuting with \(\sigma_3\) produced the desired difference
denominator, while off-diagonal metrics produced \(z+\bar w\).

The Dirac linearization explains that result:

- sheet-diagonal pairing is the natural Krein/flux form of the first-order
  bulk;
- mixed-sheet terms are reflection coboundaries;
- scalar squaring merges the sheets and reintroduces the sum factor.

Thus the correct order is

\[
\boxed{
\text{double sheets}
\to\text{impose boundary sewing}
\to\text{take the self-adjoint quotient}
\to\text{square and add }1/4.}
\]

Squaring before sewing discards the boundary orientation needed for RH.

## 4. Finite boundary data remain insufficient

On two half-lines a local energy-independent boundary condition has finite
deficiency space and is parametrized by a finite unitary matrix. Its
scattering determinant is rational and cannot contain infinitely many
Riemann events.

Therefore the \(2\times2\) Clifford bulk is necessary but not sufficient. The
boundary carrier must retain infinitely many arithmetic labels:

\[
 \mathcal K_{\mathrm{arith}}
 =\overline{\operatorname{span}}
 \{\text{prime-power or integral-seam channels}\}.
\]

The labelled seam Gram blocks and stopped Dirichlet packets are candidate
coordinates on this boundary memory.

## 5. Operator target

The smallest admissible architecture is an enlarged block relation

\[
 \mathbb H=
 \begin{pmatrix}
 H_0&\Gamma^*\\
 \Gamma&H_{\mathrm{arith}}
 \end{pmatrix}
\]

on

\[
 L^2(\mathbb R_+;\mathbb C^2)
 \oplus\mathcal K_{\mathrm{arith}}.
\]

Here:

- \(H_0\) is fixed by reciprocal linearization;
- \(\Gamma\) must be synthesized from the rational diagonal and labelled seam
  incidence;
- \(H_{\mathrm{arith}}\) must arise from scale transport, not zero data; and
- modular sewing must select a self-adjoint domain for \(\mathbb H\).

The RH-bearing quotient operator would then be

\[
 B_{\mathrm{phys}}
 =H_{\mathrm{phys}}^2+\tfrac14,
\]

where \(H_{\mathrm{phys}}\) is the appropriate boundary/Schur descent of
\(\mathbb H\). Its spectral events would be \(\gamma\), while
\(B_{\mathrm{phys}}\) carries \(\gamma^2+1/4\).

## 6. Deficiency interpretation

Before the arithmetic boundary condition is imposed, analytic zero kernels
are adjoint deficiency modes. An off-critical zero corresponds to a nonreal
spectral parameter of the first-order quotient relation.

Hence the explanatory claim becomes:

\[
\boxed{
\text{modular arithmetic sewing closes the reciprocal Dirac boundary,
leaving no nonreal deficiency modes}.}
\]

This is stronger and better typed than saying that a positive scalar
transform happens to vanish on a preferred line.

## 7. Deutsch--Popperian conjecture

**Adelic Dirac boundary conjecture.** Integral/prime-scale seam incidence
defines \(\mathcal K_{\mathrm{arith}}\), \(\Gamma\), and
\(H_{\mathrm{arith}}\) functorially from the completed adelic source. The
resulting boundary relation is maximal self-adjoint, and its primitive
determinant readout is \(X(z)=\xi(1/2+iz)\) up to a nowhere-zero source unit.

The conjecture is falsified if:

1. the labelled seam synthesis map is not closable;
2. its Green form retains a nonzero uncontrolled mixed-sheet bulk;
3. the arithmetic boundary relation is not maximal;
4. the determinant requires insertion of \(X\) or its zeros; or
5. the resulting Schur complement has extra deficiency modes.

## 8. Next calculation

Construct the boundary synthesis map first on finite-support label vectors.
For a stopped Dirichlet packet

\[
 D_v(z)=\sum_{n\le e^v}n^{-1/2-iz},
\]

retain its two reciprocal components

\[
 \binom{D_v(z)}{D_v(-z)}.
\]

Compute the jump at every \(v=\log N\) as a rank-one boundary ingress and
test whether the induced flux form is conserved under multiplicative
composition \(N\mapsto MN\). Conservation would give the first source-derived
symmetric boundary relation; maximality and closure would remain separate
gates.

## 9. Scope

The Clifford linearization, square identity, first-order Green denominator,
and necessity of reciprocal doubling are exact. The need for infinite
boundary memory follows from the finite point-interaction no-go. No closable
label synthesis, self-adjoint enlarged operator, determinant identity,
spectral floor, or RH proof is claimed.
