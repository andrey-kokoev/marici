# Theta cross zeros are incidence-divisor crossings, not operator failures

## Bounded question

Does a labelled multiport or matrix characteristic lift make a theta
cross-transfer zero impossible?

## Full relation and scalar chart

Let \(V\) be the completed port space, let \(T(z)\) be an invertible
source-derived transfer, and fix a source vector \(v\) and endpoint covector
\(\ell\). The scalar readout is

\[
F(z)=\ell(T(z)v).
\]

Its vanishing means

\[
T(z)v\in\ker\ell.
\]

The full relation can remain invertible, unitary, and norm-preserving. Only the
chosen source-to-endpoint coordinate has vanished.

Projectively, the path

\[
z\longmapsto[T(z)v]
\]

has crossed the hyperplane defined by \(\ell\). In a flag-adapted matrix chart,
this is the vanishing of a selected matrix coefficient or generalized minor:
a Schubert-type incidence divisor bounding the corresponding open cell.

## Smallest unitary hostile

Take

\[
T(\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},
\qquad
v=e_1,
\qquad
\ell=e_1^*.
\]

Then

\[
\ell(T(\theta)v)=\cos\theta.
\]

At \(\theta=\pi/2\), the scalar readout vanishes, while

\[
\det T(\theta)=1
\]

and \(T(\theta)\) remains unitary. The missing scalar component has rotated
into the complementary port.

This hostile passes:

- invertibility;
- unitarity;
- positive norm conservation;
- complete two-port observability;
- exact Julia or characteristic colligation;
- orientation preservation.

Therefore none of those properties excludes a cross zero.

## Why adding ports is insufficient

Embed the hostile rotation as a direct summand of any larger unitary or
contractive colligation. Extra primitive, square, seam, archimedean, and
residue ports can remain perfectly faithful while the selected source-endpoint
coefficient still vanishes.

A matrix-valued characteristic function retains more information than its
scalar compression, but information retention is not a nonvanishing theorem.
The allowed matrix path must be restricted.

## The correct geometric target

Let

\[
\Omega_{\ell,v}
=
\{T\in GL(V):\ell(Tv)\ne0\}.
\]

This is the open incidence cell associated with the chosen source and endpoint
ports. The zero divisor is its complement.

The RH-bearing source theorem becomes:

> The completed theta/Tate transfer path remains in
> \(\Omega_{\ell,v}\) throughout each open reciprocal sector and may meet its
> incidence divisor only on the unitary sewing seam.

This formulation preserves the distinction between:

- the full two-sector relationship;
- the labelled scalar chart;
- the locus where that chart becomes undefined or zero.

## What could enforce cell confinement

Generic unitarity cannot. A successful source law would need additional
structure such as:

1. total positivity or sign regularity of generalized minors;
2. a source-derived Gauss factorization whose pivot factors never vanish;
3. monotone transport inside an acute semigroup;
4. a conserved oriented-matroid chamber;
5. a labelled boundary current whose sign changes exactly at the incidence
   divisor.

Each candidate must be derived before inspecting the theta scalar. Choosing
the open cell because it contains the desired path is circular.

## Relation to causal cyclicity

The Hardy model-space defect and the incidence crossing describe different
levels of the same event:

- \(F(z)=0\) is a pointwise source-endpoint orthogonality;
- an inner zero creates a persistent model-space direction;
- the full characteristic relation remains valid in both descriptions.

Thus a zero is not disappearance of the carrier object. It is a loss of
transversality in one labelled comparison, recorded globally as an invariant
subspace defect.

## Result

A pre-factorization multiport lift is necessary for faithfulness but
insufficient for RH. Cross zeros are permitted incidence-divisor crossings of
an otherwise invertible and unitary relation. The new hard-to-vary conjecture
is open-cell confinement of the theta/Tate transfer in both reciprocal
sectors, with the critical line as the only authorized chart-transition
locus.

## Sharp falsifier

Any proposed multiport positivity law must reject the \(90^\circ\) rotation
above through a source-derived invariant. If it accepts the rotation, or any
direct-sum embedding of it, then it cannot exclude theta cross zeros regardless
of how many faithful ports are retained.
