# Entry 490 — The Generic Resonance Kernel Glues to the Sevenfold Odd Lattice

Entry 489 identifies the generic kernel of the lifted odd carrier map as the
intrinsic resonance represented in the original numerator by

\[
r=a^{11}(b+1).
\]

The remaining question is whether this generic line glues to the endpoint
lattice of Entries 455 and 465.

## Removing the derived relation twist

With \(c=b+1\), the degreewise divisor rule gives

\[
B(11,1)=(5,6)
\]

for the numerator representative.  But the relative kernel is formed in the
gradient-Koszul target of Benincasa Entry 487.  It therefore removes the
universal quartic relation, whose divisor is

\[
B(4,0)=(2,2).
\]

The derived kernel line consequently has divisor

\[
\boxed{
B(11,1)-B(4,0)=(3,4)=B(7,1).
}
\]

This is exactly the intrinsic odd transition divisor

\[
3[b=1]+4[b=-1]
\]

derived independently in Entries 455--456 and extended without boundary
cokernel in Benincasa Entry 465.  Thus the generic kernel and the endpoint
line are the same framed coefficient object after the Koszul relation degree
is accounted for.

## Čech obstruction

Compactify the boundary coordinate to \(\mathbb P^1_b\).  Under the
established positive-divisor convention, the kernel lattice is

\[
\mathcal O_{\mathbb P^1}(3[1]+4[-1])
\simeq\mathcal O_{\mathbb P^1}(7).
\]

Since

\[
H^1(\mathbb P^1,\mathcal O(7))=0,
\]

there is no Čech degree-one obstruction to gluing the generic resonance
kernel across the two endpoint charts.  Entry 465 supplies the local
surjectivity needed to exclude endpoint cokernels.

## Result and boundary

The odd relative fiber therefore glues, through first order in the soft
parameter, to the single framed line

\[
\mathcal L_-
=\mathcal O(3[1]+4[-1])
\]

with anti-invariant monodromy.  This closes the generic-plus-boundary gluing
gate for the odd sector.

The result remains first-order in \(u\).  It does not prove compatibility at
higher Rees order or identify the even conormal block with the full lifted
carrier fiber.  The next gate is the analogous lifted-map computation in the
invariant sector, where Entry 473 found one finite defect.

The executable audit is
`research/voevodsky/check_soft_axis_resonance_kernel_gluing.py`.
