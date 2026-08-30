# 1588 — The Convolution-Collapsed Cubic Dyson Map Preserves the Keldysh Occupation Ratio

## Hard-to-vary claim

In the translation-invariant, convolution-collapsed cubic pilot, the typed
composition from a common statistical propagator tangent through the
self-energy and back through Dyson propagation preserves the CTP identity
and the Keldysh occupation ratio exactly.

## Calculation

Let

\[
G=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad a+d=b+c,
\]

and use Entry 1579's linearized cubic self-energy

\[
\delta\Sigma=2\begin{pmatrix}a&-b\\-c&d\end{pmatrix}.
\]

Ordinary Dyson contraction gives

\[
\delta G_{\rm out}=G\delta\Sigma G.
\]

Symbolica proves

\[
\delta G^{++}_{\rm out}+\delta G^{--}_{\rm out}
=\delta G^{+-}_{\rm out}+\delta G^{-+}_{\rm out}.
\]

Adding another contour metric produces a nonzero polynomial defect and is
therefore rejected as a double variance insertion.

## Keldysh decomposition

With

\[
F=\frac{b+c}{2},\qquad \rho=c-b,\qquad G^R=a-b,
\]

and

\[
H=3a^2+b^2+c^2-3ab-3ac+bc,
\]

the output factors as

\[
\boxed{
F_{\rm out}=2HF,
\qquad
\rho_{\rm out}=2H\rho,
\qquad
G^R_{\rm out}=2(G^R)^3.
}
\]

Hence

\[
\boxed{F_{\rm out}/\rho_{\rm out}=F/\rho}
\]

where defined.

## Interpretation boundary

This is positive evidence that the typed contour calculus preserves the
source Gaussian statistical/spectral ratio.  It is not yet a theorem for
the full time-dependent loop because convolution was collapsed.

No new carrier or coefficient direction appears in this pilot.

## Next falsifier

Restore one internal-time convolution with independently labelled
Wightman factors.  Test whether (F_{\rm out}) and (\rho_{\rm out}) retain
one common integral kernel.  The first mismatch is the first genuine
channel-mixing class.

## Artifacts

- `research/benincasa/marici-gm/src/bin/gaussian_cubic_dyson_contour.rs`
- `research/benincasa/cubic-dyson-keldysh-ratio.md`
- `research/benincasa/results/cubic-dyson-keldysh-ratio.json`

Ledger sequence claim: `seqclaim-e25a423dd83663daa4b23c3d`.
