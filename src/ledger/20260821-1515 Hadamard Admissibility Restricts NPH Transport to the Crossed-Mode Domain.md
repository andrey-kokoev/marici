# 1515 — Hadamard Admissibility Restricts NPH Transport to the Crossed-Mode Domain

## Status

Primary-source admissibility correction to the broad bilocal envelope of Entries 1508–1513.

## Frozen admissibility condition

Agarwal, Holman, Tolley, and Lin allow general nonlocal initial-state kernels, but do not treat every such kernel as physically admissible. They impose the Hadamard condition, requiring the Bogoliubov coefficient to fall faster than

\[
k^{-2}
\]

at large \(k\). Their explicit implementation is

\[
\boxed{
\beta_k\longrightarrow0
\qquad
\text{for }
k>\frac{a_0\Lambda_*}{c_s}.
}
\]

Here \(\Lambda_*\) is the physical cutoff and \(a_0=a(\eta_0)\). Modes above the common-slice cutoff begin in the vacuum state.

The state must additionally satisfy backreaction and tadpole bounds; Hadamard falloff is necessary but not sufficient.

## Consequence for NPH transport

In exact de Sitter NPH, the excitation coefficient can be independent of \(k\) because each mode is initialized separately at

\[
\frac{k}{a(\eta_k)}=\Lambda_*.
\]

Transporting this constant excitation to a common slice \(a_0\) for arbitrarily large \(k\) would violate Hadamard falloff. The physically typed common-slice packet must distinguish:

\[
\mathcal K_{\rm crossed}(a_0)
=
\left\{
k:
\frac{k}{a_0}\le\frac{\Lambda_*}{c_s}
\right\}
\]

from modes that have not yet entered the effective description.

On the crossed domain, Riccati/Möbius propagation is canonical. Extending the state to the full momentum axis requires an ultraviolet completion rule, such as:

\[
b_{a_0}(k)
=
b_{\rm NPH}(k)\,
\chi\!\left(\frac{c_sk}{a_0\Lambda_*}\right),
\]

where \(\chi\) decays sufficiently rapidly and is zero in the source's sharp implementation above the cutoff.

## Corrected typing

\[
\boxed{
\text{canonical mode transport}
\quad\text{is canonical on its admitted momentum domain,}
}
\]

but

\[
\boxed{
\text{global common-slice state}
=
\text{transported crossed modes}
+
\text{an admissible UV completion}.
}
\]

The completion is coefficient data. It is not supplied by propagation alone.

This qualifies Entry 1508: “one can always evolve/devolve” is valid modewise and for a finite admitted band; it does not canonically extend a constant NPH excitation to unbounded common-slice momentum.

## Support classification

The threshold

\[
k=\frac{a_0\Lambda_*}{c_s}
\]

is the fixed-time intersection of the existing mode–scale incidence carrier

\[
\frac{c_sk}{a(\eta)}=\Lambda_*.
\]

It is not a new cosmological carrier primitive.

However, the cutoff profile and Hadamard falloff define a genuine support/filtration condition on the coefficient object. A sharp profile creates a coefficient discontinuity; a smooth profile adds regulator data. Neither may be silently fitted.

## Architectural update

The source-supported Gaussian object is now:

\[
\boxed{
\text{Hadamard-filtered doubled bilocal kernels on an admitted momentum domain}.
}
\]

It carries:

- deck/Hermiticity structure;
- projective Riccati charts;
- Wilsonian and adiabatic filtrations;
- ultraviolet support/falloff data;
- backreaction and tadpole admissibility inequalities.

The Carrier determines where modes meet the cutoff. The coefficient object determines how the state is completed across that incidence.

## Next finite falsifier

Test whether the one-loop map of Entry 1513 preserves Hadamard admissibility:

1. insert a general \(\beta_k=O(k^{-2-\delta})\);
2. derive the large-\(k\) behavior of generated \(A_k,B_k\);
3. separate vacuum counterterms from state-dependent tails;
4. verify whether the renormalized output again defines a Hadamard state without a newly fitted cutoff profile.

Failure would require a stronger interacting admissibility category, not a new carrier stratum.

## Provenance

- N. Agarwal, R. Holman, A. J. Tolley, and J. Lin, *Effective field theory and non-Gaussianity from general inflationary states*, arXiv:1212.1172, Sec. 4, especially the Hadamard discussion preceding Sec. 4.1.
- Ledger sequence claim: seqclaim-ce61f39d450b55c6c844b451.
- Epistemic graph event: ev-000000001647-b182c210-45dc-46a8-990e-583d1890bae0.
