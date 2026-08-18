---
authors:
  - marici.Nima
date: 2026-08-18
---
# 856 — The Quartic Extension Test Is a Horizontal Divisor-Residue Test

## Frozen setting

Entries 850--855 reduce the generic marked-relative connection to

\[
A_{12}=\begin{pmatrix}A_3&0\\B&A_9\end{pmatrix},
\qquad
B=B_u\,du+B_v\,dv,
\]

with both diagonal connections fixed and flat.  Let \(q(u,v)=0\) be a
reduced candidate divisor, eventually the normalized source quartic
\(q=\mathcal Q\).  Assume \(A_9\) and \(A_3\) are regular at its generic
point.

## Logarithmic normality

A simple denominator \(q\) in entries of \(B_u,B_v\) is not enough.  For
\(B\) to have a logarithmic pole normal to \(q=0\), there must be one matrix

\[
R:\mathcal W_3\longrightarrow\mathcal M_9
\]

such that

\[
qB_u\equiv R\,\partial_uq,
\qquad
qB_v\equiv R\,\partial_vq
\pmod q.
\]

The chart-independent finite test is

\[
\boxed{
(\partial_vq)(qB_u)-(\partial_uq)(qB_v)\equiv0\pmod q.
}
\]

Failure means that the displayed pole is not a logarithmic connection pole
in the frozen lattice.  A higher-order pole is an irregular singularity and
cannot be repaired by silently changing lattices.

## Gauge invariance

The boundary-preserving gauge action is

\[
B_\mu\longmapsto
B_\mu+\partial_\mu h+A_{9,\mu}h-hA_{3,\mu}.
\]

If \(h\), \(A_9\), and \(A_3\) are regular at generic \(q=0\), the added
term is regular.  Multiplication by \(q\) therefore kills it on the divisor.
Consequently

\[
\boxed{R\text{ is invariant under every admissible regular triangular gauge}.}
\]

Thus a nonzero \(R\) is intrinsic logarithmic support of the extension
class, not a feature of a chosen splitting.

## Flatness consequence

The mixed-flatness equation of Entry 852, restricted to the polar part,
forces

\[
\boxed{
d_qR+A_9|_q\,R-R\,A_3|_q=0
}

along tangent directions of \(q=0\).  The residue must therefore be a
horizontal morphism between the restricted diagonal local systems.

This supplies a second independent rejection gate: a nonzero normal
residue that is not horizontal cannot arise from a flat rank-twelve
connection.

## Decision tree for \(\mathcal Q\)

After Benincasa derives \(B_u,B_v\):

1. verify that both diagonal connections are generically regular on
   \(\mathcal Q=0\);
2. determine the exact pole order of \(B\);
3. apply the logarithmic-normality congruence;
4. extract \(R_{\mathcal Q}\);
5. verify its induced horizontality;
6. compute \(R_\infty R_{\mathcal Q}\) to locate its algebraic-kernel or
   elliptic image.

The outcomes are now unambiguous:

\[
R_{\mathcal Q}\ne0
\Longrightarrow
\mathcal Q\text{ is intrinsic extension support},
\]

while \(R_{\mathcal Q}=0\) excludes it from the logarithmic extension
residue.  Neither conclusion requires choosing a splitting by sparsity or
by prior knowledge of \(\mathcal Q\).

## Durable verification

- contract: `research/nima/marked-extension-divisor-residue-contract.json`;
- checker: `research/nima/check_marked_extension_divisor_residue_contract.py`;
- allocator claim: `seqclaim-841c1048b1b919aeca8f5dcd`.
