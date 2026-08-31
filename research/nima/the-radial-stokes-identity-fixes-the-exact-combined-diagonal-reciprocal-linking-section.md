# The radial Stokes identity fixes the exact combined diagonal reciprocal-linking section

## Question

After aligning the radial endpoint convention with the existing analytic-transpose
shell endpoint port, what exact section must the combined reciprocal and linking
ports supply?

## Claim boundary

The combined diagonal response is fixed uniquely by the source autocorrelation,
endpoint, and Wronskian probes. No asymptotic coefficient remains free. This
constructs the exact density-level target for the sum of the reciprocal and
linking ports. It does not split that sum into the two frozen G4 ports or prove
that the canonical conservative complex realizes it.

## Radial probes

For one diagonal theta label and shell, set

\[
 R(z)=\int_0^\infty e^{-zt}\rho(t)\,dt,
\]

\[
 E(z)=\frac12\int_0^\infty e^{-zt}
 \left[
 \Phi(b)\Phi(b+t)-\Phi(a)\Phi(a+t)
 \right]dt,
\]

and

\[
 W(z)=\int_0^\infty e^{-zt}w(t)\,dt.
\]

The radial Stokes identity is

\[
 zR(z)-\rho(0)=E(z)-\frac12W(z).
\]

## Existing shell-port conventions

The ordinary analytic shell is

\[
 I^{(0)}(z)=-R(z).
\]

The positive-end Evans state obeys

\[
 u_z(x)=-\int_0^\infty e^{-zt}\Phi(x+t)\,dt.
\]

Hence the already totalized regular-derivative plus wall port is

\[
 I^{({\rm end})}(z)
 =\Phi(b)u_z(b)-\Phi(a)u_z(a)
 =-2E(z).
\]

The factor two is fixed by the definition of the radial endpoint density. It
must not be absorbed into the linking coefficient.

## Exact combined response

The diagonal shell residual is

\[
 \mathcal S^{\rm diag}(z)
 =I^{(0)}(z)+I^{({\rm end})}(z)
 +I^{({\rm recip})}(z)+I^{({\rm link})}(z).
\]

Therefore exact cancellation requires

\[
 I^{({\rm recip})}(z)+I^{({\rm link})}(z)
 =R(z)+2E(z).
\]

Using the radial graph law,

\[
 I^{({\rm recip})}(z)+I^{({\rm link})}(z)
 =\frac{\rho(0)+E(z)-\frac12W(z)}{z}
 +2E(z).
\]

This is an entire section: the numerator of the apparent divided term vanishes
at \(z=0\).

## Bordered interpretation

The response is not a bare scalar loading of the Wronskian coordinate. It is a
bordered first-order readout of the quadruple

\[
 \left(\rho(0),E,W,R\right),
\]

with coefficients fixed by the radial differential:

- initial-value coefficient \(1\);
- endpoint coefficient \(1\) inside the divided term;
- Wronskian coefficient \(-1/2\) inside the divided term;
- additional endpoint coefficient \(2\).

Any conservative-complex realization must reproduce this bordered relation
before codiagonal scalarization.

## Multiplicity

Because the identity holds as an entire source equation, differentiating it
fixes every Evans parameter jet. No separate jet-dependent normalization is
permitted.

At \(z=0\), derivatives are evaluated through the removable divided difference,
equivalently through radial moments.

## Label and shell assembly

The formula holds label by label and is additive under adjacent shells. Theta
synthesis occurs only after ordered-pair formation. Off-diagonal ratio-Stokes
terms remain separately typed and may not be inserted into the diagonal
formula.

## Remaining split problem

The exact sum does not determine a unique decomposition

\[
 R+2E
 =I^{({\rm recip})}+I^{({\rm link})}.
\]

That split requires the canonical G4 conservative-complex declaration:

- which bordered coordinates belong to reciprocal history;
- which belong to ordered linking;
- how the arithmetic loading acts;
- how analytic-transpose orientation is represented.

Fitting either summand after inspecting Xi zeros remains prohibited.

## Hostile

A proposed combined response fails immediately if it omits \(\rho(0)\), uses
endpoint coefficient one instead of the required bordered-plus-two structure,
or changes the Wronskian coefficient from \(-1/2\).

## Disposition

The exact combined diagonal reciprocal-linking section is constructed from the
radial source graph. Candidate one is no longer blocked by an unknown shell
function; it is blocked by the canonical G4 split and arithmetic realization
of this fixed bordered section. No RH conclusion is authorized.
