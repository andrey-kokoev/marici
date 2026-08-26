# Pole-clock parameter identifiability: WP457

## Question

If WP448's poles and WP449's widths were experimentally calibrated, would they determine the two source parameters (g_F,mu) and the dimensionless flavor scale (g_F f/v)?

## Frozen source map

Define the flavon norm by the WP447 vacuum equation

\[
f^2=\sum_i\operatorname{Tr}X_i^2=6\mu^2.
\]

On WP449's conditional support domain, choose the triplet pole mass and common fractional width as the two readouts

\[
m_1=g_F\mu,
\qquad
r_\Gamma=\frac{\Gamma_1}{m_1}=\frac{g_F^2}{4\pi}.
\]

Their source-response Jacobian is

\[
J=\frac{\partial(m_1,r_\Gamma)}{\partial(g_F,\mu)}
=
\begin{pmatrix}
\mu&g_F\\
g_F/(2\pi)&0
\end{pmatrix},
\qquad
\det J=-\frac{g_F^2}{2\pi}.
\]

It has rank two everywhere on the admitted domain (g_F>0,mu>0). The inverse reconstruction is

\[
g_F=\sqrt{4\pi r_\Gamma},
\qquad
\mu=\frac{m_1}{\sqrt{4\pi r_\Gamma}},
\qquad
f=\frac{\sqrt6m_1}{\sqrt{4\pi r_\Gamma}}.
\]

The requested dimensionless product is simpler:

\[
\frac{g_Ff}{v}=\frac{\sqrt6m_1}{v}.
\]

Thus a calibrated pole mass reads out (g_Ff/v) without using the width, while the width supplies the complementary information that separates (g_F) from (mu).

## Selector boundary

This construction does not select a numerical value. The WP447 source action still admits every positive (mu), and (g_F) remains an independent coupling. A future measured pole would determine the realized value; it would not explain why the source chose it. The map is therefore a rank-two parameter-identification readout, neither a source selector nor a presentation rigidifier.

The quintet supplies two overidentifying relations,

\[
\frac{m_3}{m_1}=\sqrt3,
\qquad
\frac{\Gamma_3}{\Gamma_1}=\sqrt3,
\]

which test the source representation independently of the reconstructed parameters.

## Instrument boundary

Formal pole coordinates are not yet an executable experiment. Admission as a physical readout requires a flavor-tagged production and decay channel, detector resolution narrower than the relevant pole separation and widths, calibrated luminosity and background response, and uncertainty support that leaves the smallest singular value nonzero. The very large low-energy flavor scale suggested by kaon sensitivity may make direct pole production inaccessible; that reach question must be computed rather than assumed.

No reference port is introduced. The pole mass is relational to the detector energy calibration and (v) is the independently measured electroweak clock.

## Smallest exact falsifiers

- (det J=0) at an admitted positive point.
- Either pole or width ratio fails its (sqrt3) overidentifying relation.
- A claimed numerical selection persists when (mu) is varied within the source action.
- Detector convolution collapses the calibrated Jacobian to rank below two.
