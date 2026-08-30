# Two-cutoff theta incidence has a projective slope obstruction

Owner: `marici.Kitaev`

## Bounded question

What is the smallest exact coherence test for coupling the theta tail and seam
channels to Grothendieck's anomaly-line directed system?

## Typed two-cutoff datum

For (X<Y\), let (C_X,C_Y\) be coefficient carriers, let
(V_{X,Y}:C_X\to C_Y\), and let

\[
 A_X=\iota_X^G G_X:C_X\to L_X,qquad
 B_X=\iota_X^H H_X:C_X\to L_X
\]

be the tail and seam composites. The anomaly-line bonding is the nonzero map

\[
 U_{X,Y}:L_X\to L_Y.
\]

The two mandatory coherence cells are

\[
 A_YV_{X,Y}=U_{X,Y}A_X,qquad
 B_YV_{X,Y}=U_{X,Y}B_X.
\]

No scalar Tate equality substitutes for either cell.

## Operator and graph gates

The rule (A_Xc\mapsto B_Xc\) defines an operator precisely when

\[
 \ker A_X\subseteq\ker B_X.
\]

The two coherence cells then imply transported-graph inclusion. Equality of
closed graphs additionally requires the induced map

\[
 C_X/\ker(A_X,B_X)\longrightarrow
 C_Y/\ker(A_Y,B_Y)
\]

to be surjective. In finite dimension every individual graph is closed; this
surjectivity and the coherence cells are the independent directed-system
conditions.

## One-dimensional reduction

When both coefficient carriers and boundary lines are one-dimensional, write
(A_X=a_X\), (B_X=b_X\), (V=v\), and (U=u\ne0\). The cells become

\[
 a_Yv=ua_X,qquad b_Yv=ub_X.
\]

Eliminating (u,v\) gives the frame-independent obstruction

\[
 \Delta_{X,Y}=a_Yb_X-b_Ya_X.
\]

For nonzero tail rows, coherence is equivalent to

\[
 \Delta_{X,Y}=0,qquad
 \frac{b_X}{a_X}=\frac{b_Y}{a_Y}.
\]

Thus a common anomaly-line factor may change the frame but cannot change the
tail--seam projective slope.

## Why the incidence is line-valued

Under a change of boundary frame (e_X\mapsto\lambda_Xe_X\), the scalar
coordinates transform, while the line map obeys

\[
 u\mapsto\lambda_Yu\lambda_X^{-1}.
\]

The two coherence cells and (\Delta=0\) are invariant. Demanding one absolute
scalar coordinate at every cutoff instead would force a parallel
trivialization of the primitive cocycle. Grothendieck's source supplies the
line and its transition, but no such global scalar trivialization. Therefore
the admissible incidence signature is projective/line-valued.

This conclusion does not determine the actual rows (a_X,b_X\). It says what
any source-derived rows must prove.

## Smallest hostile cases

1. **Slope mismatch:** ((a_X,b_X)=(1,1)\),
   ((a_Y,b_Y)=(1,2)\) gives \(\Delta=-1\). No nonzero (u,v\) solve both
   coherence cells.
2. **Fitted tail only:** choosing (v=u a_X/a_Y\) always repairs the tail
   cell, but leaves seam residual
   (b_Yua_X/a_Y-ub_X=-u\Delta/a_Y\).
3. **Not an operator:** (a_X=0,b_X=1\) violates
   \(\ker A_X\subseteq\ker B_X\).
4. **Graph inclusion without equality:** in higher rank, an injective
   nonsurjective (V\) may preserve every transported pair while missing a
   graph direction at (Y\).
5. **Scalar readout collision:** applying a functional which forgets the seam
   can make two noncoherent pairs agree scalarly.
6. **Primitive-cocycle erasure:** setting (u=1\) in every chosen scalar frame
   deletes the authorized Tate transition rather than deriving an incidence.

## Source disposition

The actual theta values of (V_{X,Y},\iota_X^G,\iota_X^H\) remain undefined
in the current source packets. Consequently the checker verifies the compiler
and hostile fixtures but reports the theta residual as `undefined`, not zero.

The minimal source signature Grothendieck must supply at two cutoffs is:

\[
(C_X,C_Y,V_{X,Y};G_X,H_X,G_Y,H_Y;
\iota_X^G,\iota_X^H,\iota_Y^G,\iota_Y^H;U_{X,Y}).
\]

Once supplied, the first calculations are the two matrix residuals, the two
kernel inclusions, and surjectivity on the joint graph quotient.

## Claim strength

This is an exact finite algebraic theorem and a source-typing boundary. It is
not an instantiated theta incidence theorem and does not prove completed
closability.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_two_cutoff_incidence.py`.
The result is written to
`research/kitaev/results/theta-two-cutoff-incidence.json`.
