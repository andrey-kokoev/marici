# Type-fiber Adams lifts are functors on the divisibility action category

## The remaining datum

The moving-seam and Euler half-density layers determine the geometric and
scalar parts of Adams transport. The unresolved type-fiber datum has a precise
minimal form: it is a functor on the action category of the multiplicative
monoid of positive integers acting on prime-power grades.

Let the objects be grades \(k\ge1\). For every \(r\ge1\), there is an arrow

\[
(r,k):k\longrightarrow rk.
\]

Composition is

\[
(s,rk)\circ(r,k)=(sr,k).
\]

For a type fiber \(F_{p,k}\) at the prime-power port \((p,k)\), an Adams lift is
therefore a family

\[
A_{r;p,k}:F_{p,k}\longrightarrow F_{p,rk}
\]

satisfying

\[
A_{1;p,k}=1
\]

and

\[
A_{s;p,rk}A_{r;p,k}=A_{sr;p,k}.
\]

These are exactly the identity and composition laws for a functor from the
divisibility action category to the declared category of type fibers.

## Assembly criterion

Let \(T_{r;k}\) denote moving-seam transport from the cut at \(k\log p\) to the
cut at \(rk\log p\), and let \(M_{\rho_r(p,k)}\) be multiplication by

\[
\rho_r(p,k)=\frac1r p^{-(r-1)k/2}.
\]

Define the candidate full lift

\[
\Psi_{r;p,k}
=
M_{\rho_r(p,k)}
\otimes T_{r;k}
\otimes A_{r;p,k}.
\]

The seam transport and coefficient residue already obey

\[
T_{s;rk}T_{r;k}=T_{sr;k}
\]

and

\[
\rho_s(p,rk)\rho_r(p,k)=\rho_{sr}(p,k).
\]

Therefore

\[
\Psi_{s;p,rk}\Psi_{r;p,k}
=
\Psi_{sr;p,k}
\]

if the type maps satisfy their functoriality law.

Conversely, suppose the full lifts compose and the displayed tensor
factorization is faithful on the type factor. The seam maps are unitary and the
coefficient residues are nonzero. Cancelling those two factors forces

\[
A_{s;p,rk}A_{r;p,k}=A_{sr;p,k}.
\]

Thus the full Adams semigroup closes if and only if the type-fiber maps close.
No further defect is hidden in the moving seam or Euler coefficient.

## Primitive, square, and connected types

The existing analytic incidence distinguishes three operator classes:

- primitive grade \(k=1\): continuous on the test rigging and not
  Hilbert--Schmidt on the unweighted prime Hilbert space;
- square grade \(k=2\): Hilbert--Schmidt;
- connected grades \(k\ge3\): nuclear.

An Adams arrow may cross these classes. In particular,

\[
(2,1):1\longrightarrow2
\]

crosses from the primitive to the square class, while

\[
(r,1):1\longrightarrow r,\qquad r\ge3,
\]

crosses directly into the connected class. Hence a type map cannot be inferred
from equality of reassembled analytic vectors: the source and target carry
different arithmetic typing and different operator ideals.

The functoriality square also prevents independent pairwise choices. For
example, the direct primitive-to-connected map must satisfy

\[
A_{6;p,1}
=
A_{3;p,2}A_{2;p,1}
=
A_{2;p,3}A_{3;p,1}.
\]

This is the first finite hostile test for a proposed type constructor.

## Obstruction record

When all relevant type maps are invertible, define the composition defect

\[
\Omega_{s,r;p,k}
=
A_{sr;p,k}^{-1}A_{s;p,rk}A_{r;p,k}.
\]

A valid lift has \(\Omega_{s,r;p,k}=1\) for every composable pair. This notation
is not used when the maps are noninvertible; there the uncancelled composition
equation itself is the obstruction test.

The invertible formula does not turn the Adams semigroup into a group. The
Euler factor remains strictly contractive for \(r>1\), and no inverse
prime-power grade motion is source-authorized.

## Nonclaim

The present source data do not provide canonical identifications between
\(F_{p,k}\) and \(F_{p,rk}\). Declaring every \(A_{r;p,k}\) to be an identity
would silently add a global trivialization of the type bundle. The result above
classifies the required constructor and its exact coherence law; it does not
construct that missing trivialization.

Likewise, scalar frequency coincidence cannot define a type map. Primitive,
square, and connected channels remain distinct even when their reassembled
analytic representatives lie on the same source vector.

## Consequence for the tower

The Adams tower now separates into three levels:

1. moving-seam transport: unitary and closed;
2. Euler half-density: positive, cocyclic, and strictly contractive for
   \(r>1\);
3. type transport: a still-missing functor on the divisibility action
   category.

The next admissible source construction must expose the fibers \(F_{p,k}\) and
give grade-change maps satisfying the two-path test already at \(6=2\cdot3\).
Pairwise type maps without this composition square do not complete the tower.

## Verdict

The remaining Adams obstruction is categorical rather than analytic. Full
weighted transport is equivalent to a functorial type-fiber lift. The smallest
decisive finite gate is the commuting diamond from grade \(1\) to grade \(6\);
its maps are not yet source-derived.
