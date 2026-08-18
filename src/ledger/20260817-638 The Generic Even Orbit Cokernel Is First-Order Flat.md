# Entry 491 — The Generic Even Orbit Cokernel Is First-Order Flat

Entry 473 finds a cutoff-independent invariant defect of dimension one in the
global filtered orbit cokernel.  It is tempting to identify that defect with a
generic torsion summand corresponding to the even conormal cell.  The generic
point calculation refutes this interpretation.

## Generic invariant census

Use the same source-jet-preserving specialization as Entry 486 at

\[
b=0,2,3,
\]

away from both endpoints.  Project the complete orbit exact complex to even
\(a\)-parity before taking its cokernel.  At every cutoff
\(D=12,16,20,24\), one obtains

\[
\dim C_{0,+}^{\rm gen}=2,
\qquad
\dim C_{+}^{(1),\rm gen}=4.
\]

Thus the generic ordinary even cokernel is first-order flat:

\[
\boxed{
C_+^{\rm gen}\simeq
\left(\mathbb Q[u]/(u^2)\right)^{\oplus2}.
}
\]

There is no generic length-one even torsion summand analogous to the odd
resonance of Entry 486.

## Location of the conormal cell

Benincasa Entry 472 types the even contribution as

\[
\operatorname{Tor}_1^S(R,R)\cong I/I^2.
\]

The present flatness result shows why this cell must not be sought as an
ordinary nonflat summand of the source cokernel.  It arises from the derived
self-intersection in the gradient-Koszul carrier target of Benincasa Entry
487.  Forgetting that derived degree leaves only the flat even quartic
module.

Consequently Entry 473's constant global defect is not a generic interior
torsion line.  It must come from the interaction of the filtered global
presentation with the derived relation or its boundary extension.

## Next gate

Evaluate the lifted even carrier map into

\[
[\mathcal O^{\oplus2}\xrightarrow{(K_a,K_b)}\mathcal O/(K)]
\]

and compute its homotopy fiber.  The degree-zero map should account for the
two flat quartic directions, while the degree-minus-one fiber should recover
\(I/I^2\).  This must be verified from the Koszul differential, not inferred
from the dimension-one filtered defect.

The executable audit is the extended parity census in
`research/voevodsky/check_soft_axis_generic_interior_odd_cokernel.py`.
