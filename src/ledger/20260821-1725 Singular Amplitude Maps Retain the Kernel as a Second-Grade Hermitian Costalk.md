# 1725 — Singular Amplitude Maps Retain the Kernel as a Second-Grade Hermitian Costalk

## Rank-drop falsifier

Freeze the singular labelled amplitude map

\[
f_\varepsilon=\operatorname{diag}(1,\varepsilon)
\]

and an amplitude \(|u\rangle=(a,b)^T\).  The pushed density is

\[
\rho_\varepsilon
=f_\varepsilon|u\rangle\langle u|f_\varepsilon^\dagger
=
\begin{pmatrix}
a^2&\varepsilon ab\\
\varepsilon ab&\varepsilon^2b^2
\end{pmatrix}.
\]

## Associated-grade decomposition

The exact Rees packet is

\[
\operatorname{gr}^{(0)}\rho
=
\begin{pmatrix}a^2&0\\0&0\end{pmatrix},
\]

\[
\operatorname{gr}^{(1)}\rho
=
\begin{pmatrix}0&ab\\ab&0\end{pmatrix},
\qquad
\operatorname{gr}^{(2)}\rho
=
\begin{pmatrix}0&0\\0&b^2\end{pmatrix}.
\]

These are respectively the Hermitian square of the image, the image–kernel
cross term, and the Hermitian square of the kernel.

For a pure kernel amplitude \(a=0\), both the ordinary and first density grades
vanish, while

\[
\boxed{
\operatorname{gr}^{(2)}\rho=b^2|e_2\rangle\langle e_2|
}
\]

survives on the rank-drop support.

## Narrow result

Ordinary pushforward erases the kernel direction, but the existing
support-sensitive Rees calculus retains it as a second-grade Hermitian
costalk.  No new quantum operation or Cut carrier stratum is required in the
tested finite model.

## Durable artifacts

- `research/benincasa/checkers/singular_amplitude_hermitian_costalk.rs`
- `research/benincasa/results/singular-amplitude-hermitian-costalk.json`
- `research/benincasa/singular-amplitude-hermitian-costalk.md`

## Next falsifier

Compose two singular amplitude maps.  Compare the iterated kernel filtration
with the direct composite filtration and test whether their Hermitian costalks
glue strictly or carry an excess Tor/extension class.
