# Fault-root image hypergraph and correctability

## Problem

A shared selector may be one logical fault root while affecting several
physical blocks. Counting roots is not enough. The compiler must know the
physical image of each fault root.

Let \(R\) be the set of primitive fault roots and \(B\) the set of protected
blocks. Define

\[
\partial:R\to2^B,
\]

where \(\partial(r)\) is the block support that one fault at root \(r\) may
corrupt before recovery.

This is a hypergraph: roots generate fault-support hyperedges.

## Exact safety condition

Let \(f\) be the root-fault budget and let

\[
\mathcal C\subseteq2^B
\]

be the declared family of correctable block-support sets. Safety requires

\[
\boxed{
\bigcup_{r\in F}\partial(r)\in\mathcal C
\quad
\text{for every }F\subseteq R,\ |F|\le f.
}
\]

This strictly refines both:

- counting faulty roots;
- checking per-block contact load.

The correctable family is source-specific. It may allow one affected block,
one error in every independently protected block, or a more complicated
correlated pattern. The compiler must not infer it from block names.

## CDFG witness

For independent selector roots,

\[
\partial(r_C)=\{C\},\quad
\partial(r_D)=\{D\},\quad
\partial(r_F)=\{F\},\quad
\partial(r_G)=\{G\}.
\]

With budget \(f=1\), only singleton block supports occur.

For one shared lockstep selector root,

\[
\partial(r_{\rm shared})=\{C,D,F,G\}.
\]

Under a correctable family containing only supports of size at most one, the
shared implementation fails immediately even though only one root is faulty.

If the physical encoding independently corrects one induced error in each of
C/D/F/G, then the four-block hyperedge may be correctable. That stronger
claim requires an explicit joint-channel recovery theorem. It cannot be
deduced from four local correction theorems if propagation, recovery timing,
or shared governance couples the blocks.

## Interaction with selector coherence

An authorized lockstep coherence law may legitimately reduce the required
logical orbit from 16 configurations to two. It does not shrink the physical
fault hyperedge.

Thus:

\[
\text{logical diagonal coherence}
\not\Rightarrow
\text{physical fault independence}.
\]

The selector matrix \(A\), contact matrix \(M\), and fault image
\(\partial\) are three separate compiler objects.

## Finite falsifier

Given a root budget \(f\):

1. enumerate root subsets \(F\) with \(|F|\le f\);
2. form the union support \(\partial(F)\);
3. query the declared correctable family;
4. return the first uncorrectable union with its generating roots.

For CDFG under singleton-only correction, the witness is

\[
\texttt{fault\_image\_outside\_correctable\_family},
\]

with one generating root and four affected blocks.

## Cross-sector consequences

- **Strominger.** Quorum fault counts must use the signer/governance image
  of each common-cause root. One administrator compromising several nominal
  signers is a multi-vertex hyperedge.
- **Kitaev.** A shared pointer/predicate selector is one root with a
  multi-block propagation image. Lockstep semantics cannot erase it.
- **Arithmetic/RH.** One hostile source perturbation may alter several
  coupled endpoint/gamma/prime channels. Treating those as independent
  perturbations undercounts the source fault image.
- **Benincasa.** One latent adapter defect may corrupt several period
  components or contact terms simultaneously; componentwise residual tests
  need the joint image.

## Durable statement

> Fault budgets count primitive roots, but safety is decided by the union of
> their physical support images. A one-root event can be a many-block fault,
> and only a declared joint correctability theorem can admit it.

