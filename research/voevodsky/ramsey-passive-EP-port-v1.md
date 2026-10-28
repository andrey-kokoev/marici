# Passive E context bound to the parent's P/PN port family

## Result

**The structural passive binding passes under the explicit independently validated-input policy.** It does not require adding an active E->P operation. It does not yet prove equality or transport of the two readers' field amplitudes, or that the target is admitted under an E-only source policy.

This follows the difficulty diagnostic, without promoting the parent `face-chart-transition-descent` or choosing its admission policy.

## Concrete interface

For each of24 complete source markings, retain the full reversed E context on the same regular chamber. Define the complementary P reader by

- P.C0 = E.C2; P.M0 = E.M2;
- P.C1 = E.C1; P.M1 = E.M1;
- P origin = E origin +2;
- use the existing `completeP` constructor for the target's outside C2.

This is a declared comparison convention, not a newly discovered source operation. It keeps all four geometric vertices and their complementary roles. The old C2/M2 occurrences are retained exactly; C1/M1 advance by2.

The target base packet uses the declared five-slot identity permutation; the dual E packet retains its reversal permutation. Their individual validity does **not** establish a field-amplitude identification between them.

## Actual port-family binding

Fresh runtime checks construct both target PN ports, including the reader-prefixed port, for each marking. They compare all48 against the previously admitted complete PN port family:

- geometric cell keys and every reference alias agree;
- all five coefficient-slot permutations agree;
- PN operation kind, phase increment, face and permutation agree;
- the native reader-prefix length agrees;
- the explicit origin lift is +2, not silently discarded.

Allocation IDs are not geometric identities and are normalized away for this comparison. The complete original and lifted records are retained in the receipt.

All72 target PN/reader transfers validate. The original P->N->E histories are also replayed to construct the dual context reference geometry. Prior receipt source pins are checked, not trusted without inspection.

## Correct request typing

There are96 chart/face requests:

-48 have a target P PN permit and are accepted;
-48 have only one M on the requested face and are refused.

E is a contextual input, **never falsely supplied as a PN permit**. Accepted requests use the existing target-P self-span selector; refused requests are checked using a genuine complementary source-P permit. Thus acceptance does not pretend that a reversed old PN face is still PN.

## Fresh safe-Cubical result

`agda/RamseyPassiveEPPort.agda` embeds the existing traced selected-span tree into a source family containing separately tagged E contexts and PN port records. It proves:

1. The embedded PN branch encodes exactly the existing selected-span package.
2. Native P retains the E context and the selected PN branch; native E still retains all of its prerequisite family.
3. The E and target PN source occurrences are explicitly retained.
4. With both input classes admitted, each contextual package has a native realization.
5. With only E inputs admitted, the same explicit external compiler cannot certify the contextual package: its target PN leaf remains a required premise.

All48 actual accepted cases are instantiated. All96 request outcomes compute in the kernel. A false face-acceptance fixture and a false E-only-admission fixture are rejected.

The E seed payload contains only its own complete packet and frame. It does not covertly contain the already supplied target P packet.

The fifth result is a necessity theorem for this **particular explicit compiler and policy**, not an impossibility theorem for arbitrary native proofs, arbitrary source rules, or all ways of computing a target.

## What this settles about difficulty

The suspected need for an active E->P move was stronger than necessary for this structural contextual task. Existing native constructors suffice once both validated contexts are admitted. The origin mismatch and extra outside reference are manageable explicit data, not established hard obstructions.

However, this construction deliberately pairs E with a valid target PN request. It must not be relabelled as a proved semantic E/P reader equivalence merely because the pair is native. Nor is it a fresh proof of four-facet edge/triple naturality for the lifted adapter: the earlier correspondence theorem and this port-family binding remain distinct results.

The next substantive test is therefore narrowly semantic: supply the declared E/P comparison on the retained occurrences and full five-slot readouts, and check its compatibility with the actual PN restriction/overlap data. If the intended parent only asks for the retained independently admitted structural object, the present binding removes this local interface obstacle. If it asks for source-generated target admission or stronger field descent, those are separate obligations and must be stated as such.

## Verification and reproduction

    python research/voevodsky/checkers/check_ramsey_passive_EP_port.py

Passed with fresh Agda `--safe --cubical --guardedness --ignore-interfaces` closure checks. Both negative fixtures failed as intended. Compiler and formal-source inventories remained stable during checking.

- Runtime receipt: `results/ramsey-passive-EP-port-input-v1.json`.
- Kernel/binding receipt: `results/ramsey-passive-EP-port-v1.json`.

Verification boundary: JavaScript geometry, reference/slot comparison and phase bookkeeping are runtime checked and quoted as complete payloads. The kernel checks permit counts, native packaging, retained sources, package equality and the compiler-policy boundary; it does not interpret JavaScript geometry or prove amplitude semantics.

No existing conjecture-net verdict, source operation, admission policy or graph publication was changed.
