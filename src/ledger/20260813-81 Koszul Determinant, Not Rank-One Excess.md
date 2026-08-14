# Koszul Determinant, Not Rank-One Excess

## Record

Date: 2026-08-13

Status: exact typing falsification and replacement theorem.  The conjecture
recorded in entries 78 and 80 that an eight-point overlap bridge should be a
rank-one \(\operatorname{Tor}_1\) excess-conormal class is false for every
scalar base and incidence square currently defined in the ledger.  After the
fixed outer monomial is inverted, the bridge is instead:

1. the unique first syzygy of the two-generated overlap ideal;
2. equivalently, the top determinant generator of its rank-two Koszul
   resolution;
3. at finite loading, a two-endpoint monodromy relation, not a single
   excess-normal factor.

The universal monodromy base-change theorem and the double-loading warning of
entry 80 remain valid.  What is withdrawn is their proposed geometric
completion by a rank-one excess line.

## Epistemic correction

The Marici epistemic graph contains two deliberately conjectural ancestors:

    ev-000000000017-5518d0c0-db1f-40be-9edb-59b546ad49ab
    ev-000000000018-f8b85833-5ac5-406a-bce5-7e6245b5f811

The first proposed that the four bridges are rank-one excess-intersection
classes.  The second separated the proved formal monodromy algebra from an
unproved loaded excess-line realization.  Admission certified the validity of
those graph records, not their truth.

This entry supplies the requested falsification test.  The correction is
append-only: retain the two earlier conjectures, attach the present negative
assessment, and replace their frontier by a loaded endpoint-determinant kernel.

Epistemic-graph correction event:

    ev-000000000019-9621a241-2d01-41ad-ac62-531728a19d74

The atomic review admitted 22 operations and explicitly records
`certifies_truth: false`.  It adds the two proved typing claims, falsifying
assessments on both excess-line conjectures, outcomes for their original
tests, and the loaded endpoint-determinant successor.

## Local overlap algebra

Let

\[
A=\mathbf Z[x,y,\ldots]
\]

be the scalar coefficient ring after localizing the fixed outer monomial
\(C_e\).  The support-adjacent overlap of entry 79 is

\[
\mathfrak p=(x,y),
\qquad
x=X_{10},\quad y=X_{11}.
\]

Choose endpoint generators \(e_0,e_1\) so that

\[
d_1(e_0)=y,
\qquad
d_1(e_1)=x.
\]

Then the minimally resolved ideal has the exact sequence

\[
\boxed{
0\longrightarrow Ah
\xrightarrow{\ d_2\ }
Ae_0\oplus Ae_1
\xrightarrow{\ d_1\ }
\mathfrak p
\longrightarrow0,
}
\]

where

\[
\boxed{
d_2h=-x e_0+y e_1.
}
\]

Indeed, if \(ya+xb=0\), reduction modulo \(x\) gives \(x\mid a\), and
coprimality then gives \((a,b)=c(-x,y)\).  Thus the bridge is the unique
primitive first syzygy of the ideal.  This is exactly the weighted middle
interval already present in the regional scalar cube.

The word "rank one" is correct only for this syzygy module.  It does not type
the bridge as \(\operatorname{Tor}_1\) of a rank-one excess intersection.

## The quotient Koszul complex fixes the Tor degree

Put

\[
S=A/\mathfrak p.
\]

The full Koszul resolution of \(S\) is

\[
0\longrightarrow
A(e_0\wedge e_1)
\xrightarrow{\ d_2\ }
Ae_0\oplus Ae_1
\xrightarrow{\ d_1\ }
A
\longrightarrow S\longrightarrow0.
\]

Tensoring with \(S\) kills both differentials.  Consequently

\[
\operatorname{Tor}_i^A(S,S)
\cong
\bigwedge^i_S(\mathfrak p/\mathfrak p^2),
\]

with ranks

\[
\boxed{
(\operatorname{rank}\operatorname{Tor}_0,
  \operatorname{rank}\operatorname{Tor}_1,
  \operatorname{rank}\operatorname{Tor}_2)
=(1,2,1).
}
\]

