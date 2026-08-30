# The bordered zero complex is stably the scalar readout unless typing blocks elimination

Author: `marici.Nima`

Date: 2026-08-26

Status: exact stable-equivalence no-go and boundary-defect gate

## Universal triangular reduction

Let (u=Mx), (f=y(u)), and

\[
D=
\begin{pmatrix}
I&u\\
y&0
\end{pmatrix}.
\]

Define two triangular transformations

\[
L=
\begin{pmatrix}
I&0\\
-y&1
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
I&-u\\
0&1
\end{pmatrix}.
\]

Both are invertible for every (u) and (y). Their inverses are obtained by
reversing the off-diagonal signs. Neither transformation divides by (f).

Direct multiplication gives

\[
LDR=
\begin{pmatrix}
I&0\\
0&-f
\end{pmatrix}.
\]

Therefore the bordered complex is stably equivalent to a contractible
identity complex plus the one-dimensional complex defined by multiplication
by (-f).

## Exact consequence

At the level of unrestricted finite-dimensional linear algebra, the bordered
construction contains exactly the same cohomology as the scalar readout. It
does not create an independent obstruction or an independent contraction.

The explicit kernel state at (f=0) is real and forward-derived, but the
stable reduction shows that it is the scalar zero written in a larger
presentation.

This is a useful bridge, not yet an RH explanation.

## Where new information can enter

The reduction becomes nontrivial only if one of the triangular maps is not an
admitted equivalence in the source category. This can happen when:

- (u=Mx) does not define a continuous column on the completed carrier;
- (y) is an unbounded boundary trace;
- the source and observer live in different rigged levels;
- the seam current prevents the row elimination from preserving domains;
- arithmetic completion makes the inverse triangular map discontinuous;
- the transformations erase a typed primitive or square-current port.

In that case, the residual failure of (LDR) to descend is the candidate
source-local invariant. The analytic content would live in the obstruction to
Gaussian elimination, not in the formal bordered determinant.

## Categorical formulation

In an ordinary additive category with all four block maps admitted, the
bordered object splits as

\[
D\simeq I_V\oplus(-f).
\]

In the typed partial category, this equivalence exists only if (L), (R),
and their inverses preserve signatures, domains, boundary support, and
completion topology.

Thus the next RH question is exact:

> Does source-typed Gaussian elimination of the theta bordered operator
> descend through the adelic and boundary completion?

If yes, the bordered route collapses to the RH-equivalent scalar section and
must close. If no, the first failed triangular block identifies the missing
boundary coherencer.

## Control-theory interpretation

The bordered matrix is a static Rosenbrock system matrix. The scalar (f) is
its ordered transmission. A zero of (f) is a transmission zero with a
nontrivial internal zero state.

The triangular reduction is the finite analogue of eliminating internal
state. In infinite-dimensional control, boundary control and observation may
be unbounded, so this elimination can fail to preserve the system domain.
That is precisely the already observed theta seam and trace obstruction.

The unexpected control-theory appearance is therefore structural rather than
metaphorical: RH has become a question about whether a source-derived
boundary system has off-seam invariant zeros after admissible state
elimination.

## Finite falsifier

Any claim that the bordered lift by itself adds RH information is falsified by
the exact triangular reduction. Any claim that a boundary obstruction saves
the route must identify the first map among (L), (R), (L^{-1}), and
(R^{-1}) that fails to descend, together with a domain witness.

