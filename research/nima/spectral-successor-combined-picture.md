# Corrected combined picture: retained spectral decomposition and its observation

## Correction of the previous account

The earlier version incorrectly called 3 channels x 9 occurrence pairs a lossless 27-dimensional successor and claimed its endpoint/admission contract was established. It also relied on weights computed from absolute real parts rather than the declared Hermitian norm. Those claims are withdrawn.

The exact reconstruction audit below replaces that account. It concerns a declared coefficient representation; it does not select a physical or native tower successor.

## Carrier and complete spectral view

Keep the two distinct ordered occurrence spaces

    V_left: (AB, BC, CA), V_right: (BA, AD, DB).

Their complex tensor coefficient space V_left tensor V_right has dimension NINE, with nine labelled occurrence-pair basis vectors. The existing triangle spectral projectors give nine rank-one operators

    P_(lambda,mu) = E_left,lambda tensor E_right,mu.

They are Hermitian, pairwise orthogonal, and sum to the identity. Therefore, for EVERY coefficient state v,

    v = sum_(lambda,mu) P_(lambda,mu) v,
    ||v||^2 = sum_(lambda,mu) ||P_(lambda,mu) v||^2.

All nine complex components, with their channel labels, constitute a reversible spectral presentation of the coefficient state. The original occurrence manifests and registered history windows remain separate required provenance.

## The three-channel view is a restriction

Define

    D = sum_lambda P_(lambda,lambda), R = I-D.

D has rank three; R has rank six; their images are orthogonal. For any state,

    v = Dv + Rv.

The three same-mode channels alone reconstruct only states already in im(D). They do NOT provide another complete presentation of an unrestricted occurrence-pair state.

For every unit occurrence-pair basis vector, each of the nine spectral components has squared norm 1/9. Hence the three same-mode components retain 1/3, and the six cross-mode components retain 2/3. These fractions are basis-fixture results, not universal retention fractions for arbitrary states. A pure cross-mode state is entirely invisible to D; a same-mode state is retained completely.

The single-occurrence squared weight is 1/3 in each local mode, not the previously reported 3/7,2/7,2/7. Common and complex modes have equal pair intensities here. Their complex components still differ; intensities erase phase information.

## What many:many can legitimately mean

There is a useful joint incidence display linking occurrence-pair labels and spectral-channel labels. Every occurrence-pair basis vector has support in every mode-pair channel.

| Display | Association slots | Independent coefficient dimensions represented |
|---|---:|---:|
|Nine pair labels x three same-mode channels|27|3-dimensional selected image, not full input|
|Nine pair labels x nine mode-pair channels|81|9-dimensional full input|

Association counts are not new degrees of freedom. Nor does having all pair labels in a display mean that their arbitrary amplitudes can be recovered after spectral restriction.

Thus the productive combined packet is:

    complete parent histories + occurrence manifest
      + same-mode components + cross-mode residual components.

An observer may expose only the three-channel part while the record retains the residual. The complete spectral view and occurrence-coefficient view then have a checked reconstruction bridge. Arbitrary summaries/intensity tables do not.

## Follow-up: operation closure

`spectral-visible-closure-under-existing-controls.md` tests whether residuals can feed back into the visible sector. For local slot cycles, short half-phases and seed-symmetry exchange, exact checks give DTR=RTD=0. Thus visible predictions close under their compositions, while the residual evolves separately and must remain recoverable. This does not establish closure under an unspecified next-rung successor; the existing record constructors have no supplied linear action on this nine-dimensional carrier.

## Conditional bridge to a successor

`spectral-independent-successor-bridge.md` now connects the complete retained packet to the existing independent-family comparison constructor under an explicit bilinear coefficient adapter. Its actual output has 81 four-occurrence coordinates, not an unchanged nine-dimensional carrier. The reconstruction/comparison square commutes. Unit-mass aggregate means ignore the input cross-mode residuals; target-family means detect them in this singleton-family fixture. Both complete parents remain retained because product values alone do not recover them. The follow-up endpoint-composition filter admits nine of those 81 candidates while retaining the other 72. Its reconstruction square also commutes, but the SAME fixed-measure aggregate now detects a residual-residual contribution: a checked pair of equal-visible inputs gives 1/81 versus 1/243. Thus aggregate closure depends on the operation's incidence as well as the reader. The contextual-observation extension now identifies exactly what must be retained for each probe interface: same-mode probes give rank three and kernel im(R); all nine occurrence probes give rank nine and recover the complete coefficient state via the ordered decoder 81 M. Residual probes separately give rank six. These are conditional complex-amplitude interfaces, not supplied physical preparations; histories remain a separate retention channel. This pilot does not select the source's intended generator or physical reader.

## Structural synthesis: invariant sector versus lossy projection

`spectral-invariant-graded-path-algebra.md` identifies D exactly as the average of the relative rotation G=C_left tensor C_right^-1. Its three size-three occurrence-pair orbits provide real orbit coordinates for the same invariant space; these orbits are not eigenmode-labelled partitions.

