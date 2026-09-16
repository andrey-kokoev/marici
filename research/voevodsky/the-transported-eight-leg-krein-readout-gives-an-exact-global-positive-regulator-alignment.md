# The transported eight-leg Krein readout gives an exact global positive-regulator alignment

## Objective

Close the finite-cutoff alignment identity required before common-Widom-edge removal, including unequal left/right transported regulator placements.

## Fixed-signature readout

At finite regulator \(\alpha=(\Lambda,R,N,n,F)\), exact physical-to-Hardy transport supplies a linear eight-leg feature \(\Theta_\alpha\) and a fixed Hermitian involution \(K_8\) such that the centered Hermitian regulator is

\[
D_\alpha=
\Theta_\alpha^*K_8\Theta_\alpha
\]

when the two observer legs have common placement. Let

\[
E_\pm=\frac12(I\pm K_8).
\]

Define positive feature legs

\[
X_\alpha^T=E_+\Theta_\alpha,
\qquad
X_\alpha^0=E_-\Theta_\alpha.
\]

Then their ordinary Grams are positive and satisfy the exact identity

\[
\boxed{
G_\alpha^T-G_\alpha^0
=(X_\alpha^T)^*X_\alpha^T-(X_\alpha^0)^*X_\alpha^0
=
\Theta_\alpha^*K_8\Theta_\alpha
=D_\alpha.}
\]

The decomposition uses the fixed source-independent Krein signature, not the Jordan decomposition of \(D_\alpha\). Hence it is global before observer compression.

## Unequal transported regulator legs

Exact cyclic transport generally produces two linear maps \(L_\alpha\) and \(R_\alpha\), because the physical outer regulator need not commute with observer multiplication. The Hermitian centered form is the polarization

\[
D_\alpha
=
\frac12(L_\alpha^*K_8R_\alpha+R_\alpha^*K_8L_\alpha).
\]

Set

\[
C_\alpha=\frac{L_\alpha+R_\alpha}{2},
\qquad
H_\alpha=\frac{L_\alpha-R_\alpha}{2}.
\]

Direct expansion gives

\[
D_\alpha=C_\alpha^*K_8C_\alpha-H_\alpha^*K_8H_\alpha.
\]

Splitting both occurrences by \(E_\pm\) yields positive maps

\[
X_\alpha^T=E_+C_\alpha\oplus E_-H_\alpha,
\qquad
X_\alpha^0=E_-C_\alpha\oplus E_+H_\alpha.
\]

Their Gram difference is exactly

\[
\boxed{
(X_\alpha^T)^*X_\alpha^T-(X_\alpha^0)^*X_\alpha^0
=D_\alpha.}
\]

Thus noncommuting regulator placement does not obstruct positive alignment; it only requires the Hadamard common/difference doubling already native to the relative dilation.

## Physical typing

Every ingredient is inherited from the exact finite transport:

- \(L_\alpha,R_\alpha\) retain the actual transported physical regulator;
- observer factors remain on their original left/right sides;
- \(K_8\) and \(E_\pm\) are fixed finite matrix channels;
- angular assembly is a finite direct sum;
- two-copy bulk and endpoint conventions remain inside the same feature maps.

No convenient symmetric Mellin window and no packet-dependent spectral projection of \(D_\alpha\) is introduced.

## Packet naturality

For any observer inclusion \(j:E_F\hookrightarrow E_{F'}\), restriction gives

\[
X_{\alpha,F}^{T,0}=X_{\alpha,F'}^{T,0}j.
\]

Consequently

\[
G_{\alpha,F}^{T,0}=j^*G_{\alpha,F'}^{T,0}j
\]

and

\[
D_{\alpha,F}=j^*D_{\alpha,F'}j.
\]

This is genuine packet-natural positive-regulator alignment. It must not be confused with naturality of \(|D_{\alpha,F}|\), which generally fails.

## Remaining analytic gate

The exact identity does not identify a positive common edge \(C_{\alpha}^{edge}\) whose removal from both aligned Grams leaves the Jordan legs of \(D_\alpha\). Nor does it prove convergence after removing outer/angular/dyadic regulators.

Accordingly the earlier alignment gate is now algebraically closed, while the first unresolved physical statement is:

\[
\boxed{
\text{construct one packet-independent common positive subfeature of }
X_\alpha^T,X_\alpha^0
\text{ with uniformly controlled residual leakage}.}
\]

Finite-packet common-edge coercivity proves existence of a matrix subtraction after compression. It does not automatically produce this global common subfeature.

## Updated channel-2 order

1. exact positive-regulator Gram difference: constructed by fixed-signature/Hadamard splitting;
2. packet-independent positive target \(|\mathcal A_S|\): constructed on phase-energy completion;
3. global common-edge subfeature for the physical aligned legs: open;
4. uniform observer-filtration leakage estimate: open;
5. Mosco/strong-resolvent convergence: formal after 3 and 4.

## Repository dependencies

- `exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md`
- `checkers/check_relative_c34_positive_dilation.py`
- `the-finite-absolute-gram-closure-is-conditional-on-one-exact-positive-regulator-alignment.md`
- `global-absolute-gram-mosco-convergence-reduces-to-uniform-graph-core-and-compression-control.md`