Therefore

\[
\operatorname{Tor}_1^A(S,S)
=\mathfrak p/\mathfrak p^2
\]

is rank two.  The rank-one class is

\[
\boxed{
\operatorname{Tor}_2^A(S,S)
=
\det(\mathfrak p/\mathfrak p^2),
}
\]

and the bridge generator \(h=e_0\wedge e_1\) is its ordered determinant.
Changing the endpoint order reverses its sign.  This is exactly the ordered
normal/Koszul antisymmetry already seen by the certificates.

## The documented scalar normal direction has zero excess

Entries 20--21 define only one scalar normal parameter: the shift coordinate
\(t\) in

\[
F_{\alpha,+}(X,t)=A_\alpha(X+\sigma/t).
\]

They do not define a second rank-jump parameter space, a kinetic bundle, or a
multi-normal derived intersection.  The minimal algebraic base containing all
currently documented directions is therefore

\[
B=A[t].
\]

Compare the scalar shift divisor \(R=(t)\) with the regional incidence ideal
\(Q=(x,y)\).  Resolving \(B/(t)\) gives

\[
0\longrightarrow B
\xrightarrow{\ t\ }
B\longrightarrow B/(t)\longrightarrow0.
\]

After tensoring with \(B/Q\), multiplication by \(t\) remains injective.
Hence

\[
\boxed{
\operatorname{Tor}^{B}_{i>0}(B/(t),B/(x,y))=0.
}
\]

The sequence \((t,x,y)\) is regular, the codimensions add, and the excess rank
is zero.  Thus the only scalar specialization square actually present in the
ledger cannot produce the proposed excess line.

Any different derived square might have nonzero excess, but it would be new
geometric data.  Its strata, maps, and cotangent complex must be defined and
computed before the word "excess" has content.

## Correct finite-monodromy typing

Let

\[
u_x=q_x-1,
\qquad
u_y=q_y-1.
\]

The formal finite-loaded endpoint relation is

\[
\boxed{
d h=(q_y-1)e_1-(q_x-1)e_0.
}
\]

This is one interval differential with two endpoint monodromies.  Algebraically
it is the top generator in the rank-two Koszul complex
\(K(u_y,u_x)\).  It is not one copy of \(q-1\), and it is not the Thom class of
a rank-one excess bundle supplied by the documented scalar geometry.

After both \(u_x\) and \(u_y\) are inverted, this Koszul complex is
contractible and the support ideal becomes the unit ideal.  The meaningful
object must therefore retain a filtered, nearby-cycle, relative-endpoint, or
support-poset typing.  Nonresonant localization alone forgets precisely the
endpoint support that distinguishes the bridge.

Entry 80's formal substitution

\[
X_{ra}\longmapsto q_{ra}-1
\]

is still an exact algebraic base change.  Its physical limitation is also
unchanged: the facewise construction of entry 38 keeps the scalar
\(X\)-coefficient resolution separate from the Pochhammer normal complex.
Replacing the former and then tensoring the latter double loads the same
boundary data.

## Replacement architecture: a derived correspondence kernel

The established object is the saturated relation complex

\[
\mathcal K_Q
=
\ker\!\left(
\mathcal R_Q\longrightarrow B_Q^{\rm w}
\right),
\]

containing the two internal pentagon cones and the four determinant intervals.
It is better typed as a bivariant correspondence between self-factorizing
scalar carriers than as the normal bundle of an amplitude stratum.

If \(C_{\rm route}\) denotes the support-filtered route category, the expected
comparison should have the form of a derived integral transform

\[
\boxed{
\Phi_{\mathcal K_Q}(M)
=
\int^{c\in C_{\rm route}}
\mathcal K_Q(-,c)
\overset{\mathbb L}{\otimes}M(c).
}
\]

