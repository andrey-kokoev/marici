# Interval-window Fourier-moment gate

## Question

Can optical windowing provide a source-typed interval partition with a computable first absolute Fourier moment for the logarithmic-multiplier commutator bound?

## Computable sufficient datum

Use the periodic normalization

\[
\widehat\chi_k=\frac1{2\pi}\int_0^{2\pi}\chi(x)e^{-ikx}\,dx.
\]

For a periodic \(C^3\) window, three integrations by parts give

\[
|\widehat\chi_k|
\le
\frac{\|\chi'''\|_{L^1}}{2\pi |k|^3},
\qquad k\ne0.
\]

Therefore

\[
\sum_{k\in\mathbb Z}|k|\,|\widehat\chi_k|
\le
\frac{\pi}{6}\|\chi'''\|_{L^1}.
\]

A materialized interval partition \(\{\chi_j\}\) with recorded third-derivative norms would thus provide the requested constants. For windows obtained by rescaling a fixed profile to overlap width \(h_j\), the bound scales as \(h_j^{-2}\); narrow localization has a quantified leakage cost.

## Exact raised-cosine fixture

The complementary windows

\[
\chi_1(x)=\frac{1+\cos x}{2},
\qquad
\chi_2(x)=\frac{1-\cos x}{2}
\]

are nonnegative and sum to one. Each has first absolute Fourier moment \(1/2\), so the summed Schur leakage bound is one.

They are not subordinate to proper intervals: each is nonzero on every open arc except isolated zeros. They provide an exact coherence fixture, not the missing interval partition.

## Localization obstruction

No nonzero trigonometric polynomial can be supported in a proper interval. Such a function is real analytic, and vanishing on the complementary open arc forces it to vanish everywhere. Hence an exact finite-mode optical window cannot simultaneously be a nonzero proper-interval cutoff.

A sharp interval indicator has Fourier coefficients of order \(1/|k|\), so its first absolute Fourier moment diverges. This rejects sharp windowing for the stated Schur certificate. Smooth proper-interval windows can pass, but their actual overlap widths and derivative norms must be sourced.

## Disposition

Optical windowing supplies a computable acceptance test, not the absent partition itself. Required source fields are the periodic chart, interval cover, overlap widths, explicit \(C^3\) windows summing to one, and their \(L^1\) third-derivative bounds. Without those objects, neither the principal constant nor the commutator theorem determines a leakage constant. The finite-mode and sharp-cut alternatives are exact mismatches for opposite reasons: finite modes cannot have proper interval support, while sharp cuts fail the first-moment certificate.
