# Team transfer audit: the active rank-one repair is covariant but not yet null transport

## Inputs from the other lanes

Three recent results meet exactly at the theta action gap.

1. Aspect constructs the minimum positive update of the finite theta
   colligation. With

   \[
   Q(r)=\begin{pmatrix}1&2r\\2r&1\end{pmatrix},
   \qquad b=-f e_1,
   \qquad \rho=b^*Q^{-1}b,
   \]

   the source-aligned update is

   \[
   \Delta_*(r,f)
   =\frac{\rho-1}{\rho}bb^*
   =\begin{pmatrix}f^2+4r^2-1&0\\0&0\end{pmatrix}.
   \]

2. Nima proves that information erased by a quotient cannot be recovered by
   downstream postcomposition. A successful repair must have source incidence
   transverse to the erased fiber.

3. Strominger proves that an `authorized action` flag is not enough. An
   action requires dependent typing by its source, target, domain, authority
   locus, variance, geometric effect, and coherence witness.

Together with ledger 3808, these results classify the candidate repair much
more sharply than port counting does.

## Exact covariance audit

Let

\[
J=\operatorname{diag}(1,-1).
\]

The reciprocal sheet change satisfies

\[
JQ(r)J=Q(-r),
\qquad Jb=b.
\]

Because the update depends on `r` only through `r^2` and is supported on the
source line,

\[
J\Delta_*(r,f)J=\Delta_*(-r,f)=\Delta_*(r,f).
\]

It also vanishes at the feasibility boundary `rho=1`. Thus the finite update
is not an arbitrary fitted matrix: it is source-aligned, sheet-covariant,
continuous at its domain boundary, rank one, and uniquely minimizes the
declared whitened trace cost.

The repaired balance has

\[
Q_*=Q+\Delta_*=
\begin{pmatrix}f^2+4r^2&2r\\2r&1\end{pmatrix},
\qquad
\det Q_*=f^2>0.
\]

## The decisive non-transfer

This active update repairs finite colligation feasibility, but it does not
transport a zero of the completed scalar theta readout into the joint kernel
of the refined incidence packet. Its determinant remains positive wherever
the source amplitude `f` is nonzero. It therefore describes a nonsingular
local response apparatus even when an aggregated oscillatory readout may
vanish.

The distinction is structural:

- Aspect's update changes the source balance before observation;
- the RH gap asks for a law relating a particular scalar-null boundary state
  to the full source-generated transport orbit;
- covariance and optimality of the update do not supply that implication.

Hence the active reservoir is a valid constructor candidate but not yet the
missing RH action.

## Transferred ActionWitness

The finite candidate can now be typed as follows.

```text
operation_id: source_aligned_positive_balance_update
source_object: theta colligation (Q(r), b(f))
target_object: repaired colligation (Q(r)+Delta*(r,f), b(f))
domain_certificate: rho(r,f) >= 1
authority_locus: positive-update class plus whitened trace cost
variance: conjugation-covariant; reciprocal sheet covariance by J
geometric_effect: changes the generator balance along the source line
coherence_witness: J Delta*(r,f) J = Delta*(-r,f)
```

The unresolved authority question is whether the theta/Tate source itself
constructs the positive-update class and trace cost. If those are introduced
only to repair feasibility, minimality is conditional rather than physical.

## Best transfer idea

Use the rank-one update as the local coefficient of a source-derived
connection on the admissible state family, not as another port. Then ask for
an independent evolution law whose parallel sections satisfy

\[
L(v)=0
\quad\Longrightarrow\quad
L(A^kv)=0
\]

for the generated transport algebra, with boundary uniqueness forcing the
full response packet to vanish only on the seam. This changes the antecedent
from an arbitrary vector in a scalar hyperplane to a solution of a typed
source equation, avoiding the static factorization no-go.

The immediate falsifier is equally clear: if the proposed connection merely
postcomposes the scalar readout, or if its admissible solution space still
contains the two-cell cancellation witness, it adds no RH force.

## Conclusion

The team transfer does not prove null confinement. It does identify the
correct kind of next object:

> a source-authorized, sheet-covariant active connection whose solution law,
> not its passive monitor family, propagates the scalar boundary condition.

That is narrower than another positivity search and stronger than merely
adding a comparison channel.
