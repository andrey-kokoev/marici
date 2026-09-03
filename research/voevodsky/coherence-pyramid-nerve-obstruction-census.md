# Coherence-pyramid nerve obstruction census

## Question

What is the explicit current 1-skeleton and cell inventory of the integrated computad presentation, and where does it fail to be a realized global overlap nerve?

## Claim boundary

This census reads the canonical signature and cells/laws modules. It does not infer scientific arrows from partial constructors or treat presentation generators as analytically realized.

## Presentation vertices and edges

The computad has five object sorts:

- `carrier`;
- `finite_green`;
- `gauge_presentation`;
- `closed_form`;
- `quotient_form`.

Its four declared one-generators are:

- `under_embedding`: `finite_green` to `finite_green`;
- `over_quotient`: `gauge_presentation` to `carrier`;
- `vertical_restriction`: `carrier` to `carrier`;
- `closed_form_comparison`: `quotient_form` to `quotient_form`.

As an undirected incidence census, the one-generator skeleton has four connected components:

\[
\{\texttt{carrier},\texttt{gauge_presentation}\},
\quad
\{\texttt{finite_green}\},
\quad
\{\texttt{quotient_form}\},
\quad
\{\texttt{closed_form}\}.
\]

`closed_form` has no incident one-generator. Completion transport exists as a partial constructor/interface, but it has not been promoted into a general one-arrow connecting this sort to the others.

## Cell and law census

The six cell classes are:

- associator;
- left unitor;
- right unitor;
- interchange;
- Beck–Chevalley;
- completion comparison.

The five law classes are:

- pentagon;
- triangle;
- interchange hexagon;
- pasting;
- completion pasting.

These are presentation obligations. Outside the verified analytic Markov subnerve, each remains a census row requiring a sourced boundary, admitted filler, and law certificate.

## Structural consequence

The phrase `full pyramid overlap nerve` currently overstates the one-generator incidence structure. The signature is a multi-component computad presentation joined partly by higher partial constructors, not yet one connected realized nerve.

This exposes a lower obstruction than missing loop coverage: before counting global cycles across all five sorts, every intended cross-component interface must be materialized as a typed arrow, span, correspondence, or explicitly higher-arity constructor with a declared nerve model.

In particular:

- finite Green coherence cannot automatically transport to quotient coherence;
- completion comparison does not connect `closed_form` merely because its name mentions completion;
- gauge quotient and Green embedding live in different components;
- global horn language applies only after the relevant boundaries are present in one typed incidence object.

## Next acceptance test

For every intended cross-component bridge, record:

- source and target object sorts;
- variance;
- whether it is a one-arrow, span, correspondence, or multi-input constructor;
- admission predicates;
- realized analytic instance;
- comparison cells with existing generators;
- physical/readout status.

Only then recompute connected components, cycle basis, simplices, and horn coverage.

## Disposition

The current computad presentation is complete as a generator-and-obligation signature but its explicit one-skeleton is disconnected. The Markov equipment realizes one analytic subnerve; a cross-sector global section is not yet typeable across all object sorts without additional bridge generators or a declared higher-arity nerve construction.

## Verification

- `research/voevodsky/checkers/check_pyramid_nerve_obstruction_census.py`
- `research/voevodsky/results/pyramid_nerve_obstruction_census.json`
