# Fourier conjugation of the order port is universal Hardy boundary, not arithmetic current

## Question

The final Green forcing is the bilinear pairing through the order operator

\[
(Sg)(q)
=
\int_{\mathbb R}
\operatorname{sgn}(v-q)g(v)
\,dv.
\]

Does Fourier--Poisson conjugation of (S) produce the primitive and square
arithmetic currents, or only an archimedean boundary operator?

## Exact Fourier multiplier

Use the convention

\[
\widehat g(\xi)
=
\int_{\mathbb R}g(q)e^{-i\xi q}\,dq.
\]

Distributional differentiation gives

\[
\frac{d}{dq}Sg(q)=-2g(q).
\]

Therefore

\[
\widehat{Sg}(\xi)
=
2i\,\operatorname{pv}\!\left(\frac1\xi\right)
\widehat g(\xi).
\]

An arbitrary solution of the derivative equation could contain a
zero-frequency delta term.  The source order kernel removes that ambiguity:

\[
\operatorname{sgn}(v-q)
=
-\operatorname{sgn}(q-v)
\]

and reciprocal reflection gives

\[
RSR=-S.
\]

A constant kernel is reflection-even, so it is forbidden.  The principal
value multiplier is the unique reciprocal-odd convention.

## Bilinear Fourier formula

Extend the positive half-source by zero and set

\[
a_z(q)=f(q)e^{-zq},
\qquad
b_z(q)=f(q)e^{zq}.
\]

Bilinear Plancherel gives

\[
\langle a_z,Sb_z\rangle
=
\frac{i}{\pi}
\operatorname{pv}
\int_{\mathbb R}
\frac{
\widehat f(-\xi-iz)
\widehat f(\xi+iz)
}{\xi}
\,d\xi.
\]

This is the exact Fourier conjugation of the ordered port on its natural test
core.

## Half-line projection is the boundary operation

The completed bilateral theta seed may be Fourier-fixed, but the (f) in the
tail system is its positive-half restriction.  Writing

\[
f=P_+\Phi,
\]

one has

\[
\widehat{P_+\Phi}
=
\frac12\widehat\Phi
+
\frac{1}{2\pi i}
\operatorname{pv}
\int_{\mathbb R}
\frac{\widehat\Phi(\eta)}{\xi-\eta}
\,d\eta,
\]

with the same Fourier convention.

Thus Fourier transform and sector restriction do not commute.  Their defect
is the universal Hardy or Hilbert boundary operator.  This is the native
archimedean incidence carried by the ordered port.

## Why arithmetic currents do not appear yet

The principal-value multiplier and Hardy boundary formula hold for every
suitable real source.  They contain no prime labels, valuation multiplicities,
or Adams grades.  Consequently they cannot, by themselves, equal the
primitive or prime-square currents.

Those currents can enter only after the full nonarchimedean labelled source is
paired with the archimedean order port.  The possible architecture combines
the universal Hardy boundary with labelled adelic sampling to produce an
arithmetic boundary incidence.  The first input alone is insufficient.

## Consequence for the modular-current conjecture

The Fourier conjugation computation supplies an exact archimedean boundary
channel, but it does not close the doubled forcing.  A claimed cancellation
by the (k=1) and (k=2) currents must derive a separate labelled incidence
map from the restricted adelic source into this Hardy boundary space.

No scalar equality of cumulants can substitute for that map.

## Falsifiers

The proposed adelic incidence fails if:

- its constant mode violates (RSR=-S);
- it identifies the universal principal-value term with prime currents before
  labelled sampling;
- the two-shell or three-shell residual retains a nonzero prime label after
  the universal Hardy term is subtracted;
- or its graph domain is not preserved by reciprocal reflection.

## Result

Fourier conjugation of the ordered symplectic port is exactly the
principal-value inverse-frequency operator, with a Hardy boundary anomaly
created by half-line restriction.  This is universal archimedean incidence,
not the primitive or square arithmetic current.  The remaining construction
must join it to labelled adelic sampling before any cancellation claim is
typed.
