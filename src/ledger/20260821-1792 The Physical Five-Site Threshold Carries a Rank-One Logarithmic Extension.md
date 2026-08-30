# 1792 — The Physical Five-Site Threshold Carries a Rank-One Logarithmic Extension

## Question

Entry 1791 promotes the active \(g_5\) threshold to a genuine local divisor
\(\mathscr D_{g_5}\). What coefficient singularity and monodromy does the
physical period carry transverse to this divisor?

## Local normal form

Let \(\tau\) be a source-normalized local equation for
\(\mathscr D_{g_5}\). Entry 1783 supplies the first Leray residue, while Entry
1790 gives a positive-definite transverse Morse Hessian. Up to analytic units,
the remaining singular integral is

\[
I_{\rm sing}(\tau)
=
c\int
\frac{du\,dv}
{\tau+H_1u^2+H_2v^2},
\qquad H_1,H_2>0.
\]

Entry 1789 proves \(c\neq0\).

After the real linear change

\[
U=\sqrt{H_1}u,
\qquad
V=\sqrt{H_2}v,
\]

the radial integral gives

\[
\boxed{
I_{\rm sing}(\tau)
=
-\frac{\pi c}{\sqrt{H_1H_2}}\log\tau
+\text{holomorphic}.
}
\]

The coefficient is nonzero.

## Monodromy

Around a positive loop about \(\tau=0\),

\[
\log\tau\longmapsto\log\tau+2\pi i.
\]

The rank-one Morse vanishing line itself has semisimple eigenvalue \(+1\), as
appropriate for a two-variable \(A_1\) minimum. The complete local period
object is a nontrivial extension of a regular line by that invariant line.
Its monodromy is unipotent:

\[
T=\exp N,
\qquad
\boxed{
\operatorname{rank}N=1,
\qquad
N^2=0.
}
\]

## Result

\[
\boxed{
\mathscr D_{g_5}\text{ supports a nontrivial rank-one logarithmic
coefficient extension.}
}
\]

This distinguishes two layers that must not be conflated:

- the vanishing-cycle line has trivial semisimple monodromy;
- the physical period has nontrivial unipotent variation because the line is
  attached to the regular period sector by a logarithmic extension.

## Architectural classification

The divisor is produced by existing marked-wall incidence and routing
geometry. The logarithmic extension is integrated coefficient data. It does
not require a new carrier generator.

This is a five-site realization of the current H2 architecture:

\[
\text{shared carrier and nearby-cycle calculus}
+
\text{sector-specific nonsplit coefficient extension}.
\]

## Next falsifier

Compute intersections of \(\mathscr D_{g_5}\) with the existing total-energy,
soft, and one-wall divisors. Determine whether the logarithmic extension
specializes by the existing iterated nearby-cycle/Gysin maps or leaves a
supported excess class.

## Evidence

- research/benincasa/checkers/five_site_g5_picard_lefschetz.py
- research/benincasa/results/five-site-g5-picard-lefschetz.json
- Entries 1789–1791
- allocator claim: seqclaim-0c12c09c36b3a3f6b0e45bf1
