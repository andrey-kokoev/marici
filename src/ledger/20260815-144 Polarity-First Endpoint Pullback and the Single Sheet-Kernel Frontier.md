# Polarity-First Endpoint Pullback and the Single Sheet-Kernel Frontier

## Record

Date: 2026-08-15

Author: marici.Scholze

Status: synthesis and revised formula objective. This entry records the
conceptual consequence of entries 138--143. It introduces no new proof.

This entry supersedes one ordering statement in entry 147. The physical
polarity line should be loaded before choosing a carrier pointing. It does
not supersede entry 147's pointed-butterfly interpretation.

## Revised construction order

The carrier comparison has an unpointed \(\mathbb Z/2\)-torsor of lifts.
Loading the road-orientation comparison relatively by the polarity line once
changes its coefficient character from the sign line to the trivial line:

\[
\chi_{\rm or}\chi_{\rm pol}=1.
\]

Consequently

\[
H^1(D_3;\mathbb Z)=0,
\qquad
H^2(D_3;\mathbb Z)=\mathbb Z/2.
\]

Thus the correct order is

\[
\boxed{
\text{canonical carrier roof}
\longrightarrow
\text{relative polarity loading}
\longrightarrow
\text{binary existence test}
\longrightarrow
\text{unique pointing if it exists}.
}
\]

The loaded obstruction has only two outcomes:

\[
\omega_{\rm load}=0
\Longrightarrow
\pi_0\operatorname{Lift}_{\rm load}
\text{ is a singleton},
\]

\[
\omega_{\rm load}=1
\Longrightarrow
\operatorname{Lift}_{\rm load}=\varnothing.
\]

There is no remaining loaded choice once existence is proved.

## Reflection and Bockstein reduction

Restriction to the physical \(D03\) reflection subgroup detects the complete
loaded obstruction:

\[
H^2(D_3;\mathbb Z)
\xrightarrow{\sim}
H^2(\langle f_3\rangle;\mathbb Z)
\simeq\mathbb Z/2.
\]

Therefore

\[
\omega_{\rm load}=0
\quad\Longleftrightarrow\quad
\omega_{\rm load}(f_3,f_3)=0\pmod2.
\]

The established target edge-purity packet is strictly natural under
\(f_3:x_3\leftrightarrow x_4\), retains both Tor grades and all lower
Koszul--Cech terms, and has target reflection square \(+1\). Any nontrivial
defect must therefore arise on the normalization-sheet/source side.

The normalization--conductor sequence

\[
0\longrightarrow\mathbb Z
\longrightarrow P_{\rm sh}
\longrightarrow\mathbb Z_{\rm or}
\longrightarrow0
\]

has Bockstein

\[
\partial_{\rm pol}:
H^1(D_3;\mathbb Z_{\rm or})
\xrightarrow{\sim}
H^2(D_3;\mathbb Z).
\]

Hence the obstruction is the transgression of one endpoint-defect parity:

\[
\boxed{
\omega_{\rm load}
=
\partial_{\rm pol}(p_{\partial,Q}).
}
\]

The next calculation is therefore not a global group-cohomology search. It
is the construction and evaluation of one \(f_3\)-paired endpoint/\(Q\)
source connector.

## Degree-correct primitive carrier

The conductor one-extension must not be spliced with the full Tate
two-extension: that produces an \(\operatorname{Ext}^3\) object. The
degree-correct coefficient object is the derived pullback over the common
endpoint-orientation quotient:

\[
C_{\partial}^{\rm coeff}
=
\operatorname{Fib}
\left(
P_{\rm sh}\oplus P_{\rm road}^{\rm or}
\longrightarrow
\mathbb Z_{\rm or}
\right).
\]

It is an integral strict \(D_3\)-complex with

\[
H_1(C_{\partial}^{\rm coeff})\simeq\mathbb Z_{\rm or},
\qquad
H_i=0\quad(i\ne1),
\]

and no torsion. After the once-relative polarity twist, its primitive line is
trivial. No division by two or three is required.

There is no strict integral equivariant section of this primitive quotient:
such a section would require both \(2a=1\) and \(3c=1\). This is evidence for
the derived pullback, not an obstruction to it.

## Spatial and target-side closure

The actual labelled scalar triple

\[
V=\{v_+,v_-\}
\subset B_{\rm short}
\subset K_6
\]

realizes the road-side endpoint carrier. The established original-twist
support complex restricts to

\[
F_V\subset F_B\subset F_K
\]

and defines the canonical endpoint/\(Q\) object

\[
\mathcal E_{\partial,Q}^{\rm abs}=F_K/F_V
\]

with filtration

\[
0\longrightarrow F_B/F_V
\longrightarrow F_K/F_V
\longrightarrow Q=F_K/F_B
\longrightarrow0.
\]

The seven-generator \(Q\) quotient retains the top cell and physical
long-facet normal states. Thus the generic \(Q\)-leg is not lost.

The global Borel--Moore target-side Cech realization is also fixed:

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C}
=
\bigoplus_{(S,H)\notin F_V}
R[X][u_a^{-1}:a\in S\setminus H]\,[S,H],
\]

with canonical diagonal comparison

\[
\kappa[S,H]
=
\prod_{a\in S\setminus H}u_a^{-1}[S,H]_{\check C},
\qquad
d_{\check C}\kappa=\kappa d_{\rm abs}.
\]

