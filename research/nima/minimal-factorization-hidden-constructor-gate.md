# Minimal factorization and the hidden-constructor gate

## Result

Let \(Q\ge 0\) be a completed interaction form on a probe space \(V\). A
factorization

\[
Q=\Gamma^*A\Gamma,\qquad A\ge0,
\]

does not by itself identify a physical interaction constructor. It only
identifies one realization of the form. After absorbing \(A^{1/2}\), write
\(J=A^{1/2}\Gamma\), so \(Q=J^*J\).

The correct finite gate is minimality:

\[
\overline{\operatorname{span}J(V)}=H.
\]

Two minimal Gram/Kolmogorov realizations of the same \(Q\) are related by a
unique unitary on their generated carrier spaces. Nonminimal realizations
contain a dark constructor space

\[
D=\operatorname{span}J(V)^\perp,\qquad
\dim D=\dim H-\operatorname{rank}Q.
\]

Operators supported on \(D\), or couplings between \(D\) and the generated
space, are invisible to the present scalar form. They can become visible
after later transport. Such directions therefore have no authority merely
because they occur in a positive factorization.

## Smallest finite falsifier

Take \(V=\mathbb R^2\) and \(Q=I_2\). Compare

\[
J_{\min}=I_2,\qquad
J_{\mathrm{dark}}=
\begin{pmatrix}
1&0\\0&1\\0&0
\end{pmatrix}.
\]

Both obey \(J^*J=Q\), but the second carrier has the dark direction \(e_3\).
The nonzero operator

\[
Z=|e_3\rangle\langle e_3|
\]

has zero compression \(J_{\mathrm{dark}}^*ZJ_{\mathrm{dark}}=0\). Likewise
the coupling

\[
M=|e_1\rangle\langle e_3|+|e_3\rangle\langle e_1|
\]

has zero initial compression. Rotate \(e_1\) toward \(e_3\) by \(\pi/4\).
For \(J'=UJ_{\mathrm{dark}}\),

\[
{J'}^*M J'=\operatorname{diag}(1,0).
\]

Thus two present-time realizations of the same positive form have different
future compositional content unless dark directions are excluded or typed by
independent source authority.

## Uniqueness theorem and authority boundary

For minimal \(J_1:V\to H_1\) and \(J_2:V\to H_2\) with
\(J_1^*J_1=J_2^*J_2\), the assignment

\[
J_1v\longmapsto J_2v
\]

preserves inner products and extends uniquely to a unitary
\(U:H_1\to H_2\). Hence the interaction carrier is intrinsic only up to this
authorized isometric gauge.

This yields three separate requirements:

1. **Positivity:** \(Q=J^*J\).
2. **Minimality:** no dark constructor directions.
3. **Source authority:** \(J\), its carrier type, and every admitted
   transport are derived before scalar positivity is invoked.

Minimality removes hidden realization slack. It does not make a
post-hoc square root \(Q^{1/2}\) noncircular.

## Cross-sector consequences

- **Arithmetic/RH.** A minimal Gram realization of the Weil/Pick kernel is
  still circular if constructed only after assuming that kernel positive.
  The gate removes hidden carrier directions but supplies no orientation for
  \(C_Y\).
- **Kitaev.** The rank of the phase kernel fixes the minimal interaction
  carrier. The exact one-controlled-\(S\) decomposition and \(|CS\rangle\)
  injection are implementation realizations; they do not authorize the
  missing source-derived state factory or encoded exRec.
- **Strominger.** Deletion witnesses and irredundant quorum roots play the
  role of minimality. A latent signer/capability invisible to the present
  proof can affect later composition and must be explicitly typed under the
  fault model.
- **Benincasa.** Faithful analytic dressing preserves the rank-seven
  response carrier. Higher jets are an enlargement of coefficient/readout
  space, not authority to add dark Carrier incidence.

## Decision

The constructor/lens programme survives only in this sharpened form:

> A completed positive interaction has source-bearing explanatory force only
> through a source-derived minimal factorization, unique up to an admitted
> isometry, whose transport remains closed under composition.

The finite falsifier is: find a nonzero carrier operator \(X\) with
\(J^*XJ=0\), then exhibit an admitted transport \(U\) for which
\((UJ)^*X(UJ)\ne0\). Its existence disproves constructor minimality or
transport closure.

