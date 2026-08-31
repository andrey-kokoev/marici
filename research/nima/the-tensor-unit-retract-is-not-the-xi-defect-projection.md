# The tensor-unit retract is not the Xi defect projection

## Available source splitting

On the diagonal Mellin orbit,

\[
\Delta f=(\mathcal M_nf)_{n\ge1},
\]

the multiplicative unit label supplies the canonical counit

\[
\varepsilon_1
=
\mathcal M_1^{-1}\operatorname{ev}_1,
\qquad
\varepsilon_1\Delta=I.
\]

Therefore the labelled carrier has a source-derived splitting into the unit
coordinate and the kernel of unit evaluation.

## Different target line

The Xi defect line is defined by the theta Mellin dual section after complete
label synthesis and Fourier--Poisson sewing.  Its value depends on the full
label packet, not only the \(n=1\) coordinate.

The unit counit instead serves the first Adams constructor before scalar theta
synthesis.  It deliberately discards all coordinates with \(n>1\).

Hence

\[
\operatorname{ran}\Delta
\xrightarrow{\varepsilon_1}
H
\]

is a constructor retract, while

\[
\mathcal L_\theta
\xrightarrow{\tau}
\mathcal O
\]

is the divisor-bearing completed observer.  These maps have different source
and target types.

## Kernel mismatch

The kernel of \(\varepsilon_1\) contains every labelled packet with zero unit
coordinate, including packets with nonzero completed theta synthesis.  Thus
\(\varepsilon_1\) is not faithful on the full label carrier.

Conversely, a Xi-zero packet can have a nonzero \(n=1\) coordinate whose
contribution is cancelled by the retained higher labels after synthesis.
Therefore

\[
\ker\tau
\ne
\ker\varepsilon_1
\]

in general.

No source theorem currently identifies these kernels after restriction to the
completed divisor family.

## Projection consequence

The bounded projection supplied by unit evaluation cannot be used as the
splitting

\[
H=i(\mathcal L_\theta)\oplus Q
\]

required for the G4 defect/complement normal form. Doing so would replace the
Xi defect line by the first Adams tensor-unit fibre and erase higher-label
cancellation.

## Valid retained use

The tensor-unit retract remains authoritative for:

- recovering the single Stieltjes boundary copy;
- fixing first-Adams normalization;
- proving the unit-fibre Green metric comparison;
- applying constructor counit before scalar theta synthesis.

It supplies no divisor projection and no Xi kernel state.

## G4 consequence

The source-derived Xi defect projection remains missing. The most obvious
existing retract has the wrong kernel and cannot isolate the divisor-bearing
line. A valid projection must retain complete theta synthesis and be derived
before zero inspection, likely through a chain map from the Xi Koszul line
rather than label-unit evaluation.

No RH conclusion is authorized.
