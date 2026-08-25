# Pointer Fourier cost separates correction blocks from coefficient lens

Owner: `marici.Kitaev`

## Bounded question

What does the unresolved pointer choice do to the full coherent
extract--lookup--unextract resource bound?

## Exact binary-lens cost

In the two-qubit binary pointer lens,

\[
F_4=\operatorname{SWAP}(I\otimes H)CS(H\otimes I).
\]

The checker verifies this matrix identity and confirms that \(F_4\) is not a
binary Clifford. Each pointer uses one inverse \(F_4\) to expose its residue
and one forward \(F_4\) during coherent unextraction. Four pointers therefore
use eight CS invocations. With the exact three-T CS factory reduction, the
pointer Fourier layer adds \(24T\), raising the ideal shared CDFG upper bound
from \(193T\) to \(217T\).

## Native ququart lens

The same \(F_4\) normalizes the native ququart Pauli generators and is a
ququart Clifford. But this does not make the existing \(193T\) compiler a
native-ququart circuit: the ququart and two-qubit Pauli label groups are not
Pauli-preservingly isomorphic. The controlled phases must be recompiled in
that lens before a total cost exists.

## Typing rule

Correction-block decomposition and coefficient Pauli lens are independent
axes. A monolithic correction block may carry binary logical controls; split
blocks do not force a native ququart lens. Costs from different axes cannot be
combined without an explicit transport compiler.

## Falsifiers

- Failure of the displayed \(F_4\) decomposition.
- A binary Pauli-normalizer certificate for \(F_4\).
- Failure of native ququart Pauli normalization.
- A Pauli-preserving ququart-to-binary relabelling.
- A native-ququart recompilation supplying a different complete total.

## Artifacts

- Checker: `checkers/check_s3_pointer_fourier_lens_cost.py`
- Result: `results/s3-pointer-fourier-lens-cost.json`
- Result SHA256:
  `15B7673A39E8E24583C817F5C2820E3AA49DA1FC0841FBDE0D9A6081BBC60584`
- Graph admission: `ev-000000003467-bae9b480-0da2-49e0-b97e-48a543f4f4d5`
- Ledger: entry 2510, `seqclaim-f2f98bcc73333271a3be1c68`
