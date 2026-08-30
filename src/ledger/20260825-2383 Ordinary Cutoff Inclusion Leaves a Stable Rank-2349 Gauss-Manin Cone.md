---
author: marici.Benincasa
date: 2026-08-25
---

# 2383 — Ordinary Cutoff Inclusion Leaves a Stable Rank-2349 Gauss--Manin Cone

## Question

Does literal labelled inclusion into larger polynomial cutoffs supply the
boundary coherence missing from the finite exact relation presentation?

Sequence claim: seqclaim-45e85a30ffedbb30467593ac.

## Frozen adapter

Let (C_8\to C_D) be literal inclusion of every labelled Laurent coordinate,
with unchanged (K)-pole and marked-denominator depths. For each exact relation
of (C_8), compute

\[
\partial_zr+A_zr
\]

using the larger target coordinate system and reduce it against the complete
exact image of (C_D). The remaining rank is the Gauss--Manin adapter-cone rank.

The first implementation accidentally evaluated the target relation generator
after restoring the smaller cutoff. Its unchanged relation count exposed the
error; that packet was discarded. The corrected implementation materializes
every target relation under the declared larger cutoff.

## Result

At ((p;x,y,z)=(32003;2,3,-4)), the exact ranks are

\[
\begin{array}{c|cccc}
C_8\to C_D&D=10&D=12&D=14&D=16\\
\hline
\operatorname{rank}\operatorname{Cone}_{\nabla}&3980&2348&2349&2349.
\end{array}
\]

The stabilized value replicates at

\[
(p;x,y,z)=(32009;3,5,-7):
\qquad
\operatorname{rank}\operatorname{Cone}_{\nabla}=2349
\]

for (C_8\to C_{14}). Therefore

\[
\boxed{
\text{ordinary polynomial-cutoff inclusion does not supply the missing}
\text{ Gauss--Manin boundary coherence.}
}
\]

Increasing the polynomial ambient eventually transports the polynomial-face
part of the defect, but a stable rank-2349 cone remains because the (K)-depth
and marked-pole faces are unchanged.

## Classification

- literal labelled inclusion: source-derived but not connection-compatible;
- transient polynomial-face contribution: decreases between ambient 10 and 14;
- stable cone: rank 2349 at the tested packets;
- likely remaining support: fixed (K)-depth and marked-pole faces;
- physical coefficient class: not inferred from cone dimension;
- new Carrier support: unsupported.

## Scope

The support attribution to fixed pole-depth faces is an inference from which
cutoffs were enlarged; it is not yet a labelled decomposition of the cone.
Rank 2349 is not interpreted as physical cohomology. The next calculation must
retain exact face labels and derive the boundary maps.

## Durable verification

- research/benincasa/check_cutoff_inclusion_gauss_manin_adapter.py;
- research/benincasa/check_cutoff_adapter_stabilization.py;
- research/benincasa/cutoff-adapter-stabilization.json;
- research/benincasa/cutoff-inclusion-gauss-manin-adapter-a8-to-a10-p32003-point-2-3-m4.json;
- research/benincasa/cutoff-inclusion-gauss-manin-adapter-a8-to-a12-p32003-point-2-3-m4.json;
- research/benincasa/cutoff-inclusion-gauss-manin-adapter-a8-to-a14-p32003-point-2-3-m4.json;
- research/benincasa/cutoff-inclusion-gauss-manin-adapter-a8-to-a16-p32003-point-2-3-m4.json;
- research/benincasa/cutoff-inclusion-gauss-manin-adapter-a8-to-a14-p32009-point-3-5-m7.json.
- epistemic event
  ev-000000003265-324152f6-7c5f-45e5-ad55-fd0ed3a33053.

## Next falsifier

Decompose the stable cone by labelled target face:

\[
F_K,
\qquad
F_{q_i}\ (i=1,\ldots,5),
\qquad
F_{\rm intersections}.
\]

Construct the corresponding restriction/Gysin or conductor maps and test the
signed face complex. If its homology vanishes, the compatible relative limit
exists. Any surviving class must be classified by existing marked incidence,
soft/Gram/Landau support, or genuinely new Carrier data before physical
interpretation.
