# Theta heat finite part constructs the relative Euler detector

## Theta-native regulator

Let the arithmetic label operator be

\[
 Ne_n=ne_n,
 \qquad N=e^Q,
\]

where `Q e_n=(log n)e_n`.  The theta source supplies the Gaussian heat
regulator

\[
 R_\varepsilon=e^{-\pi\varepsilon N^2},
 \qquad \varepsilon>0.
\]

Pairing the raw Euler covector with the regulated distinguished coefficient
state gives

\[
 Z_\varepsilon(s)
 =\sum_{n\ge1}n^{-s}e^{-\pi\varepsilon n^2}.
\]

For every positive `epsilon` this sum is absolutely convergent and is derived
from the source heat operator, not from the zero set.

## Boundary asymptotic

Mellin transformation of the Gaussian, or Euler--Maclaurin applied with the
same endpoint convention, gives for nonexceptional `s`

\[
\boxed{
 Z_\varepsilon(s)
 ={1\over2}\Gamma\left({1-s\over2}\right)
 (\pi\varepsilon)^{(s-1)/2}
 +\zeta(s)
 +\sum_{k\ge1}{(-\pi\varepsilon)^k\over k!}\zeta(s-2k).}
\]

The displayed series is interpreted in its standard local asymptotic domain;
for the finite-part statement only the constant term is required.

Thus the unique divergent heat-boundary channel in the critical half-strip is

\[
 B_\varepsilon(s)
 ={1\over2}\Gamma\left({1-s\over2}\right)
 (\pi\varepsilon)^{(s-1)/2}.
\]

For `1/2<Re(s)<1`, its magnitude diverges as `epsilon->0`, while all positive
powers of `epsilon` vanish.

## Relative detector

Define the source-relative heat pairing by its finite part:

\[
\boxed{
 \langle\ell_s^{\rm heat},\Omega_s^{\rm raw}\rangle_{\rm rel}
 :=\operatorname{FP}_{\varepsilon\downarrow0}
 \left[Z_\varepsilon(s)-B_\varepsilon(s)\right].}
\]

The expansion gives

\[
 \boxed{
 \langle\ell_s^{\rm heat},\Omega_s^{\rm raw}\rangle_{\rm rel}
 =\zeta(s).}
\]

Multiplication by the source-fixed archimedean gamma and elementary
completion factors produces the completed Tate readout.

This constructs the detector as a relative boundary value on the
Mellin/Fock rigging. It is not ordinary Riesz duality, in agreement with
packet 187.

## Compatibility with the two regularity sectors

The regulated bulk lies in every positive Mellin Hilbert level because of
Gaussian decay.  The removed term is a one-dimensional boundary current with
the exact complementary regularity.  Therefore the pairing has the form

\[
 \boxed{
 \text{regularized bulk}
 -\text{explicit heat boundary current}
 \longrightarrow\text{finite relative scalar}.}
\]

The boundary term is defined before inspecting any zero.  Changing it changes
the constant finite part and is not an innocent regularization convention.

## What this closes

The source-derived detector now exists in the critical half-strip as a
relative finite-part functional.  Together with packet 185:

1. the normalized distinguished Fock state exists in the open sector;
2. the raw Euler detector is correctly typed as distributional;
3. theta heat flow supplies a common regulator;
4. the explicit boundary current supplies the relative extension;
5. the finite part reproduces the Euler/Tate section.

Thus detector construction is no longer the missing object.

## What remains—and why it is exactly difficult

The finite-part value can vanish even though every regulated bulk sum is
nonzero.  A zero is cancellation between the diverging heat boundary channel
and the asymptotic bulk constant term:

\[
 \operatorname{FP}_{\varepsilon\downarrow0}
 [Z_\varepsilon(s)-B_\varepsilon(s)]=0.
\]

Consequently positivity of the Gaussian regulator and existence of the Fock
state do not orient the finite part.  The remaining theorem is precisely:

\[
 \boxed{
 \operatorname{FP}_{\varepsilon\downarrow0}
 [Z_\varepsilon(s)-B_\varepsilon(s)]\ne0
 \quad(\Re s>1/2),}
\]

with the completed boundary terms and reciprocal sector included.  This is a
source-native formulation of the RH transversality gate, not a proof of it.

## Hostile tests

1. Subtracting only the divergent magnitude but not its complex phase changes
   the finite part.
2. Replacing the Gaussian by an arbitrary cutoff requires a proved equality
   of boundary currents; equality of limiting scalars is insufficient.
3. Adding a finite counterterm manufactures a desired divisor and is
   unauthorized.
4. The hostile symmetric multiplier changes the finite part without arising
   from the heat boundary expansion, so it fails source provenance.

## Scope

This packet constructs one canonical theta-heat relative detector and computes
its finite part. It does not prove regulator-independence beyond
source-authorized heat/Poisson equivalences, nor prove nonvanishing of the
finite part in the critical half-strip.
