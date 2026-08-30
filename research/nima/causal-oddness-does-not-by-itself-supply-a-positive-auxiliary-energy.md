# Causal oddness does not by itself supply a positive auxiliary energy

## Fourier multiplier audit

On the bilateral logarithmic carrier, let

\[
(H_+f)(t)
=
\int_0^\infty \Phi(r)f(t+r)\,dr
\]

with real integrable history kernel \(\Phi\). Its adjoint is the reflected causal history \(H_+^*=RH_+R\).

Under Fourier transform,

\[
m_+(\xi)
=
\int_0^\infty\Phi(r)e^{i\xi r}\,dr,
\qquad
m_-(\xi)=\overline{m_+(\xi)}.
\]

The source-native skew history is

\[
T_{\mathrm{hist}}
=
\frac{H_+-H_+^*}{2},
\]

with multiplier

\[
i\,\operatorname{Im}m_+(\xi).
\]

Thus

\[
iT_{\mathrm{hist}}
\]

is Hermitian with real multiplier

\[
-\operatorname{Im}m_+(\xi)
=
-\int_0^\infty\Phi(r)\sin(\xi r)\,dr.
\]

The reciprocal-odd typing is exact.

## The tempting even block

The most immediate even companion is

\[
S_{\mathrm{hist}}
=
\frac{H_++H_+^*}{2},
\]

whose multiplier is

\[
\operatorname{Re}m_+(\xi)
=
\int_0^\infty\Phi(r)\cos(\xi r)\,dr.
\]

But \(\Phi\ge0\) does not imply that this cosine transform is positive. Even when it is positive, it need not dominate the sine transform.

Therefore causal/anti-causal decomposition alone does not prove

\[
S_{\mathrm{hist}}\pm iT_{\mathrm{hist}}>0.
\]

It supplies orientation, not positive auxiliary energy.

## Exact scalar contraction test

Where \(\operatorname{Re}m_+(\xi)>0\), the normalized auxiliary odd multiplier is

\[
k(\xi)
=
-\frac{\operatorname{Im}m_+(\xi)}
{\operatorname{Re}m_+(\xi)}.
\]

The contraction theorem becomes

\[
\operatorname*{ess\,sup}_{\xi}
\left|
\frac{\operatorname{Im}m_+(\xi)}
{\operatorname{Re}m_+(\xi)}
\right|
<1.
\]

Equivalently, the boundary values of the history transform must remain inside the open sector

\[
|\arg m_+(\xi)|<\frac{\pi}{4}
\]

up to the frozen sign convention. This is a strict sectoriality theorem, not a consequence of causality.

## Minimal hostile

Take

\[
\Phi(r)=e^{-r}.
\]

Then

\[
m_+(\xi)
=
\frac{1}{1-i\xi}
=
\frac{1+i\xi}{1+\xi^2}.
\]

Its even part is positive:

\[
\operatorname{Re}m_+(\xi)
=
\frac1{1+\xi^2},
\]

but

\[
\left|
\frac{\operatorname{Im}m_+(\xi)}
{\operatorname{Re}m_+(\xi)}
\right|
=
|\xi|.
\]

Hence the normalized odd operator is unbounded and the auxiliary contraction fails outside \(|\xi|<1\). A perfectly valid causal history with exact reflected adjoint does not yield a positive global block \(S+iT\).

## Possible positive companions

A different positive even block could be built from objects such as

\[
H_+^*H_+,
\qquad
|H_+|,
\qquad
\text{or a source Green energy}.
\]

But none is interchangeable with \((H_++H_+^*)/2\). Each changes the order, units, kernel, and Schur return. It must be independently derived from the source Green identity.

In particular, choosing \(S=|iT|+\varepsilon I\) would force positivity algebraically but would be a fitted majorant unless source-authorized.

## Rigged-domain qualification

The multiplier ratio may be unbounded on the ambient Hilbert space while defining a continuous map between different rigging rungs. That can authorize a sectorial form, but not the Hilbert contraction previously claimed. The theorem must state whether \(K\) is:

- a bounded Hilbert contraction;
- a relatively form-bounded perturbation;
- or only a continuous rigged-space arrow.

These geometries lead to different Schur and completion theorems.

## Revised constructor split

The source burdens are now independent:

1. causal reflection derives \(T_{\mathrm{hist}}\) and its reciprocal sign;
2. the Green/PV source derives a positive even block \(S\);
3. a sectorial domination theorem proves
   \[
   |\langle x,iT_{\mathrm{hist}}x\rangle|
   \le
   (1-\varepsilon)\langle x,Sx\rangle;
   \]
4. endpoint compression identifies the Euler odd port.

The next calculation must extract the actual history kernel \(\Phi\) and source Green energy \(S\), then test their cosine-sine or form-sector bound. Causality alone closes only the orientation gate.
