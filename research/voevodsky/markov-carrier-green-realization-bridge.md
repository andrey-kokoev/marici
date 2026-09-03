# Markov carrier-to-Green realization bridge

## Question

Is the missing carrier-to-analytic incidence bridge already realized on a restricted sourced domain?

## Claim boundary

The constructor applies only to typed finite ordered paths and finite rooted trees with contraction transfers. It does not map arbitrary Carriers to Green objects and supplies no physical readout.

## Constructor

A Markov Carrier consists of typed vertex fibers and contraction transfers on either:

- a finite ordered path;
- a finite rooted tree with one parent per nonroot vertex.

The realization constructor sends it to its finite Green covariance:

- ordered path products for path carriers;
- lowest-common-ancestor products for rooted-tree carriers.

Positivity follows from the corresponding innovation recursion. Therefore this is a sourced partial constructor

\[
\mathsf{Carrier}_{\mathrm{Markov}}
\longrightarrow
\mathsf{FiniteGreen}.
\]

## Naturality

Existing exact results establish compatibility with:

- ordered-subset restriction via effective covariances;
- rooted ancestor-closed subtree restriction;
- seam-compatible path amalgamation;
- conditionally independent rooted-branch amalgamation;
- orthogonal vertex gauge;
- uniform completion for path carriers.

The restriction comparisons are identity Beck–Chevalley cells. Amalgamation associators and pentagons are strict on the admitted domains.

## Incidence consequence

Adding this partial bridge to the completion hyperedge connects all five computad object sorts at the hypergraph level:
The `carrier`–`gauge_presentation` component is thereby joined to the
`finite_green`–`quotient_form`–`closed_form` component.


The connection is domain-restricted. It proves connectedness only for the Markov analytic subnerve and presentation incidence, not for arbitrary cross-sector Carriers.

## Gauge presentation placement

The existing `over_quotient` generator connects `gauge_presentation` to `carrier`. Within the Markov domain, composing it with the realization bridge produces a path from gauge presentation to finite Green data only when the quotient Carrier retains typed Markov transfers. This composition requires its own interface certificate; graph connectivity alone does not establish it.

## Disposition

The missing incidence shape exists on a nontrivial analytic domain: typed Markov Carriers realize finite Green kernels naturally. The five-sort hypergraph becomes connected, while global cross-sector realization remains partial because the bridge domain excludes arbitrary Carriers and physical sectors.

## Verification

- `research/voevodsky/checkers/check_markov_carrier_green_bridge.py`
- `research/voevodsky/results/markov_carrier_green_bridge.json`
