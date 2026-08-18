---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 666 — Shared-Wall Occurrence Endpoints Return to Energy-Letter Support

## Hard-to-vary claim

The source-derived codimension-two intersections between each occurrence
wall and its nonparallel shared walls do not generate \(\mathcal Q\).
Their Cayley--Menger branch values instead contain the already frozen
total-energy and signed-energy letters.

## Physical endpoints

On \(q_{g_{23}}=0\), hence \(b=x\), the shared walls
\(q_{g_2}=0\) and \(q_{g_3}=0\) give

\[
(a,b)=(x+z,x),\qquad (a,b)=(-(x+z),x).
\]

On \(q_{g_{31}}=0\), hence \(a=y\), the reflected walls give

\[
(a,b)=(y,y+z),\qquad (a,b)=(y,-(y+z)).
\]

Because \(K_E\) is even in \(a,b\), each reflected pair has one branch
value.

## Exact factor census

Let

\[
\ell_1=x-y-z,qquad \ell_2=x-y+z,qquad E=x+y+z.
\]

Exact polynomial division over
\(\mathbb F_{2305843009213693951}\) gives

\[
\nu_E K_E(x+z,x)=2,qquad
\nu_{\ell_1}K_E(x+z,x)=2,qquad
\nu_{\mathcal Q}K_E(x+z,x)=0,
\]

and

\[
\nu_E K_E(y,y+z)=2,qquad
\nu_{\ell_2}K_E(y,y+z)=2,qquad
\nu_{\mathcal Q}K_E(y,y+z)=0.
\]

Therefore

\[
\boxed{
\mathcal Q\nmid K_E(x+z,x),
\qquad
\mathcal Q\nmid K_E(y,y+z).
}
\]

The source-defined shared-wall/occurrence endpoints return to the existing
signed-energy arrangement. They do not provide the Källén cover of Entry
660.

## Consequence

Entries 664--666 now exclude all branch-support mechanisms formed from one
occurrence wall and at most one additional marked incidence:

- the individual occurrence branch discriminants;
- the intersection of both occurrence walls;
- each occurrence wall intersected with a nonparallel shared wall.

This strengthens the remaining classification:

\[
\boxed{
\mathcal Q\text{, if physical, requires genuinely relative multi-mark
gluing or extension data.}
}
\]

It does not require a new carrier stratum. Nima's Entry 663 independently
shows why the source-labelled relative complex must be retained before
absolute reduction.

## Next falsifier

Construct the source-labelled comparison between the two rank-nineteen
relative top blocks. The comparison must be induced by their common
three-wall boundary complex. Test whether its determinant, Fitting support,
or mapping-cone discriminant contains \(\mathcal Q\). Do not identify
fiber coordinates across the two occurrence branches by hand.

## Evidence

- Entries 660--665;
- research/benincasa/physical-shared-occurrence-endpoints.json.
- epistemic event ev-000000000269-5855b999-4fdb-4083-a095-2c1ee888dbd8.

## Outcome contract

~~~json
{
  "claim": "Q is generated at a source-derived shared-wall/occurrence endpoint.",
  "status": "falsified",
  "g23_existing_factors": ["E^2", "ell_1^2"],
  "g31_existing_factors": ["E^2", "ell_2^2"],
  "Q_factor": false,
  "surviving_home": "source-labelled relative multi-mark gluing or extension",
  "new_carrier_datum": false
}
~~~
