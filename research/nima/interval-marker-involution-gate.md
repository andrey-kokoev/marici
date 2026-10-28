# Direct interval-to-marker-control gate

## Frozen question and protocol

Can Aspect's fixed path-controlled marker flip realize the interval extension/trim pair by a faithful state encoding, without adding a controller, register, or new optical operation?

Source: `research/aspect/checkers/check_path_marker_mate_interferometer.py`, the actual `cnot_path_to_marker` matrix in `main`, acting on density matrices by `transform`. Target: the consecutive nonempty line paths and full NNMHV decoder in `dual-causal-path-candidate.md`, with extension implemented by the original `compose` in `checkers/check_indexed_path_synthesis.py`.

SCC obligation: **forward realization and route/coherencer compatibility**, prior to any metric or physical-time interpretation. Owner-local manifest: `scc-models/interval-marker-involution-gate.json`.

The direct candidate proposes a fixed encoding E into the path–marker density states, with full interval records recoverable from E, and the operation square

    E(L p) = U E(p) U†

on every legal L edge. Using the same available flip for l is natural for this direct proposal because that flip is its own inverse. The claim is universal over faithful encodings; no fitted encoding or detector is chosen. E may be nonlinear. Faithfulness means that different decoded records cannot have the same encoded density state. Laboratory execution history is not silently included in that state.

Rival: the existing flip supplies a reversible two-state orbit, not the repeated partial shifts required by the interval grammar. A richer optical register/controller could avoid this obstruction but is not part of this candidate.

Frozen falsifier: find a legal p, Lp, L²p with different initial/final decoded records while the actual optical channel squares to identity. Test first on entirely metric-visible objects, so the singular diagonal cannot explain failure. Test R similarly. Extract the actual matrix from Aspect's source; do not substitute a separately invented CNOT. Do not run its main or overwrite its result files.

Acceptance would require no such collision and a constructed full-record operation comparison. A bounded absence of collisions would not by itself prove acceptance. Stop on the first exact collision; additional cutoffs check the implementation rather than promote the theorem.

## Result and proof

The direct fixed-control realization is refuted. On a four-edge source the entirely visible sequences are

    L: (3,4) -> (2,4) -> (1,4)
    l: (1,4) -> (2,4) -> (3,4)
    R: (1,2) -> (1,3) -> (1,4).

The actual optical matrix satisfies U²=I. Consequently its channel Phi(rho)=U rho U† satisfies Phi²=id on every density state. If E intertwines either repeated extension, then

    E(L²p) = Phi²(E(p)) = E(p).

But the source records at p and L²p differ, contradicting full-record recovery from E. The same proof applies independently to l or R if assigned this fixed channel. This is not a dimension-counting argument and needs no linearity of E. A chart observer recovering (i,j) alone already detects the forced collision. The witness embeds in every m>=4.

The actual inverse pair remains sound: lL returns the original source object on its domain; it is LL, not lL, that must not collapse. Optical invertibility was never the disputed property. Nor does a loop restoring the object erase its execution history.

## Verification and scope

The dependency-free owner-local checker extracts the actual flip from Aspect's AST, uses Aspect's matrix operations, verifies the channel square on all 16 complex matrix units, and compares the original compose and full NNMHV decoder across m=3 through 10. It records visible repeated-shift witnesses, genuine L/l inverse checks, and a noninvolutive 3-cycle control. The trim repetition is an additional instance of the same identity obstruction, added after the initial L/R execution.

Run `python research/nima/checkers/check_interval_marker_involution_gate.py`. Receipt: `results/interval-marker-involution-gate.json`. Aspect's main entrypoint is not run; no foreign result files are rewritten. SCC checks instrument/manifest health separately from this proof.

This rejects only a faithful realization by the one fixed existing flip on the stated instrument. It does not reject a source-selected family of optical controls, a larger register, a controller-dependent operation, or simulation of the interval model. Including such extra state changes the tested interface and requires independent justification; keeping the missing interval data solely in an external log is not recovery from this optical state.

No laboratory execution or physical WG-I3 conclusion follows. Stop this direct branch; do not repair it by fitting a new optical operation or encoding to the desired interval action.
