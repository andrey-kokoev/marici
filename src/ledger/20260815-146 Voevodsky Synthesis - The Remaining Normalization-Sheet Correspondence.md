# Voevodsky Synthesis: The Remaining Normalization-Sheet Correspondence

## Record

Date: 2026-08-15

Author: marici.Voevodsky

Status: research-direction synthesis from entries 138--143. This entry adds no
new existence theorem. It records the strongest jointly warranted formulation,
the unique remaining blocker, and its falsification test.

## Synthesis

The six-point NLSM primitive is no longer missing an endpoint object, a road
carrier, a target Cousin complex, or a group-cohomological obstruction theory.
Those pieces are now fixed.

The road-side endpoint object is

\[
\mathcal E_{\partial,Q}^{\rm abs}=F_K/F_V,
\qquad
0\to F_B/F_V\to F_K/F_V\to Q\to0,
\]

and entry 143 constructs its target-side extended Cousin realization

\[
\mathcal E_{\partial,Q}^{\rm BM,\check C}.
\]

The coefficient comparison is the degree-correct derived pullback of entry
142, not the degree-three splice of the conductor extension with the complete
Tate extension. Its only integral homology is the primitive line

\[
H_1(C_{\partial}^{\rm coeff})\simeq\mathbb Z_{\rm or},
\]

which becomes the trivial physical line after the once-relative polarity
twist. The absence of a strict equivariant section is therefore not a defect
of the derived object: demanding such a section is exactly what introduces
the illicit factors \(1/2\) and \(1/3\).

Entries 138--141 further show that polarity loading converts the residual
endpoint defect into a binary existence obstruction

\[
\omega_{\rm load}
=\partial_{\rm pol}(p_{\partial,Q})
\in H^2(D_3;\mathbb Z)\simeq\mathbb Z/2.
\]

Restriction to the physical reflection detects this class, and entry 140
proves that the target purity packet has reflection square \(+1\). Hence any
nontrivial obstruction comes entirely from the normalization-sheet/endpoint
comparison.

## Refined meaning of the primitive

The candidate \(\mathsf J\) should therefore not be described as an ordinary
function extracted from the scalar amplitude. At six points its presently
defensible form is a derived correspondence between two independently
constructed self-factorizing carriers:

\[
\boxed{
\mathsf J_{6,+}^{\rm cand}
=
\operatorname{DPB}
\left(
\mathcal S_{\rm sh}^{\rm norm,reg}
\xrightarrow{\alpha_{\rm sh}^{!,\check C}}
\mathbb D_{\rm supp}
(\mathcal E_{\partial,Q}^{\rm BM,\check C})\otimes\chi_N
\xleftarrow{\mathbb D(\iota_{\rm road}^{\check C})}
\mathbb D_{\rm supp}((F_B/F_V)^{\rm BM,\check C})\otimes\chi_N
\right).
}
\]

Here `DPB` denotes the correctly typed derived pullback/butterfly after its two
endpoint connector 2-cells have been constructed. This formula is a target
theorem, not a definition by desired output.

The only missing datum is

\[
\boxed{
\alpha_{\rm sh}^{!,\check C}:
\mathcal S_{\rm sh}^{\rm norm,reg}
\longrightarrow
\mathbb D_{\rm supp}
(\mathcal E_{\partial,Q}^{\rm BM,\check C})\otimes\chi_N
}
\]

together with the two endpoint comparison 2-cells. They must be derived from
normalization--conductor geometry, not selected by choosing the desired
reflection parity.

## Mandatory test order

Keep the target object, its filtration, and the road inclusion fixed. Then:

1. construct the full normalization--Cech bivariant kernel and both endpoint
   connector cells;
2. form the filtered derived pullback;
3. forget endpoint/support framing and verify the required contraction;
4. compute integral rank and torsion before normalization;
5. only afterward evaluate the conductor grade, the based nonzero \(Q\)-leg,
   the \(x_3\) purity residue, and reflection parity;
6. apply the proved conductor Bockstein to determine \(\omega_{\rm load}\).

No additional target complex, road module, residue convention, blowup, or
group-cohomology computation is presently justified.

## Falsification trichotomy

The experiment has three admissible outcomes:

- a zero spatial derived pullback falsifies the proposed local scalar
  synthesis;
- one primitive torsion-free line proves uniqueness up to orientation and
  reduces existence to the computed reflection parity;
- higher rank or torsion proves that another coherence datum is missing.

Even in the favorable case, this closes only the six-point positive-sheet
primitive. Rotation, the negative sheet, Cut naturality, all-multiplicity
factorization, and the CHY identification remain downstream obligations.

## Outcome contract

~~~json
{
  "claim": "Entries 138--143 reduce the six-point positive-sheet NLSM half-object problem to one support-typed mixed-variance normalization-sheet correspondence and its two endpoint connector cells. The road-side endpoint/Q object, target Cousin realization, coefficient derived pullback, target reflection square, and obstruction transgression are already fixed.",
  "status": "conditional",
  "assumptions": [
    "The exact results and scopes of entries 138--143 are retained without promoting carrier or coefficient statements to a spatial correspondence.",
    "The target object E_{partial,Q}^{BM,Cech}, its filtration, and the road inclusion are held fixed.",
    "The missing source arrow and endpoint 2-cells must be derived independently of the desired rank, residue, Q-leg, and reflection parity."
  ],
  "evidence_refs": [
    "ledger entries 138--143",
    "research/voevodsky/check_conductor_road_endpoint_pullback.rs",
    "research/voevodsky/check_two_endpoint_tate_carrier.rs",
    "research/voevodsky/check_global_k6_koszul_cech_promotion.rs"
  ],
  "factorization_test": {
    "construction": "Build alpha_sh^{!,Cech} and both endpoint connector 2-cells, then form the filtered derived pullback.",
    "ablation": "Forgetting endpoint/support framing must contract the extraordinary contribution.",
    "integral_verdict": "Compute rank and torsion before evaluating prescribed shadows.",
    "posthoc_shadows": ["conductor associated grade", "based nonzero Q-leg", "x3 edge purity", "physical-reflection parity"]
  },
  "counterevidence": [
    "A zero spatial derived pullback falsifies the local synthesis.",
    "Higher rank or torsion shows that the stated geometry is insufficient.",
    "A construction requiring a chosen reflection cochain, division by 2 or 3, or modification of the target differential is circular."
  ],
  "next_experiment": "Construct only the reciprocal normalization-sheet bivariant kernel into the fixed supported dual endpoint/Q Cousin object and derive its two endpoint connector cells; then run the forgetting ablation and integral Hom computation before reading physical shadows."
}
~~~
