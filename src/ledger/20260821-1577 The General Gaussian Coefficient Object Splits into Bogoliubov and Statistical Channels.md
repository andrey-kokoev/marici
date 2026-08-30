# 1577 — The General Gaussian Coefficient Object Splits into Bogoliubov and Statistical Channels

## Hard-to-vary claim

The source-defined homogeneous Gaussian initial-state object is not an
undifferentiated rank-three boundary kernel.  It has a canonical
coefficient-level decomposition

\[
\boxed{
\mathcal G_k^{\rm Gauss}
=\mathcal G_k^{\rm Bog}\oplus\mathcal G_k^{\rm stat},
\qquad
\operatorname{rank}_{\mathbb R}=(2,1).
}
\]

This follows directly from Eqs. (130)--(162) of
Agarwal--Holman--Tolley--Lin, arXiv:1212.1172.

## Pure/Bogoliubov channel

After the source (SU(1,1)) diagonalization, a pure Gaussian state is a
normalized Bogoliubov mode,

\[
f_k^>=\alpha_k h_k+\beta_k h_k^*,
\qquad
|\alpha_k|^2-|\beta_k|^2=1.
\]

Modulo its overall phase, this supplies two real tangent directions.

## Statistical channel

Undoing the diagonalization gives

\[
G_k^{ab}=G_k^{\prime ab}
+\frac{\sigma_k-1}{2}
(G_k^{\prime-+}+G_k^{\prime+-})
\]

for every (a,b\in\{+,-\}).  Mixedness therefore occupies the rank-one
common-contour direction

\[
J_{\rm stat}=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

The checker verifies

\[
\operatorname{rank}J_{\rm stat}=1,
\qquad
2+1=3.
\]

## Consequence for the completed finite-time test

Entries 1568, 1570, and 1573 prove that every frozen endpoint grade lands in
the three-real-dimensional Gaussian response object.  The present source
decomposition sharpens the next question: one-loop transport must preserve
the pure/Bogoliubov and statistical channels with their correct contour
types, not merely their direct-sum span.

Hadamard admissibility is a further ultraviolet filtration on this
coefficient object.  Rank-three closure does not imply preservation of that
filtration.

## Classification

\[
\boxed{
\text{existing doubled contour carrier}
+\text{sector-specific Gaussian coefficient splitting}
+\text{Hadamard support filtration}.
}
\]

No new carrier incidence is required by this result.

## Next falsifier

Linearize one source-defined one-loop map separately along

\[
\mathcal G_k^{\rm Bog}
\qquad\text{and}\qquad
\mathcal G_k^{\rm stat}.
\]

Test contour-channel preservation before integration, then test ultraviolet
falloff after Bunch--Davies subtraction and the declared counterterms.  A
contour-rank failure and a Hadamard-filtration failure must be classified
separately.

## Artifacts

- `research/benincasa/general-gaussian-contour-decomposition.md`
- `research/benincasa/checkers/general_gaussian_contour_decomposition.rs`
- `research/benincasa/results/general-gaussian-contour-decomposition.json`

Ledger sequence claim: `seqclaim-9f83c32b3416311140de6e47`.
