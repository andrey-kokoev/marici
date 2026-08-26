---
author: marici.Benincasa
date: 2026-08-26
sequence_claim: seqclaim-8dddea783fbac4a76b7d4ba1
---

# 2994 — Labelled Forgetting Explains Shared Information Retention Without Shared Physics

## Scope

This entry proposes a Deutschian explanation for the repeated Boolean occurrence structure found in scattering, cosmology, finite score tomography, and resolved coefficient models.

It is not a claim that those sectors share dynamics, coefficient objects, states, or observables.  It explains why they can share a compositional base without those identifications.

## The problem

Across sectors we repeatedly encounter:

- labelled source occurrences;
- all subsets obtained by retaining or forgetting occurrences;
- alternating deletion maps;
- Möbius reconstruction from a complete deletion tower;
- support-sensitive corrections when restriction ceases to be exact;
- physical readouts that see only a quotient of the labelled packet.

Merely naming this a shared Boolean calculus does not explain it.  The explanatory problem is:

> Why is the same compositional structure forced, which information does it preserve, and why does its presence not imply common physics?

## Explanation

Let (O) be a finite set of independently addressable source occurrences.  Before a sector assigns amplitudes, periods, covariance blocks, or physical meanings, the admissible acts of forgetting occurrences generate the Boolean poset

[
mathcal B(O)={Smid Ssubseteq O},
]

with a unique arrow (S	o T) when (Tsubseteq S).

This category is forced by three source facts:

1. occurrences remain labelled;
2. each occurrence may be retained or forgotten;
3. forgetting distinct occurrences composes independently.

No dynamical assumption enters this construction.  It is the free compositional bookkeeping of independent labelled forgetting.

A sector does not equal (mathcal B(O)).  It supplies a coefficient functor

[
F_alpha:mathcal B(O)^{mathrm{op}}longrightarrowmathcal C_alpha,
]

where (mathcal C_alpha) may contain scalar forms, Gauss--Manin systems, covariance data, Kummer lines, Ward packets, or other sector-specific objects.

A physical experiment or observable supplies a further readout

[
ho_alpha:F_alpha(O)longrightarrowmathcal O_alpha.
]

Thus three types remain distinct:

- the occurrence category says what may be separately retained or forgotten;
- the coefficient functor says how a sector transports information through those operations;
- the readout says what a physically authorized observation reports.

The same base category can therefore govern information retention without identifying either the coefficient functors or the readouts.

## Why Möbius inversion appears

Suppose a labelled packet has primitive components (v_S), one for each retained subset.  A deletion measurement at (T) sees every primitive component whose support contains (T):

[
M_T=sum_{Ssupseteq T}v_S.
]

This is the zeta transform of the Boolean incidence algebra.  The inverse is forced:

[
v_S=sum_{Tsupseteq S}(-1)^{|T|-|S|}M_T.
]

Therefore the complete labelled deletion tower is faithful.  This is not a special property of cosmological coefficients; it follows from the incidence algebra of independently forgettable labels.

Faithfulness fails when a later map identifies labels.  If physical variables tie several occurrences together, the score tower reconstructs only permutation-orbit sums.  If route amplitudes are aggregated before inspection, nonzero packets may enter the aggregation kernel.  The information was present in (F_alpha(O)) but absent from the chosen readout.

## Why derived coherence appears

Ordinary Boolean incidence is enough only when every restriction remains exact and preserves variance.

When forgetting an occurrence crosses support, changes a regular object into a costalk, or encounters repeated normals, the naive square may fail to commute in the ordinary category.  The missing data are not optional new observations.  They are coherence data required to make the same forgetting operations compose:

- Koszul--Cech comparison maps;
- Gysin or residue morphisms;
- Tor or excess grades;
- homotopies and mapping cones.

This derived enhancement is forced by a composition problem.  It must be constructed from the sector's coefficient geometry; it cannot be inferred from the Boolean support census alone.

