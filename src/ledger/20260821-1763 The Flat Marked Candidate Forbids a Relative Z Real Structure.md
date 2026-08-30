# 1763 — The Flat Marked Candidate Forbids a Relative \(Z\) Real Structure

## Candidate scope

Entry 868 analyzes the exact rational \(4\times3\) marked-extension
candidate. It proves that every marked generator has a nonzero component
along both split algebraic lines:

\[
\mathcal A_{--}
\simeq\mathcal L_1\oplus\mathcal L_2.
\]

Entry 870 proves the candidate is exactly flat. Its remaining limitation is
source provenance: the full characteristic-zero reduction identities have
not certified that this candidate is the source-selected extension.

## Extension-incidence graph

Form a bipartite graph with:

- three marked quotient generators \(w_1,w_2,w_3\);
- two algebraic target lines \(\mathcal L_1,\mathcal L_2\);
- one edge for every nonzero extension component.

The candidate graph is

\[
K_{3,2}.
\]

In particular, it is connected.

Let a diagonal antiunitary real structure assign signs

\[
\epsilon_{w_i},\qquad \epsilon_{\mathcal L_j}\in\{\pm1\}.
\]

Preservation of a nonzero extension edge requires

\[
\epsilon_{w_i}=\epsilon_{\mathcal L_j}.
\]

Connectivity therefore forces

\[
\boxed{
\epsilon_{w_1}=\epsilon_{w_2}=\epsilon_{w_3}
=\epsilon_{\mathcal L_1}=\epsilon_{\mathcal L_2}.
}
\]

Only the all-plus and all-minus assignments survive.

## Narrow result

For the exact flat candidate, every diagonal antiunitary lift is a global
sign times plain conjugation \(K\). A relative

\[
Z=\operatorname{diag}(1,-1)
\]

between the two algebraic lines is incompatible with the nonzero marked
extension edges.

Thus the candidate does not activate Entry 1760's selective \(ZK\)
extension either. This strengthens Entry 1762 at candidate level.

The source conclusion remains open until the marked block is independently
certified or its two-line nonvanishing is derived directly from source
forms. No new carrier stratum is implicated.

## Durable artifacts

- research/benincasa/checkers/marked_extension_sign_centralizer.rs
- research/benincasa/results/marked-extension-sign-centralizer.json
- research/benincasa/marked-extension-sign-centralizer.md

## Next falsifier

Derive only the support graph of the source marked block—without
reconstructing its rational coefficients. It suffices to prove that every
marked generator has a nonzero source projection to both algebraic lines.
If so, the no-\(ZK\) conclusion becomes source-derived without completing
the expensive 132-identity certificate.
