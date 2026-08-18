---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 747 — The Literal Physical Chain Misses Every Principal Incidence Support

## Source-derived physical chamber

In the normalized chart used by the Gysin connection,

\[
X_1=1,\qquad E_T=u,\qquad X_2=y=\frac{u+v}{2}-1,
\qquad X_3=z=\frac{u-v}{2}=u-y-1.
\]

The closure of the literal positive-energy Bunch--Davies base chamber obeys

\[
u\ge0,\qquad y\ge0,\qquad z\ge0.
\]

The fiber chain is the positive Cayley--Menger twisted cycle with its
source orientation. It is covariant as a Borel--Moore/relative chain and
pairs contravariantly with the de Rham coefficient complex.

## Divisor support audit

The three resonant divisors are

\[
D_1=(z=0),\qquad D_2=(y-u^2=0),\qquad D_3=(y+u^2=0).
\]

The soft divisor \(D_1\) meets the physical base closure. By contrast, on
\(D_2\),

\[
z=u-u^2-1=-(u^2-u+1)<0
\]

for real \(u\), and \(D_3\) can satisfy \(y\ge0\) only at
\(u=y=0\), where \(z=-1\). Thus \(D_2\) and \(D_3\) are disjoint
from the physical closure.

## Incidence supports

The resolved points are

\[
Z_{12}:u^2-u+1=0,
\]

which has no real points;

\[
Z_{13}:u^2+u-1=0,\quad z=0,\quad y=u-1,
\]

whose two real points both violate \(u\ge0,y\ge0\); and

\[
Z_{23}:(u,y,z)=(0,0,-1).
\]

Therefore

\[
\boxed{
\overline B_{m phys}\cap
(Z_{12}\cup Z_{13}\cup Z_{23})=\varnothing.
}
\]

## Supported comparison

For the literal, uncontinued chain, all restriction/boundary maps to the
three point supports vanish by disjointness. The maps to \(D_2,D_3\)
vanish for the same reason. A map to \(D_1\) would require the soft
nearby-cycle specialization of the family; it is not an ordinary boundary
of a fixed fiber chain.

Entries 736 and 740 independently give zero principal corner maps from
\(D_1\) to both \(Z_{12}\) and \(Z_{13}\). Hence even an unresolved
soft component on \(D_1\) cannot hit the rational grade-zero line through
the already derived principal corner differential.

With the orientations of Entry 734, the literal point-supported map is the
zero chain map. Its chain-map commutator is zero, its induced map on the
Entry 740 hypercohomology line is zero, and the point-supported part of its
comparison cone retains

\[
Z_{12}\sqcup Z_{13}\sqcup Z_{23}.
\]

Only \(Z_{23}\) lies on \(\mathcal Q=0\).

## Deliberate limit

This is not a vanishing theorem for analytically continued Bunch--Davies
transport. The primary paper fixes the positive Cayley--Menger chain and
the generic twisted-period prescription, but it does not export:

- a chain family lifted to the weighted \((u,y)\) resolution;
- its exceptional boundary current;
- its \(\mu_2\) trace and overlap homotopy;
- a specialization map to the principal coefficient complex.

Consequently the full
\(\Phi_{\rm phys}:\mathcal C_{\rm phys}\to\mathcal K_{\rm pr}\)
remains undefined at the soft/infinity nearby-cycle level. Assigning a
nonzero \(Z_{23}\) component would fit the desired quartic answer.

## Narrow conclusion

\[
\boxed{
\text{the literal physical chain does not activate the principal Čech line;}
\quad
\text{only a separately derived soft/infinity continuation could do so.}
}
\]

## Evidence

- primary integration-domain definitions in arXiv:2408.16386,
  Section 2 and Appendix A;
- Entries 180, 717, 736, 740, 744--746;
- machine-readable packet
  'research/benincasa/marici-gm/physical-principal-cech-support.packet';
- Symbolica certificate
  'research/benincasa/marici-gm/src/bin/physical_principal_cech_support.rs';
- allocator claim 'seqclaim-c2d63604d36ba99ff678d7f0'.
- epistemic event
  'ev-000000000361-8cb76ef6-7cfa-4caa-842b-66ad4675ad64'.

## Next falsifier

Construct the analytically continued chain in the weighted charts from an
independently frozen boundary-value path. If no primary source fixes the
simultaneous \(E_T=X_2=0\) approach and weighted lift, record that exact
missing datum rather than selecting a \(Z_{23}\) boundary by hand.
