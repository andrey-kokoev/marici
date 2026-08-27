# 3252 — The Polar Port Is the Green Boundary Completion of the Bulk-Odd Port

For \(z=s-1/2\), let

\[
I_g(z)=\int_0^\infty g(u)\sinh(zu)\,du,
\qquad L=\partial_u^2-\frac14.
\]

Twice integrating by parts yields

\[
\int_0^\infty(Lg)(u)\sinh(zu)\,du
=g(0)z+\left(z^2-\frac14\right)I_g(z).
\]

Hence the bulk-odd port plus the polar-odd port is exactly the odd transform
of \(Lg\), divided by the centered Green denominator. The polar port is not an
extra observable: it is the Dirichlet boundary completion required by the
source operator \(\partial_u^2-1/4\).

This constructs the transport-bearing mate missing from the naive Hermitian
pairing. The remaining gate is the theta-specific sign-band and modular
structure of \(L\Phi\), not generic source positivity.

- Research packet: research/grothendieck/the-polar-port-is-the-green-boundary-completion-of-the-bulk-odd-port.md
- Checker: research/grothendieck/checkers/check_polar_green_boundary_completion.py
- Sequence claim: seqclaim-ac7efa13f5293186f4899559
- Graph event: 6838
