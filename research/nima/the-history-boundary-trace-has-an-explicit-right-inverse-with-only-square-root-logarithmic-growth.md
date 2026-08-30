# The history boundary trace has an explicit right inverse with only square-root logarithmic growth

## Result

The analytic boundary-triple side of the endpoint-lift problem admits an explicit right inverse.

On the interval

\[
[\log p,2\log p],
\]

affine interpolation realizes arbitrary primitive and square endpoint states with graph norm growing only as

\[
O(\sqrt{\log p}).
\]

This growth is far below the available prime-summability threshold. Hence analytic boundary lifting and global diagonal summability are not the remaining obstruction.

The missing datum is only the arithmetic-to-endpoint comparison that chooses the correct endpoint states and Green pairing.

## History graph

Let \(\mathcal H\) be the analytic endpoint Hilbert space and set

\[
L=\log p.
\]

Use the history graph

\[
\mathcal G_L
=
H^1([L,2L];\mathcal H)
\]

with norm

\[
\|h\|_{\mathcal G_L}^2
=
\int_L^{2L}
\left(
\|h(t)\|_{\mathcal H}^2
+
\|h'(t)\|_{\mathcal H}^2
\right)\,dt.
\]

The boundary trace is

\[
\Gamma_Lh=(h(L),h(2L)).
\]

## Explicit right inverse

For endpoints \(x,y\in\mathcal H\), define

\[
R_L(x,y)(t)
=
\frac{2L-t}{L}x
+
\frac{t-L}{L}y.
\]

Then

\[
R_L(x,y)(L)=x,
\qquad
R_L(x,y)(2L)=y.
\]

Therefore

\[
\Gamma_LR_L=I_{\mathcal H\oplus\mathcal H}.
\]

The construction is canonical after choosing the affine coordinate on the source comoving cell. It is not fitted to a scalar output.

## Graph estimate

For \(t\in[L,2L]\), convexity gives

\[
\|R_L(x,y)(t)\|^2
\le
\frac{2L-t}{L}\|x\|^2
+
\frac{t-L}{L}\|y\|^2.
\]

Integrating yields the sharper bound

\[
\int_L^{2L}\|R_L(x,y)(t)\|^2\,dt
\le
\frac L2
\left(
\|x\|^2+\|y\|^2
\right).
\]

The derivative is constant:

\[
\partial_tR_L(x,y)
=
\frac{y-x}{L}.
\]

Hence

\[
\int_L^{2L}
\|\partial_tR_L(x,y)\|^2\,dt
=
\frac1L\|y-x\|^2
\le
\frac2L
\left(
\|x\|^2+\|y\|^2
\right).
\]

Therefore

\[
\|R_L(x,y)\|_{\mathcal G_L}^2
\le
\left(
\frac L2+\frac2L
\right)
\left(
\|x\|^2+\|y\|^2
\right).
\]

Thus

\[
\|R_L\|
\le
\sqrt{\frac L2+\frac2L}.
\]

Since \(L\ge\log2\), the small-interval term is uniformly bounded, and

\[
\|R_L\|=O(\sqrt L)=O(\sqrt{\log p}).
\]

## Trace lower control

Because \(\Gamma_LR_L=I\), the endpoint pair is exactly retained. The right inverse introduces no radical on the endpoint plane.

The standard trace theorem also gives a bounded \(\Gamma_L\), though its constant depends on \(L\). On the range of \(R_L\), the endpoint data and affine history are topologically equivalent with explicit constants.

## Prime summability

The strict primitive-square coefficient product has size

\[
\frac12p^{-3/2-\sigma}.
\]

Even if two affine history lifts contribute a full factor of \(O(\log p)\), the diagonal majorant is

\[
\sum_p
\frac{\log p}{p^{3/2+\sigma}},
\]

which converges uniformly through \(\sigma=0\).

Thus the analytic right-inverse growth lies safely below the earlier exponent budget \(\theta<1/2\).

No power growth in \(p\) is introduced.

## Compatibility with raw windows

For the actual endpoint windows,

\[
x=M_{W_L}\psi,
\qquad
y=M_{W_{2L}}\psi,
\]

the contraction bounds give

\[
\|x\|,\|y\|\le\|\psi\|.
\]

Hence

\[
\|R_L(M_{W_L}\psi,M_{W_{2L}}\psi)\|_{\mathcal G_L}
\le
\sqrt{L+\frac4L}\,\|\psi\|.
\]

The source history \(t\mapsto M_{W_t}\psi\) may be preferable to affine interpolation because it satisfies the actual differential Green identity. The affine right inverse is not a replacement for that source history; it proves surjectivity and a quantitative trace-range bound.

## Green identity qualification

An arbitrary affine history has endpoint difference

\[
y-x
=
\int_L^{2L}h'(t)\,dt,
\]

but it need not reproduce the source multiplication propagator

\[
M_{W_{2L}-W_L}.
\]

Therefore the right inverse closes:

- boundary trace existence;
- endpoint surjectivity;
- graph growth;
- cutoff-compatible summability.

It does not close:

- the source Green/Stokes kernel;
- arithmetic delta incidence;
- reciprocal adjoint orientation;
- the pulled-back mixed form.

## Constructor consequence

The endpoint-lift problem now separates into two arrows:

\[
\text{arithmetic endpoint packet}
\xrightarrow{J_{P,p}\oplus J_{Q,p}}
\mathcal H\oplus\mathcal H
\xrightarrow{R_L}
\mathcal G_L.
\]

The second arrow exists explicitly and has harmless logarithmic growth.

The first arrow remains the earliest missing constructor. It must identify the primitive and square arithmetic incidences with the correct analytic endpoint states in the reduced Green metric.

## Next gate

The next source extraction should therefore target only

\[
J_{P,p}\oplus J_{Q,p}:
\mathcal P_{\sigma,p}\oplus\mathcal Q_p
\longrightarrow
\mathcal H\oplus\mathcal H.
\]

Once that map is constructed with uniform endpoint scales, the history graph lift and prime-diagonal completion follow automatically.
