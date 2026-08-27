# The native equalizer law is a conditional off-seam contraction

Scope correction: the rational parameter \(z\) below is the real normal
coordinate \(\operatorname{Re}(s)\), not the full complex spectral parameter.
On the full plane, the reciprocal sector is typed by
\(1-\overline{s}\), so the difference is
\(2\operatorname{Re}(s)-1\).

## The law, not the observer

Let one labelled state \((G,r_1,\ldots,r_N)\) be presented to both reciprocal
sector dynamics in a common source frame:

\[
(P+z)G+\sum_j b_jr_j=0,
\qquad
(P+\lambda_j)r_j=0,
\]

and

\[
(P+1-z)G+\sum_j b_jr_j=0,
\qquad
(P+\lambda_j)r_j=0.
\]

The seam law is the equalizer requiring both presentations to describe the
same labelled boundary state with the same incidence coefficients \(b_j\).

## Conditional contraction theorem

Subtracting the two tail equations gives

\[
(2z-1)G=0.
\]

If \(z\ne1/2\), then \(G=0\).  The remaining equation is

\[
\sum_jb_jr_j=0.
\]

Writing \(r_j=c_je^{-\lambda_jq}\), distinct rates and nonzero incidences imply
\(c_j=0\) for every \(j\).  Therefore the native equalizer is trivial off the
critical seam.

At \(z=1/2\), the two equations coincide.  For one mode with
\(\lambda\ne1/2\), the nonzero state

\[
r(q)=ce^{-\lambda q},
\qquad
G(q)=-\frac{bc}{1/2-\lambda}e^{-\lambda q}
\]

lies in the equalizer.  Thus the law contracts the normal direction without
erasing tangential seam states.

## Why the theorem remains conditional

The proof depends entirely on common-frame authority.  The actual
Fourier--Tate comparison must derive that the two sector presentations have:

- the same labelled reservoir coordinates;
- the same incidence coefficients;
- the same endpoint and completion domain;
- no hidden parameter-dependent re-normalization.

Without that law, an off-seam state can be manufactured by changing the
reciprocal incidence.  For one mode, direct and reciprocal solutions agree if

\[
b_- = b_+\frac{1-z-\lambda}{z-\lambda}.
\]

This is precisely the fitted parallelization that source typing must reject.
Reciprocal symmetry alone does not reject it.

## DPC verdict

There is now a clean conditional zero-confinement mechanism requiring neither
positivity nor division by the completed scalar section:

1. retain the labelled source reservoir;
2. derive a common-frame equalizer law from the source;
3. subtract the reciprocal first-order dynamics;
4. use labelled exponential independence to eliminate the common kernel.

The unresolved RH-bearing statement has narrowed to one source question:
whether Fourier--Tate normalization really supplies this native equalizer law,
rather than a nontrivial comparison transform between the two state carriers.

The finite falsifier is a single off-seam mode admitted by the actual
source-derived comparison.  If its reciprocal incidence differs by the ratio
above, or any source-authorized analogue admits a nonzero equalizer state, the
conditional route fails.

## Verification

`check_rh_native_equalizer_law.py` verifies exact off-seam triviality for
several labelled packets, constructs a nonzero seam state, and constructs the
one-mode fitted-frame hostile off the seam.
