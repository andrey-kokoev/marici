# Two closed-loop exclusion laws collapse and only global small gain remains distinct

## Setup

Let the source-derived boundary loop be

\[
L(z)=C(z)A(z)^{-1}B(z),
\]

with normalized boundary Schur complement

\[
S_{\partial}(z)=I-L(z).
\]

An off-seam zero requires a nonzero boundary state \(v\) satisfying

\[
L(z)v=v.
\]

Three possible source-local exclusion laws were proposed:

1. strict grade raising;
2. strict dissipativity;
3. small gain.

The first two can now be classified before the full theta blocks are available.

## Strict grade raising trivializes the determinant

Assume the boundary carrier has a well-founded grading

\[
\mathcal B=\bigoplus_{n\ge0}\mathcal B_n
\]

and \(L\) strictly raises degree:

\[
L\mathcal B_n
\subseteq
\bigoplus_{m>n}\mathcal B_m.
\]

At every finite graded cutoff, \(L\) is strictly triangular. Hence

\[
\operatorname{Tr}(L^k)=0
\]

for every \(k\ge1\), and

\[
\det(I-L)=1.
\]

If the completed loop is trace class and the cutoff determinants converge compatibly, the Fredholm determinant remains

\[
\det(I-L)=1.
\]

Therefore a strictly grade-raising loop cannot carry a nontrivial completed determinant section. If all of \(\Xi\) is moved into the direct block \(D(z)\), the loop no longer explains the divisor and the construction becomes scalar packaging.

Strict grading may organize the open arithmetic transport, but it cannot be the full closed boundary loop law.

## Strict dissipativity returns to the boundary positivity criterion

Suppose

\[
\operatorname{Re}
\langle v,S_{\partial}(z)v\rangle
>0
\]

for every nonzero admissible boundary state in an open half-plane.

Then \(S_{\partial}(z)\) has no kernel there. This is a valid sufficient law.

But after scalar projection onto the distinguished boundary line, it becomes positivity of the completed boundary response. That is the Herglotz, Pick, or Weil orientation already known to be RH-equivalent.

Therefore dissipativity is explanatory only if it is proved on a richer source-derived boundary module through an operator identity that:

- exists before the determinant section;
- survives hostile signed prime perturbations for a source-specific reason;
- does not reduce to positivity of the scalar completed logarithmic derivative;
- retains endpoint, gamma, and prime channels as one coupled form.

No such richer identity is currently constructed.

## Small gain remains logically distinct

If

\[
\|L(z)\|<1,
\]

then \(1\) is excluded from the spectrum and \(I-L(z)\) is inverted by the Neumann series

\[
(I-L(z))^{-1}
=
\sum_{n\ge0}L(z)^n.
\]

This supplies an explicit contraction without dividing by \(\Xi\). It is therefore a genuinely noncircular mechanism if the norm bound is derived from the source realization.

However, it cannot be proved factorwise. Grothendieck's one-place Julia calculation already produces off-seam local defects whose variance changes with vertical height. Local positivity or contraction does not survive as a uniform prime-by-prime law.

Any viable bound must emerge only after the complete reciprocal, seam, primitive, square, and archimedean incidence is assembled.

## Reciprocal constraint

A source-derived loop must also respect reciprocal sewing. Typically the two open sectors carry opposite transport orientations. A contraction estimate may hold in the inward direction of each sector while its reciprocal transport is expansive.

Therefore the correct test is not one norm inequality imposed on the same directed loop across both half-planes. It is a typed pair (L_+(z)) and (L_-(z)), with the reciprocal comparison map declared. Each estimate must be applied in its own causal direction.

Smearing those directed loops into one scalar operator can create a false contradiction or a false contraction.

## Finite decision procedure

After \(A_X,B_X,C_X,D_X\) are source-derived at a labelled cutoff, compute:

\[
L_X=C_XA_X^{-1}B_X.
\]

Then test, in this order:

1. Schur reconstruction:
   \[
   S_{\partial,X}=D_X-C_XA_X^{-1}B_X.
   \]

2. Directional reciprocal typing of \(L_{+,X}\) and \(L_{-,X}\).

3. Largest singular value:
   \[
   \sigma_{\max}(L_{\pm,X}).
   \]

4. Smallest dissipativity eigenvalue of \(I-L_{\pm,X}\).

5. Grade-diagonal entries and traces of powers, to reject a falsely strict triangular claim.

The first cutoff with \(\sigma_{\max}\ge1\) falsifies uniform small gain for that norm. A cutoffwise bound approaching \(1\) does not establish completion-stable contraction.

## Disposition

Strict grade raising is incompatible with a nontrivial loop determinant. Strict dissipativity currently returns to the RH-equivalent completed boundary positivity problem.

Global, directionally typed small gain is the only remaining independently formulated exclusion law. It must be tested on the complete source-derived Schur realization, not on local Euler factors or the open Volterra bulk.
