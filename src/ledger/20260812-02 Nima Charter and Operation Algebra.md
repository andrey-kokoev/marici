# Nima Charter and Operation Algebra

## Status and provenance

This entry is the foundational record for the Nima branch of Marici. It preserves the Nima
continuation brief received on 2026-08-12 and fixes the vocabulary against which later proofs and
falsifications will be recorded.

The structures below are **inherited working structure** unless a later ledger entry supplies an
independent derivation or citation. Recording a claim here does not upgrade it to a theorem.

## Branch identity

Nima owns the theory-producing geometry problem:

> Determine whether a scalar master amplitude or surface object carries intrinsic operations whose
> derived normal sectors produce known physical theories.

This is narrower than a search for a universal scalar Lagrangian and stronger than observing that
several amplitudes can be reconstructed from scalar data. The sought structure must explain why
the extraction operations, physical quotients, pairings, and sewing laws are intrinsic and
compatible.

## Correction to the original master picture

The current hypothesis is not that different theories are literal faces of one already formed
scalar amplitude. The sharper proposal is that the scalar master is a **premodular
theory-producing object**. Distinct physical theories arise only after distinct normal and derived
operations:

\[
\text{scalar master}
\longrightarrow
\text{normal extraction}
\longrightarrow
\text{descent, retract, or polarization}
\longrightarrow
\text{dualizable tree object}
\longrightarrow
\text{modular completion}.
\]

The extraction step is part of the definition of the theory. A theory need not be a quantum
subsector of a larger object that was quantized first.

## Candidate primitive operations

| Operation | Intended role | Current use | Status |
| --- | --- | --- | --- |
| \(\operatorname{gr}_R\) | normal associated grade at rank-jump stratum \(R\) | NLSM | inherited working structure |
| \(J_F^1\) | first normal jet at fusion stratum \(F\) | raw Yang–Mills symbol | inherited working structure |
| \(H_{\rm gauge}\) | gauge or BRST cohomological descent | physical Yang–Mills | inherited working structure |
| \(I_{\rm scalar}^{-1}\) | inverse multiparticle scalar pairing | KLT/CHY-type pairing and index raising | inherited working structure |
| \(\operatorname{HarmSchur}_\lambda\) | harmonic/Brauer idempotent splitting | tensor-sector selectors | candidate operation family |
| \(\operatorname{PrimSym}_g^2\) | traceless symmetric retract for \(\lambda=(2)\) | pure graviton sector | inherited working structure |
| \(\operatorname{Strict}^{\rm QTDS}_P\) | parity-core transfer over the alternating order cover | quartic NLSM grammar | six-point scalar-cell transfer established; dg/Jordan coherence open |
| \(\operatorname{Mod}\) | modular completion by compatible sewing | quantum theory | structural target |

This list is not yet an algebra in the mathematical sense. For that claim to become precise, every
operation needs a declared domain and codomain, functoriality under boundary maps, and relations or
natural transformations comparing the composites that are simultaneously defined.

## First candidate relations

The leading relation is an order-of-operations warning. For an extraction or idempotent \(E\), one
must not assume

\[
\operatorname{Mod}\circ E
=
E\circ\operatorname{Mod}.
\]

Gravity supplies the working counterexample: forming the primitive-symmetric retract before
sewing gives induced pure-Einstein internal states, whereas projecting only the external states of
an already completed NS–NS theory does not remove its dilaton and two-form internal sectors.

Other candidate relations requiring type-correct formulations are:

\[
H_{\rm gauge}\circ J_F^1,
\]

because the first jet alone retains gauge redundancy;

\[
I_{\rm scalar}^{-1}
\quad\text{compatible with scalar boundary gluing},
\]

because pairing must commute with factorization if it is to generate theories; and

The earlier relation \(\operatorname{Strict}_J\simeq\operatorname{id}\) on tree amplitudes has
now been retyped. Entry 16 proves that the bare class cannot naturally select one ordering,
polarity, or Jordan realization. The viable comparison is an augmentation

\[
\epsilon_P:\mathcal Q_P\xrightarrow{\simeq}\pi^*\mathsf J^R_P
\]

over the alternating cyclic-order cover, compatible with deck flip and factorization. After
ordered evaluation this augmentation is amplitude preserving; constructing it before pairing
remains open.

## Candidate master principle

The working formulation is:

> A physical quantum theory is the modular completion of a dualizable derived normal sector of the
> scalar master geometry.

This is a research principle, not an established classification theorem. In particular, the
following obligations remain open:

1. define the scalar master object independently of the desired daughter theory;
2. type every normal operation and show it is intrinsic;
3. prove boundary and factorization naturality of the extracted tree object;
4. construct its evaluation and coevaluation, or identify the obstruction to dualizability;
5. show that modular completion exists and has the claimed physical content.

## Epistemic perimeter

Do not infer from amplitude reconstruction that an intrinsic half-object exists. Do not call the
candidate operations an algebra before their types and composition laws are fixed. Do not assume
that extraction commutes with quantum completion. Do not transfer a tree-level equality to an
off-shell or loop-level canonical representative without additional data.

## Decision

Adopt the premodular derived-sector picture as Nima's organizing hypothesis. Test it first at the
NLSM rank jump, where the missing object is precise enough to fail: an intrinsic half-object
\(\mathsf J\) with a scalar-boundary definition, a CHY cohomology class, and natural factorization
before it is paired with any second half.
