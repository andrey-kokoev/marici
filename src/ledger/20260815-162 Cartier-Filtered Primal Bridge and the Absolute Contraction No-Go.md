---
authors:
  - marici.Nima
date: 2026-08-15
---
# Cartier-Filtered Primal Bridge and the Absolute Contraction No-Go

## Record

Date: 2026-08-15

Status: proved strict Cartier-filtered chain solution with a scoped
absolute-contraction no-go. The associated symbol is nonzero, but the
absolute mapping class and its derived conductor pullback are zero.

This entry records the exact coefficient result following entries 160--161.
It does not construct a normalization-provenanced source, relative support
mapping fiber, endpoint-pointed trace, or physical obstruction class.

## Frozen coefficient complex

Work over the legal unlocalized \(D03\) target-Cech ring \(C\), and put

\[
x=x_3,\qquad y=\frac{X_D}{u_D}.
\]

The source and target differentials are

\[
dH=q-x\xi,\qquad dq=xb,\qquad d\xi=b,\qquad dn_D=yp_D.
\]

The pair \(x,y\) is regular in this scoped coefficient system.
The inverse \(u_D^{-1}\) occurs only in its legal target Cech summand;
\(x\) is never inverted.

For a degree-zero primal lower column write

\[
T(q,p_D)=k,\qquad T(\xi,p_D)=c,\qquad T(b,n_D)=a.
\]

With the fixed tensor sign convention, closedness gives

\[
k-xc=0,\qquad xa+yk=0,\qquad a+yc=0.
\]

## Strict lower-column theorem

**Theorem.** Every strict lower-column solution is uniquely

\[
\boxed{
\bigl(T(q,p_D),T(\xi,p_D),T(b,n_D)\bigr)
=h(x,1,-y),\qquad h\in C.
}
\]

The solution module is saturated, torsion-free, and rank one. Positive
Cartier orientation fixes the primitive coordinate normalization \(h=1\).
All chain equations then pass:

\[
x-x=0,\qquad x(-y)+yx=0,\qquad -y+y=0.
\]

### Proof

The \(H\)-equation forces \(k=xc\). The \(\xi\)-equation forces
\(a=-yc\), and substitution makes the middle equation automatic. Thus every
solution is \(h(x,1,-y)\), with \(h=c\), and every such triple is closed.
Since \(x,y\) is a regular pair, the syzygy module of \(yk+xa=0\) is
\(C(x,-y)\), without integer or \(x\)-torsion. Positive orientation selects
\(h=1\). \(\square\)

## Cartier associated symbol

For the normalized solution,

\[
T(q,p_D)=x\in I=(x).
\]

The ideal-line evaluation

\[
I^\vee\otimes I\longrightarrow C,\qquad x^\vee(x)=1
\]

therefore gives

\[
\boxed{\operatorname{gr}_xT(q,p_D)=1.}
\]

This is an associated symbol without \(x^{-1}\). Its ordinary conductor
value is still

\[
T(q,p_D)\bmod x=0.
\]

Thus entry 177 is sharpened, not reversed: the smallest legal generic
coefficient is \(x\), while the ideal coordinate extracts the symbol \(1\).

## Absolute contraction no-go

Define the unimodular generator

\[
m=q-x\xi.
\]

Then the complete source splits strictly as

\[
\boxed{
[H\xrightarrow{1}m]\oplus[\xi\xrightarrow{1}b].
}
\]

An explicit contraction is

\[
s(m)=H,\qquad s(b)=\xi,\qquad s(H)=s(\xi)=0.
\]

In the original basis this is entry 133's contraction

\[
s(q)=H,\qquad s(b)=\xi,
\]

with the remaining values fixed by the homotopy equation. Consequently every
absolute cross-degree cocycle, including \((x,1,-y)\), is exact in the
unrestricted mapping complex.

The rebase and contraction use unit matrices and survive derived base change
to \(x=0\). Therefore

\[
\boxed{
[T]_{\rm abs}=0,\qquad Li_{x=0}^*[T]=0.
}
\]

The filtered coordinate is not a nonzero absolute trace, conductor class, or
Ext class. Ideal evaluation does not turn a contractible source into
nonzero cohomology.

## Full-source lower-term gate

The full-source \(H\otimes p_D\) equation has the primitive form

\[
\boxed{
1=x(\text{lower-term contribution}).
}
\]

The triple \((x,1,-y)\) supplies all lower coefficients required by the
chain equations, while the source contraction supplies the homotopy making
the absolute cocycle exact. Passing the chain equations is necessary but not
sufficient for a physical class.

## Necessary geometric gate

A nonzero class requires a geometrically typed relative support mapping
fiber whose admissible homotopies make the absolute contraction
inadmissible. It must retain:

- the pre-quotient \(q\)-chain and based \(Q\) image;
- the ideal-valued \(\xi,b\) column and both Tor grades;
- all target Cech lower terms;
- both endpoints and their comparison cells;
- reciprocal-regular source versus BM--Cech target variance; and
- entry 160's localization/Beck--Chevalley square.

Forgetting support, \(Q\)-framing, or endpoint recollement must restore the
absolute contraction. A class surviving that ablation is an ordinary
coefficient artifact.

## Relation to entries 133 and 156--161

- Entry 133 proves the full mixed source is contractible and ordinary Hom
  is acyclic.
- Entries 156--157 show that zero-section restriction and principal-line
  relabelling do not create a global trace.
- Entries 158--159 leave the global source and combined
  generic-\(Q\)/local-Cartier kernel unconstructed.
- Entry 160 identifies the primal localization obstruction and missing
  Beck--Chevalley cell.
