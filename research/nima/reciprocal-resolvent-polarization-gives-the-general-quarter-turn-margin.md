# Reciprocal resolvent polarization gives the general quarter-turn margin

## Reciprocal auxiliary pair

On reduced auxiliary support, let

\[
D_{+}=S+iT,
\qquad
D_{-}=S-iT,
\]

where \(S=S^{*}>0\) and \(T^{*}=-T\) in the real carrier presentation. Reciprocal reflection exchanges \(D_{+}\) and \(D_{-}\).

Normalize the odd component by

\[
K=S^{-1/2}(iT)S^{-1/2}.
\]

Then \(K=K^{*}\), and

\[
D_{\pm}
=
S^{1/2}(I\pm K)S^{1/2}.
\]

Therefore both reciprocal blocks are positive precisely when

\[
-I<K<I
\]

as forms on reduced support. Uniform reciprocal positivity is the contraction condition

\[
\|K\|\le1-\varepsilon.
\]

This is the operator generalization of \(s>|\tau|\) in the minimal two-dimensional cell.

## Even and odd resolvent polarization

Define

\[
R_{\mathrm{ev}}
=
\frac12(D_{+}^{-1}+D_{-}^{-1}),
\qquad
R_{\mathrm{odd}}
=
\frac1{2i}(D_{+}^{-1}-D_{-}^{-1}).
\]

The resolvent identity gives

\[
R_{\mathrm{odd}}
=
-D_{+}^{-1}TD_{-}^{-1}.
\]

In normalized coordinates,

\[
R_{\mathrm{ev}}
=
S^{-1/2}(I-K^2)^{-1}S^{-1/2},
\]

and

\[
\frac12(D_{+}^{-1}-D_{-}^{-1})
=
-S^{-1/2}K(I-K^2)^{-1}S^{-1/2}.
\]

The formulas are valid because both terms are functions of the same self-adjoint \(K\). They separate even propagation from reciprocal orientation without choosing a basis for the \(K\)-\(V\) carrier.

For real endpoint incidence \(C\), the two compressed Schur returns are

\[
Q_{\pm}=CD_{\pm}^{-1}C^{*}.
\]

Their reciprocal-even and reciprocal-odd parts are obtained by compressing the corresponding resolvent polarizations. Hence the Euler odd coordinate must be identified with the endpoint matrix coefficient of the compressed odd resolvent, not with a free imaginary Gram parameter.

## Domination theorem

For every spectral value \(\lambda\in(-1,1)\),

\[
\left|
\frac{\lambda}{1-\lambda^2}
\right|
\le
\|K\|
\frac1{1-\lambda^2}.
\]

Functional calculus therefore gives the form inequality

\[
\left|
K(I-K^2)^{-1}
\right|
\le
\|K\|(I-K^2)^{-1}.
\]

After congruence by \(S^{-1/2}\) and endpoint compression, the odd return is dominated by the even return with relative constant \(\|K\|\). This is the general operator form of the finite area-energy bound.

It yields two distinct quantitative requirements:

- orientation margin:
  \[
  1-\|K\|>0;
  \]
- absolute resolver control:
  bounds on \(S^{-1/2}\), \(C\), and \((I-K^2)^{-1}\).

The first does not imply the second if the even metric scale degenerates.

## Radical-safe version

If \(S\) is only semidefinite, the construction must first pass to its quotient support. The necessary compatibility is

\[
\ker S\subseteq\ker T
\quad\text{and}\quad
\ker D_{\pm}\subseteq\ker C.
\]

Only then may reduced inverses or pseudoinverses be used. A formal \(K\) built with an undeclared pseudoinverse is not a source constructor.

## Reciprocal reflection test

The reflection law must satisfy

\[
\mathscr R S\mathscr R^{*}=S,
\qquad
\mathscr R T\mathscr R^{*}=-T,
\]

and consequently

\[
\mathscr R K\mathscr R^{*}=-K.
\]

It exchanges \(Q_{+}\) and \(Q_{-}\), fixes the even compressed return, and reverses the odd return. This is a stronger test than verifying only the sign of one endpoint matrix entry.

## Hostiles

1. **One-sided positivity:** \(D_{+}\ge0\) but \(D_{-}\not\ge0\). One sheet is valid while reciprocal sewing fails.
2. **Odd domination failure:** a fitted endpoint odd current exceeds the compressed even resolvent budget. No positive reciprocal auxiliary pair realizes it.
3. **Scale collapse:** \(\|K\|\) stays below one while \(S^{-1/2}\) diverges.
4. **Radical rotation:** the kernels of \(D_{+}\) and \(D_{-}\) are not annihilated by the same endpoint incidence.
5. **Reflection defect:** an involution flips the observed scalar current but does not conjugate \(K\) to \(-K\).

## Next source theorem

Derive \(S_p,T_p,C_p\) and the reciprocal reflection on the tail/PV carrier. Then prove the normalized odd operator

\[
K_p=S_p^{-1/2}(iT_p)S_p^{-1/2}
\]

is a strict contraction uniformly on compact off-seam regions. The scoped Euler odd current must arise from compression of its odd resolvent polarization. This converts the minimal area identity into a basis-free operator theorem.
