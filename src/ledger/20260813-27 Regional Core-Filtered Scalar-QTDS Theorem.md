# Regional Core-Filtered Scalar--QTDS Theorem

## Record

Date: 2026-08-13

Status: the contact theorem of entry 26 extends to every partial physical core at all even
multiplicity. After fixing the set of propagators that remain uncancelled, the scalar associated
grade and the complete QTDS period have the same occurrence-resolved Laurent polynomial. Both
sides factor canonically over the even polygonal regions cut out by that core, and the direct
Catalan bijection tensors over those regions.

This closes the complete coefficient-level transfer. It does not yet give one cellular or
twisted-chain map compatible with incidence between different cores. That assembly problem, and
the subsequent filtered Pochhammer/Cousin comparison, are the remaining Nima frontier.

Forward status: entries 28--75 construct the complete scalar incidence
envelope, close every transverse mixed square, and reduce the first
nontransverse eight-point comparison to one normalized torsion-free derived
route class. The remaining local datum is its occurrence-decorated extension
from the physical four-facet belt across the two source caps and source cube.

## Setup

Let \(n=2m\geq 4\), with the vertices of the cyclic polygon colored alternately. A diagonal is

- **scalar** when its endpoints have the same color;
- **physical** when its endpoints have opposite colors.

For a scalar triangulation \(T\), write

\[
P(T)=\{e\in T:e\text{ is physical}\}
\]

for its physical core. A partial physical core \(P\) is any noncrossing collection of physical
diagonals that extends to a quadrangulation. Put

\[
p=|P|,
\qquad
r=p+1.
\]

Cutting the polygon along \(P\) produces \(r\) even polygonal regions

\[
\mathcal R(P)=\{R_1,\ldots,R_r\}.
\]

If \(|R_i|=2m_i\), then the elementary polygon count gives

\[
\sum_{i=1}^{r}|R_i|=2m+2p
\]

and therefore

\[
\sum_{i=1}^{r}(m_i-2)
=m-p-2.
\]

The right-hand side is the number of propagators that must be cancelled in a full
quadrangulation containing \(P\).

## Exact-core scalar cells factor over regions

A scalar triangulation has exact physical core \(P\) if and only if it is obtained by choosing,
independently in every region \(R_i\), a zero-core scalar triangulation \(T_i\). Thus

\[
\{T:P(T)=P\}
\simeq
\prod_{R\in\mathcal R(P)} Z_R,
\]

where \(Z_R\) is the zero-core set of the even polygon \(R\).

The propagators belonging to \(P\) are unshifted. Every other propagator is shifted in the
alternating scalar normal direction. A triangulation with \(p\) physical diagonals contains

\[
2m-3-p
\]

shifted scalar diagonals. Its lowest power of the normal parameter is therefore
\(t^{2m-3-p}\). Reaching the distinguished associated grade \(t^{2m-2}\) requires

\[
(2m-2)-(2m-3-p)=p+1=r
\]

excess powers.

## Regional leading cancellation

For one even region \(R\), the zero-core scalar series has two parity sheets. Its lowest
coefficient cancels between the sheets: every zero-core cell has an odd number of scalar
diagonals, the two sheets carry opposite products of shift signs, and the two Catalan sets have
the same cardinality.

Consequently every region must contribute at least one excess power. There are exactly \(r\)
regions and exactly \(r\) available excess powers, so the global associated grade is forced to
take precisely the first nonzero coefficient from every region.

Entry 26 computed that first regional coefficient. Define the marked contact polynomial

\[
C_R
=
-\sum_{T\in Z_R}\ \sum_{d\in T}X_d.
\]

Then the scalar grade at exact core \(P\) is

\[
\boxed{
\left[\operatorname{gr}_{R}A_{\rm scalar}\right]_P
=
\frac{1}{\prod_{e\in P}X_e}
\prod_{R\in\mathcal R(P)}C_R.
}
\]

Equivalently, before collecting repeated monomials it is

\[
\frac{(-1)^r}{\prod_{e\in P}X_e}
\sum_{(T_R,d_R)_{R\in\mathcal R(P)}}
\prod_{R\in\mathcal R(P)}X_{d_R}.
\]

This is an occurrence-level factorization, not merely a polynomial identity after collecting
equal diagonal labels.

## QTDS with a retained core

Let \(Q\supseteq P\) be a full quadrangulation and let \(\Gamma_Q\) be its dual tree, directed by
one of the two alternating coorientations. To extract the Laurent sector whose remaining
denominator support is exactly \(P\):

