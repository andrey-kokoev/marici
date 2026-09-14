# The infinity component difference in an adapted blow-up marking

Choose the standard Picard basis

\[
\operatorname{Pic}(S)=
\mathbb Z\langle H,E_1,\ldots,E_7\rangle,
\]

with

\[
K_S=-3H+E_1+\cdots+E_7,
\qquad
-K_S=3H-E_1-\cdots-E_7.
\]

The two components above a bitangent line are a Geiser-conjugate pair of exceptional curves. The Weyl group acts transitively on exceptional curves, so choose a marking adapted to the infinity component:

\[
C_+=E_7.
\]

Since the pair sums to the anticanonical pullback of the bitangent line,

\[
C_++C_-=-K_S,
\]

we obtain

\[
C_-=3H-E_1-E_2-E_3-E_4-E_5-E_6-2E_7.
\]

Both classes have square \(-1\) and anticanonical degree one:

\[
C_+^2=C_-^2=-1,
\qquad
(-K_S)\cdot C_+=(-K_S)\cdot C_-=1.
\]

They meet at the two tangency points:

\[
C_+\cdot C_-=2.
\]

Their oriented difference, which supplies the geometric \(e_6\)-line, is

\[
\begin{aligned}
e_{6,\mathrm B}
&=C_--C_+\\
&=3H-E_1-E_2-E_3-E_4-E_5-E_6-3E_7.
\end{aligned}
\]

It satisfies

\[
e_{6,\mathrm B}^2=-6,
\qquad
K_S\cdot e_{6,\mathrm B}=0,
\]

and it is primitive. Thus \(e_{6,\mathrm B}\) lies in the \(E_7\) algebraic kernel while carrying norm \(-6\), rather than being a root of norm \(-2\).

A useful mod-two identity follows immediately:

\[
e_{6,\mathrm B}\equiv-K_S\pmod{2\operatorname{Pic}(S)}.
\]

Indeed, for any bitangent pair \(C,C'\) with \(C+C'=-K_S\),

\[
C'-C=-K_S-2C\equiv-K_S\pmod2.
\]

Therefore every split-bitangent component difference has the same mod-two Picard class. This explains why the paired-node construction supplies one canonical mod-two direction even before choosing which bitangent is called infinity.

The marking is canonical up to the Weyl stabilizer of the chosen bitangent pair. An absolute identification with a pre-existing labelled blow-up configuration would require the seven explicit blow-up points; the integral orbit and all intersection data already follow from the adapted marking.

Certificate:

- `research/voevodsky/checkers/mark_infinity_components_in_picard_basis.py`;
- `research/voevodsky/results/infinity_component_picard_marking.json`.
