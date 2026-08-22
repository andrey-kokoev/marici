# Photon Capacity-Preference Falsifier

## Question

Does an already source-derived physical weight favor alternatives with greater
connected future capacity?

The dimension-eight photon EFT supplies both quantities in one fixed theory.
Choose the admitted positivity-boundary ray

\[
f_2=g_2>0.
\]

For incoming \(++\) helicity and \(z=\cos^2\theta\), the exact source map is

\[
\Phi_1=16g_2,
\qquad
\Phi_2=8g_2(3+z),
\qquad
\Phi_5=0.
\]

Put

\[
y=\frac{\Phi_2}{\Phi_1}=\frac{3+z}{2}.
\]

After removing the common positive factor \(|\Phi_1|^2\), the differential
source weight per solid angle is

\[
R(z)=1+y^2.
\]

The pre-positive connected residue is \(\det M=\Phi_1\Phi_2\), and its
normalized positive support is

\[
C(z)=\det\rho_A=\frac{y^2}{(1+y^2)^2}.
\]

## Exact result

Throughout \(0\le z\le1\), one has \(y>1\), and therefore

\[
\frac{dR}{dz}>0,
\qquad
\frac{dC}{dz}<0.
\]

For the interior comparison \(z=0\) and \(z=1/4\),

\[
R(0)=\frac{13}{4}
<
\frac{233}{64}=R(1/4),
\]

while

\[
C(0)=\frac{36}{169}
>
\frac{10816}{54289}=C(1/4).
\]

Thus the more strongly weighted angular record has lower connected helicity
capacity.

## Disposition

\[
\boxed{
\text{ordinary source/Born weighting does not monotonically maximize
connected transport capacity.}
}
\]

This is a within-theory falsifier, not a comparison of independently chosen
EFTs.  It rejects the simplest implementation of the Operator's conjecture:
identifying the proposed developmental pressure with the already existing
differential source weight.

It does not exclude a more global constraint on histories, interactions, or
constructor networks.  Such a law would have to be additional to ordinary
local rate weighting and must explain why it does not contradict this angular
anti-correlation.  No such law is currently derived.

Certificate:
`research/nima/checkers/check_photon_capacity_preference_falsifier.py`
