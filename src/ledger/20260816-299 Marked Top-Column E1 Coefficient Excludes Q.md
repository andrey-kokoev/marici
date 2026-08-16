---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Source-Normalized Marked Top-Column E1 Coefficient Excludes Q at Generic Fibers

> **Further update (Entry 310).** The exclusion below is no longer confined
> to one projected top-column coefficient.  A direct reduction at a generic
> finite-field point on \(\mathcal Q=0\) finds the complete frozen
> \(4\times4\) block and its invariant algebraic plane regular.  Thus
> \(\mathcal Q\) is not an unavoidable connection-support divisor in that
> tested model.

## Narrow result

The frozen rank-twelve marked relative reduction has now been continued through
the first ordinary normal order at which the source quartic can contribute.
After the canonical Rees shift

\[
\widehat\Omega_{111}=\Omega_{111}+\frac{e_6}{8E},
\]

the fixed \(e_6\)-coordinate of the \(E^1\) connection term is not

\[
[E^1]\frac12\partial_E\log(-\mathcal Q)=\frac1{2xy}
\]

at either of two independent generic kinematic scales. The failure is stable
when the exact-form polynomial space is enlarged from total degree four to
five.

Thus the source quartic is not the canonical half-log coefficient of the
source-normalized primitive two-wall top-column extension in the tested
relative Gauss--Manin model.

This closes the last local half-log home left open by Entries 297--298. It
does not promote the stronger statement that \(\mathcal Q\) cannot occur in
a global period presentation or in a noncanonical scalar operator.

## Frozen calculation

Use

\[
l_1=b+x-E,qquad l_2=a+y-E
\]

and the source lift

\[
\Omega_{111}=\frac{da\wedge db}{l_1l_2\sqrt{K_E}}.
\]

No basis element or support summand is added. The reduction is performed
modulo exact one-forms on the four predeclared strata

\[
l_1l_2\sqrt K,qquad l_1\sqrt K,qquad
l_2\sqrt K,qquad \sqrt K,
\]

with the frozen rank-twelve basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]

The exact total-energy family is

\[
K_E=R^2+EK_1+E^2K_2+E^3K_3+E^4K_4-6(x+y)E^5+2E^6,
\]

where

\[
R=xa^2+yb^2-xy(x+y).
\]

All Laurent coefficients from \(E^{-2}\) through \(E^3\) are solved
simultaneously over \(\mathbb F_{1000003}\). At exact-field degree five
each fiber gives 522 polynomial equations in 1080 variables and rank 416,
with no contradiction.

## Stabilization at the first fiber

At \((x,y)=(2,3)\), degree four and degree five give the same fixed model
coordinate

\[
[e_6E^1]_{\rm raw,model}=828535
\quad\text{in }\mathbb F_{1000003}.
\]

The computational family uses the opposite normal orientation from the
source convention. This is fixed independently by

\[
c_{111}^{(-1)}=-1\quad\text{in the model},
\qquad
c_{111}^{(-1)}=+1\quad\text{in the source}.
\]

Therefore odd normal coefficients change sign, and

\[
[e_6E^1]_{\rm raw,source}=171468.
\]

The invariant-line correction from Entry 298 is

\[
\frac1{8(x+y)^3}+\frac{3(x+y)}{8x^2y^2}=93417.
\]

Hence the complete shifted coefficient is

\[
\boxed{264885},
\]

whereas the quartic half-log prediction is

\[
\frac1{2xy}=\frac1{12}=416668.
\]

Their difference is

\[
\boxed{848220\neq0}
\quad\text{in }\mathbb F_{1000003}.
\]

## Independent fibers

The exchanged fiber \((3,2)\) reproduces the same values, with the expected
exchange of the one-wall and \(e_8,e_9\) coordinates.

At the genuinely different scale \((x,y)=(2,5)\), the fixed degree-five
data give

\[
[e_6E^1]_{\rm raw,model}=354384,
\qquad
[e_6E^1]_{\rm raw,source}=645619.
\]

Adding the invariant-line correction \(523686\) gives

\[
\boxed{169302},
\]

while

\[
\frac1{2xy}=650002.
\]

The difference is again nonzero:

\[
\boxed{519303\neq0}.
\]

Because all denominators used in the comparison are nonzero at these fibers
modulo the chosen prime, either mismatch is a finite falsifier of equality of
the two rational functions in the frozen source normalization.

## What has been excluded

The following candidate has failed:

\[
\boxed{
\text{the marked primitive top-column Rees extension carries }
\frac12d\log(-\mathcal Q)
\text{ on its canonical }e_6\text{ coordinate}.
}
\]

The conclusion is narrower than basis-independent absence of \(\mathcal Q\).
It concerns the fixed source lift, the canonical \(e_6/(8E)\) Rees
regularization, and the exact relative quotient modulo the predeclared
degree-five exact calculus.

Together with Entries 209--212 and 287--288, the present test leaves no
derived intrinsic home for \(\mathcal Q\) in the pure elliptic quotient,
generic algebraic kernel, generic algebraic extension, physical relative-chain
monodromy, absolute smoothing discriminant, enhanced-point discriminant, or
the canonical local marked top-column half-log coefficient.

## Classification

| Structure | Classification |
|---|---|
| rank-twelve marked top column | existing relative coefficient object |
| \(E^{-2}\) correction | Rees gauge on the invariant algebraic Kummer line |
| fixed \(E^1e_6\) term | Tate/Kummer extension data |
| \(\mathcal Q\) half-log equality | finitely falsified in this local source normalization |
| elliptic modification | none |
| new carrier datum | none |

The evidence therefore updates toward

\[
\text{shared carrier}
+
\text{shared derived calculus}
+
\text{sector-specific coefficient objects},
\]

while downgrading \(\mathcal Q\) to apparent or presentation-dependent
alphabet data unless a distinct, independently forced global construction
produces it.

## Deutsch--Popperian update M2.42

The hard-to-vary claim

\[
\text{the source quartic is the logarithmic connection of the canonical
marked two-wall algebraic extension}
\]

is falsified by exact finite calculations at two independent generic scales.

The smaller surviving conjecture is

\[
\boxed{
\text{the primitive marked extension is intrinsic Tate/Kummer data on the
frozen carrier, while }\mathcal Q\text{ is not its canonical local
half-log divisor.}
}
\]

## Next hostile test

Stop searching for \(\mathcal Q\) by projecting additional local scalar
coordinates. Instead construct the canonical global nearby-cycle
decomposition of the complete rank-twelve marked system. Determine:

1. the elliptic rank-two quotient and its rank-one nilpotent;
2. the algebraic/Tate--Kummer kernel and conductor characters;
3. the four enhanced semistable classes;
4. the occurrence-root two-torsion gluing;
5. the integral lattice index and physical relative-chain compatibility.

A failure to assemble these pieces over the unchanged energy/Cut carrier is
the next finite falsifier of the shared-carrier hypothesis.
