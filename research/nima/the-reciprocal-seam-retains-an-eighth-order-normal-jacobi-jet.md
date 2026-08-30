# The reciprocal seam retains an eighth-order normal Jacobi jet

## Result

The scalar odd port

\[
\Phi'(u)
\]

must vanish at the reciprocal seam \(u=0\). The correct seam datum is its first normal jet,

\[
\nu_{\mathrm{seam}}=\Phi''(0).
\]

Differentiating the exact derivative-comb realization gives a source-defined eighth-order Jacobi formula. Thus scalar seam cancellation does not erase the odd constructor; it moves the information into a normal jet.

This note constructs that jet. It does not yet prove its nonvanishing or a uniform lower bound.

## Starting formula

With \(r=e^{2u}\),

\[
\Phi'(u)
=
e^{u/2}
\left[
\frac{r^3}{8\pi^3}\Theta_6
+
\frac{15r^2}{8\pi^2}\Theta_4
+
\frac{15r}{4\pi}\Theta_2
\right],
\]

where

\[
\Theta_k=\partial_z^k\Theta(0,r).
\]

The heat equation gives

\[
\partial_u\Theta_k
=
\frac{r}{2\pi}\Theta_{k+2}.
\]

## Exact normal derivative

Differentiate term by term. The eighth-order contribution is

\[
\frac{r^4}{16\pi^4}\Theta_8.
\]

The sixth-order coefficient receives contributions from the differentiated sixth-jet coefficient and from heat propagation of the fourth jet:

\[
\frac{13r^3}{16\pi^3}
+
\frac{15r^3}{16\pi^3}
=
\frac{7r^3}{4\pi^3}.
\]

The fourth-order coefficient is

\[
\frac{135r^2}{16\pi^2}
+
\frac{30r^2}{16\pi^2}
=
\frac{165r^2}{16\pi^2}.
\]

The second-order coefficient is

\[
\frac{75r}{8\pi}.
\]

Therefore

\[
\Phi''(u)
=
e^{u/2}
\left[
\frac{r^4}{16\pi^4}\Theta_8
+
\frac{7r^3}{4\pi^3}\Theta_6
+
\frac{165r^2}{16\pi^2}\Theta_4
+
\frac{75r}{8\pi}\Theta_2
\right].
\]

At the seam \(r=1\),

\[
\nu_{\mathrm{seam}}
=
\frac{1}{16\pi^4}\Theta_8(0,1)
+
\frac{7}{4\pi^3}\Theta_6(0,1)
+
\frac{165}{16\pi^2}\Theta_4(0,1)
+
\frac{75}{8\pi}\Theta_2(0,1).
\]

## Derivative-comb form

For the Gaussian front \(g_{z,r}\),

\[
\langle\Delta',\partial_z^k g_{z,r}|_{z=0}\rangle
=
-\Theta_{k+1}(0,r).
\]

Define the seventh-order odd normal-front jet

\[
J_{\mathrm{normal}}(u)
=
e^{u/2}
\left[
\frac{r^4}{16\pi^4}\partial_z^7
+
\frac{7r^3}{4\pi^3}\partial_z^5
+
\frac{165r^2}{16\pi^2}\partial_z^3
+
\frac{75r}{8\pi}\partial_z
\right]g_{z,r}\bigg|_{z=0}.
\]

Then

\[
\Phi''(u)
=
-\langle\Delta',J_{\mathrm{normal}}(u)\rangle.
\]

In particular,

\[
\nu_{\mathrm{seam}}
=
-\langle\Delta',J_{\mathrm{normal}}(0)\rangle.
\]

The observer and state remain elliptic-odd; their contraction is elliptic-even. Under reciprocal scale reflection, \(\Phi'\) is odd and its outward normal derivative at the fixed seam is an even scalar attached to an oriented normal line. Reversing the chosen normal reverses the typed normal coordinate even though the numerical second derivative is unchanged.

## Jet-valued seam port

The appropriate seam observer is not the scalar value alone. It is the first jet

\[
j^1_0(\Phi')
=
\left(
\Phi'(0),\Phi''(0)
\right)
=
\left(
0,\nu_{\mathrm{seam}}
\right).
\]

This is the standard fixed-point behavior of an odd function. The zero value records reciprocal antisymmetry; the normal component records the surviving oriented amplitude.

Consequently, a seam observer margin should be formulated on the normal line:

\[
|\nu_{\mathrm{seam}}|
\ge
m_{\mathrm{normal}}
\|J_{\mathrm{normal}}(0)\|_{\mathrm{source}},
\]

not on the vanished scalar component.

## Analytic typing

The new formula raises the direct spatial trace order from six to eight. A naive ambient Sobolev realization of eighth derivative evaluation requires

\[
s>\frac{17}{2}.
\]

That is only a sufficient fallback. The source heat orbit again offers the sharper route: on a uniformly positive heat range, every fixed derivative evaluation is bounded relative to a midpoint heat-history graph norm, with a constant depending on derivative order and the positive sub-time.

The seam is at \(r=1\), so positive heat time is available locally. The remaining issue is whether the adjacent-window incidence carries that heat-history graph norm into the seam attachment.

## Nonvanishing remains a theorem

Parity alone does not imply

\[
\nu_{\mathrm{seam}}\ne0.
\]

An odd smooth function may vanish to third or higher order. The explicit theta series makes the question finite and falsifiable, but the sign or nonzero value must be proved from the source series or an authorized monotonicity theorem.

Therefore the seam gate separates:

1. construction of the normal jet — completed here;
2. boundedness on the source heat range;
3. nonvanishing of \(\nu_{\mathrm{seam}}\);
4. comparison with the Wronskian and Euler odd ports;
5. a normalized lower frame bound.

## Next calculation

The next exact test is:

> Evaluate the eighth-order theta combination defining \(\nu_{\mathrm{seam}}\), prove its sign without numerical fitting, and compare its normalization with the source Wronskian current.

That theorem would turn the jet-valued seam port from a typed carrier into a faithful observer.
