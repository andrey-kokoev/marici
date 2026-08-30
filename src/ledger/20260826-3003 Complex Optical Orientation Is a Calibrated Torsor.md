# 3003 — Complex Optical Orientation Is a Calibrated Torsor

**Status:** narrow exact descent result  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-3c73d3e59182d5840ba84a8b`

## Scope

Entry 3001 proves that a source-defined circular-polarization analyzer supplies the missing complex two-qubit probe. This entry asks the next question: does the resulting complex orientation glue canonically across labelled photon ports, or only after source calibration?

The result concerns orientation of the complex coordinate. It does not retract informational completeness of the calibrated optical instrument.

## Frozen involution

In the linear polarization basis, complex conjugation acts on the Pauli frame by

\[
KIK^{-1}=I,
\qquad
KXK^{-1}=X,
\qquad
KYK^{-1}=-Y,
\qquad
KZK^{-1}=Z.
\]

Thus every real local probe is blind to reversal of the circular orientation. A circular analyzer detects the missing direction only after its retardance sign, fast-axis convention, H/V phase frame, and bandwidth calibration have fixed which local outcome is called positive \(Y\).

For two labelled ports, independent conjugations generate

\[
C_2^{(1)}\times C_2^{(2)}.
\]

Their action on the critical product row is

\[
Y\otimes Y
\longmapsto
(-1)^{\epsilon_1+\epsilon_2}Y\otimes Y.
\]

Simultaneous reversal on both ports preserves \(Y\otimes Y\); reversal on one port changes its sign and exchanges the labels of the hostile pair \(\rho_+\) and \(\rho_-\).

## Covariance rather than absolute selection

For any state \(\rho\) and analyzer \(M\), conjugating both leaves the probability invariant:

\[
\operatorname{Tr}(\rho M)
=
\operatorname{Tr}(K\rho K^{-1}\,KMK^{-1}).
\]

Therefore static count probabilities cannot choose an absolute handedness. They determine the complex coordinate only relative to the calibrated analyzer frame.

The correct object is consequently a \(C_2\)-orientation torsor, or equivalently a rank-one sign local system, attached to the complex coefficient lens. Source calibration chooses a section of that torsor. The underlying Carrier need not contain a preferred global sign.

## Narrow conclusion

The optical source establishes two distinct facts:

1. Circular probes are physically available, so the rebit composite is observationally incomplete.
2. The sign of the imaginary direction is not absolute; it descends only relative to synchronized source calibration across labelled ports.

Hence the strongest supported architecture is

\[
\text{shared labelled Carrier}
+
\text{complex coefficient lens}
+
\text{source-calibrated orientation torsor}.
\]

This is not arbitrary gauge freedom. A mismatch between two port calibrations changes odd-\(Y\) product coordinates and is experimentally detectable once the ports are compared.

## Falsifier

Transport one calibrated circular frame around a closed source-derived transition loop. There are three outcomes:

- identity holonomy: the orientation section glues globally on that loop;
- sign holonomy: the coefficient lens carries a nontrivial \(C_2\) local system;
- transition not derivable from the source: global orientation remains untyped.

No basis-dependent choice may be used to force identity holonomy.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-3c73d3e59182d5840ba84a8b`, value 3003.
- Exact involution: \(K(I,X,Y,Z)K^{-1}=(I,X,-Y,Z)\).
- Composite action: \(Y\otimes Y\mapsto(-1)^{\epsilon_1+\epsilon_2}Y\otimes Y\).
- Instrument provenance and calibration data: Entry 3001 and `research/aspect/local-stokes-pauli-probe-provenance.md`.
- Epistemic-graph admission: `ev-000000005717-8e0ceb04-23b4-42d9-89b6-4b362f570881`.
