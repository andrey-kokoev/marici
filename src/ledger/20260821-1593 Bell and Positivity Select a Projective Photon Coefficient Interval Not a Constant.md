# 1593 — Bell and Positivity Select a Projective Photon Coefficient Interval, Not a Constant

Date: 2026-08-21

Sequence claim: `seqclaim-bf2b2736f57addc69c9b6af9`

## Result

Let \(r=f_2/g_2\).  Entry 1592 and the exact Born readout give

\[
I(x,r)=\frac{8\sqrt2,r(1-x+x^2)}
{1+4r^2(1-x+x^2)^2}.
\]

Eliminating \(x\in[0,1]\) proves that strict Bell violation at every angle is

\[
\frac23(\sqrt2-1)<|r|<\frac{\sqrt2+1}{2}.
\]

After intersecting the independent photon positivity condition
\(g_2>0, |f_2|\le g_2\), the exact locus is

\[
\boxed{
\frac23(\sqrt2-1)<|f_2/g_2|\le1.
}
\]

The weak lower inequality gives the closed Bell-saturation locus.

Bell is homogeneous of degree zero in \((g_2,f_2)\).  Its Jacobian has the
radial coefficient vector in its kernel, so Bell cannot determine the EFT
scale.  Signed data at two distinct angles determines \(r\) generically;
absolute Bell data determines only \(|r|\).

The benchmark audit separates four rays:

- one-loop QED \(|r|=3/11\) lies strictly below the all-angle boundary;
- the Bell-saturating lower boundary is
  \(\frac23(\sqrt2-1)\);
- the unique worst-angle maximin point is \(|r|=1/\sqrt3\);
- Born--Infeld has \(r=0\) and no Bell violation in this packet.

Therefore the present Marici+Bell result is an exact projective coefficient
interval, not a recovery of a fundamental constant.  Selecting a unique ray
would require an independently derived Carrier operation or another physical
readout; recovering the scale additionally requires an unnormalized observable
such as a cross section.

## Evidence

- `research/nima/check_photon_d8_bell_coefficient_locus.py`
- `research/nima/results/photon-d8-bell-coefficient-locus.json`
- `research/nima/photon-d8-bell-coefficient-locus.md`
- Entries 1578, 1586, and 1587 for the Born and support controls.
- epistemic-graph event:
  `ev-000000001773-efe15b68-eb1b-4c1f-8b0f-93913c3ac4d8`.
