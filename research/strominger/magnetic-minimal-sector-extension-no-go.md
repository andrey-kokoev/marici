# Minimal sector extension does not activate the magnetic portal

At \((g,d)=(6,17/3)\), the three candidate source monomials have labels

\[
(a,m)=
\left(0,-\frac{50}{3}\right),
\left(\frac{14}{3},2\right),
\left(\frac{20}{3},0\right).
\]

Relative to the original lattice \(a\in2\mathbb Z\), \(m\in\mathbb Z\), the
minimal exponent-lattice saturation therefore contains three affine sectors:

\[
\Lambda_{00}=(0,0)+(2\mathbb Z,\mathbb Z),
\]

\[
\Lambda_{01}=\left(0,\frac13\right)+(2\mathbb Z,\mathbb Z),
\]

\[
\Lambda_{20}=\left(\frac23,0\right)+(2\mathbb Z,\mathbb Z).
\]

The magnetic differential changes the exponents by integral lattice moves, so
these affine sectors remain separate transport blocks. The candidate in
\(\Lambda_{01}\) has deck charge \(2\), while the two candidates in
\(\Lambda_{20}\) have charge \(1\).

A charge-\(2\) adapter can align the first candidate with the other two. If
the adapter is invertible, however, it is only an isomorphism between charge
sectors. It cannot introduce a relation among source columns. Direct exact
construction still gives rank three.

This is an instance of a general no-go statement. Let

\[
F=\bigoplus_{\lambda\in L}F_\lambda
\]

be an injective transport graded by affine lattice sectors. Any construction
made solely from:

- adjoining further independent sectors;
- direct sums;
- faithfully flat scalar extension;
- grading relabellings;
- invertible charge adapters;

preserves injectivity. Each operation is exact and faithful on the admitted
packet. Their composite cannot create a kernel.

Therefore a magnetic portal cannot consist merely of the missing fractional
states plus an invertible charged adapter. It must add at least one genuinely
relation-producing constructor:

1. a non-flat defect restriction, producing a Tor boundary;
2. a nonfaithful target quotient;
3. an off-diagonal tail differential coupling distinct affine sectors;
4. a new readout pairing that is not an isomorphism.

This sharpens the missing-constructor diagnosis. The absent datum is not just
a larger state space. It is a source-authorized relation between otherwise
independent sectors.

The distinction is experimentally falsifiable. If exponent-lattice saturation
and invertible charge alignment alone make the full three-column matrix lose
rank, the no-go theorem fails. Exact computation gives the opposite result.

Replay:

\`python research/strominger/checkers/magnetic_minimal_sector_extension_checks.py\`
