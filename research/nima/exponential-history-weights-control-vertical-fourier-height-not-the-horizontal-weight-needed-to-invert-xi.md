# Exponential history weights control vertical Fourier height, not the horizontal weight needed to invert Xi

## Question

Does the existing rapid/projective completed-history topology already supply the exponential Fourier weight needed for raw two-line Xi deconvolution?

## Claim boundary

No by the declared seminorms. Exponential decay in the real logarithmic-history variable controls analytic continuation to vertical Fourier height. The inverse Xi multiplier instead requires exponential control in the real Fourier frequency, which corresponds to analytic continuation of the history itself in a complex physical strip. These are different regularity directions. No current carrier declaration identifies them.

## Existing history control

The rapid completed-history packets control weighted real-variable seminorms of the form

\[
P_{N,\eta}(h)
=
\sup_{t\in\mathbb R}
(1+|t|)^N e^{\eta|t|}
\left|\partial_t^j h(t)\right|,
\]

or their graph-norm analogues. Such control makes

\[
\widehat h(x+iy)
=
\int_{\mathbb R}h(t)e^{-ixt}e^{yt}\,dt
\]

well-defined for \(|y|<\eta\). It therefore controls the vertical displacement \(y=\operatorname{Im}z\).

This is exactly the direction used by the two-line observer at \(z=x\pm iR\).

## Missing horizontal control

Division by the completed Xi factor requires compensation for

\[
|\Xi(x\pm iR)|
\sim
\text{polynomial}(x)e^{-\pi|x|/4}.
\]

A raw observer must therefore control a quantity with the form

\[
e^{\pi|x|/4}(1+|x|)^{-N_R}
|\widehat h(x\pm iR)|.
\]

Exponential weight in \(x=\operatorname{Re}z\) is not a consequence of exponential decay in real \(t\). By Fourier duality, exponential decay in \(x\) is tied to holomorphic continuation of \(h(t)\) away from the real \(t\)-axis, together with boundary control in that complex strip.

Thus the two requirements are transverse:

\[
\text{real-history exponential decay}
\Longrightarrow
\text{vertical Fourier extension},
\]

whereas

\[
\text{complex-history strip control}
\Longrightarrow
\text{horizontal Fourier exponential decay}.
\]

The first arrow does not imply the second.

## Translation does not repair the mismatch

A source label acts by real translation,

\[
h(t)\longmapsto h(t-L_{p,k}).
\]

This changes vertical-line amplitudes by the expected factors \(e^{\pm RL_{p,k}}\), which is why the deconvolved Bohr observer recovers projective weights. It does not enlarge the complex-history strip or improve boundary regularity there. Prime summability therefore cannot manufacture the missing horizontal exponential weight.

## Current authority result

The labelled history carrier and its projective completion declare:

- real translations and reflection;
- real-variable rapid and exponential weights;
- graph derivatives and wall traces;
- projective summability over prime-power labels.

They do not declare:

- holomorphic continuation of every common history to a physical strip;
- boundary norms at the strip width selected by the gamma factor;
- a Paley--Wiener isomorphism carrying those boundary norms to the raw two-line Fourier observer.

Consequently the exponentially weighted raw-line norm is not currently an authorized consequence of the completed-history topology.

## Direction rescore

- Existing real-history weights as sufficient Xi compensation: rejected, 0/10.
- New physical-strip carrier with boundary norms: 5/10; mathematically plausible but lacks source and G4 authority.
- Specialized-range parametrix avoiding full strip control: 6/10.
- Deconvolved two-line recovery: completed conditionally.
- Label-retaining recovery before codiagonalization: completed and remains preferred.
- G4 choice between these routes: interface-blocked.

## Disposition

The raw post-codiagonal recovery route cannot be closed from the declared history seminorms. It needs a separately sourced complex-history strip topology or parametrix. Until G4 exposes such an observer, continuous source recovery must remain label-retaining. The next productive direction is to test whether a specialized-range coefficient extractor can use real-history localization without global Xi division; otherwise this branch terminates at the G4 interface gate. No RH or closed-range conclusion is authorized.
