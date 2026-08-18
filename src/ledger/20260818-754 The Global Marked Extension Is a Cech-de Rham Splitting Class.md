---
authors:
  - marici.Nima
date: 2026-08-18
---
# 754 — The Global Marked Extension Is a Čech–de Rham Splitting Class

## Retyping the frontier

After Entry 752 the object to classify is

\[
0\longrightarrow E:=\mathbb V_{\rm ell}(-1)
\longrightarrow V:=\mathbb V_{\triangle}
\longrightarrow T:=\mathcal T
\longrightarrow0,
\]

without using \(\mathcal Q\) as support.  In a Gysin-adapted frame write

\[
\nabla_V=
\begin{pmatrix}
\nabla_T&0\\
C&\nabla_E
\end{pmatrix}.
\]

A splitting gauge \(X:T\to E\) must solve

\[
\boxed{
\nabla_{\operatorname{Hom}}X
:=dX+A_EX-XA_T=-C.
}
\]

Entry 721's pole-free polynomial search through degree ten tests only one
bounded class of global solutions.  Entries 724--725 show that the residue
equation has no local obstruction, but residue solvability is not a local
splitting and does not imply global descent.

## Intrinsic Čech class

Choose a predeclared cover \(\{U_i\}\) on which actual meromorphic/logarithmic
solutions \(X_i\) of the complete two-direction equation have been derived.
On overlaps,

\[
g_{ij}=X_i-X_j
\]

satisfies

\[
\nabla_{\operatorname{Hom}}g_{ij}=0,
\qquad
g_{ij}+g_{jk}+g_{ki}=0.
\]

Thus \(\{g_{ij}\}\) represents

\[
[V]\in
\mathbb H^1\!\left(
B,
\operatorname{DR}\operatorname{Hom}(T,E)
\right).
\]

Changing the local splittings adds a Čech coboundary.  Hence this class—not
the numerator or denominator of any chosen \(X_i\)—is the global invariant.

Equivalently, the extension splits exactly when there exists a global
horizontal idempotent projector on \(V\) whose image is \(E\).  This gives a
basis-independent cross-check on any Čech computation.

## Required cover

The cover must be built only from source divisors already present in the
adapted connection.  The three positive-resonance divisors

\[
D_1=(v-u),\qquad D_2=(y-u^2),\qquad D_3=(y+u^2)
\]

require their resolved logarithmic charts.  The other ordinary source
divisors may enter as localization denominators.  Neither \(P_6\) nor
\(\mathcal Q\) may be inserted as a fitted support for the extension:
Entry 725 found no extension residue on either.

## Immediate consequence

The currently certified data do **not** yet establish either splitting or
nonsplitting:

- absence of a polynomial solution through degree ten is bounded;
- vanishing residue obstruction is necessary but insufficient;
- the principal-cell Čech quotient of Entries 736--744 is supported
  indicial data, not the generic extension class above.

## Narrow conclusion

\[
\boxed{
\text{the next invariant is the Čech--de Rham class of complete local
splittings on the ordinary resolved divisor cover.}
}
\]

## Evidence

- Entries 721--725, 729--744, and 752;
- `research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`;
- `research/benincasa/marici-gm/gysin-polynomial-split-d10.json`;
- `research/benincasa/marici-gm/gysin-local-residue-obstruction-16.json`;
- allocator claim `seqclaim-0a12a4f46e8ba0b86f4ec1f9`.
- epistemic event
  `ev-000000000368-4683a247-e25b-4b60-ab95-70a4a876cb05`.

## Next finite falsifier

Derive complete local solutions \(X_i\) on the three resolved resonant
charts with a fixed logarithmic pole bound.  Compute every overlap
difference by exact matrix algebra, then test whether the resulting cocycle
is a coboundary.  Independently solve the horizontal-idempotent equations
with the same pole bound.  Agreement of the two tests is required.
