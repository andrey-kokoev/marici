# Dimension-eight photon coefficient plane and helicity map

## Source conventions

Use the parity-even four-photon EFT

\[
\mathcal L_8=
\frac{g_2+f_2}{16}(F_{\mu\nu}F^{\mu\nu})^2+
\frac{g_2-f_2}{16}(F_{\mu\nu}\widetilde F^{\mu\nu})^2.
\]

The checker multilinearizes both quartic operators in four independently
labelled linearized field strengths.  This gives the contact tensor before any
helicity specialization.  Consequently replacing any polarization by its
momentum makes its field strength zero and proves all four Ward identities
without a gauge choice.

## Exact helicity image

In center-of-mass kinematics with energy normalized to one,

\[
s=4,qquad t=-2(1-\cos\theta),\qquad
u=-2(1+\cos\theta).
\]

After fixing the common S-matrix normalization by
\(\Phi_1=g_2s^2\), direct oriented-helicity contraction gives

\[
\boxed{
\Phi_1=16g_2,qquad
\Phi_2=8f_2(3+\cos^2\theta),qquad
\Phi_5=0.
}
\]

Equivalently,

\[
\Phi_1=g_2s^2,qquad
\Phi_2=f_2(s^2+t^2+u^2).
\]

The vanishing of \(\Phi_5\) is therefore exact at dimension eight; it is not
inserted as a Bell-state assumption.  The parity and identical-leg residuals
also vanish exactly.

## Marici interpretation

The two quartic field-strength tensors define a rank-two parity-even
coefficient fiber inside the fixed-kinematics four-point Ward quotient.  The
current Marici Carrier supplies the Ward/helicity evaluation machinery needed
to host this fiber.  It does not yet supply a scale-carrying integrated map
that chooses a particular ray \([g_2:f_2]\).

Thus the established statement is

\[
\text{Carrier-compatible coefficient plane},
\]

not

\[
\text{Carrier-derived QED coefficient vector}.
\]

Reproduce with:

```text
uv run --with sympy python research/nima/check_photon_d8_helicity_map.py
```
