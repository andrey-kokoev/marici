# The exponential radial test space continues the wall crossing and all Laplace jets entirely through the seam

## Question

Which explicit rigging replaces the divergent Hilbert resolvent at the radial seam?

## Claim boundary

The projective exponential test space makes every bilateral wall Laplace functional and every parameter jet continuous and entire. The free rank-one wall crossing consequently extends as an entire map from the test space to its strong dual. This constructs the free seam continuation, but not the full G4 arithmetic response or its vector-valued cancellation theorem.

## Test space

Define

\[
\mathcal S_{\exp}(\mathbb R_+)
=
\bigcap_{a>0}L^2(\mathbb R_+,e^{2at}dt)
\]

with seminorms

\[
p_a(f)=\|e^{at}f\|_2.
\]

The completed-theta radial densities, endpoint terms, and Wronskian currents belong to this space because they decay faster than every exponential.

## Entire Laplace functional

For \(z\in\mathbb C\), define

\[
\ell_z(f)=\int_0^\infty e^{-zt}f(t)\,dt.
\]

Choose \(a>|\operatorname{Re}z|\). Cauchy--Schwarz gives

\[
|\ell_z(f)|
\le
p_a(f)
\left(\int_0^\infty e^{-2(a+\operatorname{Re}z)t}\,dt\right)^{1/2},
\]

hence

\[
|\ell_z(f)|
\le
\frac{p_a(f)}{\sqrt{2(a+\operatorname{Re}z)}}.
\]

Because \(a>|\operatorname{Re}z|\), the denominator is positive on either side of the seam and on the seam itself. Thus \(\ell_z\in\mathcal S_{\exp}'\) for every complex \(z\).

## Jet bounds

Differentiation gives

\[
\partial_z^j\ell_z(f)
=(-1)^j\int_0^\infty t^j e^{-zt}f(t)\,dt.
\]

The same weighted estimate yields

\[
|\partial_z^j\ell_z(f)|
\le
p_a(f)
\left(
\frac{(2j)!}{[2(a+\operatorname{Re}z)]^{2j+1}}
\right)^{1/2}.
\]

On any compact parameter set \(K\), choose one \(a>\sup_{z\in K}|\operatorname{Re}z|\). Then all fixed jets are uniformly continuous on \(K\) with respect to the single seminorm \(p_a\).

Dominated differentiation proves that

\[
z\longmapsto\ell_z\in\mathcal S_{\exp}'
\]

is weakly entire and compact-locally equicontinuous on bounded test sets. No stronger dual-topology claim is needed here.

## Exponential kernel as a dual vector

The function

\[
k_z(t)=e^{-zt}
\]

need not lie in unweighted \(L^2\) on the seam. It nevertheless defines a continuous dual vector by the same pairing estimate. Therefore the rank-one expression

\[
C_z=-u\,k_z\otimes\ell_z
\]

is an entire continuous map

\[
C_z:\mathcal S_{\exp}\longrightarrow\mathcal S_{\exp}'.
\]

Its reciprocal partner uses \(e^{zt}\) and is controlled by choosing the same \(a>|\operatorname{Re}z|\). The two oriented half-plane Hilbert crossings are restrictions of these distinct rigged boundary channels.

## What is and is not continued

The construction continues the wall factorization and all Laplace jets. It does not assert that the unweighted Hilbert resolvent exists on the seam. Nor does it identify the incoming and outgoing boundary values: reciprocal orientation remains part of the doubled carrier.

The Volterra diagonal also acts continuously between suitable exponential test and dual rungs, but its exact projective continuity must be checked with the chosen source graph seminorms. The present theorem needs only the wall channel used by the radial border.

## Application to the radial Stokes section

For

\[
D_t\rho=e-\frac12w,
\]

the three functionals

\[
R(z)=\ell_z(\rho),
\qquad
E(z)=\ell_z(e),
\qquad
W(z)=\ell_z(w)
\]

are entire, and integration by parts gives

\[
zR(z)-\rho(0)=E(z)-\frac12W(z)
\]

for every \(z\), by analytic continuation from either convergent half-plane. Every parameter derivative may be taken inside the pairing.

Thus the exact radial section already has the rigged seam regularity that the free Hilbert resolvent lacks.

## G4 consequence

The canonical conservative interface should expose a Gelfand triple containing

\[
\mathcal S_{\exp}
\subset L^2(\mathbb R_+)
\subset\mathcal S_{\exp}'.
\]

Off the seam, its response must agree with the Hilbert resolvent formulas. On the seam, it must agree with the entire source pairing while preserving the two reciprocal boundary channels. This supplies a precise conformance test instead of an unspecified limiting-absorption condition.

The remaining hard gate is whether the arithmetic synthesis and its typed return act continuously on the same projective test space and make the full Schur response entire with all jets.

## Hostiles

A checker must reject:

1. choosing one fixed exponential weight for an unbounded parameter region;
2. using \(a+\operatorname{Re}z\le0\);
3. claiming an unweighted \(L^2\) kernel on the seam;
4. identifying the two reciprocal rigged channels;
5. continuing only the scalar zeroth-order response while omitting jets;
6. assuming arithmetic feature continuity from free wall continuity.

## Disposition

The free wall seam continuation is constructed explicitly on the projective exponential radial test space. All Laplace jets are entire and compact-locally bounded in one suitable seminorm. Candidate one is now narrowed to continuity and exact source identification of the arithmetic and Wronskian feature maps on this same rigging, followed by the polarized G4 chain comparison. No RH conclusion is authorized.
