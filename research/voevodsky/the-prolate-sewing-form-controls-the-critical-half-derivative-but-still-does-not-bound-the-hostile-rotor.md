# The prolate sewing form controls the critical half derivative but still does not bound the hostile rotor

## Objective

The bare Plancherel bulk cannot Douglas-dominate real-boundary evaluation. The next possible source of control is the off-diagonal prolate sewing form, whose commutator estimate contains one logarithmic derivative of transition mass.

The resulting regularity is exactly the critical Sobolev order \(1/2\). Point evaluation in one dimension requires strictly more than \(1/2\). Therefore the known prolate sewing estimate still does not absorb the hostile rotor.

## Half-line commutator form

After logarithmic Fourier transform, let \(\Pi\) be the Hardy projection corresponding to the physical half-line cutoff, and let \(M_f\) denote multiplication by a sufficiently regular spectral function. The Hilbert--Schmidt commutator form has the standard kernel expression

\[
\|[\Pi,M_f]\|_{HS}^2
=
c
\iint_{
\mathbb R^2
}
\frac{
|f(x)-f(y)|^2
}
{
|x-y|^2
}
\,dx\,dy,
\]

up to the Fourier-normalization constant \(c>0\).

Equivalently,

\[
\boxed{
\|[\Pi,M_f]\|_{HS}^2
\asymp
\int_{
\mathbb R
}
|\xi|
|\widehat f(\xi)|^2
\,d\xi.
}
\]

The right side is the homogeneous Sobolev seminorm

\[
\|f\|_{\dot H^{1/2}}^2.
\]

This is the additive-coordinate form of the established multiplicative estimate

\[
\int
|h(a)|^2
|\log|a||
\,d^*a.
\]

Thus the known sewing row contributes exactly half a derivative.

## Criticality

In one real dimension, Sobolev embedding gives continuous point evaluation on

\[
H^s(\mathbb R)
\]

only when

\[
s>
\frac12.
\]

The endpoint space \(H^{1/2}\) does not embed into \(C^0\), and evaluation at a fixed point is unbounded.

## Explicit critical sequence

Choose smooth Fourier cutoffs supported in

\[
1\le
\xi
\le
N
\]

and equal to \(1\) on a slightly smaller interval. Define, schematically,

\[
\widehat f_N(\xi)
=
\frac{
\chi_N(\xi)
}
{\xi}.
\]

Then

\[
f_N(0)
=
\frac1{2\pi}
\int
\widehat f_N(\xi)
\,d\xi
\asymp
\log N,
\]

whereas

\[
\|f_N\|_{
\dot H^{1/2}
}^2
=
\int
|\xi|
|\widehat f_N(\xi)|^2
\,d\xi
\asymp
\log N.
\]

After normalization

\[
g_N
=
\frac{
f_N
}
{
\|f_N\|_{H^{1/2}}
},
\]

one has

\[
\|g_N\|_{H^{1/2}}
=1,
\]

but

\[
|g_N(0)|
\asymp
\sqrt{
\log N
}
\longrightarrow
\infty.
\]

Translation gives the same failure at every \(\gamma\in\mathbb R\).

Consequently

\[
|f(\gamma)|^2
\nleq
C
\left(
\|f\|_{L^2}^2
+
\|[\Pi,M_f]\|_{HS}^2
\right)
\]

for any universal \(C\).

## Symmetry-completed rotor

The two-point row

\[
b_{\pm\gamma}(f)
=
(
f(\gamma),
f(-\gamma)
)
\]

is likewise unbounded on the critical sewing graph. A translated critical sequence can concentrate at one rotor blade while remaining negligible at the other.

Therefore

\[
\boxed{
b_{\pm\gamma}
b_{\pm\gamma}^*
\npreceq
C_{L^2}
+
C_{sew}^{1/2}.
}
\]

Here \(C_{sew}^{1/2}\) denotes the positive quadratic form supplied by the known Hilbert--Schmidt commutator control.

## Relation to prolate transition mass

The sewing estimate has the form

\[
|\mathcal E_\Lambda(g)|
\le
\left[
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
\right]^{1/2}
\|[P,H_g]\|_{HS}.
\]

The transition mass satisfies the known scale

\[
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
=
O(\log\Lambda).
\]

This logarithm is consistent with the critical sequence above: endpoint evaluation can escape like \(\sqrt{\log N}\) under unit critical Sobolev control.

Thus the logarithmic prolate transition layer is not accidental slack. It is the characteristic critical behavior of half-derivative boundary regularity.

## What would suffice

Any one of the following would reopen the Douglas gate.

### Supercritical graph control

Prove that the physical common bulk controls

\[
\|f\|_{H^{1/2+\varepsilon}}
\]

for some \(\varepsilon>0\). Then

\[
|f(\pm\gamma)|^2
\le
C_{
\varepsilon,
\gamma
}
\|f\|_{H^{1/2+\varepsilon}}^2.
\]

No such estimate follows from the established Hilbert--Schmidt commutator form.

### Logarithmically strengthened endpoint space

At critical order, an additional logarithmic Fourier weight can make evaluation bounded, for example a norm controlling

\[
\int
(1+|\xi|)
\log^{1+\delta}(2+|\xi|)
|\widehat f(\xi)|^2
\,d\xi
\]

with \(\delta>0\).

The known prolate transition estimate does not supply this stronger logarithmic weight.

### Atomic rotor sector

Adjoin the two character fibers at \(\pm\gamma\). This bypasses Sobolev evaluation by representing the atoms with discrete counting measure.

This remains the minimal completion supported by the hostile fixture.

## Tetrahedral interpretation

The known \(H_{234}\) sewing face already contains a critical regularity row:

\[
H_{234}^{sew}
\sim
\dot H^{1/2}.
\]

The hostile rotor requires

\[
H_{234}^{rot}
\sim
\text{evaluation at }
\pm\gamma.
\]

The inclusion needed for a Douglas filler would be

\[

otag
H^{1/2}
\hookrightarrow
\mathbb C_\gamma
\oplus
\mathbb C_{-\gamma},
\]

but this inclusion is not continuous.

Thus the terminal pro-horn remains analytically open even after the sewing row is included. The obstruction sits exactly at the critical Sobolev threshold.

## Consequence for the positive lift

The internal transported positive rotor can still be defined formally. The external physical comparison cannot be contractive with respect to the currently proved Plancherel-plus-sewing norm.

Therefore the positive-lift gate has the sharpened form

\[
\boxed{
\text{physical rotor absorption requires either }
H^{1/2+\varepsilon}
	ext{ control, a supercritical logarithmic refinement, or atomic mass.}
}
\]

## Disposition

The existing prolate geometry does improve the bare \(L^2\) bulk, but only to the critical half-derivative boundary form. That regularity is still insufficient for point evaluation. The hostile rotor therefore survives the known sewing estimate.