- Entry 177 falsifies the primitive incidence-only value \(k=\pm1\).

The present theorem supplies the unique legal filtered column required of a
future construction and proves that this column alone is not that
construction.

## Provenance and exact certificate

Exact certificate:

- research/voevodsky/check_d03_cartier_filtered_primal_bridge.rs
- SHA-256
  046a54ad8c939b3c382f51713759e46aedbfcce8eaa3b1ddc78fca1375144d23

The checker verifies regular-pair syzygy classification, saturation, absence
of torsion, all lower-column equations, primitive orientation, ideal
evaluation, conductor vanishing, the source rebase, absolute exactness, and
persistence of contraction after derived pullback to \(x=0\).

Source and target provenance:

- research/voevodsky/check_d03_pabs_morse_pullback.rs;
- research/voevodsky/check_global_k6_koszul_cech_promotion.rs;
- research/voevodsky/check_primal_zero_section_trace_obstruction.rs; and
- research/voevodsky/check_d03_generic_incidence_pairing_obstruction.rs.

## Falsifiers and scope

The strict theorem is falsified by a legal solution not of the form
\(h(x,1,-y)\), torsion in the solution module, or failure of a displayed
chain equation. The absolute no-go is falsified by nonzero unrestricted
mapping cohomology or failure of the unit contraction after pullback to
\(x=0\). The checker rules out these failures in the frozen model.

This entry does not falsify a relative support class with geometrically
restricted homotopies. It does not construct that mapping fiber, the global
source, endpoint cells, or physical \(\operatorname{ob}_{03}\).

## Anti-circularity controls

Prohibited repairs are:

- declaring the associated symbol \(1\) to be a global trace class;
- deleting \(H\) or another source generator to evade contraction;
- inverting \(x\), a Rees/monodromy parameter, or an integer;
- defining admissible homotopies merely by excluding the known contraction;
- prescribing \(Q\), endpoint, residue, or purity values; or
- replacing entry 143's target generators by ideal-labelled generators.

The relative support category must be derived independently from geometry.

## Next experiment

Build the full ideal-valued pre-quotient localization correspondence. Define
its relative support mapping complex and admissible homotopies from the
normalization/DNC and endpoint/\(Q\) geometry. Test whether
\((x,1,-y)\) survives while both mandatory forgetting functors restore the
absolute contraction. Only then evaluate entry 160's obstruction and the
endpoint-fixed mapping fiber.

## Outcome contract

~~~json
{
  "claim": "All strict lower-column solutions are h*(x,1,-y), with primitive filtered orientation h=1 and associated ideal symbol 1. The full source is contractible after m=q-x*xi, so the absolute mapping class and derived x=0 pullback are zero.",
  "status": "proved",
  "scope": "strict D03 coefficient and Cartier-filtered mapping complex with scoped absolute-contraction no-go",
  "assumptions": [
    "x=x3 and y=X_D/u_D form the frozen legal regular pair.",
    "x is not inverted and target Cech variance is retained.",
    "The full source H,q,xi,b is retained.",
    "No relative support or endpoint framing is inserted into the absolute mapping complex."
  ],
  "factorization": {
    "strict_solution_module": "C*(x,1,-y)",
    "primitive_orientation": "h=1",
    "all_chain_equations": "passed",
    "filtered_ideal_symbol": "1_without_x_inversion",
    "ordinary_conductor_value": "zero",
    "absolute_mapping_class": "zero",
    "derived_x0_pullback": "zero",
    "source_contraction": "m=q-x*xi gives two unit contractible pairs",
    "relative_support_mapping_fiber": "unconstructed",
    "physical_ob03": "untyped"
  },
  "evidence_refs": [
    "research/voevodsky/check_d03_cartier_filtered_primal_bridge.rs",
    "research/voevodsky/check_d03_pabs_morse_pullback.rs",
    "research/voevodsky/check_global_k6_koszul_cech_promotion.rs",
    "research/voevodsky/check_primal_zero_section_trace_obstruction.rs",
    "research/voevodsky/check_d03_generic_incidence_pairing_obstruction.rs",
    "src/ledger/20260814-133 Ordinary-Derived Ablation and the Framed Off-Diagonal Objective.md",
    "src/ledger/20260815-156 Zero-Section Trace No-Go and the Principal-Dual-Line Gate.md",
    "src/ledger/20260815-157 Principal-Line Relabeling No-Go and the Ext-One Globalization Gate.md",
    "src/ledger/20260815-158 Local Gysin Sufficiency No-Go and the Global Mapping-Fiber Definition Gate.md",
    "src/ledger/20260815-159 Global-Q versus Local-Cartier Dichotomy and the Missing Conductor Nullhomotopy.md",
    "src/ledger/20260815-160 Primal Localization-Triangle Obstruction and the One-Road Beck-Chevalley Cell.md",
    "src/ledger/20260815-177 Generic-Incidence Pairing No-Go and the Extraordinary Lower-Term Gate.md"
  ],
  "checker_sha256": "046a54ad8c939b3c382f51713759e46aedbfcce8eaa3b1ddc78fca1375144d23",
  "counterevidence": [
    "Associated-grade ideal evaluation is nonzero although absolute cohomology is zero.",
    "The unit source contraction survives derived base change to x=0.",
    "Removing source generators or defining homotopies from the desired answer is inadmissible."
  ],
  "next_experiment": "Construct the full ideal-valued pre-quotient localization correspondence and a geometrically typed relative support mapping fiber, then test survival of (x,1,-y) with mandatory forgetting ablations."
}
~~~
