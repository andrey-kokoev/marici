# RS-1 source-realization gate from the mass collision

## Question

Can the free four-branch decoder's rank-three syndrome be promoted to a
physical relative object by comparison with an existing source-derived fold?

## First complete source packet

Entry 1543 supplies a genuinely typed example:

\[
V_{\rm split}=\mathbb Q\langle\gamma_+,\gamma_-\rangle,
\qquad V_{\rm coll}=\mathbb Q\langle\gamma_0\rangle,
\]

with transfer and specialization

\[
T=(1,1)^T,
\qquad S=\tfrac12(1,1),
\qquad ST=1,
\qquad TS=\frac{1+\sigma}{2}.
\]

The residue pairing descends exactly. Thus this packet has all three pieces
required by RS-1: source-defined channels, source-defined fold, and physical
readout compatibility.

## Exact characteristic gate

Let \(N=1+\sigma\). If the deck order two is invertible, then

\[
e=N/2
\]

is an idempotent and the residual channel is simply

\[
\ker(e)=\mathbb Q\langle\gamma_+-\gamma_-\rangle.
\]

In characteristic two, normalization is impossible and

\[
N^2=2N=0.
\]

This is the modular mechanism behind Grothendieck's norm homology. But the
change of coefficient characteristic is not supplied by the physical
mass-collision source. It therefore cannot be used to retrofit the free
rank-three decoder with physical meaning.

## Verdict

The mass collision validates the *form* of the Relative-Syndrome Conjecture
and falsifies its current rank-three candidate:

\[
\boxed{
\text{source channels and their deck order determine the fold and residue;}
\quad
\text{branch count alone does not.}
}
\]

The first complete source realization has two channels and a rank-one
anti-invariant physical kernel over \(\mathbb Q\). The rank-three coincidence
with \(C_5\) modular norm homology remains untyped because it changes both the
source group and the coefficient field.

## Revised RS-1 admission rule

A syndrome candidate is admissible only with a commutative packet

\[
(A,\sigma,N,e)\longrightarrow(C,\operatorname{Per})
\]

in which:

1. \(A\) and its deck action come from source geometry;
2. the fold is the corresponding trace/norm, not a free augmentation;
3. coefficient localization or reduction is independently source-authorized;
4. the period/readout pairing descends through the same fold;
5. the claimed residue is invariant under source-admissible presentation changes.

The next search should therefore target a source with nonsemisimple deck
specialization already present in its physical coefficient system. It should
not search by desired homology dimension.

## Durable evidence

- `src/ledger/20260821-1543 The Mass-Collision Cycle Map Is the Rational Deck Projector.md`
- `research/grothendieck/finite-p-group-norm-socle-homology.md`
- `research/nima/checkers/check_rs1_deck_projector_characteristic_gate.py`
- `research/nima/results/rs1-deck-projector-characteristic-gate.json`
