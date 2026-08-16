---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Endpoint Polar Jets Cancel in the Tangential Relative Cone

## Record

Status: the two endpoint principal parts left open in entry 238 agree
identically on the frozen square-root sheet. Their oriented difference in
the source tangential relative cone is zero. Thus the complete weight-\(-1\)
occurrence correction leaves neither a punctured-wall class nor an
endpoint-supported relative class.

No endpoint summand, carrier incidence, projector, or fitted tangential
coordinate is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{although }\eta_{-1}=d\Phi_{-1},\text{ the two endpoint polar jets
may have a nonzero oriented difference.}
}
\]

The finite falsifier was equality of the complete Laurent principal parts
in the source-fixed square-root coordinate.

## Frozen endpoint cover

Retain entry 238's notation

\[
a=xy,
\qquad
s=x+y,
\qquad
w^2=an^2-2s.
\]

The two physical wall endpoints are

\[
p_+:n=+N,
\qquad
p_-:n=-N,
\qquad
N^2=\frac{2s}{a},
\]

and both lie over \(w=0\). The frozen positive sheet and lower-half-plane
continuation select the endpoint involution

\[
\iota:(n,w)\longmapsto(-n,w).
\]

Changing \(w\) independently at one endpoint would change the already
frozen branch and is not admissible.

## Complete principal parts

The primitive of entry 238 is, up to its common source scalar,

\[
\frac{3an^2-5s}{w^3}.
\]

Since

\[
an^2=w^2+2s,
\]

one has the exact identity

\[
3an^2-5s=3w^2+s.
\]

Therefore

\[
\boxed{
\Phi_{-1}
=
C\left(\frac{s}{w^3}+\frac3w\right),
\qquad
C=\frac{(x-y)(x+y)}{8x^{7/2}y^{7/2}}.
}
\]

There are no omitted regular or higher polar terms: this expression is
exact on the cover. At both endpoints the ordered coefficient vector of
\((w^{-3},w^{-1})\) is

\[
\operatorname{PP}_{p_+}\Phi_{-1}
=
\operatorname{PP}_{p_-}\Phi_{-1}
=
C(s,3).
\]

Hence

\[
\boxed{
\operatorname{PP}_{p_+}\Phi_{-1}
-
\operatorname{PP}_{p_-}\Phi_{-1}
=0.
}
\]

## Relative-cone consequence

For the oriented source interval from \(p_-\) to \(p_+\), endpoint data
enter through the reduced difference

\[
[p_+]-[p_-].
\]

The diagonal endpoint germ is killed in this reduced cone. Since the two
full principal parts coincide, the meromorphic primitive trivializes both
the interior form and its oriented endpoint jet:

\[
\boxed{
[\eta_{-1}]_{\rm tang,rel}=0.
}
\]

This is stronger than the regularized-period statement of entries 235 and
238. The result does not rely on discarding divergent terms; their complete
coefficient vectors cancel.

## Verdict

The surviving-endpoint-jet conjecture is falsified:

\[
\boxed{
\text{complete weight }-1\text{ relative wall correction}=0.
}
\]

The first nonzero Laurent coefficient in entry 235 is therefore an exact
representative with a diagonal endpoint germ, not a surviving relative
coefficient class. No comparison with the absolute nine-master kernel,
\(L_1\), or \(\mathcal Q\) is generated at this grade.

## Classification

- existing carrier: unchanged two endpoint flags and wall interval;
- punctured-wall class: zero;
- endpoint principal parts: nonzero individually and identical;
- oriented endpoint relative class: zero;
- physical regularized pairing: zero;
- elliptic/infinity-Gysin image: zero;
- absolute nine-master coordinate: not defined and unnecessary;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_wall_endpoint_principal_parts.rs`;
- `research/benincasa/wall-endpoint-principal-parts.json`;
- exact cover identity at 33,792 integer specializations;
- exact equality of both principal-part coefficient vectors;
- warnings-denied optimized Rust compilation and exact JSON comparison.

## Next finite falsifier

Advance one complete Rees grade. Compute the weight-\(0\) logarithmic wall
form from the literal unsplit occurrence lift, including one further order
of each frozen source factor. Before pairing it with a chain, test in order:

1. whether its logarithmic coefficient is nonzero;
2. whether it is exact on the punctured wall cover;
3. whether any primitive has a nonzero oriented endpoint principal-part
   difference;
4. only then whether a relative class maps through a separately derived
   realization functor.

This ordering prevents another nonzero coefficient from being mistaken for
a cohomology class. A genuinely nonzero relative class remains coefficient
data over the existing carrier unless it requires a new endpoint incidence.

## Outcome contract

~~~json
{
  "claim": "The exact weight -1 primitive has a nonzero oriented endpoint polar-jet difference.",
  "status": "falsified",
  "primitive_on_cover": "C*(s/w^3+3/w)",
  "endpoint_principal_parts": {
    "plus": ["C*s", "3*C"],
    "minus": ["C*s", "3*C"]
  },
  "oriented_difference": [0, 0],
  "weight_minus_one_tangential_relative_class": 0,
  "new_carrier_incidence": false,
  "next_experiment": "Compute and reduce the complete weight-0 wall form."
}
~~~
