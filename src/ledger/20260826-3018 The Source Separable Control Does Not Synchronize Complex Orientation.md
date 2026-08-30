# 3018 — The Source Separable Control Does Not Synchronize Complex Orientation

**Status:** source-derived hostile control  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-c15f26ecbb1d83ab20755f5b`

## Scope

Entry 3017 certifies relative-orientation sewing for the source’s physical NPT estimate. This entry tests whether the same conclusion is merely an artifact of the tomography and positivity machinery by applying it to a separable family proposed in the same source programme.

## Frozen control family

White et al. identify mixed polarization states of the form

\[
\rho_\gamma
=
\frac{|HH\rangle\langle HH|
+\gamma|VV\rangle\langle VV|}{1+\gamma},
\qquad
\gamma\ge0,
\]

as a source-accessible target under depolarization. This is a classical mixture of two labelled product states.

## Exact audit

The matrix is diagonal in the linear polarization basis, so

\[
\rho_\gamma^{T_2}=\rho_\gamma\ge0.
\]

Its only nonzero two-port Pauli correlation among the Cartesian axes is

\[
ZZ=1.
\]

In particular,

\[
XX=YY=0.
\]

Aspect’s handedness witness gives

\[
W_\gamma
=
\frac{1-XX+YY-ZZ}{4}
=0.
\]

Reversing \(Y\) on either port changes no state coefficient or predicted count. Positivity therefore supplies no relative-orientation selection on this family.

## Reconstruction control

The same sixteen-setting local tomography frame remains informationally complete once its analyzers are calibrated. It can reconstruct \(\rho_\gamma\) uniquely in either synchronized convention. What fails is not tomography but the source-internal criterion selecting the relative \(C_2\) orientation between independently calibrated components.

Thus

\[
\text{complete local readout}
\not\Rightarrow
\text{relative handedness selection}.
\]

The NPT support in Entry 3017 supplies the additional relation.

## Narrow conclusion

The paired source tests isolate causation cleanly:

- NPT entangled estimate: relative orientation is synchronized;
- separable diagonal control: relative orientation remains ambiguous.

Therefore the synchronization in Entry 3017 is carried by entangled positivity support, not by the maximum-likelihood algorithm, the Pauli basis, or the mere availability of circular analyzers.

## Cross-sector consequence

This is the optical counterpart of the distinction between alignment and orientation in Flavor. A complete bilinear or tomographic comparison may align the available coordinates while leaving reflection unresolved. A source-distinct relational witness is still required.

## Next falsifier

Move continuously from the NPT source family toward the separable control under a declared depolarizing channel and locate the exact support boundary where the orientation selector vanishes. The channel must be source-derived before its threshold is interpreted physically.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-c15f26ecbb1d83ab20755f5b`, value 3018.
- Primary provenance: arXiv:quant-ph/9908081, proposed depolarized mixed family.
- Exact control: \(\rho_\gamma^{T_2}=\rho_\gamma\), \(W_\gamma=0\).
- Epistemic-graph admission: `ev-000000005815-4f329409-992a-470c-9ba9-df44d8b72778`.
