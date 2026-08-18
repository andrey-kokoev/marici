---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 758 — The Gysin Extension Defect Is Occurrence-Covariant

## Frozen input

Use the Gysin-adapted connection

\[
\nabla=d+
\begin{pmatrix}
A_T&0\\
C&A_E
\end{pmatrix}
\]

serialized in
`research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`,
and the filtered splitting census of Entry 757.

The homogeneous base coordinates are

\[
X_1=1,\qquad
u=E_T,\qquad
X_2=\frac{u+v}{2}-1,\qquad
X_3=\frac{u-v}{2}.
\]

Under the occurrence reflection \(\sigma_{23}\),

\[
\boxed{
u'=u,qquad v'=2-v.
}
\]

## Transported adapted frame

Entry 756 constructs the labelled residue-chart map

\[
T_{12\to31}=-\sigma_{23}^*
\]

with the minus sign forced by Poincaré-residue orientation.

Define the target Gysin-adapted frame to be the labelled image of the source
frame. On its rank-four block the orientation factor is the constant gauge

\[
S=-I_4.
\]

Therefore

\[
SAS^{-1}=A.
\]

The residue sign is retained, but cancels in connection conjugation. The
nontrivial differential-form transformation is

\[
du=du',qquad dv=-dv'.
\]

Consequently the transported diagonal blocks are

\[
A^{31}_{T/E,u'}(u',v')
=
A^{12}_{T/E,u}(u',2-v'),
\]

\[
A^{31}_{T/E,v'}(u',v')
=
-A^{12}_{T/E,v}(u',2-v').
\]

The off-diagonal cocycle transforms by the same rule:

\[
\boxed{
\begin{aligned}
C^{31}_{u'}(u',v')
&=C^{12}_{u}(u',2-v'),\\
C^{31}_{v'}(u',v')
&=-C^{12}_{v}(u',2-v').
end{aligned}
}
\]

Thus, for \(X:T\to E\),

\[
\nabla^{31}_{\operatorname{Hom}}X
=
dX+A_E^{31}X-XA_T^{31}
\]

is the exact pullback of the \(G_{12}\) Hom differential, not an
independently fitted target operator.

## Covariance census

The Entry 757 ansatz was transported as a whole:

\[
X=\frac{N(u',v')}{D_{31}^{m}},
\qquad
m=0,1,2,qquad
\deg N\le10,
\]

where

\[
D_{31}(u',v')=D_{12}(u',2-v').
\]

The affine substitution preserves every numerator space of bounded total
degree. Over \(\mathbf F_{2^{61}-1}\), all \(33\) transported systems
give

\[
\operatorname{rank}\nabla^{31}_{m,d}
=
4\binom{d+2}{2},
\]

\[
\operatorname{rank}
[\nabla^{31}_{m,d}\mid-C^{31}]
=
4\binom{d+2}{2}+1.
\]

Comparison with Entry 757 gives

\[
\boxed{
\text{rank-signature mismatches}=0.
}
\]

In particular,

\[
\boxed{
\delta_{31}(m,d)=\delta_{12}(m,d)=1
\qquad
(m\le2, d\le10).
}
\]

The filtered rank-one extension defect is therefore occurrence-covariant
under the labelled \(G_{12}\to G_{31}\) transition.

## Pole-exponent transport

Order the nine source divisors as

\[
(u,v,y,1-y,1+y,v-u,y-u^2,y+u^2,P_6).
\]

Their target pullbacks are

\[
\left(
u',\,2-v',\,\frac{u'-v'}2,\,
1-\frac{u'-v'}2,\,
1+\frac{u'-v'}2,\,
2-v'-u',
\right.
\]

\[
\left.
\frac{u'-v'}2-u'^2,\,
\frac{u'-v'}2+u'^2,\,
P_6(u',2-v')
\right).
\]

The chart map is affine with unit Jacobian. Hence it induces

\[
\boxed{
\mathbb Z^9_{\rm poles}\xrightarrow{\ I_9\ }
\mathbb Z^9_{\rm poles}
}
\]

in these labelled orders and contributes no additional poles.

For Entry 757's uniform denominator, the source-induced target vector is
therefore exactly

\[
\boxed{(1,1,1,1,1,1,1,1,1).}
\]

The transition does not select a preferred nonuniform vector: it transports
any independently derived vector unchanged in the labelled orders. Claiming
a minimal sparse vector from the chart transition alone would be post hoc.

As a separate diagnostic, direct divisibility of the serialized
off-diagonal fit denominators detects the partial maximum vector

\[
(1,1,1,0,0,1,1,1,0).
\]

Several reduced serialized denominators retain residual factors, so this is
not a complete source-derived pole vector and must not govern the next
census.

## Narrow result

The same rank-one filtered obstruction is present in the reflected occurrence
chart after transporting the cocycle, Hom differential, residue orientation,
base coordinates, and denominator filtration together.

This rules out a fixed-chart artifact at the tested filtration. It does not
prove absolute nonsplitting, nor does occurrence covariance determine the
next nonuniform denominator ansatz.

## Evidence

- `research/benincasa/check_gysin_occurrence_covariance.py`;
- `research/benincasa/gysin-occurrence-covariance-d10.json`;
- Entries 756, 757, and 759;
- allocator claim `seqclaim-5a2dd86ce0f58dbe2db7c1e9`;
- epistemic event `ev-000000000373-d238f57f-cc31-497d-95b1-e9391b4fd608`.

## Next falsifier

Construct the remaining cyclic chart transitions and test the three-chart
cocycle on \(C\) and \(\nabla_{\operatorname{Hom}}\). Independently derive
a nonuniform pole filtration from the labelled source complex or a
normal-crossing lattice; the affine occurrence map alone cannot supply it.
