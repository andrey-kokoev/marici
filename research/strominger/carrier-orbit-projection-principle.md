# The orbit-projection principle

The magnetic parity theorem is the `Z_2` instance of a general mechanism.

Let a finite symmetry group `G` act on transported carrier data, and suppose

\[
T:\mathcal S\longrightarrow\mathcal P
\]

is an injective equivariant transport.  A physical port selecting an
irreducible representation `rho` is an isotypic projector

\[
\pi_\rho:\mathcal P\to\mathcal P_\rho.
\]

Its source kernel is

\[
\ker(\pi_\rho T)=T^{-1}
\left(\bigoplus_{\lambda\ne\rho}\mathcal P_\lambda\right).
\]

Thus the kernel belongs to the selected interface, not to transport.

## Stabilizers predict structural zero ports

An orbit with stabilizer `H subset G` carries the permutation representation

\[
\operatorname{Ind}_H^G\mathbf1.
\]

By Frobenius reciprocity, the multiplicity of `rho` on that orbit is

\[
\dim\operatorname{Hom}_G
\left(\rho,\operatorname{Ind}_H^G\mathbf1\right)
=\dim\rho^H.
\]

Therefore

\[
\boxed{
\rho^H=0
\quad\Longrightarrow\quad
\text{the rho-port is structurally absent on that orbit}.
}
\]

This predicts zero columns before constructing any determinant.

For magnetic reflection, `G=Z_2`:

- at `q=0`, the orbit is fixed, so `H=G`; only the trivial representation
  has an `H`-fixed vector, while the sign port is absent;
- at `q>0`, the orbit is free, so `H={1}`; the regular representation contains
  both trivial and sign ports once.

Hence towers are forced by stabilizer representation theory, while free-orbit
circuits require an additional rank defect in the transported image.

## Structural absence versus alignment defect

The principle separates two kernel mechanisms for any group:

\[
\begin{array}{c|c|c}
\text{mechanism}&\text{test}&\text{meaning}\\
\hline
\text{structural absence}&\rho^H=0&
\text{the orbit cannot carry the selected port}\\
\text{alignment defect}&\rho^H\ne0,
\ T(\mathcal S)\cap\ker\pi_\rho\ne0&
\text{the port exists, but a transported combination avoids it}\\
\text{transport loss}&\ker T\ne0&
\text{the complete carrier packet erased information}
\end{array}
\]

Strominger realizes the first two rows and excludes the third:

- towers: structural absence of the sign port on fixed orbits;
- grade-two circuits: alignment defects on free orbits;
- one-sheet theorem: transport loss is impossible.

## Complementary-port faithfulness

If every isotypic port is retained, their direct sum is the identity on the
transported representation:

\[
\bigoplus_\rho\pi_\rho=1_\mathcal P.
\]

Consequently

\[
\bigcap_\rho\ker(\pi_\rho T)=\ker T.
\]

For injective transport, the complete family of symmetry ports is jointly
faithful even when each individual port has a kernel.

This gives a general diagnostic for other Marici sectors:

1. identify the transported carrier object before projection;
2. determine orbit stabilizers;
3. compute which irreducibles have stabilizer-fixed vectors;
4. classify structural missing ports without matrices;
5. use rank/route analysis only for alignment defects in represented ports;
6. test the joint family of complementary ports against the transport kernel.

The stabilizer calculation predicts where information cannot appear.  The
carrier calculation determines whether information that could appear actually
does.  The transport calculation determines whether anything was erased
before either question was asked.
