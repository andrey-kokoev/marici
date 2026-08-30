# No Adams-natural Gaussian pivot pairs the two boundary covectors

## Candidate variance change

After the dual--dual obstruction, the most economical repair is Gaussian
smoothing in logarithmic label.  Let

\[
L e_n=(\log n)e_n
\]

on finite arithmetic packets and, for \(\tau>0\), put

\[
K_\tau=\exp(-\tau L^2).
\]

The super-polynomial decay of

\[
e^{-\tau(\log n)^2}
\]

makes \(K_\tau\) a continuous variance-changing map from the polynomially
growing sequence dual into the rapid-decay test space.  It therefore defines
a legitimate regularized dual--dual contraction

\[
B_\tau(\xi,\eta)=\langle\xi,K_\tau\eta\rangle.
\]

This is not an arbitrary analytic trick: it is the simplest possible use of
the source's logarithmic spectral generator.  It nevertheless fails the
arithmetic naturality gate.

## Adams covariance

Let \(\psi_k\) be the positive-Fock Adams operation sending label \(n\) to
\(n^k\).  On its algebraic image,

\[
L\psi_k=k\psi_kL.
\]

Hence

\[
K_\tau\psi_k=\psi_kK_{k^2\tau}.
\]

For \(K_\tau\) to be a natural endomorphism of the fixed arithmetic source,
it would have to commute with every \(\psi_k\).  This requires

\[
K_\tau=K_{k^2\tau}
\]

on every nonzero logarithmic label.  For any \(k>1\), that equality forces
\(\tau=0\).  But \(K_0=I\) does not change variance and does not define the
missing dual--dual pairing.

Therefore no nontrivial member of the Gaussian smoothing family is both:

1. strong enough to send the completed boundary covectors to test grade; and
2. natural under the source's Adams operations.

## Meaning of the failure

The family is covariant rather than invariant.  Adams transport acts on its
scale by

\[
\tau\longmapsto k^2\tau.
\]

Thus Gaussian smoothing can be retained only as a scale-indexed comparison
tower.  Selecting one positive \(\tau\) is extra clock or metric data.  It is
not determined by the arithmetic constructor grammar.

This recovers, in a new modality, the same obstruction seen in the weighted
Hilbert pivots \(Z_\delta\): every positive regularity grade supplies a
pairing, but the source symmetries do not select one grade.  Heat covariance
organizes the choices; it does not collapse them to a canonical choice.

## Surviving possibilities

The minimal theta carrier must do something stronger than provide a smoothing
semigroup.  A successful variance-changing constructor must be one of:

- an Adams-equivariant correspondence whose scale is itself retained as a
  typed dynamical coordinate;
- an integral over the entire heat orbit with a source-fixed measure;
- a state-valued control port already present before arithmetic completion;
- a relative pairing that never contracts the two boundary covectors
  directly.

The hostile test for any proposed fixed smoothing is immediate: compare the
two paths around the Adams square.  A residual

\[
K_\tau\psi_k-\psi_kK_\tau
=
\psi_k(K_{k^2\tau}-K_\tau)
\]

is a source-typed naturality failure, not a removable numerical error.

The search has therefore moved one level deeper.  The missing datum is not a
preferred smoothing strength.  It is a source law that integrates or
transports the whole regularity-scale orbit coherently.

