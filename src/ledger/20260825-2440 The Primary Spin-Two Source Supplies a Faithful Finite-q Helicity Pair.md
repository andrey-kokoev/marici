---
author: marici.Benincasa
date: 2026-08-25
---

# 2440 — The Primary Spin-Two Source Supplies a Faithful Finite-q Helicity Pair

## Question

Entry 2439 closes the scalar interaction action under physical weighted Gram
base change but leaves the first tensor enlargement untyped. Before inserting a
spin-two numerator into the marked one-loop system, derive the local
scalar--scalar--graviton vertex and its physical ports from a frozen primary
source.

## Frozen primary source

Baumann, Duaso Pueyo, Joyce, Lee, and Pimentel,
*The Cosmological Bootstrap: Spinning Correlators from Symmetries and
Factorization*, arXiv:2005.04234v3, gives on page 58, equation (6.22),

\[
V_{\gamma\varphi\varphi}^{ij}
=
\frac{1}{2\eta^2}\,\beta_u^i\beta_u^j,
\]

where $\beta_u$ is the difference of the two scalar momenta at the vertex.
The same source fixes the conformally coupled scalar action and stress-tensor
Ward identity on page 32, equations (4.30)--(4.35), and the transverse-traceless
projector on pages 106--107, equations (E.5) and (E.10).

These conventions are retained without fitting them to the scalar
rank-sixty packet.

## Exact TT reduction

Choose the finite transfer momentum along the third axis,

\[
q=(0,0,q_z),
\qquad
\beta=(\beta_x,\beta_y,\beta_z).
\]

The transverse projector is $\pi=\operatorname{diag}(1,1,0)$. Applying the
spin-two TT projector gives

\[
\Pi_{2,2}(\beta\otimes\beta)
=
\begin{pmatrix}
(\beta_x^2-\beta_y^2)/2&\beta_x\beta_y&0\\
\beta_x\beta_y&(-\beta_x^2+\beta_y^2)/2&0\\
0&0&0
\end{pmatrix}.
\]

Direct contraction verifies both transversality and tracelessness.

## Two physical helicity ports

With

\[
e_\pm=\frac{1}{\sqrt2}(1,\pm i,0),
\]

the two helicity responses are

\[
V_+
=
\frac{(\beta_x+i\beta_y)^2}{4\eta^2},
\qquad
V_-
=
\frac{(\beta_x-i\beta_y)^2}{4\eta^2}.
\]

Writing the real quadrupole coordinates as

\[
A=\beta_x^2-\beta_y^2,
\qquad
B=2\beta_x\beta_y,
\]

their transfer is

\[
\begin{pmatrix}4\eta^2V_+\\4\eta^2V_-\end{pmatrix}
=
\begin{pmatrix}1&i\\1&-i\end{pmatrix}
\begin{pmatrix}A\\B\end{pmatrix}.
\]

The determinant is $-2i$. Hence both real transverse quadrupole coordinates
are recovered faithfully from the two physical tensor polarizations.

The quadrupole map itself has Jacobian

\[
\det\frac{\partial(A,B)}{\partial(\beta_x,\beta_y)}
=4(\beta_x^2+\beta_y^2).
\]

On the real physical locus, rank is lost only when $\beta$ is parallel to
$q$. This is existing Gram/collinear support, not a new incidence divisor.

## Local Ward packet

For scalar momenta $k_2,k_4$ at the vertex,

\[
q=k_2+k_4,
\qquad
\beta=k_2-k_4,
\]

so

\[
q\mathbin{\cdot}\beta=k_2^2-k_4^2.
\]

The unprojected longitudinal contraction is therefore an endpoint/inverse-
kinematics difference. The physical TT projector kills it. This identifies
the local Ward boundary, but it does not yet construct the loop-level contact
completion.

## Result

\[
\boxed{
\text{the primary finite-$q$ spin-two vertex supplies a faithful pair of
physical helicity ports away from existing Gram support.}
}
\]

No tensor-specific Carrier support appears at the local vertex.

## Scope

This is a local source-provenance and observer-rank theorem. It does **not**
authorize multiplying the scalar rank-sixty master system by a quadratic
numerator and calling the result the gravitational marked-relative system.
The factor $\eta^{-2}$ must be transported through the source time integral,
and the Ward contact completion must be derived before loop-level cyclic,
Gauss--Manin, localization, or physical-cycle claims are made.

## Durable evidence

- `research/benincasa/check_finite_q_tensor_vertex_ports.py`;
- `research/benincasa/finite-q-tensor-vertex-ports.json`;
- Baumann et al., arXiv:2005.04234v3, equations (4.30)--(4.35), (6.22),
  (E.5), and (E.10);
- sequence claim `seqclaim-f2743c60ec548d585756a4e5`.

## Next falsifier

Derive the source-normalized time-integral action of $\eta^{-2}$ on the
conformally coupled scalar seed. Determine whether it is a strict energy
contiguity operator, a marked-pole-order shift, or requires an additional
contact term. Only then insert the two-helicity packet into the full
marked-relative loop complex.