1. retain the propagators \(X_e^{-1}\) for \(e\in P\);
2. cancel every propagator belonging to \(Q\setminus P\) against a linear QTDS vertex
   numerator;
3. select no numerator term proportional to an edge of \(P\).

Delete from \(\Gamma_Q\) the dual edges labelled by \(P\). The resulting forest has

\[
r=p+1
\]

components. Within each component, the vertex-local identity of entry 26 says that an internal
propagator can be cancelled only at the source of its directed edge.

A component with \(v\) vertices has \(v-1\) propagators to cancel. Since every QTDS vertex
numerator is linear, those cancellations can be chosen at distinct vertices if and only if the
component has a unique sink. When it does:

- each non-sink vertex cancels its unique outgoing propagator;
- the sink vertex remains and contributes either of its two scalar diagonals.

Write these two diagonals as \(d_C^0,d_C^1\) for a component \(C\). The exact contribution of
the diagram \(Q\) at retained core \(P\) is therefore

\[
\boxed{
\left[A_{Q}^{\epsilon}\right]_{\operatorname{den}=P}
=
\frac{(-1)^{p+1}}{\prod_{e\in P}X_e}
\prod_{C\in\pi_0(\Gamma_Q\setminus P)}
\left(X_{d_C^0}+X_{d_C^1}\right)
}
\]

when every component has a unique sink, and it is zero otherwise.

The sign follows directly. There are

\[
(m-2)-p
\]

cancelled propagators, each contributing a minus sign, while the diagram convention contributes
\((-1)^{m-1}\). Their product is

\[
(-1)^{m-1+m-2-p}
=(-1)^{p+1}
=(-1)^r.
\]

## Regional Catalan product bijection

Fix \(P\) and a polarity \(\epsilon\). In every region \(R\), entry 26 gives the direct marked
Catalan bijection

\[
\Phi_{\epsilon|R}:
(T_R,d_R)
\longleftrightarrow
(Q_R,d_R)_{\rm sink}.
\]

The restriction \(\epsilon|R\) is again an alternating coorientation because every region has
even size and every cut edge joins opposite colors.

Take the Cartesian product over all regions:

\[
\Phi_{\epsilon,P}
=
\prod_{R\in\mathcal R(P)}\Phi_{\epsilon|R}.
\]

On the source side this chooses one marked zero-core scalar triangulation in every region. On the
target side the regional quadrangulations join with \(P\) to form a unique full
quadrangulation \(Q\supseteq P\); after deleting \(P\), every component has a unique sink, with
the prescribed marked scalar slot. The inverse is obtained simply by restricting \(Q\) to its
regions and applying the regional inverse of entry 26.

Hence

\[
\boxed{
\prod_{R\in\mathcal R(P)}
\{(T_R,d_R)\}
\simeq
\left\{
(Q,(d_C)):
Q\supseteq P,
\ \Gamma_Q\setminus P
\text{ has one sink per component}
\right\}.
}
\]

The bijection preserves every marked diagonal, every remaining propagator, and the common sign
\((-1)^{p+1}\). It therefore identifies scalar and QTDS terms occurrence by occurrence.

## Core-filtered theorem

Summing the preceding diagram formula over all \(Q\supseteq P\), and using the regional Catalan
product bijection, gives for every partial physical core and either polarity

\[
\boxed{
\left[\operatorname{gr}_{R}A_{\rm scalar}\right]_P
=
\left[A_{\rm QTDS}^{\epsilon}\right]_{\operatorname{den}=P}.
}
\]

Summing over all partial cores gives the complete cyclic period identity

\[
\boxed{
\operatorname{gr}_{R}A_{\rm scalar}
=
A_{\rm QTDS}^{\epsilon}.
}
\]

This statement is stronger than the earlier reconstruction of the same amplitude from an
ordering basis. It identifies:

1. exact denominator support;
2. full quadrangulation carrier;
3. one marked scalar numerator in every cut region;
4. coefficient and sign;
5. factorization into regional occurrences.

The two QTDS polarities give the same complete period because both are identified with the same
scalar grade. Their presentations remain distinct lifts exchanged by one-step rotation.

## Cut monoidality at fixed core

The theorem supplies a precise coefficient-level form of factorization naturality. Cutting on
all edges of \(P\) gives

\[
\left[\operatorname{gr}_{R}A_{\rm scalar}\right]_P
=
\frac{1}{\prod_{e\in P}X_e}
\bigotimes_{R\in\mathcal R(P)} C_R,
\]

and the QTDS directed forest gives the identical tensor product. Thus the scalar transfer is
monoidal on every fixed cut stratum.

