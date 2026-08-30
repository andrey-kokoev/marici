---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2145 — The Generic Contact Residue Has No Half-Kummer Normal Character

## Hard-to-vary claim

At generic nonsoft kinematics, the source measure at a component-contact
threshold supplies logarithmic unipotent monodromy but no half-Kummer
character in the normal variable.

## Local residue normal form

Away from the soft and triangle factors in Entry 2136, the branch--pole
tangency is ordinary. In analytic coordinates it has the source-equivalent
normal form

\[
q=v,
\qquad
K=u^2+v+\nu,
\qquad
\Omega=\frac{du\wedge dv}{q\sqrt K}.
\]

Taking the pole residue gives

\[
\operatorname{Res}_{q=0}\Omega
=
\frac{du}{\sqrt{u^2+\nu}}.
\]

Under \(u=\sqrt\nu,t\), the two half-powers cancel:

\[
\frac{du}{\sqrt{u^2+\nu}}
=
\frac{dt}{\sqrt{1+t^2}}.
\]

The collision of its two branch points produces the familiar logarithmic
period. Its semisimple character is \(+1\), with a rank-one nilpotent
variation. No residual factor \(\nu^{1/2}\) remains.

## Consequence for the mixed comparison

Tensoring two contact residues therefore produces the rank-one mixed
variation of Entry 2143, but its image remains in the \((+1,+1)\)
eigenspace. The source residue measure does not provide the
\((-1,-1)\) half-Kummer twist required by Entry 2144.

Hence

\[
\boxed{
\text{the direct contact-product to lower-Kummer comparison is closed at
generic nonsoft kinematics.}
}
\]

This is not a return to the retracted additive argument. The source product
and its nonzero mixed variation are retained; the obstruction is now the
correct monodromy eigenspace.

## Scope

The conclusion excludes the soft and triangle intersections where the
prefactors in Entry 2136 vanish and the ordinary tangency normal form can
degenerate. Those are existing supported strata and require separate local
models.

## Evidence

- Entries 2136 and 2143--2144;
- `research/benincasa/checkers/contact_residue_exponent.rs`;
- allocator claim `seqclaim-a8447bcb221f15d35de2291f`.

## Next falsifier

Move to the existing soft/triangle intersections of the contact threshold.
Derive their degenerate residue normal forms before asking whether a
half-integral character or supported comparison appears. Do not extrapolate
the generic logarithmic model onto those deeper strata.
