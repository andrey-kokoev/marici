# Native Mellin transport has a transverse first-moment defect

## Native transport

Before inventing an active theta connection, test the source's ordinary
horizontal Mellin transport. On a source packet `h(u)`, let

\[
(A h)(u)=u h(u),
\qquad
L(h)=\int h(u)\,du.
\]

The transported packet is `h_r(u)=e^{ru}h_0(u)` and satisfies

\[
\partial_rh_r=Ah_r.
\]

The scalar readout is `L(h_r)`. Since `L` is constant in this frame, its
parallel-kernel defect is

\[
\Omega=L A,
\qquad
\Omega(h)=\int u h(u)\,du.
\]

Thus the defect is exactly the first-moment port.

## Exact obstruction

The first moment is not proportional to the total integral. For example, let
`h` equal `+1` on `(0,1)`, `-1` on `(1,2)`, and zero elsewhere. Then

\[
L(h)=0,
\qquad
\Omega(h)=\frac12-\frac32=-1.
\]

Therefore

The class `[L A]` is therefore nonzero in

\[
V^*/\langle L\rangle.
\]

The scalar-null hyperplane is not parallel under native Mellin transport.
A cancellation at one horizontal position need not persist at the next.

The same obstruction appears on every finite cell model with at least two
distinct source coordinates: the rows `(1,...,1)` and `(u_1,...,u_n)` have
rank two.

## Consequence for the RH programme

The active null-transport law from ledger 3813 does not arise from bare
Mellin character transport. A successful connection must include an
additional source-derived term `B` satisfying

\[
L(A+B)=\alpha L.
\]

Equivalently, it must cancel the transverse first-moment class.

Such a correction can always be manufactured algebraically after choosing a
splitting of `L`, so its mere existence carries no evidence. The correction
must instead arise from independently authorized theta/Tate structure—prime
currents, reciprocal sewing, endpoint augmentation, or the active reservoir
identified by Aspect—and must reject hostile sources before their zero sets
are inspected.

This also clarifies the role of the seam. Bare horizontal transport does not
distinguish it. Any sectorwise null-preserving connection must be a completed
transport whose extra boundary terms change or become singular at the seam.

## Smallest next test

For a proposed finite labelled connection `A_X+B_X`, compute

\[
\Omega_X=L_X(A_X+B_X)
\]

before using a scalar zero. Acceptance requires the two rows `L_X` and
`Omega_X` to have rank one on the source-admissible module. The primitive,
prime-square, archimedean, and reciprocal-seam contributions to `B_X` must be
kept typed so that an accidental scalar cancellation cannot masquerade as a
source identity.

The first-moment defect is the first real obstruction encountered by the
active-connection programme.
