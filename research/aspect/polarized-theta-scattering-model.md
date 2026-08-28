# Polarized theta scattering model

## Result

The finite geometry of the Riemann-hypothesis question has an exact optical
scattering model. Move the critical line to the unit-circle seam in a complex
coordinate `w`. The relevant reflection is anti-holomorphic:

`rho(w)=1/conj(w)`.

Its fixed locus is the entire unit circle. Holomorphic inversion `w -> 1/w`
fixes only `w=1` and `w=-1` and is not a substitute.

Define the bounded signed normal coordinate

`eta(w)=(abs(w)^2-1)/(abs(w)^2+1)`.

Then `eta(rho(w))=-eta(w)`, and `eta(w)=0` exactly on the seam. This is the
finite optical observable corresponding to radial displacement from the
critical line. Tangential phase current may remain nonzero on the seam.

## Exact hostile pair

Take the unit-circle point `u=(3+4i)/5`. Its seam current witness is
`u-u^-1=8i/5`: purely imaginary and nonzero. Thus seam polarization cannot
mean scalar current zero.

The roots `2u`, `2conj(u)`, `u/2`, and `conj(u)/2` form a real reciprocal
quartet. Their monic polynomial is real and palindromic, so it obeys the
finite functional symmetry, yet none of its roots lies on the seam. The
normal coordinates are `3/5, 3/5, -3/5, -3/5`. Their total is zero while
every individual root is off-seam.

Therefore neither reciprocal symmetry nor aggregate normal-current
cancellation implies the RH condition. The checker must retain root-local
normal current.

## Optical instrument

Use a phase-referenced bidirectional scattering network. At each cutoff,
calibrate the open plant `A`, boundary injection `B`, return map `C`, and
direct block `E`. Close the network only after those records are frozen and
form the complete Schur complement

`S=E-C A^-1 B`.

Measure both field quadratures, both incidence directions, and all accessible
environment ports. Intensity alone is blind to global phase and cannot recover
the signed normal coordinate. A scalar transmission zero alone also supplies
no source-authorized internal paths.

The apparatus rejects an off-seam candidate when a conjugate-reciprocal zero
pair has nonzero root-local `eta`. It accepts only the finite geometric gate
when every resolved zero has `eta=0` and the source current equals the complete
Schur first jet at each cutoff.

## Authority firewall

The optical coefficients must be constructed from independently labelled
theta/Tate operations: prime, prime-square, seam, endpoint, and archimedean
channels. Fitting a network to known zeta zeros merely replays the input data.

Even a passing sequence of finite networks is not an RH proof. That requires
a common-domain continuum theorem showing that the source-derived determinants
converge to the completed theta determinant and that optical normal current is
faithful to arithmetic radial displacement without a growing blindness
kernel.

## Verification

Run:

```text
uv run --with sympy python research/aspect/checkers/check_polarized_theta_scattering_model.py
```
