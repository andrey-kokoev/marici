---
author: marici.Benincasa
---

# 2091 — A Positive Quadratic Source Selects the Gaussian Covariance Lens

## Falsifier

At the smallest Gaussian rank, ask whether the frozen symplectic Carrier data, positivity, purity, and equivariance uniquely determine the physical covariance lens.

They do not. For one mode, the pure positive covariances form the compatible-complex-structure space

\[
Sp(2,\mathbb R)/U(1).
\]

For example, both

\[
V_1=\frac12I,
\qquad
V_2=\begin{pmatrix}1&0\\0&1/4\end{pmatrix}
\]

are positive and satisfy

\[
\det V_i=\frac14,
\]

but they are distinct. Equivariance transports this family; it does not choose a member.

## Source selector

Freeze an independently supplied positive quadratic Hamiltonian

\[
H=\frac12\xi^Th\xi,
\qquad h=h^T>0,
\]

and the symplectic form \(\Omega\). In one mode,

\[
A_h=\Omega h,
\qquad
A_h^2=-(\det h)I.
\]

The positive-frequency choice determines the compatible complex structure

\[
\boxed{
J_h=\frac{\Omega h}{\sqrt{\det h}}.
}

The selected vacuum covariance is

\[
\boxed{
V_h=-\frac12J_h\Omega
=\frac{\sqrt{\det h}}2h^{-1}.
}

It is invariant under irrelevant positive rescaling:

\[
V_{\lambda h}=V_h,
\qquad \lambda>0.
\]

## Uniqueness

Write

\[
h=\begin{pmatrix}a&c\\c&b\end{pmatrix},
\qquad
V=\begin{pmatrix}x&z\\z&y\end{pmatrix}.
\]

Source stationarity

\[
A_hV+VA_h^T=0
\]

gives

\[
cx+bz=0,
\qquad
az+cy=0,
\qquad
by=ax.
\]

Therefore \(V\) is proportional to \(h^{-1}\). Purity \(\det V=1/4\) and positivity select the unique positive proportionality factor \(\sqrt{\det h}/2\).

An exact rational checker verifies the example

\[
h=\begin{pmatrix}5&1\\1&2\end{pmatrix},
\qquad
V_h=\begin{pmatrix}1/3&-1/6\\-1/6&5/6\end{pmatrix}.
\]

## Result

\[
\boxed{
\text{Carrier constraints define the admissible Gaussian lenses; source dynamics selects the physical lens.}
}

Equivalently, the positive Hamiltonian supplies a source polarization map whose pullback of the standard positive Hermitian form is the covariance lens. This is the Gaussian analogue of the source-record construction \(E^\dagger E\): naturality governs transport, while source framing performs selection.

The result also aligns with the source-normalized Leray covector: an endpoint framing/readout is additional typed source data, not another Carrier law.

## Provenance

- `research/benincasa/checkers/one_mode_gaussian_source_lens.py`;
- `research/benincasa/checkers/results/one-mode-gaussian-source-lens.json`;
- allocator claim `seqclaim-f7583083a016dbe61c59f5fb`;
- epistemic event `ev-000000002873-bd4ae427-f648-49ef-9e2c-9a359693f386`;
- Nima Entries 2073, 2074, 2077, and 2083.

## Next falsifier

At two modes, test whether a positive quadratic Hamiltonian still selects the full covariance lens uniquely when symplectic eigenfrequencies are degenerate. The expected obstruction is not a new Carrier cell but a source-polarization stabilizer acting inside the degenerate frequency subspace.
