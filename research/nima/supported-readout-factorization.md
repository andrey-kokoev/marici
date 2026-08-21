# Supported Readout Factorization and Extension Ambiguity

Let

\[
q:V\longrightarrow W
\]

be any source-declared linear comparison and let \(\ell\in V^*\).  Then

\[
\ell|_{\ker q}=0
\]

is equivalent to the existence of a unique functional

\[
\ell_{\rm supp}\in(\operatorname{im}q)^*
\]

such that

\[
\ell=\ell_{\rm supp}\circ q.
\]

This supported functional is canonical.  A functional on the whole target
\(W\) extending \(\ell_{\rm supp}\) is generally not canonical.  Over a
finite field \(\mathbb F_p\), the set of extensions has size

\[
\boxed{
p^{\dim W-\operatorname{rank}q}.
}
\]

Thus:

\[
\boxed{
\text{kernel annihilation gives canonical support-level descent, not a
canonical ambient-target readout.}
}
\]

The exhaustive checker verifies every matrix with domain and codomain
dimensions at most three over \(\mathbb F_2\), and at most two over
\(\mathbb F_3\).  It checks existence, the exact extension count, and
agreement of all extensions on \(\operatorname{im}q\).

## Why this matters for Marici

This theorem isolates a recurring mistake:

- a source map canonically determines a supported quotient line or image;
- choosing a projection, complement, primitive lift, or ambient extension
  is then treated as though it were part of the source.

It is not.  Only the functional on the actual image is canonical.  This
matches the earlier fitting-line and primitive-transport failures: the
supported class may be real while its extension to a preferred ambient
coordinate is section-dependent.

For a surjective \(q\), \(\operatorname{im}q=W\), so the ambiguity
vanishes and the previous physical-readout descent criterion is recovered.

Artifacts:

- `research/nima/check_supported_readout_factorization.py`
- `research/nima/results/supported-readout-factorization.json`
