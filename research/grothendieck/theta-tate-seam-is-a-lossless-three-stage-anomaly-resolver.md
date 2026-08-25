# The Tate seam is a lossless three-stage anomaly resolver

## Operator stimulus

The operator and Nima proposed reading the two local valuation cones as typed
variants joined by a lossless bidirectional resolver.  The important demand
was exact reconstruction: the non-normalizable residuals must remain explicit
fields of the resolved object rather than being discarded as errors.

This packet tests the weakest mathematical content of that analogy.

## Resolved local object

At a prime `p`, the two valuation charts are related by the source-derived
transition

\[
 \gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}}.
\]

On `Re(s)=1/2`, this transition is unitary.  Its connected logarithm admits
the canonical filtration

\[
 \log\gamma_p=C_{1,p}+C_{2,p}+C_{\ge3,p},
\]

where

\[
 C_{1,p}=2ip^{-1/2}\sin(t\log p),
 \qquad
 C_{2,p}=ip^{-1}\sin(2t\log p),
\]

and

\[
 C_{\ge3,p}
 =2i\sum_{k\ge3}\frac{p^{-k/2}\sin(kt\log p)}{k}.
\]

The corresponding resolved datum is not the regularized scalar alone.  It is
the typed triple

\[
 \boxed{\mathcal R_p=(C_{1,p},C_{2,p},\gamma_p^{[3]})}
\]

with reconstruction map

\[
 \operatorname{reassemble}(\mathcal R_p)
 =e^{C_{1,p}+C_{2,p}}\gamma_p^{[3]}
 =\gamma_p.
\]

This is an exact finite-prime identity, not an asymptotic equivalence.

## Global typing

After taking the prime direct sum/product, the three fields occupy distinct
summability strata:

\[
 C_1\in\bigcap_{q>2}\ell^q\setminus\ell^2,
 \qquad
 C_2\in\ell^2\setminus\ell^1,
 \qquad
 C_{\ge3}\in\ell^1,
\]

generically in the spectral parameter.  Therefore no single ordinary Hilbert
or trace-class value type contains the complete global seam.

The source instead presents a three-stage relative object:

\[
 \text{distributional boundary current}
 \longrightarrow
 \text{Hilbert determinant anomaly}
 \longrightarrow
 \text{trace-class determinant value}.
\]

Here “anomaly” means a precisely retained obstruction to descending to the
next stricter summability class. It does not mean an inconsistency, and it is
not permission to quotient the obstruction away.

## Completion as a candidate anomaly inflow

The arithmetic half alone supplies the obstruction fields but not a canonical
global scalar.  The completed zeta source also has an archimedean endpoint and
reciprocal modular sewing.  The resulting hard-to-vary conjecture is:

\[
 \boxed{
 \text{archimedean/modular completion is the boundary morphism that absorbs
 }C_1\text{ and }C_2\text{ while preserving finite-cutoff reconstruction}.}
\]

If true, completion is not a factor appended to repair convergence. It is the
second half of a relative determinant object whose arithmetic component is
not independently scalar-valued.

This also identifies what completion cannot yet explain. Anomaly cancellation
would construct the global determinant line and protect its divisor under
authorized presentation changes. It would not by itself orient that divisor
onto the critical line. RH would still require an off-seam coercivity or
transversality theorem for the completed resolver.

## Decisive calculation and falsifier

Derive the archimedean logarithmic countercurrents directly from the completed
theta/Mellin source, before using zeta continuation, and compare them with
finite prime cutoffs:

\[
 \sum_{p\le X}C_{1,p},\qquad \sum_{p\le X}C_{2,p}.
\]

The proposal fails if either:

1. the archimedean seam has no independently derived maps into both residual
   types;
2. cancellation requires a divisor-dependent or zero-aware choice;
3. reassembly differs from the original completed finite-cutoff readout by a
   non-unit scalar or an uncontrolled phase;
4. the resulting transition depends on a noncanonical cutoff path.

The first calculation should therefore be a boundary-term audit of the
completed Mellin transform, not another finite zero or positivity census.

