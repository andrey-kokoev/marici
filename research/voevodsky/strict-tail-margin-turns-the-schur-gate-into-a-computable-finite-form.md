# A strict tail margin turns the Schur gate into a computable finite form

## Question

Can the finite Schur condition be replaced by a finite matrix whose entries do not require evaluating the inverse of an infinite tail operator?

## Claim boundary

Yes, as a sufficient certificate. Doubling the concentration threshold yields a strict tail margin \(C_M\geq1/40\). Operator monotonicity then bounds the exact Schur correction by \(40B_MB_M^*\). The resulting finite form depends only on compressions of \(A\) and \(A^2\). Its positivity has not been evaluated.

## Strict tail margin

For the corrected one-prime operator, write

\[
A\geq
\delta I-(\delta+C_-)T,
\qquad
\delta=\frac1{20},
\qquad
C_-<\frac{16}{5}.
\]

Choose the stricter concentration threshold

\[
\eta_*
=
\frac{\delta}{2(\delta+C_-)}.
\]

Then

\[
\eta_*>rac1{130}.
\]

If the tail concentration norm is at most \(\eta_*\), its compression satisfies

\[
C_M=QAQ
\geq
\frac\delta2Q
=
\frac1{40}Q.
\]

The rational transition count now requires

\[
M>
\operatorname{Tr}(T)
+130\operatorname{Tr}(T-T^2).
\]

Using the certified bounds gives

\[
M>
\frac{152362604}{4347},
\]

so

\[
M=35051
\]

is sufficient.

## Elimination of the infinite inverse

With respect to \(P=P_M\) and \(Q=I-P\), write

\[
A=
\begin{pmatrix}
F&B\\
B^*&C
\end{pmatrix}.
\]

Since \(C\geq1/40\),

\[
C^{-1}
\leq40Q.
\]

Therefore

\[
BC^{-1}B^*
\leq40BB^*.
\]

It is consequently sufficient to prove positivity of the finite form

\[
G_M
=
F-40BB^*.
\]

No infinite inverse is needed because

\[
BB^*
=PAQAP
=PA^2P-(PAP)^2.
\]

Thus

\[
G_M
=
PAP
-40\left(PA^2P-(PAP)^2\right)
\]

is determined by two finite compressions.

## Logical force

If

\[
G_M\geq0,
\]

then

\[
F-BC^{-1}B^*
\geq G_M
\geq0,
\]

and hence \(A\geq0\) on the first-prime support window. Failure of \(G_M\geq0\) is inconclusive because this sufficient form overestimates the exact Schur correction.

## Remaining executable gate

Construct certified interval matrices for

\[
PAP
\quad\text{and}\quad
PA^2P
\]

in the first \(35051\) concentration modes and certify the least eigenvalue of \(G_M\). This is finite but remains computationally large. A negative interval enclosure for \(G_M\) would not refute local positivity; it would require returning to the exact Schur complement or a sharper tail-resolvent bound.

## Disposition

The infinite-tail resolvent is removed from the sufficient certificate. The remaining first-prime gate is a concrete finite Hermitian interval problem, not yet solved and still RH-bearing only when combined with all support windows.

## Verification

- `research/voevodsky/checkers/check_strict_tail_schur_form.py`
- `research/voevodsky/results/strict_tail_schur_form.json`
