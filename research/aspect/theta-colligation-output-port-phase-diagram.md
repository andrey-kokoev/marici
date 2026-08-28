# Theta colligation output-port phase diagram

## Result

The positive conservative completion of Nima's two-state theta source has an exact optical phase diagram. Let

\[
f(y)=2e^{-\pi y},\qquad
Q(r)=I+2r\sigma_x,\qquad |r|<\tfrac12.
\]

Then

\[
\det Q=1-4r^2,
\qquad
\rho(r,y)=\frac{f(y)^2}{\det Q}
=\frac{4e^{-2\pi y}}{1-4r^2}.
\]

The exact boundary is

\[
y_c(r)=\frac{\log 2-\tfrac12\log(1-4r^2)}{\pi}.
\]

It divides the strip into three apparatus regimes:

- if \(y>y_c(r)\), then \(\rho<1\): three output ports give a positive lossless completion, with slack amplitude \(\sqrt{1-\rho}\);
- if \(y=y_c(r)\), then \(\rho=1\): the slack port closes and exactly two output ports suffice;
- if \(y<y_c(r)\), then \(\rho>1\): output dilation alone is impossible; the apparatus needs an additional independent input reservoir or an indefinite completion.

A scalar output is impossible throughout the open strip. The dissipation matrix has eigenvalues \(1-2r\) and \(1+2r\), hence rank two there, while a scalar output Gramian has rank at most one.

## Optical meaning

The two response modes are not optional bookkeeping. They resolve the rank-two positive dissipation of the source colligation. The third detector is a slack channel measuring unused positive budget. Below the critical curve, no number of output-only slack detectors repairs the excess forcing: a new incident degree of freedom must enter.

Strominger's composite polarization connection cannot supply that degree of freedom. Because it is constructed from the response field, it removes the field's phase and becomes singular at a dark point. The required reservoir is independent of the measured response, regular on its declared domain, and capable of carrying its own curvature or defect data.

Thus the theta forcing itself predicts a change in minimal optical architecture. On the seam \(r=0\), the transition occurs at \(y=\log 2/\pi\). At \(y=\log 4/\pi\), three outputs work with slack \(\sqrt3/2\). At \(y=\log 2/(2\pi)\), \(\rho=2\), so a new input reservoir is compulsory.

This is an exact finite-dimensional realization constraint. It is not a proof of the Riemann hypothesis. Its value is sharper: any proposed positive optical realization of this theta source can be rejected by counting ports and locating its operating point relative to \(y_c(r)\).

## Reproduction

Run:

```text
uv run --with sympy python research/aspect/checkers/check_theta_colligation_port_phase_diagram.py
```

The checker verifies the determinant, spectrum, phase boundary, reflection symmetry, monotonicity, and three exact sample points.
