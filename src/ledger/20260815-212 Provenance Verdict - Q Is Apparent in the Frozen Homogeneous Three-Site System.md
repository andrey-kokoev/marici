---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Provenance Verdict: \(\mathcal Q\) Is Apparent in the Frozen Homogeneous Three-Site System

## Record

Date: 2026-08-15

Status: completed provenance classification at generic nonsoft kinematics
for the source-displayed homogeneous three-site one-loop simplex integral.
Intersections with the frozen discriminant/soft union and generic
multi-external-leg specializations are outside this theorem.

This entry synthesizes entries 181, 183, 209, and 211. It introduces no
denominator, support summand, projector, splitting chosen from the target, or
carrier cell.

## Frozen question

Determine whether the printed quartic
\[
\mathcal Q
=-16X_1^2X_2^2-8X_1X_2E^2
+8(X_1+X_2)E^3-5E^4
\]
has an intrinsic home in:

1. the gauge-normalized algebraic Gysin-plane extension;
2. another block of the rank-seven algebraic kernel;
3. discriminant extension or the physical relative chain; or
4. only a cyclic/master-presentation alphabet.

## Candidate-by-candidate verdict

### Algebraic Gysin plane

The diagonal characters are
\[
g_{00}=-\frac12d\log P_6,
\qquad
g_{11}=d\log D_1,
\]
with unique \(d\log\mathcal Q\) weight zero.

The off-diagonal equation
\[
dh+(g_{00}-g_{11})h=-g_{10}
\]
has a polynomial degree-seven solution. Its denominator powers in the frozen
search basis \((D_1,P_6,\mathcal Q)\) are
\[
(0,0,0).
\]
The split identity passes 2,048 disjoint directional tests.

Verdict:
\[
\boxed{\mathcal Q\text{ is absent from the algebraic-plane extension.}}
\]

### Remaining rank-seven kernel

The other source parity blocks have ranks \(1,2,2\). Their complete
bivariate connections have poles only on
\[
u=0,
\qquad
1-\frac{u+v}{2}=0,
\]
or are constant triangular. Their blockwise mismatch census is
\[
(0,0,0)
\]
over 2,048 directional tests, and no entry has a \(\mathcal Q\)
denominator.

Verdict:
\[
\boxed{\mathcal Q\text{ is absent from the generic algebraic kernel.}}
\]

### Discriminant and physical relative chain

Entry 181 freezes the source-positive sheet by
\[
W=|R_L|,
\qquad
\Gamma_{\rm phys}\cap L
\subset D_L^{\operatorname{sign}R_L}.
\]
The sheet can switch only on the already frozen branch-at-pair strata.

The exhaustive raw discriminant census rejects \(\mathcal Q\) from all
1,719 nonconstant surface/component/incidence conditions in one residue
sector. Cyclic transport tests all three target quartics against all three
sectors:
\[
3\cdot1719=5157
\]
exact factor rejections.

The resulting simultaneous relative SNC pair extends over a generic
transverse \(\mathcal Q\)-disk. Hence
\[
T_{\mathcal Q}=1,
\qquad
N_{\mathcal Q}=0,
\qquad
\operatorname{Var}_{\mathcal Q}(\Gamma_{m phys})=0.
\]

The source lower sector has the complete ten-linear-letter alphabet and no
\(\mathcal Q\) component. The literal six-term cyclic assembly has
coefficients \(+1\), common orientation, and the same physical chain, so
its variation is also zero.

Verdict:
\[
\boxed{
\mathcal Q\text{ is neither discriminant support nor physical-chain
support at generic nonsoft homogeneous kinematics.}
}
\]

## Final classification

All intrinsic candidate homes are eliminated in the frozen system:
\[
\boxed{
\mathcal Q
\text{ is apparent cyclic/master-presentation alphabet data.}
}
\]

More precisely:

- existing carrier support: no \(\mathcal Q\) component;
- coefficient support: none generically;
- algebraic extension support: none;
- physical relative-cycle support: none;
- cross-sector extension: none detected by the literal source period;
- genuinely new carrier datum: none.

The occurrence of \(\sqrt{\mathcal Q}\) in a printed algebraic letter is
therefore not a singular-support statement. A singular master-basis
presentation may retain apparent \(\mathcal Q\) poles without changing the
period or its monodromy.

## Scope boundary

This verdict is generic along \(\mathcal Q=0\) for the displayed
homogeneous three-site simplex integral. It excludes intersections with:

- soft support;
- the ten lower-sector linear letters;
- the frozen residue/coefficient discriminant union.

It does not classify generic multi-external-leg algebraic letters, integral
lattice extension, or an arbitrary nonhomogeneous specialization.

## Evidence

- entry 181 and
  `research/benincasa/q_sheet_resolution_result.json`;
- entry 183 and
  `research/benincasa/cyclic_q_assembly_result.json`;
- entry 211 and
  `research/benincasa/marici-gm/q-algebraic-kernel-certificate.json`;
- primary source
  `temp/arxiv-2408.16386-source/sections/applications.tex`,
  SHA-256
  `3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b`.

## Outcome contract

~~~json
{
  "objective": "Determine the intrinsic home of Q in the frozen homogeneous three-site one-loop coefficient system.",
  "status": "complete_generic_nonsoft_homogeneous_system",
  "algebraic_plane_Q_support": false,
  "other_rank7_blocks_Q_support": false,
  "discriminant_Q_support": false,
  "physical_chain_Q_support": false,
  "cross_sector_Q_extension": false,
  "T_Q": "identity",
  "N_Q": 0,
  "Var_Q_physical": 0,
  "classification": "apparent_cyclic_master_presentation_alphabet_data",
  "existing_carrier_sufficient": true,
  "new_carrier_datum": false,
  "scope": "generic nonsoft locus of the source-displayed homogeneous three-site simplex integral"
}
~~~
