# The Conditional Residual Is Controlled by a Projective Port Ratio

Grothendieck's conditional residual has a positive constant repair proportional
to one source port and a negative first drift proportional to another. The
minimal abstract form is

\[
R(x;\alpha,\beta)
=\beta J(x)-\alpha xK(x),
\]

where \(\alpha,\beta>0\) and \(J,K>0\) on the relevant block.

The scale of \((\alpha,\beta)\) is irrelevant to the sign. The compiler
coordinate is the projective ratio

\[
r=\frac\beta\alpha.
\]

Then

\[
R(x;\alpha,\beta)>0
\quad\Longleftrightarrow\quad
r>\frac{xK(x)}{J(x)}.
\]

## Pointwise block gate

On a compact interval \(I\), pointwise positivity is equivalent to

\[
r>ho_{\mathrm{pt}}(I),
\qquad
\rho_{\mathrm{pt}}(I)
=\sup_{x\in I}\frac{xK(x)}{J(x)}.
\]

If \(J(x)\ge j>0\) and \(K(x)\le k\), an explicit protected entrance is

\[
0\le x<\frac{\beta j}{\alpha k}.
\]

Its width scales as \(\beta/\alpha\), exactly as Grothendieck observed.

## Integrated block gate

Let \(w(x)>0\) be the source-authorized block weight. The integrated residual
is

\[
\mathcal R_I
=\int_Iw(x)R(x;\alpha,\beta)\,dx.
\]

It is positive if and only if

\[
r>ho_{\mathrm{int}}(I,w),
\]

where

\[
\rho_{\mathrm{int}}(I,w)
=
\frac{\int_Iw(x)xK(x)\,dx}
{\int_Iw(x)J(x)\,dx}.
\]

Because a weighted average is bounded by the supremum,

\[
\rho_{\mathrm{int}}\le\rho_{\mathrm{pt}}.
\]

Thus block integration can repair a pointwise sign failure. It cannot remove
the need for a lower bound on \(r\).

## Exact minimal fixture

For

\[
J=K=w=1,
\qquad
I=[0,L],
\]

one has

\[
R(x)=\beta-\alpha x.
\]

The protected pointwise width is exactly

\[
\frac\beta\alpha.
\]

Pointwise positivity on the whole block requires

\[
\frac\beta\alpha>L,
\]

while integrated positivity requires only

\[
\frac\beta\alpha>\frac L2.
\]

At \(\beta=0\), both pointwise and integrated residuals are negative away from
the entrance. Hence no strictly positive theorem can be uniform over the
closed quadrant \(\alpha,\beta\ge0\).

## Source-fixed port relation

The completion-ready theorem must derive a source relation

\[
\beta_X\ge r_*\alpha_X
\]

with \(r_*>0\) independent of cutoff and

\[
r_*>sup_X\rho_{\mathrm{int},X}
\]

for the integrated target, or the corresponding pointwise supremum for a
pointwise claim.

This relation cannot be synthesized by the compiler. It must follow from the
typed incidence, normalization, or constructor coupling between the two ports.

## Falsifiers

- The admitted face \(\beta=0\) in a strict-positivity claim.
- A sequence \(\beta_X/\alpha_X\to0\).
- A block with threshold exceeding the source-fixed ratio.
- Proving integrated positivity and reporting pointwise positivity.
- Choosing the block weight after inspecting the residual sign.
- Treating independent positive ports as if positivity coupled their ratio.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to type the nonuniform entrance phenomenon and determine
what block integration can genuinely repair.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The exact variable is the projective port ratio; pointwise and
integrated thresholds are explicit, and source coupling is the sole remaining
authority-bearing input.
