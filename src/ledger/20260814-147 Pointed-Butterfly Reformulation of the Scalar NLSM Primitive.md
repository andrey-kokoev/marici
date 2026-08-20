# Pointed-Butterfly Reformulation of the Scalar NLSM Primitive

## Record

Date: 2026-08-14

Author: marici.Scholze

Status: synthesis and formula objective. This entry records the conceptual
consequence of entries 110--136. It introduces no new proof.

## Revised object

The accumulated six-point evidence no longer supports treating the intrinsic
NLSM primitive as an ordinary scalar function, subcomplex, strict projection,
or unframed degree-one extension class. The strongest defensible formulation is

\[
\boxed{
\mathsf J
=
\text{a loaded, endpoint-pointed, factorization-coherent butterfly}
}
\]

between the scalar support/Yoneda two-extension and the scalar
PL--Tate/Cartier two-extension.

Before physical loading, the carrier comparison is the canonical roof

\[
\mathcal R_{\rm AD}^{\rm car}:
\qquad
U\xleftarrow[\sim]{g_{\rm cap}}C_{\rm tag}
\xrightarrow{m}T,
\qquad
m_1=R-R^2.
\]

The physical half-object is conjecturally obtained by equipping this roof with
endpoint connector 2-cells and then loading the same pointed object with
occurrence, multi-Rees, positive-support, reciprocal/Borel--Moore,
PC/Cousin, polarity, determinant, and physical-normal data.

## Why this reformulation is forced

Four exact results delimit the possible object.

1. The unrestricted common-ring target is integrally and
   \(D_3\)-equivariantly contractible. Therefore ordinary coefficientwise Hom
   has zero cohomology. Any viable class must retain support, the based
   \(Q\)-leg, endpoint recollement, and extraordinary variance.

2. A comparison of two fixed two-extensions is a path object. Existence is
   controlled by their difference in \(\operatorname{Ext}^2\); once nonempty,
   choices form an \(\operatorname{Ext}^1\)-torsor. An Ext-one group alone is
   not the primitive.

3. At carrier level the Ext-two obstruction vanishes. The lift space is
   nonempty and its components form an unpointed \(\mathbb Z/2\) torsor.

4. The minimal strict Alexander projection is obstructed modulo three, while
   the full augmented cone has an integral affine rank-nine family of strict
   lifts. Relative AW/cap geometry canonically determines the common derived
   roof, but selects no member of that strict family.

Consequently neither a direct strict projection nor an arbitrary full-cone
lift is intrinsic. The missing datum is a coherent pointing of the canonical
roof.

## Immediate theorem objective

Construct

\[
\boxed{
\widehat{\mathcal R}_{\rm AD}^{\rm car}
\in
\operatorname{Lift}_{\operatorname{Arr}^2_{D_3}}
\left(
\mathcal R_{\rm AD}^{\rm car};
\mathbb E_F,\mathbb E_\triangle
\right)
}
\]

as a pointed butterfly with:

- endpoint identities represented by connector homotopies rather than a
  strict degree-zero inverse;
- both cone-connector coherence equations;
- integral \(D_3\)-equivariance;
- no inversion of three;
- a derived, rather than imposed, reflection parity.

Only after this carrier pointing is constructed should it be loaded and the
physical shadows evaluated:

\[
\operatorname{gr}_{\mathfrak c}^1G
=K_{\rm alt}\otimes L_{\rm pol},
\qquad
\operatorname{gr}_Q(\rho_G)(N_{\rm road})
=+[q_\Sigma],
\qquad
\operatorname{Res}_{x_3}G
=\operatorname{pur}_{x_3,\partial}^{\rm PC}.
\]

These are tests of the loaded pointing, not inputs defining it.

## Falsification boundary

The reformulation fails in its present form if any of the following occurs:

- no integral endpoint-compatible \(D_3\)-equivariant butterfly exists over
  the canonical roof;
- every pointing requires division by three;
- the two connector coherences cannot be satisfied simultaneously;
- loading destroys the carrier comparison or produces a nonzero loaded
  Ext-two obstruction;
