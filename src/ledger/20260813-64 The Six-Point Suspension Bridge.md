# The Six-Point Suspension Bridge

## Record

Date: 2026-08-13

Status: exact integral and equivariant carrier theorem. Its extension to the
physical scalar-first-jet coefficient complex and to a matched Cut remains
open.

The two canonical six-point scalar tripods of entry 21 form, after contracting
their subdivided legs, the marked-theta incidence graph

\[
\boxed{K_{2,3}=S^0*R_3,}
\]

where \(S^0=\{+,-\}\) is the polarity set and
\(R_3=\{D_0,D_1,D_2\}\) is the set of three physical channels. The QTDS
contact difference is a reduced zero-cycle on \(R_3\). Suspending it between
the two polarity cores produces canonically an integral Ward circuit in
\(H_1(K_{2,3})\).

This replaces the provisional statement that QTDS and Ward merely use the
same triangle Laplacian. Their low-point carrier modules are connected by the
Mayer--Vietoris boundary of an actual scalar presentation subcomplex.

## The scalar tripods

At six points let

\[
D_0=(0,3),\qquad D_1=(1,4),\qquad D_2=(2,5)
\]

be the three physical channels. Entry 21 constructs two parity-central scalar
cells \(E_+\) and \(E_-\), three channel-facet barycenters \(b_i\), and canonical
incidence paths

\[
\gamma_i^\varepsilon:E_\varepsilon\longrightarrow b_i.
\]

For each fixed polarity, the three paths form a contractible tripod

\[
U_\varepsilon=\operatorname{Cone}_{E_\varepsilon}(R_3).
\]

The two tripods share their three channel endpoints. Contracting each
subdivided path to one edge gives

\[
U_+\cup_{R_3}U_-
=
S^0*R_3
=
K_{2,3}.
\]

Thus the six incidence edges are not freely invented. They are the contracted
images of the six scalar paths \(\gamma_i^\varepsilon\).

## Mayer--Vietoris suspension

Both \(U_+\) and \(U_-\) are contractible and their intersection is the
discrete road set \(R_3\). The reduced Mayer--Vietoris sequence therefore gives
the connecting isomorphism

\[
\boxed{
\widetilde H_0(R_3;\mathbb Z)
\xrightarrow{\ \Sigma\ }
H_1(K_{2,3};\mathbb Z).}
\]

Orient every incidence edge from its polarity core to its road endpoint and
write it as \(e_{\varepsilon i}\). For

\[
c=(c_0,c_1,c_2),
\qquad
c_0+c_1+c_2=0,
\]

the suspension is the explicit cycle

\[
\boxed{
\Gamma(c)
=
\sum_{i=0}^{2}c_i
\bigl(e_{+i}-e_{-i}\bigr).}
\]

Indeed,

\[
\partial\Gamma(c)
=
\left(\sum_i c_i\right)(E_--E_+)
=0.
\]

The edge coefficients recover \(c\), so \(\Gamma\) is injective. Both sides
have rank two, and the image is saturated. Hence \(\Gamma\) is the integral
suspension isomorphism, not a rational comparison.

## The difference of scalar primitives is a Ward cycle

The six-point QTDS polarity difference supplies a contact vector

\[
c_i=\frac{N_i^+-N_i^-}{X_i},
\qquad
\sum_i c_i=0.
\]

On each scalar tripod, entry 21 constructs

\[
\eta_6^\varepsilon
=
\sum_i c_i\gamma_i^\varepsilon,
\qquad
\partial\eta_6^\varepsilon
=
\sum_i c_i b_i.
\]

The two scalar primitives have the same boundary. Their difference is
therefore closed, and after tripod contraction it is exactly the suspension
cycle:

\[
\boxed{
\eta_6^+-\eta_6^-
\longmapsto
\Gamma(c)
\in H_1(K_{2,3}).}
\]

This gives the first precise cross-sector interpretation:

> The marked-theta Ward harmonic class is the carrier-level transgression of
> the ambiguity between the two six-point scalar/QTDS polarity primitives.

This statement is about the integral carrier. It does not yet assert that the
full Yang--Mills first-jet coefficient attached to that Ward class is the QTDS
contact polynomial.

There is nevertheless an exact coefficient-module consequence.  In the six
independent boundary variables used by the symbolic scalar audit, the QTDS
contact map is

\[
C_{\rm QTDS}=
\begin{pmatrix}
1&1&0&-1&-1&0\\
0&-1&-1&0&1&1\\
-1&0&1&1&0&-1
\end{pmatrix},
\]

whose columns lie in \(A_2\).  Compose it with the suspension \(\Gamma\) and
the integral Ward bridge \(\Theta:H_1(K_{2,3})\to\ker t\) of entry 59.  In the
Ward quotient coordinates

\[
(l_{00},l_{01},l_{10},l_{11},q_0,q_1,q_2),
\]

the result is the integral matrix

\[
\boxed{
\Theta\Gamma C_{\rm QTDS}=
\begin{pmatrix}
0&-1&-1&0&1&1\\
-1&-1&0&1&1&0\\
0&1&1&0&-1&-1\\
1&1&0&-1&-1&0\\
-1&-1&0&1&1&0\\
0&1&1&0&-1&-1\\
1&0&-1&-1&0&1
\end{pmatrix}.}
\]

