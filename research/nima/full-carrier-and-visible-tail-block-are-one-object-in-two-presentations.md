# Full carrier and visible-tail block are one object in two presentations

For an orthogonal cutoff projection `P_X`, put `T_X=I-P_X` and define

\[
J_X:\mathcal H\to P_X\mathcal H\oplus T_X\mathcal H,
\qquad
J_Xx=(P_Xx,T_Xx).
\]

Its inverse is

\[
J_X^{-1}(v,t)=v+t.
\]

Orthogonality gives

\[
\|J_Xx\|^2=\|P_Xx\|^2+\|T_Xx\|^2=\|x\|^2,
\]

so `J_X` is unitary and hence a homeomorphism.

Every completed operator `F` transports by conjugacy to

\[
\widetilde F_X=J_XFJ_X^{-1}
=
\begin{pmatrix}
P_XFP_X&P_XFT_X\\
T_XFP_X&T_XFT_X
\end{pmatrix}.
\]

If `F` is a homeomorphism or unitary, so is `F_tilde_X`. Composition and inversion are preserved exactly:

\[
\widetilde{FG}_X=\widetilde F_X\widetilde G_X,
\qquad
\widetilde{F^{-1}}_X=(\widetilde F_X)^{-1}.
\]

Thus the undivided carrier and visible-plus-tail block carrier are one object in two topological presentations.

For two cutoffs `X<=Y`, the chart change

\[
J_YJ_X^{-1}:
P_X\mathcal H\oplus T_X\mathcal H
\xrightarrow{\cong}
P_Y\mathcal H\oplus T_Y\mathcal H
\]

is also unitary. It reclassifies the shell `(P_Y-P_X)H` from tail to visible without changing the underlying state. Regulator refinement therefore acts as an atlas change on the fully retained carrier.

## Non-equivalent compression

The visible-only map

\[
\pi_XJ_X=P_X
\]

forgets `T_Xx` and is not injective unless `T_XH=0`. Consequently

\[
\mathcal H\not\cong P_X\mathcal H
\]

in general. Likewise `P_XFP_X` is not the same presentation of `F`; it is a lossy compression. The off-diagonal leakage blocks are precisely the data required to recover the homeomorphic block presentation.

## Axis effect

`full` versus `visible plus retained tail` is presentation data and can be quotiented into the homeomorphism groupoid. `visible only` versus `completed full` remains a genuinely directed regulator/observation distinction. This confirms that tail retention repairs presentation equivalence without creating an independent ninth axis.
