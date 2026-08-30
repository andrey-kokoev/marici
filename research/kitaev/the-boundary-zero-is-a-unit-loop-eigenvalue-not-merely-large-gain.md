# The boundary zero is a unit loop eigenvalue, not merely large gain

## Question

What is the strongest source-independent invertibility criterion after the
connected prime channel has been isolated as an invertible bulk block?

## Exact reduction

Let

\[
A_s=I-K_s,
\qquad
\mathcal M_s=
\begin{pmatrix}
A_s&B_s\\
C_s&D_s
\end{pmatrix}.
\]

Assume first that both `A_s` and `D_s` are boundedly invertible on their typed
spaces.  The boundary Schur complement factors as

\[
S_s=D_s(I-L_s),
\qquad
L_s=D_s^{-1}C_sA_s^{-1}B_s.
\]

Therefore the exact algebraic obstruction is

\[
1\in\operatorname{spec}(L_s).
\]

In finite boundary dimension this is exactly

\[
\det(I-L_s)=0.
\]

A zero is thus a unit closed-loop eigenvalue.  Large loop norm alone is not a
zero, and a norm below one is only a robust sufficient exclusion certificate.

If `D_s` is not invertible, the invariant statement remains
`ker S_s != 0`; the normalized loop factorization is then unavailable and
must not be manufactured.

## Three gates that must remain separate

### Algebraic gate

At a fixed parameter and cutoff, invertibility is equivalent to absence of a
unit loop eigenvalue.  A witness is a nonzero boundary vector `y` satisfying

\[
D_sy=C_sA_s^{-1}B_sy.
\]

This is the first failed law in constructor order: direct boundary action and
the returned bulk-mediated action cancel on the same typed boundary state.

### Robust metric gate

Completion-stable invertibility requires a lower singular-value margin, not
merely spectral exclusion:

\[
\inf_{s\in K,\,N}
\sigma_{\min}(S_{s,N})>0
\]

for each claimed compact parameter set `K`.  In a nonnormal family, a uniform
distance between `1` and the spectrum of `L_{s,N}` does not by itself control
the inverse norm.  Resolvent or singular-value control is the correct gate.

### Source-authority gate

Neither gate can be evaluated from the completed scalar section.  The source
must independently provide the boundary space, `B_s`, `C_s`, `D_s`, their
sector metrics, and their cutoff maps.  Reconstructing these blocks from the
desired determinant would fit the realization from its diagnostic shadow.

## Explicit connected-bulk reserve

For the plus sector on the prime coefficient space,

\[
K_se_p=p^{-s}e_p,
\qquad \sigma=\operatorname{Re}s>0.
\]

The diagonal bulk obeys

\[
\|A_s^{-1}\|
\le \frac{1}{1-2^{-\sigma}}.
\]

Consequently, when `D_s` is invertible, the source-independent small-gain
certificate is

\[
\|D_s^{-1}C_s\|\,\|B_s\|
<1-2^{-\sigma}.
\]

For the reciprocal sector the corresponding reserve is

\[
1-2^{-(1-\sigma)}.
\]

Both sector certificates hold wherever

\[
\|D_s^{-1}C_s\|\,\|B_s\|
<
\min\left(1-2^{-\sigma},1-2^{-(1-\sigma)}\right).
\]

At the seam the common bulk reserve is `1-1/sqrt(2)`.  This number is an
available robustness budget, not a claim that the theta boundary loop fits
inside it.

## Accretive alternative

Small gain is not necessary.  A second sufficient route is a boundary energy
law.  If, in the source-authorized boundary metric,

\[
\operatorname{Re}\langle y,D_sy\rangle\ge\delta\|y\|^2
\]

and

\[
\operatorname{Re}\langle y,C_sA_s^{-1}B_sy\rangle
\le\eta\|y\|^2,
\qquad \eta<\delta,
\]

then `S_s` is bounded below by `delta-eta`.  A sign-indefinite or Krein
boundary metric does not authorize this Hilbert-space argument globally; it
must be applied chartwise or replaced by the appropriate indefinite-metric
statement.

## Hostile models

### Equality at unit gain

For scalar blocks `A=D=1` and `B=C=1`, the loop is `L=1` and the Schur
complement vanishes.  This is the minimal exact boundary zero.

### Large gain without a zero

For `A=D=1`, `B=2`, and `C=1`, the loop is `L=2` while `S=-1` is invertible.
This falsifies any proposed equivalence between gain exceeding one and the
existence of a zero.

### Spectral separation without stable completion

Let

\[
I-L_N=
\begin{pmatrix}
1&-N\\
0&1
\end{pmatrix}.
\]

Every `L_N` has spectrum `{0}`, so the unit eigenvalue is uniformly absent,
but

\[
\|(I-L_N)^{-1}\|\to\infty.
\]

Thus spectral exclusion at every cutoff does not establish completion-stable
invertibility.

### Vanishing singular margin with fixed diagonal spectrum

Equivalently, nonnormal feedback can retain fixed eigenvalues while its least
singular value tends to zero.  The completion theorem must control the
Rosenbrock or Schur graph, not only the scalar determinant or eigenvalue set.

## Disposition

The connected-channel theorem supplies an explicit open-loop inverse budget.
It does not close the RH-bearing boundary theorem because no source-derived
bounds for `B_s`, `C_s`, and `D_s` are yet pinned.  The next highest-information
object is therefore the smallest typed boundary colligation, followed by one
of two genuinely explanatory laws:

1. a strict closed-loop gain bound using the explicit prime-bulk reserve; or
2. a sector-native accretive/passive identity that controls the returned
   boundary action without requiring small norm.

Failure of both does not produce a zero.  It means only that these robust
certificates are unavailable; the exact unit-eigenvalue gate remains the
decisive test.

## Claim boundary

This packet proves an abstract block-operator reduction and exact hostile
models.  It does not derive the theta boundary blocks, authorize a Hilbert
metric across both sectors, establish Fredholmness, or prove any uniform
completion estimate.
