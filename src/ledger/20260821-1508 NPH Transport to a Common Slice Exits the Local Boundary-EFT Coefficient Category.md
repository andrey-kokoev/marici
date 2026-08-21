# 1508 — NPH Transport to a Common Slice Exits the Local Boundary-EFT Coefficient Category

## Status

Primary-source refinement of Entries 1504 and 1506.

**Qualification from Entry 1515.** The transport below is canonical modewise and on a finite admitted momentum band. A global common-slice state on unbounded momentum additionally requires Hadamard ultraviolet completion; propagation alone does not canonically supply it.

## Canonical transport exists

Greene, Schalm, van der Schaar, and Shiu emphasize that a new-physics-hypersurface state can always be evolved or devolved to one chosen time \(t_0\). Thus the fixed-scale and fixed-time presentations are not separated by an absence of propagation.

For a mode basis \(u_k,u_k^*\), write

\[
v_k=N(k)\bigl(u_k+b(k)u_k^*\bigr).
\]

On the common slice, the quadratic boundary kernel \(\kappa(k)\) imposes

\[
\partial_n\phi|_{t_0}=-\kappa(k)\phi(t_0).
\]

The source relation [astro-ph/0503458, Eq. (8)] is

\[
b(k)
=
-
\frac{
\kappa(k)u_k(t_0)+\partial_n u_k|_{t_0}
}{
\kappa(k)u_k^*(t_0)+\partial_n u_k^*|_{t_0}
}.
\]

Whenever the denominator is nonzero, this can be inverted:

\[
\boxed{
\kappa(k)
=
-
\frac{
\partial_n u_k+b(k)\partial_n u_k^*
}{
u_k+b(k)u_k^*
}\bigg|_{t_0}.
}
\]

This is a source-derived transport map from Bogoliubov data to a common-slice boundary kernel.

## Where equivalence fails

Local boundary EFT restricts \(\kappa(k)\) to a derivative expansion. Its leading irrelevant correction is [Eq. (6)]

\[
\kappa_{\rm BEFT}(k)
\simeq
\kappa_{\rm BD}
+
\beta\frac{k^2}{a_0^2M}
+\cdots.
\]

By contrast, the NPH coefficient contains the finite-scale phase [Eq. (4)]

\[
b_{\rm NPH}(k)
\sim
\widetilde\beta\,
\frac{H(k)}{2iM}
\exp\!\left[-\frac{2iM}{H(k)}\right].
\]

Substitution into the exact transport formula produces a well-defined common-slice kernel, but generically not a finite regular polynomial in \(k^2/(a_0^2M^2)\). Even in de Sitter space, the common-slice mode functions contribute finite-time oscillatory \(k\)-dependence. In slow roll, the additional phase \(M/H(k)\) strengthens the non-polynomial dependence.

Therefore:

\[
\boxed{
\text{NPH state}
\xrightarrow{\text{canonical evolution}}
\text{common-slice kernel}
\notin
\text{generic finite local boundary-EFT coefficients}.
}
\]

The source states this distinction directly: NPH does not conflict with boundary EFT *per se*, but it does not conform to generic boundary-EFT predictions because it imposes specially near-scale-invariant initial data.

## Type classification

The correct comparison has three layers:

1. **Carrier/propagation:** common and canonical at the free mode level.
2. **General coefficient object:** the full momentum-dependent quadratic boundary kernel \(\kappa(k)\).
3. **Local EFT subobject:** kernels admitting the prescribed derivative expansion.

NPH and BEFT meet in layer 2, not generically in layer 3.

This sharpens H2:

\[
\text{shared carrier and evolution calculus}
+
\text{different admissible coefficient subcategories}.
\]

The failure is not evidence for a new cosmological carrier stratum.

## Hard-to-vary conjecture

The natural common coefficient envelope of finite-time and fixed-scale Gaussian initial states is the sheaf of momentum-dependent boundary kernels obtained by Riccati/Möbius transport. Local boundary EFT and NPH are distinct subobjects selected respectively by derivative locality and near-scale-invariant finite-scale phase data.

## Finite falsifier

Expand the transported \(\kappa_{\rm NPH}(k;t_0)\) in the frozen local boundary operator basis and test whether it closes:

- at every finite derivative order;
- as a convergent or controlled asymptotic completion;
- without fitted nonlocal kernels or additional singular support.

Finite-order failure is expected and already visible in the incompatible spectral dependence. Controlled all-order closure remains open.

## Provenance

- B. Greene, K. Schalm, J. P. van der Schaar, and G. Shiu, *Extracting New Physics from the CMB*, arXiv:astro-ph/0503458, especially Eqs. (1), (4)–(10).
- Ledger sequence claim: seqclaim-748fca4f8d126a29e22882aa.
- Epistemic graph event: ev-000000001635-26a184b9-acbb-41a3-982c-0c94d071444f.
