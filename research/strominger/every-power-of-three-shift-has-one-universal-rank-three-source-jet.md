# Every power-of-three shift has one universal rank-three source jet

Owner: `marici.Strominger`

## Question

Does the rank-one spectral bridge directly carry the normalized source
increments responsible for strict Plücker contacts?

## Result

No. The simplest bridge explanation is falsified.

For the fixed constructor \(C\), define the normalized power-of-three
increment by

\[
J_r=
\frac{C^{3^r}-I}{3^{r+1}}
\pmod 3.
\]

Exact computation through \(0\le r\le8\) gives

\[
v_3(C^{3^r}-I)=r+1
\]

and one constant matrix

\[
J_r=J=
\begin{pmatrix}
2&2&0&2\\
0&0&2&1\\
2&1&2&1\\
1&0&0&2
\end{pmatrix}
\pmod3.
\]

Its rank over \(\mathbb F_3\) is three, not one.

Thus every power-of-three shift supplies the same source direction after
normalization, but that direction does not lie on the rank-one spectral
bridge.

## Unbounded induction

The finite computation supplies the base congruence

\[
C=I+3J\pmod9,
\qquad
J\not\equiv0\pmod3.
\]

Suppose

\[
C^{3^r}=I+3^{r+1}J_r
\pmod{3^{r+2}}.
\]

Cubing gives

\[
C^{3^{r+1}}
=I+3^{r+2}J_r
\pmod{3^{r+3}},
\]

because every term containing at least two copies of \(3^{r+1}J_r\) has
greater 3-adic depth. Therefore

\[
J_{r+1}=J_r\pmod3.
\]

Since the base jet has rank three, this proves for every \(r\ge0\):

\[
v_3(C^{3^r}-I)=r+1,
\qquad
J_r=J,
\qquad
\operatorname{rank}_{\mathbb F_3}(J)=3.
\]

## Explanatory shift

The source increment is universal; the character is not. Hence the variation
of

\[
\chi(n,3^r)
\]

must be produced by the grade-dependent derivative of the nonlinear magnetic
readout acting on the fixed direction \(J\).

This reduces the missing recurrence from two variables to one:

\[
\chi(n,3^r)
=
\text{normalized derivative of the grade-}n\text{ readout along }J.
\]

The shift exponent controls the available 3-adic depth. It does not change the
leading source direction.

## Relation to the spectral bridge

The rank-one bridge

\[
(C-I)(C^2-147458C+I)
\]

remains an exact constructor invariant, but it does not directly contain the
power-of-three source jet. Any role for that bridge must pass through an
additional source-derived map or through the derivative of the nonlinear
readout. Its existence alone does not explain Plücker scalarity.

## Claim boundary

The power-of-three source-jet law is unbounded and exact. The subsequent claim
that the readout derivative sends this rank-three direction to the observed
Plücker line remains bounded evidence. No connecting exact sequence or
cross-sector functor is asserted.

## Disposition

One proposed explanation was falsified, but the falsifier produced a stronger
simplification: all shifts share one universal source jet. The next task is to
derive the grade recurrence of the readout derivative evaluated on this fixed
matrix.

## Verification

Run:

```powershell
python research/strominger/checkers/power_three_source_jet_checks.py
```

Four of four gates pass. Machine-readable output is in
`research/strominger/results/power_three_source_jet_checks.json`.
