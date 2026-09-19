# The canonical bordered evaluation vector solves the divisibility square at finite cutoff but not the Green promotion

The existing ordered-readout border already contains an explicit source-derived
incidence of the Koszul carrier line.  At finite cutoff let

\[
f(s)=y_s(M_sx_s),\qquad u_s=M_sx_s,
\]

and define

\[
D_s=
\begin{pmatrix}I&u_s\\y_s&0\end{pmatrix}
:V_s\oplus\mathbb C\to V_s\oplus\mathbb C.
\]

Set

\[
i_s(1)=(-u_s,1),
\qquad
w_s(1)=(0,-1).
\]

Then directly

\[
D_si_s(1)
=
\binom{0}{-y_s(u_s)}
=w_s f(s).
\]

Thus

\[
D_si_s=w_sf
\]

is exactly the carrier-line divisibility square.  Moreover `i_s` is injective
for every parameter because its evaluation-wall coordinate is identically
one.  At `f(s_0)=0`, the state `(-u_(s_0),1)` is nonzero and lies in
`ker D_(s_0)` without division by the scalar section.

This closes the finite algebraic incidence problem for the bordered
characteristic complex.  It also identifies why the evaluation wall is
essential: even if `u_(s_0)=0`, the carrier-line lift does not vanish.

It does not yet solve the middle-facet Green problem.  The operator `D_s` is
the ordered characteristic border, not the maximal-isotropic conservative
Green differential `C_FP(s)`.  Promotion requires a source-derived chain map

\[
J_s:[V_s\oplus\mathbb C\xrightarrow{D_s}V_s\oplus\mathbb C]
\longrightarrow C_{\rm FP}(s)
\]

that carries `(-u_s,1)` to the Green domain, preserves its wall coordinate and
rigged mate, and commutes with the differentials.  Composing `J_s` with the
explicit `i_s` would give the desired Green incidence.

Accordingly, the earliest missing constructor is refined from an arbitrary
`i_s` to the characteristic-to-Green chain map `J_s`.  At finite cutoff the
source incidence is already canonical; completion and conservative promotion,
not zero-to-state bordering, are the unresolved steps.
