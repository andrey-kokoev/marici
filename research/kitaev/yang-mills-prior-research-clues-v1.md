# Yang–Mills: clues from prior research

## Search scope

Operator request: search prior research for clues about the current Yang–Mills obstruction. This is a reading/search synthesis, not a new proof, checker replay, or continuum result.

Read the existing Kitaev microprogram and iterations 3, 6, 8, 9 and 10; searched peer research for reconstruction, form convergence and gap references; read Voevodsky's completion interface and cofinal positive pro-completion packets, plus Nima's carrier-energy and protected-kernel audits. Queried the existing PDF index for Yang–Mills and for constructive-theory names. The generic query returned mostly supersymmetric scattering/geometry mentions. A targeted Osterwalder/Balaban/Dobrushin/Seiler/Fröhlich/Kogut–Susskind query returned only an unrelated Osterwalder bibliographic mention. This is not an exhaustive literature search. No live external literature search was available or performed.

## 1. Best immediate clue: the actual vacuum interaction, not just the gap

Iteration 9 already writes the actual finite-box log ground function as connected interactions with

- N_2(Phi) <= R = 4096 r/3;
- contraction factor q = 262144 r/27 < 1;
- actual conditional influence row <= R/2 < 9/128.

These concern the actual vacuum measure, not the older degree-two surrogate. They are a strong starting point for a thermodynamic construction via summable interactions, Dobrushin uniqueness and boundary comparison. The missing operation is to construct a compatible infinite-lattice interaction/state from the finite-box solutions and prove boundary control. Having estimates uniform over boxes is not the same as having compatible solutions.

A useful prospective test is a fixed interior gauge-invariant observable in two growing boxes: bound its expectation difference by a quantity tending to zero with distance to the boundary. Connected-support weights and fixed-point iteration suggest a route, but no such boundary-decay theorem is proved here.

Even a completed equal-time probability measure would not yet construct the full quantum state, Euclidean multi-time correlations, or continuum theory. Those need the actual dynamics and compatible insertion maps.

Source: `yang-mills-anchored-casimir-v1.md` and `yang-mills-linked-density-v1.md`.

## 2. There is already a temporal source to use

Iteration 3 defines the reflection-positive anisotropic heat-kernel transfer step

S_tau = P_G exp(-tau V/2) exp(-tau H_0) exp(-tau V/2) P_G.

At fixed spatial graph its time refinement converges to exp(-tH). Thus the next question need not start from a formal path integral: use this declared source to ask for compatible thermodynamic multi-time correlation packets.

Limits and regulator identity must remain explicit. Fixed-graph temporal convergence is not spatial refinement, restored Euclidean rotational covariance, or equivalence to the isotropic Wilson action.

Source: `yang-mills-ground-state-transfer-v1.md`.

## 3. Completion research identifies what must be transported

Voevodsky's finite-to-closed-form interface separates domain/closability, form or resolvent convergence, radical identification, quotient coercivity, and restriction/completion coherence. Its checker is admission logic, not a construction of these analytic witnesses.

The cofinal positive pro-completion papers also explicitly distinguish packetwise convergence from an ordinary Hilbert-space limit requiring additional tail/Mosco control. This is directly relevant as a warning about finite-observable diagonal arguments, not a ready-made Yang–Mills theorem.

For our problem, a promising theorem target is passage of the centered ground-state energy inequality to the limiting physical state. It needs actual state/dynamics identifications and a justified domain for the limiting generator. We must not assume a common Hilbert space or stable vacuum projector just because every finite box has the same numerical gap bound.

Sources:
- `research/voevodsky/coherence-pyramid-completion-interface.md`
- `research/voevodsky/cofinal-finite-packet-minimalization-constructs-the-regular-physical-positive-pro-completion.md`
- `research/voevodsky/a-cofinal-spectrally-adapted-diagonal-assembles-the-finite-packet-absolute-grams-as-an-asymptotically-coherent-pro-system.md`

## 4. Weak coupling needs a different estimate, not merely a better constant

Iteration 10 uses weighted curvature >= 1/2 - 4096 r. With the declared conventional matching r = 4/g^4, this sufficient criterion moves in the wrong direction as g tends to zero. Failure of this lower bound does not prove failure of the actual gap or of other Poincare methods.

The clue is to investigate block-scale/multiscale estimates rather than extrapolate this small-r contraction. Any such replacement needs source-derived blocked observables, effective actions and scale conversion; a fitted block Hamiltonian would change the problem.

Nima's carrier audits reinforce the boundary: metric positivity and symmetry alone do not select a physical energy generator or energy scale. They are finite-model counterexamples, not statements proving or disproving Yang–Mills.

## Published literature leads to obtain and check

These are bibliographic leads from established background knowledge, not papers retrieved or verified in this search:

1. Osterwalder and Seiler, *Gauge Field Theories on a Lattice* (1978): lattice gauge construction and positivity framework.
2. Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories* (1977): transfer-matrix structure.
3. Dobrushin uniqueness and cluster-expansion literature: exact hypotheses for infinite-volume consistency and boundary independence of our actual vacuum interactions.
4. Balaban's rigorous renormalization-group work on lattice gauge fields: ultraviolet control, not a completed infrared mass-gap theorem.
5. Magnen, Rivasseau and Sénéor, *Construction of YM4 with an Infrared Cutoff* (1993): particularly relevant for distinguishing ultraviolet construction from removal of the infrared cutoff.
6. Osterwalder–Schrader reconstruction: hypotheses for turning a compatible Euclidean correlation functional into the target quantum theory.

## Recommended order

Independent review of iterations 9–10 remains necessary. Subject to that review, prioritize the strong-coupling thermodynamic state and its multi-time correlations using the existing interaction/transfer source. In parallel, obtain the constructive-Yang–Mills references for the separate weak-coupling/refinement problem. Neither lane is a continuum mass-gap claim.
