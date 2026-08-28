# Positive absolute separation does not confine complex zeros

## Result

The Green separation port has a simpler exact form than its signed presentation
suggests. For a nonnegative source measure \(f\),

\[
K_f(z)
=
\iint f(q)f(v)\operatorname{sgn}(v-q)
\sinh\!\bigl(z(v-q)\bigr)\,dq\,dv
=
\iint f(q)f(v)\sinh\!\bigl(z|v-q|\bigr)\,dq\,dv.
\]

Thus \(K_f\) is the hyperbolic-sine transform of the positive pushforward of
\(f\otimes f\) by absolute separation. This explains its strict sign on the
positive real axis. It does not confine its complex zeros to the reciprocal
seam.

## Smallest explicit hostile source

Take the positive three-atom source

\[
f=\delta_0+2\delta_1+\delta_2.
\]

The ordered pairs at distance one have total weight eight, and those at
distance two have total weight two. Therefore

\[
K_f(z)=8\sinh z+2\sinh(2z)
=4\sinh z\,(2+\cosh z).
\]

Besides the seam zeros of \(\sinh z\), the second factor vanishes at

\[
z=\pm\operatorname{arcosh}(2)+(2k+1)\pi i,
\qquad k\in\mathbb Z.
\]

These zeros have nonzero real part. Yet the source is positive, the order port
is positive for every positive real \(z\), and reciprocal oddness
\(K_f(-z)=-K_f(z)\) remains exact.

## Modular transport

Simultaneous reciprocal reflection of the two source coordinates reverses
both their order and their signed separation. Consequently the two signs
cancel inside the ordered integrand. The oriented port is invariant under the
combined reflection; modular symmetry preserves it rather than forcing it to
vanish or selecting the sign of its complex values.

## Consequence

The port is reconstructed by the full one-sided autocorrelation. Its following
visible properties are still insufficient for zero confinement:

- positive source measure;
- positive absolute-separation measure;
- positive real-axis orientation;
- reciprocal oddness;
- invariance under simultaneous source reflection.

The missing theta theorem must restrict the positive separation measure beyond
these properties. In particular, it must exclude the three-atom separation
polynomial by a labelled heat, Poisson, or arithmetic-scale coherence law.

## Falsifier for the next proposal

Any proposed modular order law that also admits
\(f=\delta_0+2\delta_1+\delta_2\) has no RH force. A successful law must reject
this source before inspecting the zeros of \(K_f\), and must identify the
specific source constructor that fails.
