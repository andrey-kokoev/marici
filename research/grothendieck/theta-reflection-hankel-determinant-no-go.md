# Reflection compression gains discreteness but loses the xi density

Epistemic-graph event: 1412.

## Canonical non-translation-invariant quotient

Let \`k\` be the real even theta kernel from Ledger 1377, normalized so that
its Fourier transform is \`Xi(t)\). Let \`R f(y)=f(-y)\` be logarithmic
reflection and \`P_+\` restriction to the functional-equation fundamental
domain \`R_+=(0,infinity)\`.

The reflected compression

\`H=P_+ C_k R P_+^*\`

has the Hankel kernel

\`H(x,y)=k(x+y)\`, for \`x,y>0\`.

This is the first canonical operation in the present source that breaks
translation invariance: it uses precisely the involution behind
\`s <-> 1-s\`, not a boundary fitted to zeros.

## Compact discrete spectrum

The theta kernel and all of its derivatives decrease faster than every
exponential on the positive half-line. Hence \`k(x+y)\` is a smoothing,
rapidly decreasing kernel on the quadrant. The resulting Hankel operator is
self-adjoint and belongs to every Schatten class. In particular it is trace
class and has a discrete real spectrum \`lambda_n\` accumulating only at zero.

Moreover, for every \`N>0\`, its singular values obey

\`s_n(H)=O_N(n^{-N})\`.

This follows by factoring the smoothing map through arbitrarily high weighted
Sobolev spaces and using the corresponding compact-embedding singular-value
bounds.

Thus reflection compression genuinely repairs the continuous-spectrum defect
of the full-line theta multiplier.

## Fredholm determinant density

Its canonical Fredholm determinant is

\`F_H(z)=det(I-zH)=prod_n(1-z lambda_n)\`.

The zeros are the reciprocal nonzero eigenvalues \`z_n=1/lambda_n\`. The
rapid singular-value decay forces extremely sparse reciprocal zeros. Indeed,
for every positive integer \`N\`,

\`#{n:|z_n|<=R}=#{n:|lambda_n|>=1/R}=O_N(R^(1/N))\`.

Hence the zero count is \`O_epsilon(R^epsilon)\` for every \`epsilon>0\`.
Completed Riemann \`xi\`, by contrast, has \`asymp R log R\` zeros in a disk
of radius \`R\`. Therefore

\`det(I-zH) != exp(a z+b) xi(alpha z+beta)\`

for every nonzero affine scaling \`alpha\`; a nowhere-zero exponential cannot
change the zero count.

There is also a reality obstruction: because \`H\` is self-adjoint, every zero
of its coupling determinant is real. Equality with a critical-line
normalization of \`xi\` would already imply the Riemann hypothesis. The density
contradiction is unconditional and stronger for this particular operator.

## Interpretation

The theta-reflection quotient passes two gates that the direct convolution
failed: it is source-derived and has discrete spectrum. It fails the third
gate because smoothing is too strong. The Riemann spectrum needs eigenvalues
whose reciprocals have \`R log R\` density, whereas the theta Hankel
eigenvalues decay faster than every power.

A viable nonlocal boundary cannot simply compress the completed smooth theta
kernel. It must retain a first-order or singular component—presumably the
intrinsic-prime scattering trace—strong enough to produce the required Weyl
density.

## Scope

This is a determinant no-go for the canonical theta reflection-compressed
Hankel operator and its affine rescalings. It does not exclude singular Hankel
systems, energy-dependent boundaries, or prime-coupled canonical systems.
