# The second-wall root swap sources the antisymmetric simple mixed detector

## Question

Does the existing carrier already contain a source-derived operation producing the simple mixed vector \(g_{101}-g_{110}\), without retyping the doubled-pole shape response?

## Claim boundary

This packet uses the established two-wall conductor monodromy and the marked algebraic extension. It constructs the algebraic detector route. A physical record still requires the already declared monodromy/period readout interface; loop transport is not assigned temporal meaning.

## Existing integral transport

In the basis

\[
(g_{101},g_{110},g_{\rm top}),
\]

the second-wall root swap acts by

\[
T_2(g_{101})=g_{101},
\qquad
T_2(g_{110})=-g_{110},
\qquad
T_2(g_{\rm top})=g_{\rm top}-g_{110}.
\]

Apply it to the canonical symmetric mixed residue

\[
s_+=g_{101}+g_{110}.
\]

Then

\[
T_2(s_+)=g_{101}-g_{110}=s_-.
\]

The first-wall root swap gives the opposite orientation,

\[
T_1(s_+)=-s_-.
\]

Thus the antisymmetric simple mixed observable is already sourced by either labelled wall monodromy. No inversion of the shape derivative and no division by two is needed.

## Primitive physical coordinate

The marked algebraic extension is

\[
\begin{aligned}
g_{101}&\longmapsto-\frac1{4xy}e_4-cv_{\rm alg},\\
g_{110}&\longmapsto-\frac1{4xy}e_2+cv_{\rm alg},
\end{aligned}
\qquad
c=\frac1{4x^3y^3(x+y)}.
\]

Therefore

\[
s_-\longmapsto
\frac1{4xy}(e_2-e_4)-2c\,v_{\rm alg},
\]

and the \(v_{\rm alg}\) coefficient is nonzero away from the declared pole locus.

## Information path

The relevant path through the coherence pyramid is

\[
\text{canonical mixed residue }s_+
\xrightarrow{\text{labelled wall root swap }T_2}
s_-
\xrightarrow{\text{marked algebraic extension}}
(e_2-e_4)-\text{tail}
\xrightarrow{\pi_{v_{\rm alg}}}
-2c.
\]

The wall label must remain present through the root-swap step. Quotienting the two walls by exchange before transport removes the choice distinguishing \(T_1\) from \(T_2\) and destroys the sign of the detector.

The exchange-odd shape response remains a separate differentiated-response route. Its parity reversal does not construct this simple class; the labelled wall monodromy does.

## Disposition

The supposedly missing antisymmetric simple input is present in the existing two-wall conductor monodromy. The remaining coherence obligation is to prove that its marked algebraic period readout is the same physical readout used for the first \(e_6\) channel, with integral Betti normalization retained.

Verification:

- `research/voevodsky/checkers/check_second_wall_root_swap_mixed_detector.py`
- `research/voevodsky/results/second_wall_root_swap_mixed_detector.json`
