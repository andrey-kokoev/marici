# Positive-real impedance can have an off-seam dark scattering zero

## Result

The control-theoretic retyping of a scalar zero as a selected-channel
transmission zero removes another proposed orientation mechanism.

Losslessness, reciprocal sewing, stability, and even a strictly positive-real
source impedance do not imply zero-freeness of a selected scattering
amplitude.

## Exact one-port witness

Let the two open sectors be the right and left half-planes, with the imaginary
axis as their common seam. For a real parameter (a>0), define

\[
h_a(s)=\frac{s-a}{s+a}.
\]

This is the reflection amplitude obtained by the Cayley transform of

\[
Z_a(s)=\frac{1+h_a(s)}{1-h_a(s)}=\frac{s}{a}.
\]

The impedance is strictly positive-real in the open right half-plane:

\[
\operatorname{Re} Z_a(s)=\frac{\operatorname{Re}s}{a}>0.
\]

Nevertheless,

\[
h_a(a)=0.
\]

The selected reflection channel therefore has an off-seam zero at (s=a).
Its reciprocal partner is a pole at (s=-a).

The sewing law is exact:

\[
h_a(-\overline{s})=\frac{1}{\overline{h_a(s)}}.
\]

On the seam (s=i\omega), this reduces to

\[
|h_a(i\omega)|=1.
\]

Thus seam losslessness does not exclude an off-seam zero. It pairs that zero
with complementary-sector pole data.

## Physical interpretation boundary

The zero is an analytic matching point: at (s=a), the source impedance equals
the reference impedance and the reflected transfer vanishes. But (s=a) is
off the physical frequency seam. This scalar witness alone does not authorize
an on-shell energy-routing claim. Literal transfer into a complementary port
requires an explicit lossless multiport dilation and a physical seam input.

This is the simplest exact distinction between:

- positivity of the source impedance;
- seam losslessness of the scalar scattering system;
- nonvanishing of one selected scattering coefficient.

The first two do not imply the third.

## Consequence for the theta/Tate programme

The critical seam can be the unitary sewing locus of two sectors without
confining the zeros of a distinguished scalar readout to that seam. Reciprocal
sewing supplies a divisor-pairing law, not an orientation law.

Any proposed RH mechanism based only on passivity, reciprocal symmetry, or a
positive-real Cayley transform is therefore incomplete. It must first prove
that the completed scalar section is itself the source-authorized impedance
quantity to which strict positivity applies. Applying positivity to an
upstream impedance while reading a downstream reflection or overlap leaves
dark transmission zeros admissible.

For a source-derived realization with distinguished transfer (h(s)), the
finite falsifier remains the Rosenbrock rank test

\[
\operatorname{rank}
\begin{pmatrix}
sI-A & -B\\
C & D
\end{pmatrix}
< n+m.
\]

The exact witness above passes the stronger upstream gate

\[
\operatorname{Re} Z_a(s)>0
\]

while failing selected-channel zero exclusion. Consequently the next viable
law must distinguish an impedance port from a scattering readout before any
positivity claim is transported.

## Decisive classification

Two-sector losslessness does not destroy off-seam zeros. It transports their
missing amplitude into complementary-sector pole or port data. The unresolved
RH content is not conservation but a source-derived theorem forbidding the
distinguished completed readout from being a dark scattering channel.
