# Transported-form lift needs no independent return map

## Question

Once Gaussian analysis and reconstruction satisfy the Hilbert identity, is a second source-valid return map independently required to lift that identity to a closed form?

## Claim boundary

No. A form defined on the Gaussian analysis range pulls back uniquely through the existing reconstruction. In infinite dimension the substantive gates are source definition, closability, and semiboundedness of that form. Equality with the Weil form remains a separate comparison theorem.

## Existing identity

Let

\[
\mathcal A:
\mathcal H_{\rm ord}
\longrightarrow
\mathcal R_G
\]

be Gaussian analysis and let

\[
\mathcal S=
\mathcal A^{-1}:
\mathcal R_G
\longrightarrow
\mathcal H_{\rm ord}.
\]

Then

\[
\mathcal S\mathcal A
=
1_{\mathcal H_{\rm ord}}.
\]

## Form transport

Suppose the source supplies a Hermitian form \(k\) on a dense subspace \(D_G\subset\mathcal R_G\). Define

\[
D=
\mathcal S(D_G)
\]

and

\[
q(f,g)
=
k(\mathcal Af,\mathcal Ag).
\]

Conversely,

\[
k(F,G)
=
q(\mathcal SF,\mathcal SG).
\]

These operations are inverse. No additional return arrow is available or needed: \(\mathcal S\) already performs reconstruction.

If \(k\) is closable in the transported Hilbert norm, then its pullback \(q\) is closable, and their closures correspond under \(\mathcal A\). Semiboundedness is likewise preserved.

## Core status

If the initial source form is defined on the algebraic Gaussian span and is closable, that span is a core for its closure by construction. A separate graph-core theorem is needed only to identify this closure with a pre-existing larger operator or form domain.

Thus graph-core density is not an independent prerequisite for forming the minimal closed realization. It becomes a comparison gate when claiming equality with another realization.

## Revised dependency structure

The minimal completed-form lift of the observer identity requires:

1. a source-defined polarized kernel
   \[
   K(\tau,\sigma)
   \]
   on the Gaussian span;
2. closability of the induced form relative to the order norm;
3. the required lower bound.

It does not independently require a second reconstruction map.

After this lift exists, a source--Weil comparison asks whether its closed form agrees with the zero-side realization on a common core. That theorem is not part of the observer identity itself.

## Residual interpretation

The observer identity has zero residual before adding form structure. A nonzero completed-form residual can therefore arise only from failure of the source kernel to descend continuously through the Hilbert realization. Its first manifestation is precisely a base-null, form-Cauchy sequence violating closability.

## Disposition

The prior four-blocker description overcounted dependencies. `source_valid_realization_return` is removed from the minimal form-lift gate, and `graph_form_core_faithfulness` moves to the later comparison gate unless a larger domain is asserted. The first missing object remains the polarized jointly regularized source kernel, followed by closability and semiboundedness.

## Verification

- `research/voevodsky/checkers/check_transported_form_identity_lift.py`
- `research/voevodsky/results/transported_form_identity_lift.json`
