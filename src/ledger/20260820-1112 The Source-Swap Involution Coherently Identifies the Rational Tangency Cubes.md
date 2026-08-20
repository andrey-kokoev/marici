# 1112 — The Source-Swap Involution Coherently Identifies the Rational Tangency Cubes

## Correction

Entry 1111 called the center \((u,v)=(-1,0)\) a cyclic partner of
\((2/3,0)\). That terminology was too strong.

The frozen tangency packet labels the centers by

\[
(r,s)=\left(\frac32,-1\right),
\qquad
(r,s)=\left(-1,\frac32\right).
\]

They are related by the involution

\[
\boxed{r\leftrightarrow s,}
\]

not by a \(C_3\) generator. Entry 1111's local calculation remains valid; only
its symmetry typing is corrected.

## Source-derived involution

From

\[
u=\frac1r,
\qquad
v=\frac{2r+2s-1}{r},
\]

the label swap gives, with \(d=u+v-2\),

\[
\boxed{
u'=\frac{2u}{d},
\qquad
v'=\frac{2v}{d}.
}
\]

In the \(q_{\mathcal G_{12}}\)-residue chart,

\[
a=y_{23},
\qquad
b=y_{31}.
\]

Exchanging source sites \(1\leftrightarrow2\) swaps these two loop edges and
renormalizes by the old second site energy. Therefore

\[
\boxed{
a'=\frac{2b}{d},
\qquad
b'=\frac{2a}{d}.
}
\]

Applying the transformation twice returns \((u,v,a,b)\), since
\(d'=4/d\).

## Linearized normal transport

At

\[
(u,v,a,b)=\left(\frac23,0,0,-\frac13\right),
\]

use source normals \((p,q,A,B)\) from Entry 1109 and target normals
\((p',q',A',B')\) from Entry 1111. The exact linearization is

\[
\begin{pmatrix}
p'\\q'\\A'\\B'
\end{pmatrix}
=
\frac18
\begin{pmatrix}
-18&-6&0&0\\
0&-12&0&0\\
3&3&0&-12\\
0&0&-12&0
\end{pmatrix}
\begin{pmatrix}
p\\q\\A\\B
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{-\frac{243}{32}.}
\]

For the doubled-conductor and smoothing factors,

\[
T'=-3T,
\qquad
q'=-\frac32q,
\]

and

\[
V_-=-\frac34U_-,
\qquad
V_+=-\frac34U_+.
\]

Thus the involution preserves both coefficient-branch labels and carries the
existing \(L_1\) occurrence to the existing \(L_2\) occurrence.

## Orientation and deck audit

On the ordered support factors

\[
(\rho,q,U_-,U_+),
\]

the transition units are

\[
\left(1,-\frac32,-\frac34,-\frac34\right).
\]

Their product has sign \(-1\), so the ordered support cube reverses
orientation.

The Cayley--Menger polynomial is homogeneous of degree six. With
\(y=d/2\), the source swap therefore gives

\[
w'=\frac{w}{y^3}=\frac{8w}{d^3}.
\]

At fixed base kinematics,

\[
\det\frac{\partial(a',b')}{\partial(a,b)}
=
-\frac{4}{d^2}.
\]

Consequently

\[
\frac{da'\wedge db'}{w'}
=
-\frac d2\frac{da\wedge db}{w}.
\]

At the present center \(d=-4/3\), the relative fiber-residue unit is
\(+2/3\), so it preserves orientation. However, the source involution
exchanges the ordered endpoints of the \(G_{12}\) occurrence. Its
Poincaré-residue orientation contributes an additional sign \(-1\).
The total residue orientation is therefore \(-1\), while the deck character
is \(+1\). Hence

\[
\boxed{
\text{support orientation}=-1
=
\text{ordered-cut sign}\times\text{relative-fiber sign},
\qquad
\chi_{\rm deck}=+1.
}
\]

There is no coherence-sign defect.

## Narrow conclusion

Entries 1110 and 1111 are not merely separately exact. Their occurrence-
resolved support cubes are coherently identified by the actual source-label
involution:

\[
\boxed{
L_1\longleftrightarrow L_2,
\qquad
U_\pm\longleftrightarrow V_\pm,
\qquad
\text{orientation signs match}.
}
\]

No new carrier datum or transition homotopy is required at this grade.

This remains a local algebraic/residue comparison. It does not construct a
physical relative chain.

## Verification

Checker:

research/benincasa/marici-gm/src/bin/rank12_rational_tangency_source_swap.rs.

Packet:

research/benincasa/rank12-rational-tangency-source-swap.json.

Ledger claim: seqclaim-229e79adf73e65aebb46baad.

Epistemic event:

ev-000000000811-e55ecd37-aa31-4971-8172-07f47e5d0768.

## Next finite falsifier

Return to the remaining exceptional-center atlas and identify the first center
whose local normalization has not yet been reduced to an exact labelled
simplex or normal-crossing cube. Preserve source involutions separately from
the \(C_3\) occurrence action.
