# Carrier loss births the circuit; sheet coherence kills the magnetic readout

Two route packets must not be conflated.

At the residual collision level, `L` and `R` are alternative carriers of the
boundary observation `R_2`.  Their simultaneous loss at `(g,d)=(2,5)` lowers
the source-column rank and creates the primitive circuit `(1,-3,2)`.

At the full folded-output level, define

\[
A=\partial_{\bar z}f,
\qquad
B=\partial_z\bar f.
\]

The magnetic readout is

\[
M=A-B.
\]

For both exceptional source classes `E_1` and `E_2`, exact calculation gives

\[
A=B\ne0.
\]

For `E_1=1-\bar z^{-2}`, explicitly,

\[
A=B=\frac{40(z+\bar z)}{(1+z\bar z)^3}.
\]

The `E_2` sheet is also nonzero, although its rational expression is larger.
Consequently

\[
M(E_i)=A-B=0,
\qquad
E(E_i)=A+B=2A\ne0.
\]

Thus the causal and observational mechanisms occupy different levels:

\[
\begin{array}{c|c}
\text{source-rank birth}&\text{loss of the local transverse carrier}\\
\text{magnetic invisibility}&\text{nonzero equal-sheet coherence}
\end{array}
\]

In exact-sequence language, the exceptional source class is not in the kernel
of the full sheet transport `T_sheet`.  Its image lies on the diagonal:

\[
T_{\mathrm{sheet}}(E_i)=(A,A)\ne(0,0),
\]

and the magnetic projection `[1,-1]` kills that diagonal.  The complementary
sum projection detects it.

This corrects any statement that called the full magnetic exception pure
route loss.  Route loss is the local constructor failure that permits the
source circuit; the resulting physical readout zero is lawful interference
between compatible reflected sheets.
