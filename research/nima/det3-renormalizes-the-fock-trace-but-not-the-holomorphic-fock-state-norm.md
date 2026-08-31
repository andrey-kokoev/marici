# det3 renormalizes the Fock trace but not the holomorphic Fock-state norm

## Candidate renormalized state

At finite cutoff, one may try to absorb the primitive and square cumulants
into the symmetric-Fock state:

\[
\widehat u_{3,X}(s)
=
\exp\left(
-\operatorname{Tr}L_X(s)
-\frac12\operatorname{Tr}L_X(s)^2
\right)
\Gamma_X(L_X(s)).
\]

Its scalar trace is

\[
\operatorname{Tr}\widehat u_{3,X}(s)
=
\det_3(I-L_X(s))^{-1}.
\]

Thus scalar traces converge in the native \(\mathcal S_3\) chart.  This does
not imply convergence of the state in trace norm.

## One-prime trace norm

For one eigenvalue

\[
\lambda=p^{-s},
\qquad r=|\lambda|=p^{-\operatorname{Re}s},
\]

the normalized bosonic factor has trace norm

\[
N_3(\lambda)
=
\frac{
\left|e^{-\lambda-\lambda^2/2}\right|
}{1-r}.
\]

Hence

\[
\log N_3(\lambda)
=
-\operatorname{Re}\lambda
-\frac12\operatorname{Re}\lambda^2
-\log(1-r).
\]

Writing \(\lambda=re^{i\theta}\), its leading term is

\[
r(1-\cos\theta)+O(r^2).
\]

## Real-axis cancellation is exceptional

When \(\theta=0\), the order-one and order-two terms cancel and

\[
\log N_3(r)=O(r^3).
\]

The product of normalized trace norms can then converge for
\(\operatorname{Re}s>1/3\).

For a nonreal parameter,

\[
\theta_p=-\operatorname{Im}s\log p
\]

depends on the prime.  The leading positive norm cost is

\[
p^{-\operatorname{Re}s}
\left(1-
\cos(\operatorname{Im}s\log p)
\right).
\]

The analytic counterterm cancels complex traces, not absolute occupation
mass.  Away from the real axis, no source identity makes this positive term
vanish primewise.

## Failure of local holomorphic trace-norm completion

A holomorphic trace-class family must be locally bounded in trace norm.  The
finite products satisfy

\[
\log\|\widehat u_{3,X}(s)\|_1
=
\sum_{p\le X}\log N_3(p^{-s}).
\]

On any complex neighborhood containing nonreal parameters with
\(\operatorname{Re}s\le1\), the uncancelled order-one absolute mass prevents
a cutoff-uniform trace-norm bound.  Scalar \(\det_3\) convergence therefore
does not produce a holomorphic trace-class Fock state on the
\(\operatorname{Re}s>1/3\) chart.

The same defect appears for cutoff bonding: normalized scalar transition
characters converge, while the operator-state bonding norms need not.

## Why a modulus counterterm is inadmissible

Multiplying by

\[
\exp\left(-\sum_p r_p-rac12\sum_p r_p^2\right)
\]

would control absolute mass on the real radial coordinate, but it depends on
\(|p^{-s}|\) and is not holomorphic in \(s\).  It cannot define the analytic
Fredholm family whose divisor is being compared.

## Consequence for the completed complex

Order-three regularization completes the determinant line because determinant
lines retain signed and phased cyclic traces.  A trace-class Fock state
requires absolute nuclear control, which is stronger and is not supplied by
the anomaly cancellation.

Therefore the completed theta complex cannot be obtained by simply
multiplying the finite Fock border by the \(\det_3\) counterterm.  Its state
space must be a genuinely relative or rigged complex whose determinant
functor is defined without a trace-class bosonic state.

## G4 frontier

The finite Fock complexes and the completed determinant line share the same
scalar cutoff character, but there is no bounded holomorphic state-level
bonding between them from det3 renormalization alone.  Constructing such a
relative complex remains an independent theorem.  No RH conclusion is
authorized.
