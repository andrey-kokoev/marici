# Real and reciprocal closure are coherence operations, not automatic complementary observers

## Question

Do the Real mate, reciprocal mate, and dagger mate of an analytic observer automatically provide the complementary channels required for stable reconstruction?

## Claim boundary

No. Real and reciprocal closure generate coherence-related observer copies. They become complementary only if their joint Gramian is coercive. If the original observer is Real or reciprocal invariant, the mate is redundant. Any finite family of such mates remains compact when the original observer is compact, so it cannot restore a completed-source lower margin.

## Problem

Let

\[
A:X\to Y
\]

be a bounded observer. Suppose \(X,Y\) carry conjugations \(J_X,J_Y\), and \(X\) carries a unitary reciprocal involution \(W_X\). Define the Real mate and reciprocal mate by

\[
A^{\#}=J_YAJ_X,
\qquad
A^{\rm rec}=AW_X.
\]

Because these maps are required by coherent Green/Real structure, one might count them as independent complementary observers.

## Bold conjecture

Closing an observer family under Real conjugation, reciprocal exchange, and adjoint automatically supplies stable complementarity.

## Named rivals

1. Real closure is redundant when \(A\) is Real.
2. Reciprocal closure is redundant when \(A\) is reciprocal invariant.
3. Nonredundant mates may reduce the joint kernel but still fail the lower-frame test.
4. Dagger closure changes variance rather than adding a source observation.

## Real-pair Gramian

Define

\[
\mathcal R_Ax=(Ax,A^{\#}x).
\]

Its stability is determined by

\[
S_{\mathcal R}
=A^*A+(A^{\#})^*A^{\#}.
\]

Since \(J_X,J_Y\) are antiunitary conjugations,

\[
\|A^{\#}x\|
=
\|AJ_Xx\|.
\]

If \(A\) is Real,

\[
J_YA=AJ_X,
\]

then

\[
A^{\#}=A
\]

and

\[
S_{\mathcal R}=2A^*A.
\]

Thus Real closure only repeats the same observation and cannot change its kernel or a zero lower modulus.

## Reciprocal-pair Gramian

Define

\[
\mathcal W_Ax=(Ax,AW_Xx).
\]

Then

\[
S_{\mathcal W}
=A^*A+W_X^*A^*AW_X.
\]

This is the two-element symmetry-orbit Gramian. It is coercive exactly when the original and reciprocal observations jointly form a frame.

If

\[
AW_X=V_WA
\]

for a unitary \(V_W\) on \(Y\), then

\[
\|AW_Xx\|=\|Ax\|
\]

and

\[
S_{\mathcal W}=2A^*A.
\]

In that equivariant case reciprocal closure is a target presentation alias, not a new source observer.

## Combined Real-reciprocal family

The finite family

\[
\mathcal C_Ax
=
(Ax,A^{\#}x,AW_Xx,A^{\#}W_Xx)
\]

has Gramian equal to the sum of the four positive mate Gramians. It is a stable complementary family exactly when that sum is bounded below.

If \(A\) is compact, every mate is compact because unitary and antiunitary transport preserves compactness. Therefore \(\mathcal C_A\) is compact. On infinite-dimensional \(X\),

\[
\inf_{\|x\|=1}\|\mathcal C_Ax\|=0.
\]

Finite coherence closure cannot repair completion collapse.

## Dagger qualification

The adjoint

\[
A^*:Y\to X
\]

has reversed source and target. It is not another component of a row observer on \(X\). To use it as a source observation requires a separately declared identification \(X\to Y\) or a state-effect pairing. Without that map, “add the adjoint channel” is a source-target type error.

Likewise the analytic transpose

\[
A^\top:Y^\vee\to X^\vee
\]

belongs to the dual variance. The Real comparison

\[
A^\top=J_XA^*J_Y
\]

is a coherence cell between reverse-variance maps, not a new forward observer.

## Green-boundary worked example

For radial synthesis \(U\), prior work gives

\[
J_HU=UJ_V
\]

and therefore

\[
U^\#=J_HUJ_V=U.
\]

The Real mate is exactly redundant.

The reciprocal swap satisfies

\[
W_u^2=I,
\qquad
W_u^*J_\partial W_u=-J_\partial.
\]

A reciprocal mate may expose the opposite oriented channel if the observer initially reads only one orientation. But once the declared observer already retains both oriented traces and is equivariant under the swap, reciprocal closure only permutes target ports.

The canonical fold

\[
C_uF^2=W_uC_u
\]

proves coherence of this permutation. It does not prove a larger Gramian lower bound.

## Hostile example

Let

\[
Ae_n=\frac1n e_n
\]

on \(\ell^2\), with standard conjugation and any diagonal sign involution \(W_Xe_n=\epsilon_ne_n\). Then

\[
A^\#=A,
\qquad
AW_Xe_n=\frac{\epsilon_n}{n}e_n.
\]

For the full Real-reciprocal family,

\[
\|\mathcal C_Ae_n\|^2=\frac4{n^2}\longrightarrow0.
\]

Every coherence mate is coordinatewise nonzero, yet the joint lower margin vanishes.

## Constructor-role test

The roles are now separated:

- `real_comparison`: identifies conjugate structures;
- `reciprocal_comparison`: intertwines orientation exchange;
- `dagger_mate`: reverses source and target;
- `symmetry_orbit_observer`: precomposes by a source action;
- `complementary_observer`: passes the joint Gramian lower-bound test.

A map may occupy several roles only after satisfying each signature independently. Closure under an involution does not authorize promotion to `complementary_observer`.

## Strongest falsification attempt

In finite dimension, Real or reciprocal mates can remove a kernel when they act nontrivially on source directions. This shows that coherence closure can sometimes produce an operational complement. But the Gramian test, not the existence of the mate, is decisive. On an infinite source with compact \(A\), the finite-family no-go remains absolute.

## Disposition

The bold conjecture is rejected. Green, Real, reciprocal, and dagger closure organize coherent variance and orientation; they do not automatically add stable information. The principal worked example now demonstrates both sides: exact sewing and Real squares are available, while the compact analytic observer still requires a genuinely source-sensitive complementary channel.
