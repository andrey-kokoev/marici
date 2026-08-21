# 1536 — The Third Counterterm Equation Is Uniquely the \(c_1\) Equation

## Source defect

After displaying the three counterterm contributions proportional to
\(c_1,c_2,c_3\), arXiv:1408.4801 prints the solved coefficient labels as

\[
c_3,\qquad c_2,\qquad c_3.
\]

The repeated final \(c_3\) is inconsistent with the displayed counterterm
action and leaves \(c_1\) unsolved.

## Unique algebraic correction

Cancelling independently the coefficients of
\(1,p^2\eta^2,p^4\eta^4\) forces

\[
c_3=\frac{(3\epsilon+2\delta)^2}{32}\operatorname{Inf}(I_4),
\]

\[
c_2=\frac{H^2}{M^2}\frac{(3\epsilon+2\delta)^2}{128}
\operatorname{Inf}(I_0+I_2-5I_4),
\]

and

\[
\boxed{
c_1=\frac{H^2}{M^2}\frac{(3\epsilon+2\delta)^2}{128}
\operatorname{Inf}(3I_2-5I_4-I_0).
}
\]

Thus the final printed label must be \(c_1\), not \(c_3\).

## Verification

`research/benincasa/checkers/counterterm_label_contract.rs` substitutes the
three source-derived combinations into the displayed counterterm responses.
The constant, \(p^2\eta^2\), and \(p^4\eta^4\) coefficients vanish separately
as exact integer vectors in \((I_0,I_2,I_4)\).

The machine-readable output is
`research/benincasa/results/counterterm-label-contract.json`.

## Consequence

The omitted \(\eta_0^1\) and \(\eta_0^0\) reconstruction must retain the
corrected \(c_1\) contribution.  Treating the repeated \(c_3\) literally would
double-count the four-derivative counterterm and omit the kinetic counterterm.
This is a source-internal repair, not an admissible normalization choice.
