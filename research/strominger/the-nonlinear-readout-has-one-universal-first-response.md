# The nonlinear readout has one universal first response

Owner: `marici.Strominger`

## Question

Does the nonlinear magnetic readout convert the universal source jet into a
grade-dependent matrix direction, or is the grade dependence introduced only
when exterior minors are formed?

## Derivative formula

Let \(F(n)\) be the full four-by-three magnetic response matrix. For every
power-of-three shift in the strict range, define

\[
D_n^{(r)}
=
\frac{F(n+3^r)-F(n)}{3^{r+1}}
\pmod3.
\]

The source calculation gives

\[
C^{3^r}=I+3^{r+1}J\pmod{3^{r+2}}
\]

with one fixed rank-three source jet \(J\).

The nested commutator readout is an integral polynomial in the two-sided state

\[
(U_n,V_n)=(C^n,C^{-n}).
\]

Since \(C\equiv I\pmod3\), every grade state has the same residue

\[
(U_n,V_n)\equiv(I,I)\pmod3.
\]

Consequently its derivative along the universal source jet is evaluated at one
residue-field base point. It is independent of both \(n\) and \(r\):

\[
D_n^{(r)}=D.
\]

In row-major coordinates,

\[
D=(1,1,2,;0,1,1,;0,0,2,;1,0,0).
\]

The exact checker verifies this on 51 grades and the five strict shifts

\[
9,27,81,243,729.
\]

## Where the character actually varies

The matrix response direction \(D\) is universal. The character arises only
when the derivative of the maximal exterior power is evaluated against the
normalized baseline matrix:

\[
d(\Lambda^3)_{B_n}(D)
=
\chi(n,3^r)\sigma_n.
\]

Thus all grade dependence is carried by the cofactor state of \(B_n\), not by
the source jet or by the first matrix response.

This explains why the problem develops a residue tower. Whenever the leading
cofactor state vanishes, one must retain another 3-adic digit of \(B_n\).
The successive character classes are therefore Hensel refinements of the
baseline cofactor packet.

## Prospective test

The bounded scan ended at grade 250. Before evaluating any larger grade, the
observed residue classes froze three predictions:

\[
\begin{array}{c|c|c}
n&q&\text{prediction}\\
\hline
251&9&\chi=-1\text{ and one depth gain}\\
287&27&\chi=-1\text{ and one depth gain}\\
314&81&\chi=-1\text{ and one depth gain}.
\end{array}
\]

All three passed exactly:

\[
\begin{array}{c|c|c|c}
n&q&\ell_n&\ell_{n+q}\\
\hline
251&9&7&8\\
287&27&8&9\\
314&81&9&10.
\end{array}
\]

This is the first out-of-sample success of the strict-contact character
explanation.

## What remains

The universal derivative removes the shift variable from the leading response,
but it does not yet give an unbounded recurrence for the normalized cofactor
state \(B_n\). The remaining target is a finite digit recurrence for

\[
B_n,quad
\Lambda^2B_n,quad
\Lambda^3B_n
\]

along the grade sublattice \(n\equiv2\pmod3\). That recurrence should
generate the character classes without constructing the full integer matrix.

## Claim boundary

The derivative formula follows from the integral polynomial readout and the
universal source-jet congruence. Its bounded checker covers the displayed
grades and shifts. The three prospective predictions are exact finite tests.
No unbounded classification of contact grades or source-derived Ext
interpretation is asserted.

## Disposition

The explanation has become sharply localized:

1. the source supplies one universal rank-three jet;
2. the nonlinear matrix readout supplies one universal response \(D\);
3. the baseline cofactor tower supplies all varying character data.

The next recurrence belongs to the cofactor tower alone.

## Verification

Run:

```powershell
python research/strominger/checkers/readout_derivative_prediction_checks.py
```

All four gates pass. Machine-readable output is in
`research/strominger/results/readout_derivative_prediction_checks.json`.
