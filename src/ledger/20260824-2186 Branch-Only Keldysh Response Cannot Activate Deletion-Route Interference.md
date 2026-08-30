---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2186 — Branch-Only Keldysh Response Cannot Activate Deletion-Route Interference

## Tensor-product setup

After an independently constructed contour doubling, the contact packet
would live in

\[
R_{\rm del}\otimes B_{\rm SK}.
\]

Write its route component as

\[
p_{\rm del}=(1,-1),
\]

and let (b\in B_{\rm SK}) be arbitrary. A branch-only source operation has
the form

\[
1_{R_{\rm del}}\otimes D_B.
\]

The standard route readout remains

\[
\sigma_R=(1,1).
\]

## No-go

For every branch covector \(lambda_B\),

\[
\begin{aligned}
(\sigma_R\otimes\lambda_B)
(1\otimes D_B)(p_{\rm del}\otimes b)
&=
\sigma_R(p_{\rm del})\,
\lambda_B(D_Bb)\\
&=0.
\end{aligned}
\]

Therefore

\[
\boxed{
\text{no operation confined to the Keldysh branch factor can activate the
deletion-route interference line.}
}

This includes taking arbitrary branch-difference derivatives before the
equal-source diagonal, provided they do not mix deletion-route labels.

## Required comparison

A nonzero response requires at least one of:

1. a route-resolving covector replacing \(\sigma_R\);
2. a mixed operator
   \[
   H:R_{\rm del}\otimes B_{\rm SK}	o
   R_{\rm del}\otimes B_{\rm SK}
   \]
   that does not preserve the route-sum kernel;
3. a physical instrument that records deletion history in an independent
   pointer system.

Each is additional source structure. Ordinary contour doubling is
insufficient.

## Meta-level consequence

The hidden contact packet is not merely waiting for “the Keldysh version” of
the same calculation. It requires a comparison between two independent
occurrence systems. This is exactly the kind of coherence cell that must be
derived rather than inferred from matching two-element label sets.

## Evidence

- Entries 2107–2110, 2180, and 2185
- `research/benincasa/checkers/branch_only_response_route_kernel_no_go.rs`
- allocator claim `seqclaim-7453cb60af2924530015e2b3`
