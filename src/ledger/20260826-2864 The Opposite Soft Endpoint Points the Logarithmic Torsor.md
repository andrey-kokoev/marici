# 2864 — The Opposite Soft Endpoint Points the Logarithmic Torsor

> **Corrected scope after the full fiber-cycle audit.** The physical
> (a)-cycle moves with (t) and collapses at (t=2). Therefore the
> pointwise condition (F(a,2)=0) is not defined for generic fixed (a).
> The construction below is valid only for a scalar density already pushed
> forward along the moving (a)-cycle. The pushforward must precede the
> pointing.

## Refinement of Entry 2862

The isolated logarithmic germ has no affine origin. The complete source chain contains additional data:

\[
t=\frac{q_{g1}}{X_1}=\xi+1,
\qquad
t\in[0,2].
\]

The unmarked endpoint is the source-normalized point

\[
t=2.
\]

It therefore supplies the candidate pointing

\[
F(2)=0.
\]

## Pointed primitive

For a local density

\[
f(t)=\frac Rt+\sum_{n\ge0}h_nt^n,
\]

the uniquely pointed primitive is

\[
F(t)
=
R\log(t/2)
+
\sum_{n\ge0}
\frac{h_n}{n+1}
\left(
t^{n+1}-2^{n+1}
\right).
\]

Adding a constant violates \(F(2)=0\), so the opposite endpoint removes the affine translation freedom.

After subtracting the canonical logarithmic term, the pointed finite part at the marked endpoint is

\[
\operatorname{FP}_{t=0}F
=
-\sum_{n\ge0}
\frac{2^{n+1}}{n+1}h_n.
\]

## Interpretation

The correct distinction is:

- the local marked germ determines an affine residue torsor;
- the complete oriented source chain can point that torsor;
- the pointing is unavailable if the opposite endpoint is forgotten.

Thus source normalization may supply more than branch orientation. The endpoint \(t=2\) is a candidate affine origin derived before inspecting the desired scalar value.

## Remaining acceptance gate

This is not yet a global physical scalar theorem. The pointed finite part must satisfy:

1. naturality under every source-derived occurrence and residue-chart transition;
2. compatibility with the full \(a\)-dependent relative cycle;
3. preservation under admissible regulator deformations;
4. agreement with the logarithmic residue/Leray-tube pairing.

Failure of any gate returns the object to an unpointed torsor. Passing them would produce a source-authorized renormalized bulk readout—not an arbitrary endpoint sum.

## Durable artifacts

- research/benincasa/check_soft_endpoint_chain_pointed_torsor.py
- research/benincasa/soft-endpoint-chain-pointed-torsor.json
