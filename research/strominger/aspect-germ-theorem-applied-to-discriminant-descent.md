# Aspect's germ theorem applied to discriminant descent

## The theorem used

Aspect's exact selection theorem says that a target multilinear relation may
be formed after local quotient maps (q_i) exactly when it annihilates every
local kernel direction.  In the one-input linear case, a target 

\[
b:X\longrightarrow Y
\]

factors through (q:X\to Q) exactly when

\[
\ker q\subseteq\ker b.
\]

The form needed here is the kernel-pair version, valid without linearizing the
space of constructors:

\[
b=\bar b\,q
\quad\Longleftrightarrow\quad
q(x)=q(y)\Rightarrow b(x)=b(y).
\]

Thus a local completion is legal precisely when the later construction is
constant on every fiber of that completion.

## Marked coefficient germs

Fix the magnetic affine frame and free reflection orbit:

\[
F=\begin{pmatrix}2&7\\3&7\end{pmatrix},
\qquad
D_F=\operatorname{coker}F\cong\mathbb Z/7,
\qquad
\widetilde{\mathbb Z}[O]=\mathbb Z e,
\quad \tau e=-e.
\]

The marked germ is not merely the underlying tensor product.  It is

\[
G_\alpha=(D_F,O,e,\alpha),
\]

where 

\[
\alpha:D_F\to D_F,
\qquad \alpha^2=1,
\]

is the coefficient involution.  Its unconsumed comparison port is the relative
parity law

\[
r_\alpha=-\alpha
\]

on (D_F\otimes\mathbb Ze).

## The premature completion

Let

\[
q(G_\alpha)=(D_F,O,e)
\]

forget the coefficient involution.  In particular,

\[
q(G_{+})=q(G_{-}).
\]

This is the analogue of consuming Aspect's comparison port: it preserves the
frame, modulus, orbit and anti-diagonal coordinate, but deletes the datum
required to combine their parities.

## The outer relational mate

Let the later target construction be reflection descent:

\[
b(G_\alpha)
=\left(D_F\otimes\widetilde{\mathbb Z}[O]\right)^{C_2}.
\]

For the two coefficient parities,

\[
b(G_+)=0,
\qquad
b(G_-)=D_F\cong\mathbb Z/7.
\]

The two marked germs lie in one fiber of (q), while their target descents are
not equal and do not even have the same cardinality.  Hence (b) is not
constant on the kernel pair of (q).  By Aspect's theorem, no downstream
constructor on the bare tensor object can reconstruct reflection descent.

## Required architecture

The coefficient germ and the orbit germ must be sewn before equivariant
completion:

```text
affine discriminant germ -- coefficient involution --\
                                                   relative-parity mate
free orbit germ ---------- orbit orientation ------/
                                                        |
                                                        v
                                              invariant or coinvariant descent
```

The mate computes the diagonal action

\[
r_\alpha=\alpha\otimes\chi_O.
\]

Only after this action is typed may invariants, coinvariants, or a phase-valued
readout be formed.  The correct logical precedence is therefore

```text
retain coefficient parity
form relative-parity mate
choose descent variance
form phase port, if separately authorized
```

This is logical dependence between partial constructors, not chronological
order.

## What the theorem repairs

Aspect's theorem resolves the architectural obstacle:

- it identifies the first nonfaithful arrow as forgetting 
  `coefficient_involution`;
- it proves that the missing datum cannot be restored from the bare tensor;
- it places the relative-parity mate before reflection descent;
- it explains why determinant and anti-diagonal incidence are insufficient
  even though both are exact.

It does not derive whether the magnetic source chooses 

\[
\alpha=+1
\quad\text{or}\quad
\alpha=-1.
\]

That remains the smallest source-side calculation.  One must compute how the
universal cocircuit generator, equivalently the class detected by

\[
\ell(x,y)=3x-2y\pmod7,
\]

transforms under the actual reflection lift.  Aspect's theorem says exactly
why this calculation is indispensable and where its answer must enter.

## New falsifier

Any proposed physical seven-valued port that depends only on

```text
determinant = 7
free orbit = two sheets
reduced route = anti-diagonal
```

must give the same answer on (G_+) and (G_-).  Exact descent gives different
answers.  Such a proposal is therefore rejected before positivity,
normalization, or instrument accessibility is considered.

