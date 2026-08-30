# The dynamic residue coherencer must induce the normal law

Scope correction: the minimal checker uses a real normal coordinate
\(a\).  On the full spectral plane this coordinate is
\(a=\operatorname{Re}(s)-1/2\), derived from conjugate reciprocal sewing.

## The free-residue defect

Suppose the two sector states \(x_+\) and \(x_-\) have comparison residue
classified by \(r\).  The simplest mapping-cone equations are

\[
x_+-r=0,
\qquad
-x_-+r=0.
\]

They correctly lift scalar cancellation, but their kernel is

\[
x_+=x_-=r.
\]

This kernel exists at every spectral parameter.  The classifier is only the
boundary shadow of the already-dynamical final \(+1\); exact boundary lifting
repairs the zero-to-state typing gap but does not yet identify the coherencer's
normal action.

## The minimum normal action

Let

\[
a=z-\frac12.
\]

The mixed presentation must carry its own normal law.  In the minimal model it
is

\[
ar=0.
\]

The augmented operator is

\[
T_a=
\begin{pmatrix}
1&0&-1\\
0&-1&1\\
0&0&a
\end{pmatrix}.
\]

Its determinant is \(-a\).  Therefore:

- away from the seam, \(T_a\) is invertible and the lifted residue vanishes;
- on the seam, its kernel is the one-dimensional diagonal
  \(x_+=x_-=r\).

The inverse is explicit.  If

\[
T_a(x_+,x_-,r)=(e_+,e_-,e_r),
\]

then

\[
r=\frac{e_r}{a},
\qquad
x_+=e_++\frac{e_r}{a},
\qquad
x_-=-e_-+\frac{e_r}{a}.
\]

Hence the inverse is uniformly bounded on compact sets separated from the
seam.

## Categorical interpretation

This sharpens rather than changes the established meaning of the architecture.
Every \(+1\) is already dynamical, and the third \((3+2+1)\) packet is already
a complete mixed presentation.  The calculation identifies the minimum normal
action that its operative coherencer must induce on the mixed residue.

The two additional incidence legs place the direct and reciprocal states in
that mixed presentation.  The final higher cell must prove that its boundary
classifier and its mixed normal differential are two faces of one coherent
dynamic mapping-cone constructor.

Thus the proposed architecture is genuinely recursive:

\[
\mathcal S_+,
\quad
\mathcal S_-,
\quad
\mathcal S_0,
\]

with two incidence legs into \(\mathcal S_0\), followed by one higher
coherence law.  The third packet is not merely a witness produced by the first
two; it has independent source dynamics.

## DPC gate

The minimal algebra shows exactly which action of the already-dynamical
coherencer must be sourced in theta/Tate:

1. scalar zeros lift to a mixed residue state;
2. the mixed source differential acts by the normal displacement off the seam;
3. its only allowed loss of invertibility occurs at \(a=0\);
4. the resulting inverse margin survives arithmetic completion;
5. hostile symmetric multipliers fail one of these source-level properties.

Writing \(ar\) by hand would simply encode the desired conclusion.  The
normal law must arise from the mixed theta/Tate presentation—for example from
the difference of reciprocal generators or an exact boundary-current identity.

The smallest hostile replaces \(a\) by a fitted function \(\beta(z)\) with an
off-seam zero.  The residue then survives at that zero while both incidence
legs and the scalar lifting law remain unchanged.  This proves that residue
exactness alone does not determine the normal dynamics.

## Verification

`check_rh_residue_normal_law.py` verifies the determinant, off-seam rank,
seam kernel, explicit inverse, and an off-seam fitted-normal-law hostile exactly
over the rationals.
