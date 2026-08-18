# Entry 489 — The Generic Lifted Carrier Map Has Resonance Kernel

Benincasa Entry 487 constructs the gradient-Koszul homotopy that makes
reduction to the derived quartic carrier a chain map.  Entries 486 and 488
identify the generic odd source as one flat anti-invariant line plus one
reduced resonant line.  Their images are now determined by explicit
representatives.

## Flat summand

The flat summand comes from the surviving \(a\)-tail of Entry 474.  Its
primitive representative is \([a]\).  Since the monic quartic carrier has
basis

\[
(1,a,a^2,a^3),
\]

the class \([a]\) maps nontrivially to the odd quartic carrier.  Entry 488's
half-residue shows that it carries the required monodromy character \(-1\).

## Resonance summand

Use the intrinsic resonance representative

\[
r=[a^{11}(b+1)].
\]

(The greedy representative \([a^{11}b]\) of Entry 474 differs by the chosen
filtered normal form; the intrinsic Euler class uses \(b+1\).)

Over \(\mathbb Q[u]/(u^2)\), the quartic relation gives

\[
a^4=-u\,a^2(1-b^2).
\]

Therefore

\[
a^{11}(b+1)
=a^3(a^4)^2(b+1)
=u^2a^7(1-b^2)^2(b+1)
=0.
\]

Thus the reduced resonance maps to zero in the first-order quartic carrier.

## Generic relative fiber

The lifted map has the block behavior

\[
\mathbb Q[u]/(u^2)\oplus\mathbb Q
\longrightarrow
\mathcal M_{CM,-},
\qquad
(e,r)\longmapsto([a],0).
\]

Hence it has rank one on the flat summand and

\[
\boxed{
\ker(F_-^{\rm gen})=\mathbb Q\,r.
}
\]

The generic relative fiber is exactly the reduced anti-invariant resonance
line, while the flat half-residue line maps to the physical odd quartic
carrier.  This is the interior comparison required after Entries 483--486.

The statement is first-order in \(u\) and generic in \(b\).  The endpoint
lattice extensions have been checked separately in Entries 483--484, but a
single global sheaf-level quasi-isomorphism combining generic and endpoint
charts remains to be written.

The next gate is that gluing calculation.  It must verify that the generic
kernel \(r\) extends with divisor \(3[1]+4[-1]\) and that no Čech kernel or
cokernel appears on the overlaps.

The executable audit is
`research/voevodsky/check_soft_axis_generic_lifted_carrier_map.py`.