No inverse of a singular full-amplitude pairing is used here. The statement lives directly on
the Laurent/associated-grade stratum and is therefore compatible with the nearby-cycle warning
of entry 13: one works on the induced channel sector rather than trying to invert the residue of
the global BAS matrix.

## What the theorem does not yet assemble

For every fixed \(P\), the regional transfer \(\Phi_{\epsilon,P}\) is canonical. It does not
automatically follow that these maps commute with the boundary maps relating different cores.
If a new physical edge \(e\) is added, one region splits into two and the required comparison is
schematically

\[
\Phi_{\epsilon,P}
\quad\stackrel{?}{\longrightarrow}\quad
\Phi_{\epsilon,P\cup\{e\}}
=
\Phi_{\epsilon,R_L}\otimes\Phi_{\epsilon,R_R}.
\]

The coefficient theorem proves equality after applying the augmentation that remembers Laurent
monomials. It does not yet provide the higher chain witnessing compatibility before that
augmentation.

Accordingly, none of the following is claimed here:

1. a single cellular chain map on the full scalar presentation complex;
2. compatibility with every core-incidence differential;
3. a filtered map to loaded Pochhammer or logarithmic Cousin chains;
4. equality of scalar and \((\operatorname{Pf}'A)^2\) representatives before cohomology;
5. a canonical twisted-form representative at resonant boundary kinematics.

The known genus-zero inverse-pairing argument still identifies the induced cohomology class with

\[
[(\operatorname{Pf}'A)^2]
\]

at generic kinematics. The result of this entry supplies the missing all-core factorization
naturality of its scalar-derived period presentation, not the final worldsheet chain comparison.

## Exact finite certificate

An independent standard-library audit computes the same core-filtered Laurent polynomial in four
ways:

1. the raw scalar \(t^{n-2}\) associated-grade coefficient, grouped by exact physical core;
2. the product of regional zero-core marked-contact polynomials;
3. the raw symbolic QTDS numerator expansion, grouped by remaining denominator support;
4. the componentwise unique-sink formula.

The exact results are:

| \(n\) | partial physical cores | collected Laurent monomials |
|---:|---:|---:|
| 4 | 1 | 2 |
| 6 | 4 | 18 |
| 8 | 21 | 204 |
| 10 | 126 | 2,640 |
| 12 | 818 | 36,942 |

Both polarities agree in all four constructions. These computations are regression certificates;
the all-arity theorem follows from regional leading cancellation, the vertex-local QTDS identity,
and the product Catalan bijection.

## Reproducible audit

Run:

    python research/nima/check_core_filtered_transfer.py

The script uses exact rational coefficients and formal planar variables. It does not substitute
random kinematics or infer equality numerically.

The supporting all-arity local certificates remain:

    python research/nima/check_scalar_catalan_map.py
    python research/nima/check_scalar_sink_qtds.py
    python research/nima/check_qtds_vertex_cancellation.py

## What is now established

1. exact-core scalar cells factor as zero-core cells over even cut regions;
2. regional leading cancellation forces one marked scalar contact in every region;
3. the complete scalar associated grade has a closed formula at every partial core;
4. the QTDS retained-core sector is governed by one sink in every forest component;
5. the QTDS sign is \((-1)^{|P|+1}\);
6. the direct Catalan map tensors over regions and is explicitly invertible;
7. scalar and QTDS presentations agree occurrence by occurrence at every partial core;
8. fixed-core factorization/cut monoidality holds at all even multiplicity;
9. summing the core filtration recovers the complete QTDS period for either polarity.

## Primary next test

Build the incidence complex whose objects are partial physical cores and whose local coefficient
objects are the regional marked Catalan complexes. Then solve the first nontrivial compatibility
square for

\[
P\subset P\cup\{e,f\}
\]

in the two possible orders. The required datum is a deck-equivariant higher homotopy between the
two tensor-factorization routes, with the already proved regional maps fixed on every stratum.

At eight points this must recover the zero octagonal contact curvature of entry 24. At ten and
twelve points it gives the first test not implied by coefficient equality. Only after this
incidence assembly succeeds should the construction be transported to the filtered
Pochhammer/Cousin complex.

## Decision

Promote:

> The complete core-filtered associated grade of the scalar master is canonically identical, at
> occurrence and coefficient level, to the complete QTDS period. The transfer is the regional
> tensor product of the marked Catalan bijection, and its factorization law is the one-sink rule
> on every component of the directed dual forest.

The primary Nima frontier is no longer construction of the scalar-derived QTDS coefficients. It
is the assembly of these canonical regional transfers into one core-incidence chain map, followed
by the filtered scalar-to-worldsheet comparison.
