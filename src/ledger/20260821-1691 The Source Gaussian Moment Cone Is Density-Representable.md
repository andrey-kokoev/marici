# 1691 — The Source Gaussian Moment Cone Is Density-Representable

## Predeclared-class extension test

Entry 1690 isolates the noncommutative moment-extension problem. Begin with the
general Gaussian initial-state class already admitted by the source.

For one centered mode with \([Q,P]=2i\), the covariance packet

\[
V=\begin{pmatrix}x&z\\z&y\end{pmatrix}
\]

is physical precisely on the Gaussian uncertainty cone

\[
V>0,\qquad \det V=xy-z^2\ge1.
\]

Williamson decomposition gives

\[
\boxed{
V=\nu SS^T,\qquad S\in Sp(2,\mathbb R),\qquad
\nu=\sqrt{\det V}\ge1.
}
\]

The isotropic covariance \(\nu I\) is realized by the thermal density operator
whose occupation probabilities have geometric ratio

\[
r=\frac{\nu-1}{\nu+1},\qquad 0\le r<1.
\]

A metaplectic lift of \(S\) then realizes \(V\). Hence every packet in this
predeclared Gaussian cone extends to a positive trace-class density operator.

The exact checker uses rational symplectic matrices

\[
S=\begin{pmatrix}1+k\ell&k\\ \ell&1\end{pmatrix}
\]

and verifies 3,528 thermal--metaplectic covariances with
\(\det V=\nu^2\). It also verifies 5,000 cardinality-weighted covariance
merges, all remaining in the uncertainty cone.

## Narrow result

\[
\boxed{
\text{the source one-mode Gaussian moment cone is density-representable and merge-stable.}
}
\]

This supplies one exact finite representable coefficient class. It does not
close the full cosmological process because scalar-cubic evolution generates
non-Gaussian cumulants and unbounded Schmidt rank.

## Durable artifacts

- `research/benincasa/checkers/gaussian_density_representability.rs`
- `research/benincasa/results/gaussian-density-representability.json`
- `research/benincasa/gaussian-density-representability.md`

## Next falsifier

Follow the first cubic tangent out of the Gaussian cone. Determine whether the
degree-four Gram packet of Entry 1630 lies in the tangent cone of genuinely
density-representable states, rather than merely the truncated positive cone.
Use an explicit trace-class perturbation of a thermal--metaplectic state or
record the missing extension datum.
