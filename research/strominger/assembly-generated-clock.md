# Contact assembly creates a local phase-clock reading

## Question and claim boundary

Does the existing assembly action create clock-readable phase relationships from the actual incoming mixture, rather than require the hand-prepared coherent clock used in the previous control?

**Yes, within the retained frozen-contact Hamiltonian.** Its matching coupling creates cross-topology coherence from that mixture. A state-read quadrature of the coherence supplies a local relational evolution coordinate. The full state and its native populations can be compared at that reading without fixing an external evolution rate.

This is not a newly derived primitive update or an identification of the user's two-cycle assembly with this contact Hamiltonian. The source already postulates Hamiltonian evolution of its native phase records. We extract an internal clock chart from that law; we do not derive the law, global monotone time, physical seconds or Einstein dynamics.

## Source operation, not another invented interaction

Read the actual serialized matrices in `pentachoron_connected_phase_energy_bundle.zip`: the original and connected seam operators, retained cycle-defect operator and matching projector P. Keep all forty coordinates of the two topology sectors.

The unchanged frozen-contact operator is

    H = [[H_O+2P, -2P],
         [-2P, H_C+2P]].

The actual input is

    rho_0 = diag(P_ground/4, 0).

It is the inherited equal mixture of four original ground modes. No independently prepared phase coherence or added clock degree of freedom is used. All gate diagonal terms remain, so the energy bookkeeping is the source's complete contact energy.

## Preregistered question

- **Problem:** can the assembly create the missing clock-bearing coherence?
- **Conjecture:** the existing contact generator creates a readable phase quadrature from the actual stationary input.
- **Rivals:** free-input stationarity blocks clock creation; an artificially coherent preparation is required; an external rate supplies all apparent temporal information; a local clock is wrongly promoted to a global clock.
- **Risky consequences:** nonzero contact commutator, strictly positive initial phase slope, zero slope with the matching gate removed, and unchanged relational states under common generator-rate rescaling.
- **Strongest falsifier:** disable matching while keeping the actual input and free native operators; reject a clock chart when its derivative is zero.
- **Disposition:** the local-clock conjecture survives the finite contact test. The claim that a bare two-pass return already supplies accumulated phase fails.

The [input packet](C:/Users/andrey/src/marici/research/strominger/inputs/assembly-generated-clock-freeze.json) was frozen before computation. Fingerprint: `07997e448e52f2319d86f2e1644f03b740197ea07a59cc8786afcec3fb6dcd4b`.

## Assembly generates the phase distinction

The algebraic change direction of the density is

    D rho = -i[H,rho].

No numerical elapsed-time value is needed to compute this direction from the source state and operator. With the free block-diagonal operator, `D rho_0=0`; with matching, it is nonzero.

Its original-to-connected block is exactly

    (D rho_0)_OC = -2i rho_original P.

Thus the first change is an imaginary cross-topology coherence. It arises from the actual coupling and actual mixture, not from the earlier specially phased preparation.

Use the existing P to define the Hermitian comparison quadrature

    Q = [[0,-iP],[iP,0]],
    chi = Tr(rho Q).

The initial reading is zero. Its native change direction satisfies

    D chi = 4 Tr(rho_original P).

The source matching weight is approximately `0.1`, so the initial derivative in model generator units is approximately `0.4`. That number is not a physical tick rate. The positive derivative establishes a valid local clock chart near this state.

## Relational evolution, with the external rate eliminated

Where `D chi` is nonzero, use the reading itself as the evolution coordinate:

    d rho/d chi = -i[H,rho] / Tr(-i[H,rho] Q).

This predicts changes of every native observable relative to the same phase comparison. Multiplying H by a common positive rate cancels between numerator and denominator.

The numerical audit reconstructs full states at three small fixed chi readings. An auxiliary orbit coordinate is used only to solve the native matrix orbit and is then eliminated. Repeating with H multiplied by three returns the same density at each clock reading; the largest density difference is approximately `3.51e-17`. The reconstructed derivative of chi with respect to itself is one.

All forty populations are retained. Connected-sector occupations at chi approximately `0.0004`, `0.0008`, and `0.0016` are approximately `4.00e-7`, `1.60e-6`, and `6.40e-6`. These are finite phase-record occupations, not physical formation probabilities. Phase coherence starts at first order while topology occupation starts at second order.

Trace and the full frozen-contact energy are conserved along the tested orbit. Consistent rephasing of the connected sector, its operator and its comparison quadrature leaves the reading and change rate unchanged.

## The two-cycle boundary is now explicit

The source's bare matching gate is

    J = [[I-P,P],[P,I-P]],   J^2=I.

Applying J twice restores the entire state. It does not accumulate endpoint phase. Retained execution history could distinguish the two applications, but the endpoint alone cannot.

Therefore merely calling an operation a two-cycle does not produce the local phase-clock evolution above. The concrete next bridge is to identify which actual two-cycle processing rule realizes the retained contact generator or a source-equivalent operation. The positive result is that this existing action generates clock-bearing coherence from the actual input; the unproved statement is that arrow processing inevitably selects it.

The clock is local: at a zero derivative the chart must be rejected or replaced. Global winding/history, reversal, event emission and reset authority are not supplied by the local quadrature.

## New matched-spatial result

The [new spatial refinement](C:/Users/andrey/src/marici/research/scattering/high-energy/matched_spatial_note.md) preserves expansion-directed strain transport but changes its peak magnitude by about 27.5 percent at matched omitted-mode energy. It does not justify using compression or numerical mode count as a clock.

Our comparison uses a phase quadrature rather than strain. It is an audit of the earlier finite contact operator, not a fresh verification of that refined full scattering model or a claim that its wavepacket has the same clock coordinate. Its relevance is a concrete constructor candidate, not transfer of a convergence claim across models.

## Verification

[Checker](C:/Users/andrey/src/marici/research/strominger/checkers/check_assembly_generated_clock.py) · [complete matrix result](C:/Users/andrey/src/marici/research/strominger/results/assembly-generated-clock.json)

Ten numerical checks pass. The initial algebraic identity residuals are below `5.85e-16`. These are implementation residuals, not rigorous error bounds. Source member hashes, projector identities, actual input, all forty populations and full densities at the clock readings are retained. No supplier was executed or source archive changed.