Accordingly, neither another endpoint object nor another target Cech complex
should be constructed.

## Single remaining blocker

The unresolved datum is the mixed-variance normalization-sheet kernel

\[
\boxed{
\alpha_{\rm sh}^{!,\check C}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\longrightarrow
\mathbb D_{\rm supp}
\left(
\mathcal E_{\partial,Q}^{\rm BM,\check C}
\right)
\otimes\chi_N
}
\]

together with the two endpoint comparison 2-cells that make it and the fixed
road inclusion into a pointed butterfly.

It must be derived from normalization--conductor geometry and must retain:

- both normalization sheets and their conductor difference;
- the based nonzero \(q_\Sigma\) leg;
- the two endpoint connectors;
- reciprocal-regular/Borel--Moore variance;
- occurrence and independent multi-Rees filtrations;
- both repeated-normal Tor grades;
- the established \(x_3/x_4\) edge purity and physical normal.

The current local primitive is therefore conditionally

\[
\boxed{
\mathsf J_{\rm local}
=
\operatorname{Pullback}^{\rm der}
\left(
\alpha_{\rm sh}^{!,\check C},
\iota_{\rm road}^{\check C}
\right),
}
\]

provided its reflection defect vanishes.

## Falsification boundary

The synthesis fails locally if:

- no support-typed mixed-variance kernel
  \(\alpha_{\rm sh}^{!,\check C}\) exists;
- the two endpoint connector equations are incompatible;
- the derived pullback is zero after retaining the prescribed support data;
- the reflection defect is odd, so
  \(p_{\partial,Q}=1\) and \(\omega_{\rm load}\ne0\);
- the resulting class fails the independently proved \(Q\)-leg, conductor,
  or edge-purity shadows;
- it survives the ordinary-forgetting ablation of entry 133 as a nontrivial
  unframed coefficient class;
- it fails physical Cut/Beck--Chevalley naturality after assembly.

A rank-one answer is credible only if it is produced before imposing
\(K_{\rm alt}\), \(q_\Sigma\), the residue, or the desired parity.

## Immediate research order

1. Keep
   \(\mathcal E_{\partial,Q}^{\rm BM,\check C}\),
   its filtered \(Q\)-quotient, and the road inclusion fixed.
2. Construct only
   \(\alpha_{\rm sh}^{!,\check C}\) and its two endpoint connector cells.
3. Form the filtered derived pullback.
4. Verify the mandatory ordinary-forgetting contraction.
5. Compute integral rank and torsion.
6. Read the reflection parity and apply the proved conductor Bockstein.
7. Only afterward evaluate the conductor, \(q_\Sigma\), and edge-purity
   shadows.
8. If the unique loaded lift exists, test eight-point Cut naturality.
9. Defer the CHY identification until that test succeeds.

## Outcome contract

~~~json
{
  "claim": "After entries 138-143, the local intrinsic NLSM primitive is most sharply formulated as the derived pullback of a still-missing reciprocal normalization-sheet kernel and a fixed road inclusion into the now-constructed endpoint/Q BM-Cech target. Relative polarity loading must occur before pointing; it converts the carrier ambiguity into a binary existence obstruction detected by one D03 reflection square and equal to the conductor Bockstein of the endpoint/Q defect parity.",
  "status": "conditional",
  "assumptions": [
    "The polarity line occurs relatively exactly once.",
    "The target reflection naturality and conductor Bockstein retain their proved scopes.",
    "The endpoint/Q target, its filtration, and its Cech promotion are fixed as in entry 143.",
    "No desired boundary value or parity is used to construct the missing source kernel."
  ],
  "evidence_refs": [
    "src/ledger/20260814-138 Physical Polarity Loading and the Shifted Butterfly Obstruction.md",
    "src/ledger/20260814-139 Reflection Detection of the Loaded Butterfly Obstruction.md",
    "src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md",
    "src/ledger/20260814-141 Conductor Bockstein Transgression and the Endpoint-Defect Reduction.md",
    "src/ledger/20260815-142 Unsplit Conductor-Road Endpoint Pullback and the Spatial Realization Blocker.md",
    "src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md"
  ],
  "factorization_test": {
    "loaded_H1": "zero",
    "loaded_H2": "Z/2",
    "reflection_detection": "isomorphism on H2",
    "target_reflection_square": "+1",
    "conductor_Bockstein": "isomorphism Z/2 to Z/2",
    "coefficient_endpoint_pullback": "primitive H1=Z_or, no torsion",
    "endpoint_Q_target": "constructed with nonzero seven-generator Q quotient",
    "target_BM_Cech_promotion": "constructed",
    "normalization_sheet_kernel": "unconstructed",
    "endpoint_connectors": "unconstructed",
    "loaded_obstruction_value": "undecided"
  },
  "counterevidence": [
    "Strict equivariant sections require division by two and three.",
    "Target-side closure alone cannot decide the source endpoint parity.",
    "Finite Verdier duality reverses the road arrow and does not construct the mixed-variance cospan.",
    "No d_sp,sc, full G03 Cousin map, or Cut-natural half-object has yet been constructed."
  ],
  "next_experiment": "Construct alpha_sh^{!,Cech} and its two endpoint connector cells against the fixed endpoint/Q BM-Cech target, perform the ordinary-forgetting ablation, and only then compute rank, torsion, reflection parity, and physical shadows."
}
~~~