Every one of its six columns is killed by the exact Ward contact map, and the
matrix intertwines the order-six rotation and reflection actions.  Thus an
explicit coefficient-module homomorphism exists with no denominator or basis
ambiguity.  What remains unproved is that applying the scalar first normal jet
and its kinetic/BRST differential derives this matrix rather than merely
admitting it.

## Relation to the road triangle

Let \(C_3\) be the oriented road triangle and let \(t_i\) be its edge from road
\(i+1\) to road \(i\), so

\[
\partial t_i=e_i-e_{i+1}.
\]

Suspending this boundary gives the adjacent four-circuit

\[
\Gamma(\partial t_i)
=
e_{+i}-e_{-i}-e_{+,i+1}+e_{-,i+1}.
\]

Thus the three triangle tags map one by one to the three primitive populated
Ward circuits. Their diagonal relation

\[
t_0+t_1+t_2
\]

maps to zero. The road-polygon resolution and the suspension graph therefore
fit into the exact factorization

\[
C_1(C_3)
\xrightarrow{\ \partial\ }
\widetilde C_0(R_3)
\xrightarrow{\ \Gamma\ }
H_1(K_{2,3}).
\]

The inverse-Laplacian current of entries 19 and 62 is only a section of the
first arrow. The second arrow is integral and canonical.

## Full dihedral symmetry

Let \(r\) and \(s\) act on a polarity--road pair by

\[
r:(\varepsilon,i)\longmapsto(\varepsilon+1,i+1),
\]

\[
s:(\varepsilon,i)\longmapsto(\varepsilon,-i),
\]

with indices modulo two and three. They satisfy

\[
r^6=s^2=1,
\qquad
srs=r^{-1}.
\]

The generated twelve-element action is all of

\[
\operatorname{Aut}(K_{2,3})
=
S_2\times S_3
\cong D_6.
\]

Here road rotation/reflection is the \(D_3\) action, while exchanging the two
polarity cores is the additional \(S_2\). The suspension map is equivariant.
In particular, polarity exchange reverses \(\Gamma(c)\), exactly as core
exchange reverses the oriented Ward cycle.

This derives the previously assumed identification of the QTDS polarity
character and the Ward core-exchange character at the contracted carrier
level.

## Why the comparison is now normalized

Boundary and symmetry equations alone allow a two-parameter family of
endomorphisms of the abstract cellular resolution:

\[
F_0=aI,
\qquad
F_1=aI+bJ,
\qquad
F_2=a+3b,
\]

where \(J\) is the all-ones matrix. Hence those equations alone allow the zero
map and cannot fix normalization.

The scalar incidence carrier supplies the missing datum. Each primitive road
edge must map to its individually supported four-circuit. This forces

\[
a=1,
\qquad
b=0
\]

for the declared orientation. Reversing the global suspension orientation
reverses every class simultaneously. No other freedom remains at carrier
level.

## What has and has not closed

Proved exactly:

1. the contracted union of scalar polarity tripods is \(K_{2,3}\);
2. its Ward homology is the suspension of the reduced channel module;
3. the QTDS contact difference produces a canonical integral circuit;
4. adjacent road tags map to individual primitive four-circuits;
5. the map is equivariant under the full hexagon dihedral group;
6. individual support fixes the nonzero comparison and its normalization.
7. the full symbolic QTDS contact module maps integrally into the exact
   seven-coordinate Ward kernel and passes the dihedral covariance audit.

Still open:

1. derivation of the corresponding coefficient map inside the actual scalar
   first-jet Ward complex;
2. a chain-level comparison with the resolved Brauer/open-curve target;
3. a physical Cut shared by the two sides;
4. a higher-point or all-arity suspension theorem;
5. whether the transgression is part of modular completion or a distinct
   normal-sector operation.

The existing Cut data cannot simply be equated. QTDS \(c_i\) are contact
polynomials and have zero physical pole residue. The punctured-torus retained
circuit count is a topological edge Cut and is nonzero; it does not descend
through the oriented road relation without an annulus/open-curve target and an
image for the relation generator. These are different maps until a common
target is constructed.

## Revised trajectory

At low point, the interaction between the NLSM and YM normal sectors is not a
map between their final amplitudes. It is a transgression in a cover of the
scalar presentation carrier:

\[
\boxed{
\text{difference of local scalar primitives on }R_3
\xrightarrow{\ \delta_{\rm MV}\ }
\text{global Ward circuit on }U_+\cup_{R_3}U_-.}
\]

This suggests a new classification target:

> Search for derived theories not only among normal grades and jets, but among
> the Cech/Mayer--Vietoris obstruction classes of atlases of scalar-derived
> local dictionaries.

That is a strong extrapolation from one exact carrier. The first falsifier is
to repeat the construction on the next scalar polarity atlas and test whether
its transgressed homology maps to the corresponding first-jet Ward sector with
the correct physical Cut.

## Reproducible certificate

Run:

```text
rustc --edition=2021 -O research/nima/check_m3_hodge_comparison.rs -o "$env:TEMP\\marici-m3-hodge.exe"
& "$env:TEMP\\marici-m3-hodge.exe"
```

The certificate checks the integral suspension, primitive circuit supports,
full twelve-element automorphism action, cellular comparison classification,
the explicit symbolic coefficient-module map into the Ward kernel, and the
precise Cut-typing obstruction.

## Internal dependencies

- Entry 21: scalar parity tripods and their QTDS contact primitives.
- Entries 59--63: Ward homology, circuit resolution, Green section, and flow
  torsors.
- `research/nima/check_m3_hodge_comparison.rs`: exact certificate.
