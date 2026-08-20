# 1089 — The Raw Rank-Twelve Torsor Degenerates at Every Exceptional Center

## Record

Entry 1088 identifies the existing two-variable source reducer with the
\(X_1\)-projective chart of the radial blowup.  Direct specialization of its
generic source torsor at the rational exceptional centers is not valid: every
tested center changes the exact-reduction rank and destroys the generic fixed
quotient.

Sequence claim: `seqclaim-89cfcfc10bee87dc11852093`.

## Frozen chart and centers

Use

\[
u=\frac{E}{X_1},
\qquad
v=\frac{X_1+X_2-X_3}{X_1}.
\]

The two elliptic base points visible in this chart and the four finite
conductor--energy tangencies of Entry 607 become

\[
(u,v)=(0,2),(2,0),(2,4),(1,2),(2/3,0),(-1,0).
\]

No center is added or fitted for this test.

## Exact finite-field rank audit

At the generic control point \((7,11)\), the four-stratum source system has

\[
\operatorname{rank}M=117,
\qquad
\text{fixed mask}=3847,
\]

corresponding to the seven primitive-independent coordinates of Entries 851
and 861.

At the six centers, both derivative systems remain consistent but give

\[
\begin{array}{c|c|c}
(u,v)&\operatorname{rank}M&\text{fixed mask}\\ \hline
(0,2)&73&0\\
(2,0)&82&0\\
(2,4)&92&0\\
(1,2)&92&0\\
(2/3,0)&93&5\\
(-1,0)&93&3.
\end{array}
\]

The \(u\)- and \(v\)-derivative audits agree at every center.

## Deutsch--Popperian verdict

The naive claim

\[
\boxed{
\text{specialize the generic source solution torsor directly to each
exceptional point}
}
\]

is falsified.  The generic seven-coordinate quotient is not a lattice over
those points.

This is not evidence for a new carrier stratum.  Every tested point is an
existing signed-energy base point or conductor--energy tangency.  The result
instead forces the correctly typed operation:

\[
\boxed{
\text{first derive the center-specific Rees/strict-transform source lattice,
then specialize and test its connection.}
}
\]

## Classification

- rank loss: degeneration of the raw generic presentation;
- support: existing elliptic and conductor intersections;
- required repair: source-derived Rees/strict-transform lattice;
- post-hoc quotient or fitted primitive: prohibited;
- new carrier datum: none.

## Evidence

- `research/benincasa/rank12-exceptional-center-torsor-ranks.json`;
- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- exact modular arithmetic at the source engine's primary 61-bit prime;
- identical ranks and masks in both derivative directions.

## Next falsifier

Start with the simplest center \((u,v)=(0,2)\), whose raw rank is 73.
Pull back the complete four-stratum forms to the source-derived blowup chart,
derive the valuation shift of every master and exact primitive, and recompute
the quotient after saturation.  Failure to recover a finite logarithmic
rank-twelve lattice using the already frozen signed-energy blowup would be a
genuine H2 obstruction.
