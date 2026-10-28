# Retained projective correspondence transport

## Result

Constructed a provenance-preserving execution object for the existing source-defined four-point line packet. Exact tests cover all eighteen selected n=8 prefix instances from the three frozen fixtures. Nine products are rank two and nine rank one.

The retained object composes and preserves the original cross-ratio through singular outputs because it retains the original points. **The collapsed output, even together with the complete matrix and therefore its image/kernel, does not reconstruct that cross-ratio on the tested ambient linear-packet domain.** This distinguishes retained information from recovery of erased information.

Active SCC obligations: forward realization of retained matrix executions and comparison of three readouts. No native real-endpoint chart, continuum or AdS/dS identification is constructed.

## Execution object and composition

At the independently recomputed source fixture, retain

    (source_id, origin_points, tagged_steps, intermediate_outputs).

The source ID identifies n=8, history6 and the kinematic fixture shift; the pinned constructors and their localization checks specify the source reference. The four origin points are those already derived from Z5, Z6 and the two plane intersections. A step stores the actual selected history occurrence, factor position, endpoint labels, x-versus-adjugate constructor and its matrix. Both matrices and point representatives are immutable in the executable model.

For a row-point packet P and a tagged word w=(M1,...,Mr), append computes P M1,...,P M1...Mr while retaining P and the complete word. For words u,v,

    append(append(packet,u),v)=append(packet,u concatenated v).

The empty word is identity. These equations follow by induction from the append definition and associative matrix multiplication, without any inverse. The checker verifies every split of each actual two-factor prefix and three-piece concatenation with an explicit identity control. A one-step identity history and a two-step identity history have equal outputs but remain different execution objects.

Every actual selected prefix is used in its owning factor order and checked against the owning transport constructor. Arbitrary word concatenations form a **declared matrix-execution envelope**. This does not establish that arbitrary selected NNMHV histories are natively composable; a source continuation theorem would need its own domain checks. The common row action on all four line points is the declared comparison being tested, not an independently established native evolution of that entire twistor packet.

## Form law across all ranks

Let epsilon=[[0,1],[-1,0]]. Symbolic polynomial expansion gives, for every real 2-by-2 matrix M,

    M epsilon M^T = det(M) epsilon.

Multiplication by i gives the corresponding Hermitian J0 law. The identity composes since determinants multiply, including when the product is zero. All actual factors and products satisfy it exactly.

At rank two, determinant factors cancel in the four-point cross-ratio. At rank one the alternating pairing vanishes on the image; no inverse or nondegenerate cross-ratio is assigned. Negative determinant remains a separate status: an explicit diag(-1,1) control preserves cross-ratio but reverses real projective orientation and is not positive-determinant PSL normalization.

This universal matrix identity is not a derivation of a preferred spacetime metric or of the source's real form beyond the supplied real fixtures.

## Three readouts

| Readout | What it keeps | Cross-ratio recovery |
|---|---|---|
| Final point packet | Transformed representatives; projective classes only for nonzero vectors | Preserved on the rank-two tested action; undefined after rank-one collapse |
| Final packet plus matrix/image/kernel | Full applied map and its linear incidence data | Still insufficient on the ambient linear-packet domain |
| Retained execution | Original source points, tags, every intermediate output and source binding | Original cross-ratio recoverable directly from the retained origin |

For every tested rank-one product M, the checker takes a nonzero row k with kM=0, changes one origin point P_j to P_j+t k and keeps the same matrix. It finds a value of t for which all four rival projective points remain distinct and their cross-ratio changes, while **all four affine outputs remain exactly equal**. The matrix, kernel and image are unchanged. Nine exact witnesses are stored in the receipt.

These kernel-perturbed rivals are valid ambient row-point packets, not claimed reconstructions of alternative native momentum-twistor kinematics. Consequently the counterexample refutes unrestricted linear-packet recovery; it does not exclude recovery on a separately proved smaller native image. The prior three-kinematics fixed-record counterexample remains the source-specific obstruction to forgetting kinematics.

## Zero products and guards

The declared control A=diag(1,0), B=diag(0,1) has two nonzero factors and AB=0. It is not asserted to be an actual source prefix. The execution retains its input and steps, but reports no projective matrix class, four zero output vectors and no cross-ratio. Thus the implementation uses affine matrices including zero, not an incorrectly total product on nonzero projective classes.

Validation recomputes the expected source packet and ordered factor word. Changes to source ID, origin representative, factor, factor order, occurrence tag or intermediate output are rejected. A legitimate change of source frame would require a corresponding comparison, not silently editing a packet bound to fixed source representatives. Keeping input provenance does not authorize arbitrary target operations or prove they preserve the source image.

## Verification and remaining gap

    python research/nima/checkers/check_retained_projective_correspondence.py

Receipt: `results/retained-projective-correspondence.json`. The exact checker passes eighteen source-prefix cases, nine nondegenerate kernel-collision witnesses, the symbolic form identity, zero/negative-determinant controls, composition and record-corruption tests. Inputs are hash-checked before and after execution. Prior owner artifacts are not rewritten.

The result supplies a precise richer carrier capable of retaining projective information alongside rank loss. To connect it to interval geometry, one must still construct a source-compatible real ordered endpoint comparison and show how it respects the retained data and singular domains. Merely storing the input makes preservation possible; it does not itself explain the projective endpoint geometry.
