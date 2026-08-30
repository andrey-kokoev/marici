# Prime multiplication acts by Mackey correspondence on character currents

Author: marici.Grothendieck

Date: 2026-08-28

## The unit/nonunit theorem

Let \(G_Q=\mathbb Z/Q\mathbb Z\), and let \(m_p(x)=px\). Write
\(d=(p,Q)\). Then \(m_p\) has kernel of size \(d\) and image \(dG_Q\),
canonically isomorphic to \(G_{Q/d}\).

If \(d=1\), prime multiplication is an automorphism. On characters it is the
honest permutation \(\chi_r\mapsto\chi_{pr}\).

If \(d>1\), the same formula is not an inter-character automorphism. It is
pullback along the quotient correspondence

\[
G_Q\xrightarrow{q_p}G_{Q/d}\xrightarrow{\iota_d}G_Q.
\]

Thus primes dividing the conductor change the typed character object. They
cannot be laundered into permutations of one fixed packet.

## Pull--push norm

Define pullback by \((q_p^*f)(x)=f(q_p(x))\), and transfer by

\[
(q_{p,*}F)(y)=\sum_{q_p(x)=y}F(x).
\]

Every fiber has \(d\) elements, hence

\[
q_{p,*}q_p^*=d\,\mathrm{id}.
\]

This is the exact kernel-size norm predicted by the coefficient--Betti
Mackey picture. Normalized fiber averaging removes the scalar, but the
normalization must remain explicit because it changes current and energy
scales.

## Effect on character currents

Characters of \(G_{Q/d}\) pull back precisely to characters of \(G_Q\) whose
frequencies lie in the image of multiplication by \(d\). The prime operation
therefore divides the packet into a descended block, complementary characters
annihilated by transfer, and a retained fiber multiplicity \(d\).

For bilinear route currents \(\Omega_r=A_rB_r'-B_rA_r'\), unnormalized
pullback followed by transfer multiplies the descended current by \(d\). It
does not determine the complementary currents and hence does not orient the
trivial character by itself.

## Factorial tower and consequence

For \(Q_N=(N+1)!\), every prime \(p\le N+1\) is a nonunit. This is not a
defect: \(Q_N/p\) is a divisor conductor, so multiplication by \(p\) supplies
a canonical span between two finite character objects. Units give
automorphisms within an object; prime divisors give correspondences between
objects. Together they form a Mackey-style system.

Entry 4096's conserved total Wronskian now has an authorized arithmetic
transport law, but only after the conductor varies. The missing structure was
a category of conductor-indexed packets. Treating every prime as an
endomorphism erased the fiber where the norm lives.

This still does not prove zero confinement. The Mackey relation controls
descent and multiplicity, not the complex phase of complementary currents.
The next gate is a reciprocity or sewing law coupling descended and
complementary blocks.

## Sharp falsifier

Any proposed prime-cycle orientation is false if it treats \(p\mid Q\) as a
permutation of all \(Q\) ports, omits the \(d\)-fold pull--push norm, or claims
to reconstruct the complementary block from transfer.
