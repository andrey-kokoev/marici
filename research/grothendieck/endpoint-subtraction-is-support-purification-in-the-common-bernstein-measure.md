# Endpoint subtraction is support purification in the common Bernstein measure

## Question

What does the common-measure coherencer add to the endpoint-free cone, beyond another Hankel representation?

## Claim boundary

It identifies the endpoint subtraction as removal of one known atom outside the Hausdorff support interval and states the remaining all-rank problem as one relative quadratic-form bound. This is an exact retyping, not a proof of that bound.

## Common-measure transform

Suppose a heat kernel has a Laplace representation, initially allowing a signed measure or distribution,

\[
F(t)=\int e^{-tr}\,d\sigma(r).
\]

Then

\[
\Delta_h^{i+j+1}F(t)
=\int e^{-tr}(1-e^{-hr})^{i+j+1}\,d\sigma(r).
\]

Set

\[
z=1-e^{-hr},
\qquad
d\mu_{t,h}(r)=e^{-tr}(1-e^{-hr})\,d\sigma(r).
\]

The full Bernstein-basis matrix is one Gram family:

\[
M_{ij}=
\int z^{i+j}\,d\mu_{t,h}(r).
\]

For a polynomial `p`,

\[
\mathcal Q_F(t,h;p)
=\int |p(z)|^2\,d\mu_{t,h}(r).
\]

Separate saddle estimates for different entries discard this common measure.

## Endpoint support

The elementary endpoint kernel is

\[
K_E(t)=e^{t/4}=e^{-t(-1/4)}.
\]

It is the spectral atom `r=-1/4`. Under the Bernstein coordinate it maps to

\[
z_E=1-e^{h/4}<0,
\]

outside the Hausdorff interval `[0,1)`. This is exactly the superunit endpoint atom seen in the original `y=e^{-hr}` moment coordinate, where `y_E=e^{h/4}>1`.

Subtracting `K_E` is therefore support purification: it removes a completely known atom whose location is incompatible with nonnegative spectral rates. It is not an arbitrary normalization.

## Positive zero-side support

Under RH, every zero rate is `r=gamma^2>0`, so

\[
0<e^{-hr}<1,
\qquad
0<z=1-e^{-hr}<1.
\]

The endpoint-free matrices are Hausdorff moment matrices on `[0,1)`. Conversely, positivity of all polynomial squares together with the established decay and pole rigidity reconstructs support in that interval and forces nonnegative real zero rates.

## Source-side relative bound

A direct decomposition into gamma and prime forms does not supply a reference Hilbert norm: prior sectorwise tests show that the full gamma form is not established positive on every parameter range. Instead extract a declared positive archimedean reference form `mu_0`—for example the small-heat leading radial measure—and write

\[
\mu_{t,h}=\mu_{0,t,h}+\mathcal R_{\Gamma,t,h}+\mu_{P,t,h}.
\]

A sufficient source theorem is

\[
\langle p,p\rangle_{\mathcal R_\Gamma+P,t,h}
\ge -\langle p,p\rangle_{0,t,h}
\]

for every polynomial `p` and every positive `t,h` in the reference form's proved domain. Equivalently, after quotienting null directions and completing the positive reference form, the combined gamma-remainder-plus-prime form must define a self-adjoint relative operator `T_(t,h)` satisfying

\[
T_{t,h}\ge -I.
\]

The gamma remainder and prime functional must remain coupled. This tests one operator bound rather than entrywise or sectorwise signs.

## Authority boundary

Constructing `T` by Riesz representation already assumes that the combined remainder form is bounded in the positive reference norm. Neither finite matrices nor diagonal near-null estimates establish that boundedness. The full gamma form may not be silently treated as a positive norm. If the reference form is defined only by completing the target positive sum, the construction is circular.

## Disposition

The first missing source object is a degree-uniform lower bound for the coupled gamma-remainder-plus-prime functional in a separately proved positive archimedean reference norm, with relative spectral bound `-1`. The endpoint and support conventions are no longer ambiguous.