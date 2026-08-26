# Theta labelled readout is monoid augmentation, and prime transport preserves its zero ideal

## Status

Exact labelled transport no-go. The canonical half-line split fixes the
two-route covector ((1,1)). After retaining arithmetic labels, the remaining
scalar aggregation is the trivial augmentation of the positive-integer
constructor monoid.

Every prime multiplication transport preserves this augmentation. Therefore
it also preserves the full cancellation ideal. Prime transport and scalar
aggregation alone cannot exclude a zero; the first operation capable of seeing
motion transverse to the cancellation ideal is a nontrivial arithmetic
derivation such as logarithmic scale degree.

## Canonical half-line coefficient

For an even completed source, define

\[
H(z)=\int_0^\infty\Phi(u)e^{zu}\,du.
\]

The fixed contour split gives

\[
X(z)=H(z)+H(-z).
\]

Thus the half-line readout really is the source-selected covector

\[
c_{\mathrm{half}}=(1,1).
\]

The antipodal coordinate is therefore canonical for this particular route
resolution. Grothendieck's hostile-source theorem shows that this structure is
universal among even rapidly decaying sources and has no zero-confinement force
by itself.

## Labelled arithmetic module

Before label erasure, write the positive route as

\[
H(z)=\sum_{n\geq1}H_n(z).
\]

Let (M_{\mathrm{fin}}) be the finite-packet module with basis (e_n). Its
scalar label readout is

\[
\varepsilon(e_n)=1,
\qquad
\varepsilon\!\left(\sum_na_ne_n\right)=\sum_na_n.
\]

This is the augmentation of the multiplicative monoid of positive integers.
For finite packets its cancellation submodule is

\[
I_{\mathrm{aug}}=\ker\varepsilon.
\]

The completed scalar zero condition says that the combined two-route labelled
state lands in the corresponding augmentation kernel, provided the
augmentation extends to the chosen completion.

## Prime transport preserves cancellation

Multiplication by a prime acts labelwise as

\[
T_p e_n=e_{pn}.
\]

Since every basis label has augmentation one,

\[
\varepsilon T_p=arepsilon.
\]

Consequently

\[
T_p(I_{\mathrm{aug}})\subseteq I_{\mathrm{aug}}.
\]

The same holds for every prime power and every element of the constructor
monoid.

This proves that arithmetic transport closure cannot by itself push a
cancelling state out of the scalar zero ideal. It moves cancellation packets
within that ideal.

## Two-label falsifier

For any labels (m,n), the nonzero packet

\[
v=e_m-e_n
\]

satisfies

\[
\varepsilon(v)=0.
\]

For every prime (p),

\[
T_pv=e_{pm}-e_{pn},
\qquad
\varepsilon(T_pv)=0.
\]

This two-label packet is the smallest finite falsifier for any claim that prime
transport plus the trivial readout excludes destructive aggregation.

## The first transverse arithmetic current

Define logarithmic scale degree on finite packets by

\[
Le_n=(\log n)e_n.
\]

Then

\[
[L,T_p]=(\log p)T_p.
\]

Unlike the augmentation itself, the derived readout

\[
\varepsilon L\!\left(\sum_na_ne_n\right)
=\sum_n(\log n)a_n
\]

need not vanish on (I_{\mathrm{aug}}). For the two-label packet,

\[
\varepsilon L(e_m-e_n)=\log(m/n).
\]

Thus logarithmic scale degree is the first elementary constructor that detects
motion transverse to scalar cancellation while retaining arithmetic labels.
It is the discrete counterpart of the Euler-dilation commutator in the
continuous source coordinate.

Detection is not orientation. The sign or phase of this derived current is not
fixed by the commutator relation alone.

## Completion gate

On an infinite coefficient completion, the all-ones augmentation covector may
be unbounded or undefined. The correct domain must therefore prove all of the
following:

1. finite arithmetic packets form a core;
2. the augmentation extends as the actual completed theta readout;
3. prime transports extend and preserve its kernel;
4. the logarithmic derivation has a closed graph on the same source-generated
   domain;
5. its boundary current agrees with the continuous Euler-dilation defect.

If augmentation does not extend continuously, scalar completion is itself a
typed boundary operation and its anomaly must be retained rather than replaced
by an unrestricted sum.

## Revised RH gate

The labelled problem has now separated into an exact sequence of roles:

- augmentation constructs the scalar readout;
- prime transport preserves the cancellation ideal;
- logarithmic derivation detects transverse cancellation flow;
- modular completion must orient or constrain that flow.

A genuine advance must supply a source-derived sign, phase, or conservation
law for the logarithmic mismatch current. Repeating prime transport or adding
more labels cannot do so, because the entire transport monoid stabilizes the
augmentation ideal.
