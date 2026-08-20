---
authors:
  - marici.Nima
---
# Deutsch-Popperian Pointed Alexander--Tate Butterfly Conjecture

## Record

Date: 2026-08-15

Status: conjecture with a finite integral obstruction-and-parity test.

This entry formulates the next global carrier experiment after entry 135. It
does not assert that the endpoint-compatible butterfly or its loaded
PC/Cousin lift exists.

## Established input

The labelled scalar boundary geometry supplies a canonical integral
\(D_3\)-equivariant roof

\[
U\xleftarrow{\simeq}C_{\rm tag}
\xrightarrow{M_{\rm AD}}T,
\qquad
M_{\rm AD}=R-R^2.
\]

Here \(C_{\rm tag}\) is the two-term tag complex, \(U\) is the scalar
support-pair cone, and \(T=[P_{\rm road}\xrightarrow{\epsilon}\mathbf1]\).
The Alexander--Whitney front and back representatives are joined by an
integral \(D_3\)-equivariant collar homotopy.

Entry 135 also establishes two negative controls:

- the desired saturated peripheral map has no strict integral
  \(D_3\)-equivariant realization on the reduced boundary complex;
- unrestricted full-cone lifts form a noncanonical affine rank-nine family,
  so existence of strict lifts does not select a physical representative.

Thus the roof is canonical, while a pointed endpoint-compatible
representative is not yet constructed.

## Conjecture

Ordered physical normal geometry canonically points the Alexander--Tate
butterfly.

More precisely, there exists a \(D_3\)-equivariant morphism of
two-extensions

\[
\boxed{
\mathfrak B_{\rm AD}:
\left[
0\to F_0\to F_1\to F_2/F_0\to F_2/F_1\to0
\right]
\Longrightarrow
\left[
0\to\mathbf1_{\rm or}\xrightarrow N
P_{\rm tag}\xrightarrow{1-r}
P_{\rm road}\xrightarrow{\epsilon}\mathbf1\to0
\right].
}
\]

Its middle shadow is the established Alexander--Whitney roof. Its two
endpoint comparison cells are induced by scalar augmentation, relative
duality, and ordered normal orientation rather than by a chosen inverse,
contraction, or rational splitting.

The obstruction to this pointed butterfly vanishes in

\[
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or})\cong\mathbb Z/3,
\]

and the resulting point in the residual torsor

\[
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or})\cong\mathbb Z/2
\]

is the nontrivial orientation class.

After tensoring with the established multi-Rees Cartier packets, the
butterfly admits a loaded PC/Cousin lift whose \(D03\) restriction equals the
independently constructed extraordinary endpoint residue. Its deck orbit is
the proposed global boundary-realization datum for \(\mathsf J\).

## Why the explanation is hard to vary

The ingredients are independently fixed:

- \(N\), \(1-r\), and \(\epsilon\) are the integral augmented-triangle maps;
- \(M_{\rm AD}=R-R^2\) is the saturated peripheral transgression;
- the roof is derived from the labelled Alexander--Whitney cap;
- the order-three group measures the obstruction to integral equivariant
  splitting;
- the order-two group is the complete remaining parity ambiguity;
- ordered physical normals are the only established geometric datum capable
  of selecting that parity;
- the local Cartier--Tate and \(D03\) residue packets were constructed before
  this conjecture.

Changing any of these inputs either reintroduces division by \(3\), leaves the
rank-nine lift ambiguity unresolved, or defines the target comparison from
the desired answer.

## Decisive test

Construct the two endpoint connector cells without choosing:

- a contraction of the acyclic complement;
- a preferred point in the affine rank-nine lift family;
- a rational projector;
- the desired reflection parity.

Compute

\[
o(\mathfrak B_{\rm AD})
\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or}).
\]

Only if \(o=0\), compute

\[
p(\mathfrak B_{\rm AD})
\in
\operatorname{Ext}^1_{\mathbb Z[D_3]}
(\mathbf1,\mathbf1_{\rm or}).
\]

Then construct the loaded lift and compare its \(D03\) restriction with the
existing endpoint packet, retaining both \(\operatorname{Tor}_0\) and
\(\operatorname{Tor}_1\), reciprocal-regular versus original-Borel--Moore
variance, twist reversal, and the positive physical line \([dX_{03}]\).

## Outcome matrix

- \(o\ne0\): the pointed-butterfly conjecture is falsified.
- \(o=0\) and \(p=0\): existence survives, but the predicted orientation
  system is falsified.
- \(o=0\) and \(p=1\): the carrier conjecture passes and the loaded lift
  becomes the next test.
- A loaded lift disagreeing with the established \(D03\) residue falsifies
  its identification with \(\mathsf J\).
- Agreement at \(D03\) followed by deck-orbit failure preserves the local
  construction but falsifies global descent.

## Prohibited repairs

Do not:

- define the Tate representative from the Alexander--Whitney map;
- select a rank-nine lift by coefficient size or convenience;
- invert \(2\) or \(3\);
- infer parity from the outer octagon;
- discard the excess \(\operatorname{Tor}_1\) copy;
- identify carrier equality with loaded PC equality;
- add endpoint cells whose boundaries encode the desired residue.

## Boundary

This conjecture concerns the Nima scalar-boundary branch. It does not depend
on entry 150's cosmological infinity-Gysin theorem and makes no claim about
the Benincasa \(L_1\) problem.

The established theorem is the canonical carrier roof and its strict-map
no-go. The pointed butterfly, its parity, its loaded realization, and global
deck descent remain open.

## Outcome contract

~~~json
{
  "claim": "Ordered physical normal geometry canonically points the integral Alexander-Tate butterfly; its obstruction vanishes and its residual parity is the nontrivial orientation class.",
  "status": "conditional",
  "assumptions": [
    "The established labelled Alexander-Whitney roof and augmented triangle are retained.",
    "Endpoint comparison is formulated in the arrow/two-extension category rather than as a strict projection.",
    "The loaded comparison retains both Tor grades and the established support variances."
  ],
  "evidence_refs": [
    "ledger entry 135",
    "ledger entry 144",
    "research/voevodsky/check_k6_strict_ad_chain_map.rs"
  ],
  "factorization_test": {
    "carrier_roof": "proved",
    "strict_reduced_projection": "falsified",
    "full_cone_lift_space": "affine rank nine and noncanonical",
    "Ext2_obstruction": "to compute in Z/3",
    "Ext1_parity": "to compute in Z/2",
    "loaded_D03_restriction": "open"
  },
  "counterevidence": [
    "The canonical roof does not choose a direct lift.",
    "Front/back Alexander-Whitney conventions are equivariantly homotopic and do not select parity.",
    "Any construction using a rational splitting or a fitted endpoint cell is inadmissible."
  ],
  "next_experiment": "Construct the endpoint-fixed two-extension mapping fiber, compute its Z/3 obstruction and Z/2 parity, and only then test the loaded D03 restriction."
}
~~~
