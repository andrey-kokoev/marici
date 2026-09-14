# Quasicrystal explicit formula makes temperedness itself the RH gate

## Newly located source

A web search located a source absent from the prior Marici bibliography:

J. Arias de Reyna, *Explicit formula and quasicrystal definition*, arXiv:2402.10604v2 (13 March 2025).

The primary PDF was downloaded and inspected directly.

## Arithmetic measure

The paper considers the signed Radon measure, up to its Fourier convention,

\[
\mu
=
-\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr)
+2\cosh(x/2)\,dx.
\]

This is exactly the prime comb plus the continuous endpoint counterterm that cancels its leading exponential mass growth. The paper proves:

\[
\boxed{
\mathrm{RH}
\iff
\mu\text{ is a tempered distribution}.
}
\]

Under RH, its Fourier transform is a signed zero/archimedean measure of the form

\[
\sum_\gamma\delta_{\gamma/(2\pi)}
-2\vartheta'(2\pi t)\,dt,
\]

again subject to Fourier normalization.

## What this adds

The theorem makes the global completion obstruction more primitive than positivity. The raw prime measure has exponentially growing mass. Endpoint subtraction cancels its leading asymptotic, but polynomial residual growth—hence temperedness—is already equivalent to RH.

Thus any construction that starts by placing the completed prime--endpoint comb in the Schwartz-tempered category may already be assuming an RH-equivalent statement. This is a new circularity check for proposed GNS, Fourier, or quasicrystal carriers.

In particular, one cannot argue:

1. form the completed arithmetic tempered distribution;
2. Fourier transform it;
3. prove or infer positivity of its spectral measure.

Step 1 is itself RH-strength for this unsmoothed measure.

## Why it is not the desired positive factorization

Both sides of the quasicrystal identity are signed:

- prime atoms occur with negative coefficients;
- the endpoint density is positive but exponentially growing;
- the zero comb is corrected by a signed continuous theta-phase density.

The theorem proves no positive measure, positive-definite kernel, or Hilbert Gram factorization. Its converse derives zero-free half-plane information from temperedness, so importing temperedness as a regularity hypothesis is circular.

Gaussian smoothing remains source-definable at each positive width because the log-Gaussian damps the prime comb. But a cutoff-independent passage back to the unsmoothed distribution cannot be justified merely by Schwartz continuity unless the required uniform polynomial-growth bound is proved independently.

## Relation to the rung-four gate

For every fixed Gaussian observer, explicit prime tails are finite and certifiable. The obstruction appears in universal completion across narrowing widths and arbitrary Schwartz tests:

\[
\text{finite-width source kernels}
\longrightarrow
\text{one global tempered distribution}.
\]

A positive measure factorization of the global distribution would imply temperedness and therefore RH. The paper confirms that there is no weaker hidden regularity theorem available at this interface.

## Source-provenance boundary

The usable unconditional content is:

- \(\mu\) is a locally finite signed Radon measure;
- endpoint and prime masses have matching leading exponential scale;
- Gaussian pairings at fixed positive width can be defined directly by convergent formulas.

The non-usable upstream premise is global temperedness.

## Search and verification

- Primary PDF: `temp/2402.10604.pdf`
- Extracted text: `temp/2402.10604.txt`
- Paper theorem inspected around Theorem 3 and its converse proof.
- Semantic Scholar search supplied the candidate; repository search confirmed no prior audit of arXiv:2402.10604.

## Disposition

The quasicrystal route does not supply a positive source measure. It supplies a sharp warning: even the global distributional completion of the signed prime and endpoint measures is RH-equivalent. Future positive-carrier proposals must remain width-regularized until they independently prove the global growth estimate; they may not assume a tempered unsmoothed Weil source.
