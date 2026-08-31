# Global Fourier–Poisson response intertwining reduces to archimedean cocycle and source identification

> **Correction.** The successor packet
> `correction-maximal-isotropic-response-descent-does-not-require-a-scalar-anomaly-line-trivialization.md`
> removes scalar anomaly-line trivialization from candidate two. Coherent
> line-valued or metaplectically twisted transport suffices for the
> maximal-isotropic response graph. The source-identification check remains.

## Question

After independently rereading the existing Fourier-orbit and horizontal-descent
packets, what remains of SCC candidate two?

## Claim boundary

The analytic response-density intertwiner, determinant-faithful four-chart
descent, and projective three-stratum continuity are already constructed as
separate theorems. Their composition leaves two source-specific checks:
identification of the declared global sewing with the length-preserving fiber
transport used by those theorems, and compatibility of the archimedean/anomaly
lines with the horizontal cocycle. This is a closure candidate only after those
checks; it is not currently an admitted completion of candidate two.

## Exact analytic orbit intertwiner

The response density cannot remain multiplication-only under Fourier. The
four presentations

\[
 M_j=\mathcal F^jM_f\mathcal F^{-j},
 \qquad
 u_j=\mathcal F^ju_0
\]

satisfy

\[
 \mathcal F(M_ju_j)=M_{j+1}u_{j+1}.
\]

Thus the complete multiplication/convolution/reflection orbit gives an exact
response-density and response-trace intertwiner before scalar aggregation.

## Determinant-faithful descent

The physical carrier is not the fourfold direct sum. It is the horizontal
equalizer

\[
 X_{\rm hor}
 =\{(x_0,x_1,x_2,x_3):x_{j+1}=F_jx_j\}.
\]

Evaluation at one chart is an equivalence. Consequently the descended pencil
has one kernel and one determinant multiplicity rather than a fourth power,
while all four response presentations remain related inside the state.

The Fourier graph remains maximal isotropic after this descent.

## Three-stratum completion

For a length-preserving unitary fiber transport, the sewing acts isometrically
on every projective exponential seminorm, unitarily on the Hilbert rung, and
continuously on the strong dual. It preserves Hilbert--Schmidt, trace-class,
and nuclear ideals.

Therefore primitive, square, connected, and wall strata admit the required
transport and contragredient action without collapsing their modalities.

## Remaining check one: source identification

The global Fourier--Poisson operator used by G4 must be shown to equal the
fiber transport used above. The required readback is:

- local vacuum fixed outside finitely many labels;
- valuation length preserved;
- prime and grade labels retained;
- local constant/delta exchange unitary in the declared fiber metric;
- reciprocal odd sign retained;
- no presentation-dependent Euler phase.

An abstract unitary with these properties cannot replace this source
identification.

## Remaining check two: archimedean and anomaly cocycle

The archimedean Tate multiplier is unitary on the sewing axis, but the
horizontal cocycle must also transport:

- the archimedean boundary line;
- the two bare-Euler \(\det_3\) anomaly lines;
- the relative \(\det_2\) return without double counting;
- any metaplectic central sign.

The order-four product must be the declared identity or the authorized line
character. Otherwise strict horizontal sections are replaced by twisted
sections, and determinant-line fidelity must be recomputed.

## Candidate-two square

After the two checks, the established pieces compose to

\[
 \mathcal O_{\partial,+}\operatorname{Tr}_+
 =W_{\rm FP}\mathcal O_{\partial,-}\operatorname{Tr}_-
\]

with response dual transported by \(W_{\rm FP}^{-*}\), on the descended
three-stratum carrier. The trace then lies in the maximal-isotropic sewing
graph with one Xi divisor multiplicity.

## Independence from candidate one

This construction transports any admitted kernel packet. It does not prove
that the unchanged Evans history satisfies the arithmetic lower equation.
Candidate one remains the independent requirement

\[
 B_\Sigma^\dagger\partial_z^ju(\cdot;z_0)=0.
\]

Candidate two cannot be marked closed merely because its response machinery is
ready for a state that candidate one has not yet promoted.

## Disposition

Candidate two is no longer an unspecified global response theorem. It reduces
to source identification of the global sewing and one archimedean/anomaly-line
cocycle audit. The analytic orbit, horizontal determinant-faithful descent, and
three-stratum topology are constructed. No RH conclusion is authorized.