With actual path length retained, endpoint composition in the declared two-context product model is (x_m*y_n)(i,j)=x(i,j)y(i+m,j+m), at grade m+n. Invariant inputs close under this associative graded product. However D(x*y)=Dx*Dy+D(Rx*Ry), and the last term can be nonzero. Therefore the invariant sector is a subalgebra, not a lossless algebra quotient of arbitrary inputs. Three coefficients per grade suffice only under an invariant-input contract; general inputs still require retained residuals. Coefficient periodicity never erases path histories.

## Compatibility with the source seam

The reciprocal-pair extraction singles out (AB,BA) without amplitudes. Relative rotation moves it to (CA,AD) and (BC,DB), neither reciprocal; the genuine seed symmetry instead preserves it. A conditional seam-coordinate reader does not factor through D on arbitrary inputs. The existing joined aggregate with a seam-addressed probe also distinguishes equal-D states (1/81 versus 1/243). Marker metadata remains recoverable, but is not a substitute for the missing coefficient response. Invariant preparations remain consistent and can read their seam coordinate; the restriction must not be silently extended to arbitrary states or asserted to be physically selected.

## Minimal seam-compatible refinement

`seam-respecting-minimal-interface.md` completes the observation audit. Starting with D plus the source seam-coordinate reader, joint cyclic advancement and the genuine seed symmetry generate exactly a rank-six observation space. Its minimal linear summary is P=(I+W)/2, with an explicit six-reading decoder. Static D plus seam has rank four; independent left/right advancement expands the interface to rank nine. These dimensions are not tower rungs.

The six-sector is closed for symmetric preparations under graded composition, but arbitrary antisymmetric residuals can jointly produce symmetric output. Therefore this completion is minimal for the specified joint CONTROL/READOUT interface, not an unconditional replacement for all binary contexts. Remaining residuals and histories must be retained as required by the actual permitted operations.

## Executable retained correction law

The six-plus-three split now has a checked successor implementation in `seam-respecting-minimal-interface.md`. For symmetric s and antisymmetric a, the existing graded product gives s_out=s1*s2+a1*a2 and a_out=s1*a2+a1*s2, with all length shifts included. This reconstructs the full nine-coordinate packet and retained parent tree exactly.

The a1*a2 correction spans the three symmetric off-diagonal directions: it changes the D-orbit means but not the three diagonal seam readings. This concerns the three-dimensional Q-residual, not the earlier six-dimensional R-residual. No new coupling parameter or physical law is introduced.

## Structural-dependence control: ungluing the seam

`seed-seam-ungluing-control.md` splits the shared vertex identities while keeping occurrence IDs, local cycles, coefficient preparations and address readers fixed. The spectral algebra, product-category matching and six-plus-three correction remain unchanged. The reciprocal source seam disappears, however, and graph automorphisms increase from 2 to 18. The tracked role exchange remains available but is no longer uniquely singled out by the graph.

Thus the present construction supplies a generic two-cycle response algebra plus a genuinely source-dependent reference selection. It does not yet supply a rule making the shared seam generate a different coefficient response. An unavailable reciprocal-reference query is not assigned zero response or silently replaced by a chosen marker.

## Source-domain correction: allow cross-triangle continuation

`glued-seed-path-spectral-bridge.md` now uses the actual endpoint-matched path composer on the six arrows rather than the context-separated tensor product. The glued seed admits ten two-step words; ungluing leaves six. The four added words are AB BA, BA AB, CA AD and DB BC. They are composites with retained parents, not new primitive edges or inverse laws.

The appropriate coefficient bridge is SIX-dimensional local direct-sum input to TEN-dimensional length-two path output. All six local modes reconstruct it exactly when all spectral operand pairs are retained. Same-context-only and same-mode-only truncations fail. The old three-slot triangle promotion rejects these outputs, so a closed spectral successor is not claimed. This establishes source-incidence dependence of available composition without assigning a physical interaction law.

## Bridge to the existing whole-seed spectrum

`whole-seed-occurrence-spectrum-bridge.md` factors the actual six-occurrence incoming continuation K through the four-vertex incidence M already checked in prior research: K=BH, M=HB. The four nonzero spectral modes lift exactly, while two zero-sector contrasts (CA-BA and AB-DB) must be retained for complete occurrence-coefficient recovery. The split is oblique, not a norm-preserving spectral decomposition in the old counting metric.

All ten labelled two-step records remain separate provenance. Every isolated local triangle mode mixes under the glued K; each reaches all three modes of the other triangle. These are exact incidence-representation results, not a chosen physical clock, conserved energy or inferred finite raw-operator return.

## Source-indexed observation versus actual erasure

The whole-seed bridge now tests O(x)=(H S_v x)_v using existing source families. O has rank six and an explicit decoder on this six-arrow registry; it sees both zero-sector contrasts hidden by H. Forgetting the source index recovers H exactly. But O K still has rank four and annihilates those contrasts: reading retained inputs at finer resolution is not reversing K after it has been applied.