Entry 2993 supplies a positive example: the fixed D03 packet explicitly constructs the (x_3) Koszul--Cech maps and their lower coherence terms.  Entry 2992 supplies the negative control: the five-site support census is genuine, but its A2 Cech row was preloaded rather than derived.  Shared incidence therefore does not transport authority for derived maps.

## Why the explanation is hard to vary

Removing labels destroys the ability to distinguish occurrence-specific restrictions.

Removing independent forgetting destroys the Boolean category and its Möbius inverse.

Identifying (F_alpha) across sectors falsely equates scalar, elliptic, Gaussian, and Ward coefficient types.

Identifying (ho_alpha) with (F_alpha) falsely turns a restricted physical readout into a complete state description.

Adding derived cells before a support-sensitive composition failure makes them post hoc.

Each component therefore solves a different observed problem and cannot be altered independently without losing an established success or admitting a known failure.

## Explanatory reach

The explanation accounts for:

1. Occurrence-resolved cut factors.  Identifying two labelled interface occurrences on the physical diagonal produces the factor two without a new coupling.

2. Boolean score tomography.  Complete labelled deletion scores are jointly faithful by Möbius inversion.

3. Physical score quotients.  Tied variables reconstruct orbit sums rather than labelled routes.

4. Route interference.  A nonzero labelled route packet can vanish under scalar aggregation without vanishing before aggregation.

5. Sheet exchange.  A unit normal shift may exchange two coefficient sheets while preserving the underlying occurrence cube; the correct coefficient target is then a labelled groupoid rather than a fixed scalar sheet.

6. D03 coherence.  Support-sensitive Koszul--Cech maps are derived from the coefficient geometry and require their lower terms.

7. Five-site noninheritance.  A support lattice and rank census do not by themselves construct a Cech or Gysin differential.

## Novel predictions

For any newly admitted sector with (n) independently forgettable labelled occurrences:

1. Before quotienting labels, its deletion carrier has (2^n) objects and the ordinary incidence signs of an (n)-cube.

2. A complete family of independently variable deletion probes reconstructs the labelled additive packet by Möbius inversion.

3. If probes are tied by a group action, reconstruction stops exactly at the corresponding orbit-sum quotient unless additional source-labelled probes are supplied.

4. A scalar aggregate may have a kernel even when the labelled transport is injective.  Route loss and destructive aggregation must be distinguished before interpretation.

5. New derived cells are licensed only at failures of exact restriction, variance preservation, or support-transverse composition.

6. Coefficient transport may permute sheets or characters without changing the Boolean occurrence base.

7. No physical class follows until a source-authorized readout pairs with the retained coefficient class.

## Finite falsifiers

The explanation fails if any of the following occurs:

- a source has independently forgettable labelled occurrences but its admitted deletion operations do not form the Boolean composition law;
- a complete independently variable deletion tower fails Möbius reconstruction in an additive packet;
- a purportedly shared derived map requires sector-specific cells not forced by a support or variance failure;
- two sectors require different incidence composition for the same labelled forgetting problem;
- a physical observable is proved to reconstruct information absent from every source-authorized coefficient and occurrence packet;
- the proposed ringed PC promotion of D03 fails even though all required purity, variance, and support comparisons are derived and satisfy the same coherence laws.

The first four would threaten the common compositional explanation.  The last would localize its boundary at the derived/ringed level rather than refuting ordinary Boolean incidence.

## Status

The explanation is established for the ordinary labelled-additive layer and has one genuine formal support-sensitive realization in D03.

It is not yet a theorem of one shared ringed or physical derived calculus.  The immediate hostile test remains the D03 occurrence-loaded purity/costalk comparison.  That comparison must be constructed, not transported by analogy.

## Durable verification

The explanation was checked against:

- Entries 2986 and 2988 for the Boolean cross-effect and sheet-exchange packets;
- Entries 2990 and 2992 for the absence of authority from support census alone;
- Entry 2993 and its two exact Rust checkers for a constructed formal support-sensitive realization;
- the graph claim that tied physical score variables reconstruct orbit sums rather than labelled routes;
- the graph claim that the three-site correlator adapter is an eight-sector labelled edge-deletion cube.

No site build was run.
