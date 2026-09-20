# Higher-coherence topology iteration 47: a normal Weyl commutator can exclude Xi torsion only with uniform analytic-vector control

## Candidate topology

Near a simple Xi zero choose a normal coordinate `u` with `tau=u v`, where `v`
is a unit. Let

\[
U:q\mapsto uq,
\qquad
D=\nabla_{\partial_u}.
\]

On a horizontal quotient these satisfy the normal Weyl relation

\[
[D,U]=1.
\]

Equip the codiagonal cokernel with a graph topology controlling both `U` and
all powers of `D`. This is the local positive-commutator topology associated to
the Xi normal direction.

## Algebraic iteration

If `Uq=0`, then

\[
q=[D,U]q=-U Dq.
\]

Repeated use of the Weyl relation gives

\[
q=\frac{(-1)^n}{n!}U^nD^nq
\qquad(n\ge1).
\]

Thus a torsion vector must be infinitely divisible in the normal filtration,
with derivatives growing rapidly enough to compensate the factor `U^n/n!`.

## Quantitative exclusion

Suppose the source topology gives analytic-vector bounds

\[
\|D^nq\|_r\le C A^n n!\,\|q\|_{r'}
\]

and multiplication by `u` contracts on a sufficiently small neighborhood:

\[
\|U^nh\|_r\le\rho^n\|h\|_r,
\qquad \rho A<1.
\]

Then

\[
\|q\|_r
\le C(\rho A)^n\|q\|_{r'}
\longrightarrow0,
\]

so `q=0`. This is a concrete analytic version of the connection/separatedness
argument and would kill `[H_border]` noncircularly.

## Why ordinary positivity is insufficient

A positive-commutator slogan does not provide the estimates above. Delta
vectors satisfy `U delta=0` and have derivatives of factorially worsening
order; they lie outside the controlled analytic-vector class. The topology
must prove that the bordered cokernel class belongs to the good graph domain.

Likewise, an estimate only at each finite cutoff is insufficient if `A` grows
with the cutoff or the admissible radius `rho` shrinks to zero.

## Source compatibility

On labelled Köthe coefficients,

\[
D f_\lambda
=
\partial_u f_\lambda-(\partial_u z)L_\lambda f_\lambda,
\]

and the `L_lambda` multiplier consumes exponential order. The projective
seminorm family can absorb each finite derivative, but a uniform analytic-
vector estimate requires control of all seminorm losses simultaneously.

Endpoint traces and Green closure must share this graph domain. Existing
commutator estimates for localized Hardy or sewing operators do not yet imply
the Xi-normal estimate on the codiagonal cokernel.

## Escape-function formulation

More generally, if a source-derived pseudodifferential commutant `A` has
principal symbol increasing along the characteristic flow at `N^*Z`, a uniform
estimate

\[
\|q\|_{\mathcal X}
\le C\bigl(\|Pq\|_{\mathcal Y}+\|q\|_{\rm lower}\bigr)
\]

can exclude a conormal nullstate. But no governing operator `P` with this
escape sign has yet been extracted from the bordered comparison. Choosing `P`
from the desired residual would be circular.

## Verdict for topology 47

Microlocal energy topology yields a sharp sufficient mechanism: the normal
Weyl relation plus cutoff-uniform analytic-vector bounds forbids Xi torsion.
The algebraic commutator is available formally; the required uniform graph
estimate and common Green domain are not established.

The next nonredundant topology to test is a bornological/inductive-limit
topology, asking whether bounded-disk control can make these all-order
commutator estimates uniform without demanding one impossible Hilbert norm.