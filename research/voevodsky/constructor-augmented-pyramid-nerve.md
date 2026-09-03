# Constructor-augmented pyramid nerve

## Question

Does adding the declared partial completion constructor connect the disconnected one-generator skeleton?

## Claim boundary

This packet treats a partial multi-input constructor as a hyperedge among every object sort explicitly occurring in its typed interface. It does not coerce that constructor into a total one-arrow.

## Completion hyperedge

The canonical `complete_finite_form_system` interface explicitly involves:

- `finite_green` input systems;
- `quotient_form` compatibility/output data;
- `closed_form` candidate limits and output.

It therefore supplies a partial hyperedge

\[
\{\texttt{finite_green},\texttt{quotient_form},\texttt{closed_form}\}.
\]

Adding this hyperedge merges three isolated one-skeleton components into one constructor-connected component.

## Augmented components

The constructor-augmented incidence object has exactly two components:

\[
\{\texttt{carrier},\texttt{gauge_presentation}\}
\]

and

\[
\{\texttt{finite_green},\texttt{quotient_form},\texttt{closed_form}\}.
\]

Thus completion repairs most of the one-skeleton disconnection, but no declared constructor connects the carrier/gauge component to the Green/quotient/closed component.

## Composition module caveat

The partial-composition module mentions `finite_green` and `quotient_form` in separate identity and composition clauses. Mere co-occurrence in one module is not a typed bridge. A bridge needs one constructor whose boundary includes both sorts.

## Consequence

The first missing global incidence object is now sharper: a typed bridge between

\[
\{\texttt{carrier},\texttt{gauge_presentation}\}
\quad\text{and}\quad
\{\texttt{finite_green},\texttt{quotient_form},\texttt{closed_form}\}.
\]

Possible bridge shapes include:

- a source-derived Green realization on a carrier;
- a gauge presentation of a finite Green object;
- a correspondence relating carrier restriction to Green restriction;
- a multi-input constructor with an explicit carrier and analytic-form boundary.

No such shape should be selected without a sourced map and variance declaration.

## Disposition

The augmented nerve is not globally connected, but its obstruction is no longer diffuse. Completion provides one verified presentation-level hyperedge joining the analytic form sorts. One cross-component carrier-to-analytic bridge remains the minimal incidence prerequisite before global cycle and horn coverage can be computed.

## Verification

- `research/voevodsky/checkers/check_constructor_augmented_nerve.py`
- `research/voevodsky/results/constructor_augmented_nerve.json`
