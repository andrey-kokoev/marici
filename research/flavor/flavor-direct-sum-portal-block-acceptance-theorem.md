# Direct-sum portal-block acceptance theorem: WP730

## Question

What must the linearized portal block of the simultaneous singlet-plus-triplet
source satisfy so that WP729's additive representation contrast becomes a
prediction rather than a relevant-direction or cross-coupling artifact?

## Unavoidable mixed scalar channel

Let the two representation-labelled scalar norms be (R_A) and (R_B).
Even if additional gradings forbid bilinear mixing of the scalar fields, the
renormalizable operator

\[
R_AR_B
\]

is neutral under every independent phase or sign assigned to the two sectors.
It is therefore part of the generic direct-sum scalar grammar. The portal beta
functions must be linearized as a coupled block, not as two independent copies
of the published single-model equation.

Write that block at the candidate fixed point as

\[
\beta_p=Mp-b,
\qquad
M=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
4q_A\\
3q_B
\end{pmatrix}.
\]

The vector (b) is WP729's representation-oriented additive source. The
off-diagonal coefficient (c) includes the effect of the mixed scalar
channel; (a) and (b) are the diagonal portal slopes. These letters denote
local beta coefficients and are not yet values derived from the full model.

## Exact fixed contrast

For

\[
D=ab-c^2\ne0,
\]

the unique fixed portal pair is

\[
p_*=rac1D
\begin{pmatrix}
4bq_A-3cq_B\\
3aq_B-4cq_A
\end{pmatrix}.
\]

Its ordered contrast is

\[
\Delta_*=
\frac{4q_A(b+c)-3q_B(a+c)}{ab-c^2}.
\]

Thus the cross-coupling changes both magnitude and the cancellation locus.
Whenever the denominator is defined and (a+c\ne0), the exact positive
cancellation fiber is

\[
\frac{q_B}{q_A}=\frac{4(b+c)}{3(a+c)}.
\]

No claim that representation coefficients alone fix the contrast survives
this fiber.

## RG-basin conditions

For a real symmetric two-portal block, both portal fluctuations are irrelevant
exactly when (M) is positive definite:

\[
a>0,
\qquad
ab-c^2>0.
\]

Then the fixed pair is unique within the portal block and no free portal
deformation reaches the infrared contrast. This does not eliminate relevant
directions elsewhere in the full coupling system; their threshold image must
still be tested.

If one portal eigenmode is relevant, the contrast remains predicted only when
that eigenvector is annihilated by the contrast covector (d=(1,-1)). For the
exchange-form diagonal (a=b=A), the even and odd eigenvectors are

\[
v_+=(1,1),
\qquad
v_-=(1,-1),
\]

with exponents (A+c) and (A-c). A relevant even mode is invisible to the
contrast, while a relevant odd mode makes the contrast a free UV-critical
surface coordinate.

Two exact witnesses separate these cases:

- (A=1,c=-2): the even exponent is (-1), the odd exponent is (3), and the
  relevant deformation changes only the portal sum;
- (A=1,c=2): the even exponent is (3), the odd exponent is (-1), and the
  free relevant amplitude changes the contrast directly.

For non-isomorphic sectors, equality of diagonal slopes is not automatic.
Hence the full stability eigenvectors, not the signs of diagonal entries, are
the authoritative basin test.

## Disposition

WP730 upgrades the WP729 candidate to an exact RG acceptance theorem. A
simultaneous source predicts the portal contrast only if:

1. (D\ne0) and (Delta_*\ne0);
2. every relevant eigenvector of the complete stability matrix has zero
   contrast projection, or no portal-visible relevant eigenvector exists;
3. the scalar fixed point lies in the strict stability cone; and
4. relevant directions outside the portal block do not re-enter the contrast
   through threshold matching.

The theorem neither supplies nor fits (a,b,c,q_A,q_B). Those coefficients
must be calculated from the complete simultaneous matter action. Its smallest
exact falsifiers are the shifted cancellation fiber above and a relevant odd
eigenvector.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp730_direct_sum_portal_block_acceptance.py`

Generated result: `results/wp730_direct_sum_portal_block_acceptance.json`.
