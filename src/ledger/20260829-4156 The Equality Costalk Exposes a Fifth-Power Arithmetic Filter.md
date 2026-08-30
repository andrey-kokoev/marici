# 4156 — The Equality Costalk Exposes a Fifth-Power Arithmetic Filter

## Scope

Entry 4151 identifies a generic fourth-power incidence candidate on \(x\ne y\). This entry tests the proper equality stratum \(x=y\) using the same source-fixed structural lattice.

No parameter-ring Fitting theorem is claimed.

## Equality fibers

Five all-odd equality fibers were computed through sufficient two-adic depth:

\[
\begin{array}{c|c|c|c}
(x,y,z)&v_2(x+1)&v_2(d_{\rm terminal})&
7+5v_2(x+1)\\
\hline
(5,5,7)&1&12&12\\
(9,9,11)&1&12&12\\
(3,3,5)&2&17&17\\
(11,11,13)&2&17&17\\
(7,7,9)&3&22&22
\end{array}
\]

Thus every tested equality fiber satisfies

\[
v_2(d_{\rm terminal})
=
7+5v_2(x+1).
\]

The hostile point \((11,11,13)\) was selected after the formula and confirms the predicted valuation \(17\).

## Truncation correction

At \((7,7,9)\), a depth-\(20\) census initially appeared to leave free rank \(85\). A good-prime calculation retained rank \(2194\), proving that interpretation false. Extending the Number-safe census to depth \(26\) recovered the missing terminal factor at valuation \(22\).

Therefore:

\[
\text{vanishing modulo }2^N
\not\Rightarrow
\text{a free summand}.
\]

The census now permits depths through \(26\); larger depths require BigInt arithmetic.

## Interpretation

The generic incidence filter and equality costalk carry different visible grades:

\[
x\ne y:
\qquad
2^4(y-x)^4
\quad\text{against a valuation-12 cap},
\]

while

\[
x=y:
\qquad
2^7(x+1)^5
\]

controls the exposed terminal valuation on the five tested fibers.

This is evidence for a mixed \((2,y-x)\)-Rees module with a secondary fifth-order class on the equality costalk. It is not evidence for a new carrier divisor: \(x=y\) is the already declared collision/incidence support where the generic generator vanishes.

## Correction to the minimal candidate

The \(3\times2\) module of Entry 4151 remains a valid generic-open candidate and reproduces all six \(x\ne y\) fibers. It is not globally sufficient. Its constant valuation-\(12\) generator must arise as the generic restriction of a source-dependent relation whose equality costalk has initial form proportional to

\[
2^7(x+1)^5.
\]

The exact global polynomial is uncomputed and must not be fitted from these valuations.

## Narrow conclusion

The structural barcode contains two distinct, source-aligned normal orders:

- fourth order in the labelled incidence normal \(y-x\);
- fifth order in a secondary arithmetic direction exposed after restricting to \(x=y\).

This is the first finite evidence that the terminal arithmetic object is a support-sensitive mixed-Rees module rather than a globally split sum of cyclic modules.

## Next falsifier

Construct the structural presentation over the completed local ring at

\[
(2,y-x),
\]

derive its terminal Fitting module before specialization, and compute the restriction map to \(x=y\). The calculation must derive both the fourth-order generic generator and the fifth-order costalk generator, including their extension relation. Failure to derive either one rejects the proposed mixed-Rees interpretation.
