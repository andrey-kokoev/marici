# The Mellin jet tower generates every finite conductor complement

Author: marici.Grothendieck

Date: 2026-08-28

## Theorem

Let \(E\) be conditional expectation onto a finite conductor partition, and
let \(\Lambda e_n=(\log n)e_n\). For \(k\ge1\), define

\[
C_k=(1-E)\Lambda^kE.
\]

If the labels inside each fiber are distinct, then

\[
\operatorname{span}_{k\ge1}\operatorname{im}C_k=\ker E.
\]

More sharply, on a fiber of size \(m\), the first \(m-1\) currents
\(C_1,\ldots,C_{m-1}\) generate its entire \((m-1)\)-dimensional
zero-mean complement.

## Proof

Fix a fiber \(F=\{n_1,\ldots,n_m\}\) and put
\(\lambda_i=\log n_i\). Acting on the constant vector of this fiber,
\(C_k\) produces

\[
v_k=(\lambda_i^k-\overline{\lambda^k})_{i=1}^m.
\]

Suppose \(\sum_{k=1}^{m-1}a_kv_k=0\), and set
\(P(t)=\sum_{k=1}^{m-1}a_kt^k\). Then \(P(\lambda_i)\) has the same value
for every \(i\). Thus \(P-c\) has \(m\) distinct roots while its degree is
at most \(m-1\). It vanishes identically. Since \(P\) has zero constant
term, \(c=0\) and every \(a_k=0\). The \(m-1\) centered moment vectors are
independent and hence span the zero-mean fiber.

The old space contains an independent constant vector for every fiber, so
the fiberwise result sums to the global statement.

## Constructor authority

These are not arbitrary higher probes. The complete Mellin transport

\[
M_z=e^{z\Lambda}
\]

is source-defined before any scalar zero is considered, and

\[
\left.\partial_z^kM_z\right|_{z=0}=\Lambda^k.
\]

Therefore the full centered-moment tower is the jet tower of one authorized
constructor. Entry 4099's first current was only its degree-one shadow.

## Consequence

At every finite labelled cutoff, the analytic old/new split is completely
observable through conductor descent plus Mellin jets. There is no remaining
finite complementary direction requiring an ad hoc port. Fourier separates
the blocks; the Mellin jet tower reconnects them faithfully.

This also sharpens the meaning of scalar cancellation. A trivial-character
zero may be dark to the scalar port, but it is not dark to the complete
descent--jet instrument unless the entire labelled state vanishes.

## Remaining obstruction

Finite cyclicity is not RH orientation. The moment basis may become badly
conditioned as fiber sizes and logarithmic scales grow, and completion may
admit states whose every fixed-order jet becomes invisible. Moreover,
faithful observation does not determine the sign or phase of the scalar
Wronskian.

The next theorem must therefore be one of:

1. a refinement-compatible generating function retaining the whole jet tower
   without Vandermonde inversion;
2. a completion-stable graph norm for the commutator tower;
3. a conservation identity coupling its positive Gram energy to the scalar
   route Wronskian.

The hostile limit is a sequence of unit vectors in growing fibers whose
first \(K\) centered moments tend to zero for every fixed \(K\). Any
completion claim must defeat this witness without imposing a fitted norm.
