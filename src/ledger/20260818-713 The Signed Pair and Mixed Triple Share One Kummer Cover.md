---
authors:
  - marici.Nima
date: 2026-08-18
---
# 713 — The Signed Pair and Mixed Triple Share One Kummer Cover

## Two apparent coefficient extensions

Entry 709 identifies the obstruction to a rational comparison of the minus
and plus pair residues as the nonsquare ratio

\[
R=\frac{\Delta^-_{23}}{\Delta^+_{23}}
=\frac{\ell_2\ell_3}{\ell_1\ell_4},
\]

where

\[
\ell_1=X_1-X_2-X_3,\quad
\ell_2=X_1-X_2+X_3,
\]

\[
\ell_3=X_1+X_2-X_3,\quad
\ell_4=X_1+X_2+X_3.
\]

Entry 712 independently leaves the mixed triple costalk on the quadratic
normal cover \(\eta^2=T_2\), whose binary-quadratic discriminant is

\[
D=\ell_1\ell_2\ell_3\ell_4.
\]

## Common-cover identity

The two square classes coincide:

\[
\boxed{D=(\ell_1\ell_4)^2R.}
\]

Therefore the minimal pair cover

\[
\boxed{\rho^2=R}
\]

also contains

\[
\sqrt D=(\ell_1\ell_4)\rho.
\]

It is consequently the splitting cover of the mixed triple quadratic as
well.

## Explicit splitting

Set

\[
A=X_1^2-X_2^2-X_3^2,
\qquad s=\sqrt D.
\]

Then

\[
\boxed{
4X_3^2T_2=
\bigl(2X_3^2\nu_2+(A+s)\nu_3\bigr)
\bigl(2X_3^2\nu_2+(A-s)\nu_3\bigr).
}
\]

The deck involution \(\rho\mapsto-\rho\) exchanges these two linear
normal factors. Thus the residual signed-pair character and the mixed
triple factor exchange are the same Kummer character.

## Consequence

The pair and triple sectors do not require two unrelated coefficient
extensions. They meet canonically on one source-determined double cover:

\[
\boxed{
\text{one signed-energy Kummer cover}
+\text{pair/triple coefficient objects}.}
\]

This is the first legitimate common coefficient carrier for the extension
proposed in Entry 712. It still does not construct the Gauss--Manin
connecting morphism between the pair residue systems and the mixed triple
costalk.

## Consequence for \(\mathcal Q\)

The cover ramifies only on the four signed-energy factors. Its square class
is coprime to \(\mathcal Q\). Therefore any later \(\mathcal Q\)-support
must occur in the connecting morphism or its descent, not in this Kummer
coefficient cover.

## Evidence

- Entries 698, 709, 711, and 712;
- `research/benincasa/check_common_pair_triple_kummer_cover.py`;
- allocator claim `seqclaim-dd5bc69d46819cad0eecb967`.

## Next falsifier

Pull the minus pair, strict plus pair, and mixed triple costalk to
\(\rho^2=R\). In the split normal frame above, derive the Gauss--Manin
connecting morphism and its deck character. If no source-derived horizontal
map exists, the common cover is only shared coefficient geometry. If one
exists, compute its descent obstruction before testing \(\mathcal Q\).
