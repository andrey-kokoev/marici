# Euclidean H0 tensor-completion gate

## Question

Can the source-shaped scalar functional isolated in WP522 be promoted directly
to an executable neutral-\(B_s\) lattice instrument?

The answer is no for the full massive-vector amplitude. WP524 constructs the
scalar estimator exactly, then finds the first missing arrow: WP520 froze only
the scalar flavor-space resolvent and did not derive the longitudinal and
Goldstone completion required by the nonconserved \(b\)-to-\(s\) current.

## Exact scalar estimator

Let

\[
D(Q^2)=D_6(Q^2)D_7(Q^2)
\]

be the two-cubic denominator frozen in WP522. On a hypercubic lattice use

\[
\widehat Q^2=\sum_\mu \frac{4}{a^2}
\sin^2\!\left(\frac{aQ_\mu}{2}\right),
\qquad
K_a(Q)=\frac{1}{D(\widehat Q^2)}.
\]

The proposed scalar observable is the integrated correlator obtained by
inserting \(K_a(x-y)\) between two left-handed flavor currents in a
source-to-sink \(B_s\) correlator and extracting its linear-time coefficient
after the declared contact and intermediate-state subtractions.

The checker proves exactly that both cubic factors have three negative real
roots and are coprime. Thus the six poles lie on the timelike continuation and
the Euclidean kernel has no singularity for \(Q^2\geq0\). It also proves

\[
K_a(Q)=\frac{1}{D(Q^2)}+
\frac{a^2\sum_\mu Q_\mu^4}{12}
\frac{D'(Q^2)}{D(Q^2)^2}+O(a^4),
\]

so this discretization has the intended continuum scalar kernel with a typed
leading cutoff correction.

## Hostile tensor test

For on-shell external quarks,

\[
q_\mu\,\bar s\gamma^\mu P_L b
=m_b\,\bar sP_Rb-m_s\,\bar sP_Lb.
\]

This expression is not identically zero. Consequently the longitudinal
\(q_\mu q_\nu\) numerator of a massive-vector propagator contributes. In a
gauge-complete broken theory its gauge dependence must cancel against the
corresponding Goldstone exchange and counterterms, producing additional
scalar-operator channels. Neither the scalar WP520 resolvent nor the single
WP522 \(H_0\) coordinate determines that completion.

The first nonfaithful arrow is the map from the broken flavor-gauge action to
its scalar flavor-space resolvent.

The scalar projection discards Lorentz and Goldstone data before the lattice
readout is defined. A precise scalar convolution therefore cannot repair the
loss.

## Instrument contract after repair

The next source packet must derive, in one declared gauge and renormalization
scheme:

- the complete transverse and longitudinal pole-residue tensors;
- the Goldstone couplings fixed by the same flavon kinetic terms;
- the induced left-left and scalar \(\Delta B=2\) operator kernels;
- the Ward or Slavnov--Taylor identity proving gauge-parameter cancellation;
- coincident-point subtractions and operator mixing;
- threshold matching for every light pole.

Only that gauge-independent kernel may be inserted into the calibrated
integrated \(B_s\) correlator. The resulting continuum matrix elements still
need finite-volume, heavy-quark, normalization, and covariance control before
they can enter the \(\Delta M_s\) likelihood.

## Disposition

- Admitted domain: the frozen WP520 aligned source witness.
- Faithful coordinate: not yet \(H_0\) alone; the full tensor-plus-Goldstone
  bilocal operator packet is required.
- Source-authorized probe: the WP522 scalar kernel is authorized only as one
  component of that packet.
- Contextual partition: uncomputed because the projection to the scalar
  kernel is already nonfaithful on the physical massive-vector amplitude.
- Classification: neither selector nor rigidifier; a valid scalar estimator
  contract and a negative physical-instrument gate.
- Smallest exact falsifier of scalar completeness:
  \(q_\mu J_L^\mu=m_bS_R-m_sS_L\neq0\).
- Remaining physical-instrument gate: derive the gauge-independent completion
  from the admitted flavon action, then execute the complete lattice
  correlator with calibrated uncertainties.

This result does not retract WP520's scalar-resolvent algebra or WP522's exact
compression of that scalar kernel. It retracts only the stronger inference
that measuring \(H_0\) would by itself measure the complete physical exchange.
