# An energy-dependent xi boundary is not yet an operator

Epistemic-graph event: 1415.

## Fixed domains versus spectral pencils

For the first-order Mellin generator on a compact logarithmic interval, a
fixed unitary endpoint map \`U\` defines one self-adjoint domain. Replacing it
by \`U(lambda)\` and solving

\`det(exp(i lambda L)I-U(lambda))=0\`

does not define the spectrum of that operator: the domain now changes with
the candidate eigenvalue. It defines a nonlinear operator pencil.

Consequently one may not repair the phase-collapse theorem of Ledger 1380 by
inserting the theta amplitude into an energy-dependent endpoint condition and
then call its roots a self-adjoint spectrum. A fixed linear operator must be
constructed whose elimination produces that pencil.

## The self-adjoint linearization gate

Boundary-triple theory gives the relevant necessary structure. Eliminating an
auxiliary self-adjoint system produces an operator-valued Weyl function
\`M(z)\` satisfying the Nevanlinna condition

\`M(conj(z))=M(z)^*\`,
\`Im(M(z))/Im(z) >= 0\`.

Equivalently, in a unitary characteristic-function formulation, the boundary
transfer is analytic and contractive in the upper half-plane and unitary
almost everywhere on the real axis. Poles and zeros then carry positive
spectral measures and the real-axis eigenvalues arise from a fixed
self-adjoint extension.

No such source-derived Weyl function has yet been obtained from the paired
coefficient--Betti, intrinsic-prime, or theta objects. The scalar function
\`Xi(t)\` is real on the real axis, but reality alone is not the Nevanlinna
positivity required for a self-adjoint linearization.

## Determinant equality contains the RH gate

Suppose a fixed self-adjoint operator \`A\` with discrete spectrum has a
regularized characteristic determinant satisfying

\`det_reg(z-A)=exp(g(z)) Xi(alpha z+beta)\`,

where \`alpha\` is nonzero and the affine normalization maps the real spectral
axis to the critical-line parameter. Every zero of the left side is real.
Therefore every zero of the corresponding \`Xi\` normalization must be real.
This implication is exactly the Riemann hypothesis, with multiplicities
matched by determinant order.

Conversely, assuming real zeros and suitable canonical-product convergence,
one can build a diagonal self-adjoint operator from those zeros. That
construction is spectrally circular because it uses the target zero set as
input. Hence RH is necessary but not sufficient for the requested
source-derived realization.

## Sharp surviving conjecture

The remaining noncircular task is not to write a scalar equation equal to
\`Xi\`. It is to derive from the source calculus an operator-valued
Nevanlinna/Weyl function whose:

1. auxiliary spectral measure is positive and source-derived;
2. fixed self-adjoint linearization has compact resolvent;
3. extension determinant is completed \`xi\`; and
4. construction never queries or factors the zero set.

Failure of Nevanlinna positivity, compact resolvent, or exact determinant
normalization falsifies a proposed boundary before numerical zero matching is
relevant.

## Scope

This is a typing and necessity theorem. It does not prove RH or rule out a
source-derived self-adjoint linearization; it prevents nonlinear
energy-dependent root equations from being misreported as such an operator.
