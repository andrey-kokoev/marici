# The xi Pick kernel gives a canonical indefinite boundary preshape

Epistemic-graph event: 1432.

## Source-defined Hermitian kernel

Define \`Xi\` by the theta integral and

\`M(z)=-Xi'(z)/Xi(z)\`.

On the complement of the poles, set

\`K_Xi(z,w)=[M(z)-conj(M(w))]/[z-conj(w)]\`.

Because \`Xi\` is real entire,
\`M(conj z)=conj(M(z))\`, and therefore

\`K_Xi(z,w)=conj(K_Xi(w,z))\`.

No zero list or spectral factorization enters this definition.

## Canonical algebraic boundary space

Let \`V_0\` be the finite linear span of formal kernel vectors \`k_w\`.
Define the Hermitian form

\`[sum_i c_i k_(w_i),sum_j d_j k_(z_j)]
=sum_(i,j) conj(c_i)d_j K_Xi(w_i,z_j)\`.

Quotienting by its radical gives a canonical nondegenerate indefinite
pre-space \`V_Xi\`. The kernel identity

\`(z-conj(w))K_Xi(z,w)=M(z)-conj(M(w))\`

is exactly the abstract Green/Weyl identity on its boundary vectors. Thus the
theta completion supplies an unconditional boundary preshape whose Weyl datum
is \`-Xi'/Xi\`.

This is algebraic: an indefinite completion may require a choice of Hilbert
majorant, and no claim of a canonical Krein topology is made.

## Positivity is exactly the descent gate

The form on \`V_Xi\` is positive semidefinite if and only if every finite Pick
matrix is positive semidefinite. By Ledger 1382, this is equivalent to RH.
When positive, radical quotient and Hilbert completion give the canonical
reproducing-kernel Hilbert space for \`M\); boundary-triple realization then
produces the self-adjoint compact-resolvent model and

\`det_2(I-zA^(-1))=Xi(z)/Xi(0)\`.

If any finite Gram matrix has a negative eigenvalue, the same source object
records a negative direction and falsifies Hilbert descent.

Hence the unconditional construction is not a hidden RH proof: it is
indefinite until the exact missing positivity theorem is supplied.

## Relation to the coefficient--Betti double

Ledger 1390 obtains the prime trace as a signature \`(+,-)\` polarization.
The kernel form above is the completed, cutoff-free scalar shadow expected
from that signed double. What has not been derived is a map from actual
coefficient--Betti boundary vectors into \`V_Xi\` whose Gram form reproduces
\`K_Xi\`.

Such a map would have to:

1. send finite-cutoff prime cross propagators to kernel vectors;
2. include the gamma and Gaussian corner channels;
3. intertwine cutoff refinement with the radical quotient; and
4. make positivity a source theorem rather than an imposed completion.

## Determinant status

The scalar identity

\`M=-d/dz log Xi\`

already reconstructs \`Xi\` by integration. But a characteristic determinant
of a fixed Hilbert self-adjoint operator exists only after positive descent.
Before that, \`Xi\` is the scalar boundary characteristic function of an
indefinite preshape, not the spectral determinant requested by the goal.

## Scope

This constructs a canonical source-derived algebraic indefinite boundary
preshape and proves that its Hilbert descent is equivalent to RH. It does not
construct the coefficient--Betti comparison map, a canonical Krein
completion, or the required positive self-adjoint operator.
