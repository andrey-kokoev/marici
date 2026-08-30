---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2235 — The Minimal Real Homogeneous Occurrence Adapter Is Gaussian Quadrupole Rank Two

## Even full-momentum kernel

For a real boundary field, the Gaussian kernel must satisfy

\[
a(\vec p)=a(-\vec p).
\]

The first anisotropic angular deformation is therefore quadrupolar, not
linear. On a fixed momentum-magnitude shell in two dimensions, write

\[
a(\theta)=a_0+u\cos2\theta+v\sin2\theta.
\]

The isotropic coefficient \(a_0\) supplies the trivial \(C_3\) line, while
\((u,v)\) span a rank-two angular port.

For the three equilateral directions, a scaled evaluation matrix is

\[
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix},
\qquad
\det=-6.
\]

Hence

\[
\boxed{
\text{isotropic scalar}+\text{Gaussian quadrupole}
\text{ resolves all three homogeneous occurrences}.
}

## Minimality

Entry 2234 proved that two additional directions are necessary. The
quadrupole supplies exactly two, is even under momentum reversal, and is
translation invariant. It is therefore the minimal conventional Gaussian
source enlargement with the required representation type.

## Evidence

- Entries 2233–2234
- `research/benincasa/checkers/quadrupole_gaussian_port.rs`