- the resulting endpoint realization fails the already proved Cartier
  purity, marked \(Q\)-leg, or conductor/Tate shadows;
- the pointed system fails physical Cut naturality after rotation and
  assembly.

A noncanonical rank-nine strict lift is not evidence for the conjecture. A
valid result must derive its pointing from scalar geometry.

## Research order

1. Construct the integral endpoint connector on the canonical carrier roof.
2. Compute its \(\mathbb Z/2\) reflection class.
3. Establish uniqueness in the pointed two-extension category.
4. Load that same butterfly with occurrence, multi-Rees, support, and
   PC/Cousin data.
5. Compute the loaded Ext-two obstruction before imposing physical outputs.
6. Assemble both endpoints and rotate through \(D_3\).
7. Test Cut naturality at eight points.
8. Only then identify the global system with
   \((\operatorname{Pf}'A)^2\) in CHY cohomology.

## Conceptual consequence

The compact expression

\[
I_{\rm scalar}^{-1}\operatorname{gr}_R A_{\rm scalar}
\]

should now be read as decategorified notation for an extraordinary
realization of a pointed scalar two-extension. The scalar master appears to
create the NLSM primitive not by selecting a component of an amplitude, but
by supplying a derived comparison whose support and endpoint coherences make
factorization meaningful.

## Dependencies

- entry 110: local rank jump as Cartier/Bockstein;
- entry 115: PL--Tate and multi-Rees Cartier bicomplex;
- entry 118: marked endpoint-relative carrier;
- entry 131: scoped PC edge purity;
- entry 133: ordinary-derived ablation;
- entry 134: lift-space theorem;
- entry 135: strict projection no-go and full-cone lift lattice;
- entry 136: canonical AW/cap roof and endpoint-connector gap.

## Outcome contract

~~~json
{
  "claim": "The strongest current formulation of the intrinsic NLSM primitive is a loaded, endpoint-pointed, factorization-coherent butterfly between the scalar support/Yoneda and PL-Tate/Cartier two-extensions; the immediate open theorem is the integral D3-equivariant endpoint pointing of the canonical AW/cap carrier roof.",
  "status": "conditional",
  "assumptions": [
    "Entries 110--136 retain their stated scopes and typings.",
    "The carrier roof of entry 136 is the object to be pointed rather than replaced by an arbitrary strict full-cone lift.",
    "Physical loading is performed only after the carrier pointing is constructed.",
    "The conductor, Q-leg, and residue shadows are evaluations rather than defining constraints."
  ],
  "evidence_refs": [
    "src/ledger/20260814-133 Ordinary-Derived Ablation and the Framed Off-Diagonal Objective.md",
    "src/ledger/20260814-134 Framed Lift-Space Theorem and the Relative AW Reference-Lift Gap.md",
    "src/ledger/20260814-135 Strict Alexander Projection No-Go and the Integral Butterfly Objective.md",
    "src/ledger/20260814-136 Canonical AW-Cap Roof and the Endpoint-Connector Gap.md"
  ],
  "factorization_test": {
    "ordinary_Hom": "acyclic",
    "carrier_Ext2_obstruction": "zero",
    "carrier_lift_components": "nonempty Z/2 torsor",
    "minimal_strict_projection": "obstructed modulo 3",
    "full_cone_strict_lifts": "integral affine rank 9",
    "canonical_carrier_roof": "proved",
    "endpoint_pointing": "open",
    "loaded_Ext2_obstruction": "undefined",
    "eight_point_Cut_naturality": "deferred"
  },
  "counterevidence": [
    "AW/cap geometry does not select a point in the affine rank-nine strict lift lattice.",
    "A strict endpoint identity would require 3k=1.",
    "The ordinary contraction removes every unframed coefficientwise extension.",
    "No loaded pointed butterfly has yet been constructed."
  ],
  "next_experiment": "Construct endpoint-compatible D3 connector 2-cells over the canonical AW/cap roof, compute the reflection class, and prove the two connector coherences integrally before adding any physical loading."
}
~~~