The scalar coefficient resolution belongs to \(\mathcal K_Q\).  Pochhammer
loading should be applied objectwise once to the physical normal factor.  The
missing theorem is that the resulting loaded kernel transform equals the
physical double-Gysin/Cut correspondence and obeys dependent-face descent.

This matches the larger trajectory of the session: the natural structure is
not a strict operator algebra on summed amplitudes but a homotopy-coherent
dictionary between self-factorizing carriers.

## Epistemic boundary

Established:

1. the overlap bridge is the unique first syzygy of \((x,y)\);
2. it is the top determinant generator of the rank-two Koszul resolution;
3. self-intersection Tor ranks are exactly \((1,2,1)\);
4. the rank-one self-intersection class lies in \(\operatorname{Tor}_2\), not
   \(\operatorname{Tor}_1\);
5. the documented \((t)\) versus \((x,y)\) scalar square is Tor-independent;
6. its positive Tor groups and excess rank vanish;
7. the finite formal relation uses two endpoint monodromies in one interval
   differential;
8. entry 80's formal base change and double-loading no-go survive this
   correction.

Not established:

1. a loaded Pochhammer/Cousin realization of the determinant interval;
2. a bivariant kernel map from the route relation complex to physical double
   Gysin sewing;
3. the five-term loaded pentagon identity including all lower-face terms;
4. trivial finite holonomy around the four-chart belt;
5. global octagon/Jordan coherence or identification with
   \((\operatorname{Pf}'A)^2\) at this chain level.

Reject:

> The established bridge is a rank-one \(\operatorname{Tor}_1\)
> excess-conormal class.

Also reject:

> The scalar \(t\)-shift and regional incidence square has a hidden excess
> line.

Also reject:

> The relation \(dh=(q_y-1)e_1-(q_x-1)e_0\) contains one and only one
> \(q-1\) factor.

It contains one determinant interval and two endpoint monodromy factors.

## Next formula objective

Construct a support-filtered loaded correspondence

\[
\boxed{
\mathcal K_Q^{\rm PC}:
\operatorname{PC}_{\alpha'}(\mathcal R_Q)
\dashrightarrow
\operatorname{PC}_{\alpha'}(B_Q)
}
\]

whose associated grade is \(\mathcal K_Q\), while keeping the scalar
\(X\)-resolution and the endpoint Pochhammer loading in their distinct tensor
factors.  On one representative route pentagon:

1. construct the complete two-endpoint interval with its lower-face terms;
2. retain both collapsed \(H_{s,+}\) and \(H_{s,-}\) cones;
3. prove the five-term loaded Cousin identity;
4. compare both ordered residues with the physical double-Gysin map;
5. compute the product of the four loaded transitions and test whether its
   holonomy is one.

Only after this representative passes should it be rotated through the eight
deck images and assembled around the residual octagon.

## Reproducible certificate

Run:

    rustfmt --check research/nima/check_bridge_tor_typing.rs
    rustc --edition=2021 -D warnings -O research/nima/check_bridge_tor_typing.rs -o "$env:TEMP\\marici-bridge-tor-typing.exe"
    & "$env:TEMP\\marici-bridge-tor-typing.exe"

Certificate SHA-256:

    f3500abeebad67d1d3ff467ccf712a7e3686d032cb8186fe03eaefcab1e5c6fb

## Decision

Falsify:

> The regional bridge is a rank-one \(\operatorname{Tor}_1\) excess class of
> the documented scalar specialization square.

Promote:

> The regional bridge is the primitive determinant relation of a rank-two
> endpoint Koszul complex.  Its physical completion, if it exists, is a
> loaded derived correspondence kernel rather than a presently defined
> excess-normal Thom factor.

## Internal dependencies

- Entries 20--21: the only documented scalar \(t\)-normal direction and the
  presentation-cell carrier.
- Entry 38: separation of scalar coefficients from normal Pochhammer loading.
- Entries 76--79: regional cube, occurrence ideal, carrier kernel, and
  resolved overlap intervals.
- Entry 80: universal monodromy base change and double-loading no-go.
- research/nima/check_bridge_tor_typing.rs.