Thus the spectral four-plus-two split belongs to a particular operator/coarse reading, not an intrinsic limit on observation of the retained seed. Endpoint-cell recovery also fails if distinct primitive occurrences share endpoints, as checked by a parallel-occurrence control. History and identity records remain necessary.

## Lossless retained construction and its coarse summary

`retained-path-extension-and-coarse-summary.md` factors K=A L. The six-to-ten retained extension L is injective with an exact image decoder; final-occurrence aggregation A kills the two contrast directions that L preserves as distinct words. Repeated extension through length six retains 68 possible words and commutes with the K summary at every step. The lift from primitive coefficients remains rank six; the summarized response is rank four after the first extension.

This separates growing, prefix-retaining construction from a fixed coarse spectral operator. The lift does not conserve the counting norm, does not generate arbitrary independent path amplitudes and does not assert an execution schedule.

## Registered retained-successor interface

`retained-successor-interface.md` packages the pieces in `checkers/retained_path_successor.py`: identity-bound path stages and indexed families, composable lifts/decoders, coarse summaries and inherited spectral windows. Integration checks cover stages through length four, including arbitrary intermediate payloads, provenance deconstruction and hostile registration/scope controls; the prior length-six closure is rerun.

Inherited projectors are L_n E D_n. Their sum is the origin-image projector L_n D_n, not the ambient identity. Off-origin payloads may be extended and decoded as path coefficients but are rejected as inherited spectral inputs. This is a finite retained-construction interface, not a replacement for the native triangle promotion, a physical dynamics rule or an ambient spectral closure claim.

## New branch comparisons outside the inherited image

`retained-branch-comparison-synthesis.md` classifies ker(D) for each extension J with its existing averaging decoder D. At the first successor, four sibling-detail directions have coarse rank two and a hidden kernel of dimension two, distinct from the old copied K-zero contrasts. The ledger now splits/reassembles arbitrary supplied payloads as J D y+(I-J D)y without weakening strict image decoding.

Transported introduction-stage bases remain injective through length six and jointly reconstruct all 68 coordinates as 6+4+6+10+16+26. New detail is zero under unchanged copying; nonzero values require a supplied preparation rule. This organizes the carrier beyond inherited spectra but does not assign an ambient spectral law or a physical source of new amplitudes.

## Existing bilinear composition can populate branch detail

`bilinear-branch-preparation-synthesis.md` audits B(x,y), whose all-ones right input recovers unchanged copying. One supplied signed rational input pair can realize arbitrary four-dimensional pure sibling detail. A full single-product output still has rank-one interface blocks, with two determinant constraints: generic dimension eight, although sums of products span all ten path coordinates. Generic fixed parent means leave only two independent detail parameters.

The coarse identity A B(x,y)=diag(y)Kx holds exactly. Thus varying the right input cannot expose a left K-zero input through final-occurrence aggregation, even though its retained branch detail can become nonzero. Algebraic input reachability is established; physical preparation and dynamics are not.

## Associative retained-family composition

`retained-path-family-composition-synthesis.md` generalizes the ledger's coefficient product to arbitrary supplied homogeneous path families. Weighted words are associative, while binary assembly records and parent slots remain distinct and recoverable. All 216 primitive basis triples, mixed lengths through six, and five four-input bracketings pass. The old copy successor is the all-ones primitive right-input case.

Factorization is recorded at a specified cut: a supplied rank-two primitive-pair payload can compose at 2+1 without becoming factorable at 1+2. Empty endpoint domains, numerical zero coefficients and parallel primitive IDs remain distinct. This unifies retained composition but does not introduce a physical preparation rule or extend inherited spectra to arbitrary weighted families.

## Boundary of the result

- No source/target A->A fields were derived for the next-level spectral records. In fact the chosen right occurrence order begins at B; changing its based display requires explicit transport.
- No native admission, next-rung promotion policy, interaction, preparation or detector was selected.
- The tensor interpretation is explicit. A Hom-space/conjugate-factor interpretation is another contract and must not be silently substituted.
- A coarse scalar summary is not an identity operation. The earlier claimed commuting partial-trace diagram was not established by the old scripts.
- History windows preserve occurrence provenance, not unknown coefficient amplitudes. Conversely spectral coefficients alone do not determine original history IDs.

## Exact verification

    python research/nima/checkers/check_spectral_successor_many_many.py

The faulty experiment was replaced with exact arithmetic in Q(i*sqrt(3)), reusing the existing ledger/projectors. Fresh checks pass for all projector identities, all nine pair-basis reconstructions, a complex linear-combination control, correct norms, rank-three/rank-six splitting, a completely hidden cross-mode state, and lossless residual retention.

The decoder also checks registered mode parents and complete occurrence manifests. Missing channels, forged/reordered provenance and components outside their declared images are rejected. Separate controls show that intensities fail to distinguish different basis states and that equal projectors can come from distinct retained histories.

Report: `results/spectral-successor-reconstruction.json`.
