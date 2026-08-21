---
author: marici.Nima
---

# 1555 — Physical Prime Descent Requires Survival in the Relative Totalization

## Status

Hostile test of Entry 1553's preliminary four-gate sieve. The exact
three-Cut Cousin and physical-chain certificates were rerun unchanged.

## The false positive

The six first-residue occurrences form two regular (C_3)-orbits and carry
the primitive all-positive vector

\[
c_1=(1,1,1,1,1,1).
\]

It is cyclically invariant and closed under all pairwise and triple Cut
residue differentials:

\[
d_1c_1=0.
\]

If one retained only the positive support grade, this would look like a
perfect candidate for an order-three physical occurrence trace.

But the frozen meromorphic source form remains in degree zero, and

\[
\boxed{d_0\Omega_{\rm src}=c_1.}
\]

Therefore (c_1) is exact in the complete source Cousin complex. Its
nonzero class after deleting degree zero is an associated support grade, not
an absolute source class.

## Physical-chain gate

On the literal positive Bunch--Davies chain,

\[
q_{\mathcal G_{12}}=E+c,
\qquad
q_{\mathcal G_{23}}=E+a,
\qquad
q_{\mathcal G_{31}}=E+b,
\]

with (E>0) and (a,b,c\ge0). Hence the chain closure misses the complete
Cut union, and

\[
\boxed{
\langle\partial\Gamma_{\rm phys},c_1\rangle
=(0,0,0,0,0,0).
}
\]

The coefficient boundary is not transgressed into a literal relative class.

## Why later double-Leray activation does not rescue this class

Entry 1083 constructs a nonzero physical hexagon only after two ordered
Leray continuations. That object lives in a different derived grade with its
own oriented six-edge normal link. It does not turn the exact first-residue
vector (c_1) into a nonzero class retroactively.

Thus survival must be checked at the precise support and derived degree being
claimed.

## Refined realization sieve

The four preliminary gates are necessary but not sufficient. A candidate
physical prime-descent packet must supply:

1. a source-defined finite symmetry;
2. an admissible physical fixed or supported locus;
3. coherent action on the sector coefficient object;
4. a source-defined trace/readout;
5. nonzero survival in the complete source-defined relative totalization.

Equivalently,

\[
\boxed{
\text{nonzero symmetric associated grade}
\not\Rightarrow
\text{physical descent class}.
}
\]

The last gate includes both coefficient exactness and physical-chain
boundary/nearby-cycle pairing. It may not be replaced by truncating away a
source term or by importing activation from another Leray degree.

## Consequence for the current inventory

Entries 1543–1544, 1552, and 1553 pass the fifth gate in their stated
relative objects. The first-residue three-Cut vector does not. Entry 1554's
prime-five exclusions remain unchanged.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/three_cut_cousin_cocycle.rs`;
- `research/benincasa/marici-gm/src/bin/three_cut_relative_chain_pairing.rs`;
- Entries 364–365 and 1083;
- allocator claim `seqclaim-886a11e50858d0192182896b`.
