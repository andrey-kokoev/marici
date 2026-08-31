# The natural forced history cannot satisfy the adjoint source equation off the seam

## Natural history lift

Let \(u\) be the source-derived history solving

\[
(\partial_q-a)u=c\Phi
\]

with the endpoint condition selected by the Mellin/Laplace readout. At a zero
of that endpoint readout, the two-ended history has vanishing total boundary
flux.

The exact augmented Green identity is then

\[
2a\|u\|^2
=
-2\operatorname{Re}
\bigl(c\langle u,\Phi\rangle\bigr).
\]

## Conflict with the paired adjoint equation

The minimal skew-adjoint Green completion adds

\[
V^*u=
\langle\Phi,u\rangle=0.
\]

If this equation holds, then the forcing pairing vanishes and the preceding
identity gives

\[
a\|u\|^2=0.
\]

For \(a\ne0\), a nonzero forced history therefore cannot simultaneously have:

1. zero endpoint flux;
2. the source equation \((\partial_q-a)u=c\Phi\);
3. the adjoint source equation \(V^*u=0\).

This is an exact incompatibility, not a norm estimate.

## Meaning for a hypothetical off-seam zero

Suppose the scalar Mellin section vanished at an off-seam parameter and its
natural history lift were nonzero. The endpoint zero would close the boundary
flux, but the Green identity would force

\[
\operatorname{Re}
\bigl(c\langle u,\Phi\rangle\bigr)
=-a\|u\|^2
\ne0.
\]

Hence that natural lift would fail the lower adjoint equation of the paired
pencil.

Therefore the implication

\[
\tau_s=0
\Longrightarrow
(u,c)\in\ker\mathcal D_a^{\rm pair}
\]

already contains the off-seam exclusion being sought. It cannot be justified
by endpoint cancellation alone.

## Seam case

At \(a=0\), the Green identity yields only

\[
\operatorname{Re}
\bigl(c\langle u,\Phi\rangle\bigr)=0.
\]

The paired equation requires the stronger complex identity

\[
\langle\Phi,u\rangle=0.
\]

Thus even on the seam, zero endpoint flux does not by itself place the history
in the paired kernel.

## Consequence for the divisor-to-state square

The candidate chain map cannot send the Xi Koszul residue to the natural
forced history and then declare the adjoint source equation automatic. Its
componentwise residual is exactly

\[
\mathcal R_{\rm adj}(s)=V^*u_s.
\]

Proving \(\mathcal R_{\rm adj}(s)=0\) at every Xi zero is equivalent to the
missing Green compatibility and, off the seam, already implies the desired
confinement.

## Disposition

The skew-adjoint source pair repairs the Green identity only by imposing an
additional equation that the scalar Mellin zero does not supply. The natural
history lift therefore does not close the divisor-to-state square. A larger
source complex would need a separate arithmetic variable whose equation
cancels the forcing pairing without imposing \(V^*u=0\) directly. No such
complex is currently constructed, and no RH conclusion is authorized.
