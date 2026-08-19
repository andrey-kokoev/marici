# 1004 — Cellular Exactness Does Not Descend Through the Resonant Betti Lattice

> **RETRACTED by Entry 1005.** This entry incorrectly identified dense chamber coordinates \(4,5\) with sparse source occurrences \(4,5\).  The frozen occurrence-to-dense permutation sends dense coordinates \(4,5\) to source occurrences \(0,3\).  Consequently the primitive lies on the singleton walls \((ZA_2)^2=1\) and \((A_3/Z)^2=1\), which are generically nonresonant on the \((--)\) recombination locus.  The claimed resonant Betti obstruction is false.

Retraction event: `ev-000000000624-53686c7e-25ab-4b20-a5df-113204dfda6f`.

## Lattice distinction

Entry 1002 proves that the restricted \((--)\) three-edge arc is exact in the full relative chamber complex:

\[
d_{--}=\delta_{\rm KN}p_{--},
\qquad
\operatorname{supp}p_{--}=\{4,5\}.
\]

Entry 949 independently fixes the comparison from a loaded relative chamber to a closed twisted Betti cycle.  If the local monodromy is \(M\), then

\[
\partial\gamma=(M-1)e,
\]

and closure requires a coefficient proportional to

\[
(M-1)^{-1}.
\]

Therefore relative cellular exactness may fail to descend integrally at a monodromy resonance.

## The primitive lies on the resonant repeated wall

The two nonzero primitive coordinates \(4,5\) are precisely the two labelled occurrences of

\[
U=\frac{A_3B_{34}}{Z}.
\]

Entry 949's source Fitting packet assigns this wall

\[
M_U-1=U^2-1
\]

valuation two, matching the two labelled occurrences.  Entry 1001's recombination specialization imposes

\[
U=t,
\qquad t^2=1,
\]

so

\[
M_U-1=0.
\]

The primitive that proves cellular exactness consequently requires singular closed-cycle regularization exactly on the tested support.

## Result

\[
\boxed{
d_{--}\text{ is exact in the relative chamber complex, but its exactness in the unlocalized closed Betti lattice is undetermined.}
}
\]

In particular,

\[
\text{exact after localizing }M_U-1
\not\Rightarrow
\text{supported class vanishes at }M_U=1.
\]

Entry 1002 remains correct in its stated cellular scope.  It does not close the resonant Betti question.

## What is and is not established

Established:

- the primitive occupies exactly the two repeated-wall occurrences;
- the same wall has source-derived Fitting valuation two;
- closed-cycle regularization uses \((M_U-1)^{-1}\);
- no new carrier divisor is needed.

Not established:

- whether the two singular regularizations have cancelling residues;
- whether a rank-one nearby/Bockstein class survives;
- whether any surviving class equals Entry 997's normal modification line;
- whether a physical integration cycle selects it.

## Next finite test

Construct only the \(2\times2\) source regularization block for occurrences \(4,5\), retaining their ordered orientations.  Expand it at

\[
m=\left(\frac{A_3B_{34}}Z\right)^2-1=0.
\]

Apply it to

\[
p_{--}|_{s,t}=\pm16(-e_4+e_5).
\]

Compute the coefficient of \(m^{-1}\).  A zero residue restores exactness in the Betti lattice; a nonzero residue defines a canonical supported candidate that must then be compared, with variance retained, to Entry 997's modification line.

Do not reconstruct the full six-by-six regularization matrix unless the local block fails to close.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_minus_twisted_cycle_lattice_gate.rs`
- `research/benincasa/string-six-point-minus-twisted-cycle-lattice-gate.json`

The checker matches the primitive support, occurrence block, Fitting valuation, monodromy factor, and required closure denominator across the frozen packets.

Epistemic graph event: `ev-000000000623-a9b4ae28-5d32-47f2-94a5-71e94aa3a1a7`.
