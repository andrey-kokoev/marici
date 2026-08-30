# Reciprocal Fourier Sewing Preserves the Corona Sign

## Independently constructed terminal states

Let

\[
f_0=1_{\mathbb Z_p}
\]

with self-dual Haar normalization, so

\[
\mathcal F_pf_0=f_0.
\]

On the direct residue tree, take \(r_k=p^{-k}\) and define

\[
c_k^+=(\tau_{r_k}-I)f_0.
\]

The previous completion calculation gives

\[
c_k^+\rightharpoonup-f_0.
\]

Construct the reciprocal tree independently in the Fourier chart. Its
terminal difference is

\[
c_k^-=(M_{\chi_{r_k}}-I)f_0.
\]

The local Fourier covariance relation gives

\[
\mathcal F_pc_k^+=c_k^-.
\]

Every fixed finite-conductor observable is orthogonal to
\(\chi_{r_k}\) for sufficiently large \(k\), and therefore

\[
c_k^-\rightharpoonup-f_0.
\]

Transporting back to the common self-dual frame preserves this limit:

\[
\mathcal F_p^{-1}(-f_0)=-f_0.
\]

Thus the two independently constructed corona states agree with the same
sign.

## No analytic sign cancellation

In the common boundary frame,

\[
c_\infty^+=c_\infty^-=-f_0.
\]

Consequently,

\[
c_\infty^++c_\infty^-=-2f_0,
\qquad
c_\infty^+-c_\infty^-=0.
\]

Fourier--Tate sewing supplies the equality. It does not choose the alternating
combination. Any cancellation therefore comes from an independently typed
relative incidence, not from Fourier transform or self-duality alone.

## Location of the missing sign

For a two-chart relative object, the canonical candidate is a Čech or
mapping-cone boundary map

\[
\delta(a,b)=a-\mathcal F_p^{-1}b.
\]

This map kills the diagonal common mode because its two incidence legs carry
opposite orientation. But using \(\delta\) is legitimate only after the
direct chart, reciprocal chart, their overlap, and both restriction maps have
been derived from the source.

Declaring subtraction merely because the corona states agree would be a
fitted repair. Conversely, adding the two Green identities before applying
the relative incidence doubles the terminal defect.

## Consequence for the horizontal Green identity

The archimedean additive incidence produces the correct
\(2\operatorname{Re}z\) coefficient. The local residue-tree completion
produces a nonzero common corona. Reciprocal Fourier sewing identifies the two
coronas but does not orient their cancellation.

The remaining theorem is therefore categorical and dynamic:

1. construct the two reciprocal Green complexes and their overlap;
2. derive the alternating boundary incidence from that cover;
3. prove that the forcing pairings map to the diagonal corona state;
4. show that the relative energy adds while the relative boundary flux
   subtracts;
5. pass this identity through restricted-product completion.

The third and fourth steps cannot be inferred from corona equality.

## Falsifier

Any proposed analytic cancellation that uses only
\(\mathcal F_pf_0=f_0\) has the wrong sign: the two corona limits add to
\(-2f_0\). Any proposed relative cancellation must exhibit the two
source-derived incidence maps before forming their difference. If changing
one incidence orientation leaves all declared source data unchanged, the
relative sign is unselected.
