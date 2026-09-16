# The determinant phase gives only a local quarter-turn lift with divisor-parity obstruction

## Question

Can the reflected determinant line supply the missing order-four phase that would lift the radial reciprocal involution to the full Fourier sewing?

## Claim boundary

Locally away from the determinant divisor, yes: choose a square root of the meromorphic scattering transition. Globally, a single-valued square root exists only when the transition divisor is even. No such multiplicity-parity theorem is available. Thus the determinant line does not yet close the external quarter-turn sewing interface.

## Local lift

The radial reciprocal operator satisfies

$$
W_u^2=I,
$$

whereas the full Fourier sewing has \(\pm i\) character sectors. Let

$$
\mathcal S(z)=\frac{D_+(z)}{D_-(z)}
$$

be the reflected determinant transition. On a simply connected open set \(U\) disjoint from its zero and pole divisor, choose a holomorphic branch

$$
\eta_U(z)^2=\mathcal S(z).
$$

Tensoring the radial odd sector with the phase \(\eta_U\) supplies a local metaplectic coordinate whose square reproduces the reciprocal transition. This is the correct local source for an order-four lift; no arbitrary constant square root is inserted.

## Global obstruction

For a meromorphic function to have a global meromorphic square root, every zero and pole order must be even. Indeed, if \(\mathcal S=\eta^2\), then

$$
\operatorname{ord}_\rho\mathcal S
=2\operatorname{ord}_\rho\eta.
$$

Conversely, on the relevant simply connected scalar domain, even divisor orders remove the local branching obstruction up to a nowhere-zero unit and its winding class.

For the reflected determinant ratio,

$$
\operatorname{div}\mathcal S
=
\operatorname{div}D_+-\operatorname{div}D_-.
$$

Therefore an odd-multiplicity zero or pole produces sign monodromy in \(\eta\). The natural global object is then a metaplectic double cover branched over the odd part of the divisor, not a single-valued scalar phase line.

## Consequence for G4 sewing

The unlifted radial swap can globally compare only with the Fourier half-turn:

$$
CW_{\rm FP}^2=W_uC.
$$

A faithful quarter-turn comparison requires either:

1. a declared metaplectic double-cover target carrying the branch monodromy; or
2. a proof that the determinant transition divisor is even.

The second option would impose a strong and unsupported parity statement on completed-zeta multiplicities. It must not be assumed.

## Disposition

The determinant transition constructs the missing quarter-turn phase only locally off the divisor. Globally, divisor parity is the exact obstruction. Without a metaplectic double-cover declaration, the source-authorized external comparison remains the half-turn interface, not full order-four sewing.