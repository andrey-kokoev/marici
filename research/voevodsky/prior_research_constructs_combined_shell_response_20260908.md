# Prior research constructs the combined shell response

Date: 2026-09-08

## Off-diagonal pair current

The localized ordered-pair synthesis is explicit for Gaussian atoms.  For

\[
\rho_{nm}^{[a,b]}(t)
=
\int_a^b e^{-\pi n^2x^2}e^{-\pi m^2(x+t)^2}\,dx,
\]

completion of the square gives a closed error-function formula.  A second source identity reduces every completed-theta pair shell to one base kernel:

\[
\rho_{nm}^{[a,b]}(t)
=(nm)^{-1/2}
K_{[a+\log n,b+\log n]}
\left(t+\log\frac mn\right).
\]

Product degree gives the half-density coefficient; ratio degree translates separation; the first label translates the shell.

The oriented ratio cocycle is also constructed uniquely:

\[
(\partial_d-z)C(z;d)=K_{[A,B]}(d),
\qquad C(z;0)=0.
\]

It organizes off-diagonal linking and reciprocal reversal, but vanishes identically on `n=m`.

## Diagonal response is fixed

For one diagonal label and shell define the Laplace sections `R`, endpoint section `E`, and Wronskian section `W`.  Radial Stokes gives

\[
zR(z)-\rho(0)=E(z)-\frac12W(z).
\]

With the existing shell conventions,

\[
I^{(0)}=-R,
\qquad
I^{(\mathrm{end})}=-2E.
\]

Therefore the combined reciprocal-plus-linking response required for exact shell cancellation is uniquely fixed:

\[
I^{(\mathrm{recip})}+I^{(\mathrm{link})}
=R+2E
=
\frac{\rho(0)+E-\frac12W}{z}+2E.
\]

The apparent quotient is removable at `z=0`, so this is an entire source section and determines every multiplicity jet.

## Correct remaining obstruction

The shell function itself is no longer missing.  What remains undefined is its source-authorized split into the frozen G4 reciprocal and linking ports, including arithmetic loading and analytic-transpose orientation.

This split matters because the ratio-Stokes cocycle cannot carry the dominant late-shell diagonal contribution: it and all of its parameter jets vanish for `(n,m)=(1,1)`, while that pair dominates late shells.  The diagonal reciprocal port, or a separately constructed diagonal linking port, must realize the bordered response above.

## Disposition

Prior research constructs both the off-diagonal ratio cocycle and the exact combined diagonal response.  Candidate one is blocked only at realization of that response by the declared conservative Green-complex ports.  Assigning the two summands after inspecting Xi zeros would be fitted and is prohibited.

## Evidence

- `research/nima/the-localized-polarized-gaussian-correlation-synthesis-has-an-exact-erf-kernel.md`
- `research/nima/every-completed-theta-pair-shell-is-a-product-weighted-ratio-translate-of-one-base-correlation-kernel.md`
- `research/nima/the-oriented-ratio-cocycle-is-the-unique-zero-initial-solution-of-a-first-order-stokes-equation.md`
- `research/nima/the-radial-stokes-identity-fixes-the-exact-combined-diagonal-reciprocal-linking-section.md`
- `research/nima/the-ratio-stokes-cocycle-vanishes-on-the-dominant-diagonal-pair-so-the-reciprocal-port-must-carry-the-late-shell-bulk-correction.md`
