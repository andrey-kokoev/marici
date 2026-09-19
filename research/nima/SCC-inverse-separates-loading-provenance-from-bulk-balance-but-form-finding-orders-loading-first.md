# SCC inverse separates loading provenance from bulk balance, but form-finding orders loading first

## Question

Which witness is first after categorical source-stratum separation?

## SCC inverse result

Running SCC inverse on `external_cg_identification_claim` returns exactly two
missing witnesses:

- `source_derived_arithmetic_loading`;
- `independent_bulk_balance_evidence`.

It ranks the associated experiments equally because each separates one missing
branch. This is a dependency count, not an authorization to execute them in
either order.

## Analytical ordering

The bulk-pairing experiment is not typed until the loading map exists. The
required order is

\[
D_{\rm ret}^{\rm ar}
\xrightarrow{\Lambda_{\rm ar}}
E_{C34}
\xrightarrow{\rho}
\mathcal B(H)
\xrightarrow{q_{\mathfrak F}}
\mathbb C.
\]

Without `Lambda_ar`, the proposed packet equality has no common source. A
numerical or scalar comparison would fit an observer to the desired result.

Accordingly the first admissible experiment is the source-loading provenance
test. Its pass condition is not agreement of scalar coefficients. It must
supply:

1. a source operation producing the Mellin observer;
2. its domain, grades, topology, and reciprocal action;
3. compatibility with primitive, square, endpoint, connected, and
   archimedean coordinates;
4. a transport law into the `C34` observer representation;
5. a finite hostile that can reject the map before bulk scalarization.

Only after those conditions pass can the independent bulk-pairing test be
formed.

## Disposition

The SCC inverse result confirms two logically independent missing witnesses.
The analytical form-finding rules impose a strict workflow dependency not
encoded by SCC's equal information-gain score: loading provenance precedes bulk
balance.