# Relative-trace Plancherel positivity is a new model but not a zeta Weil factorization

## New aperture

The indexed PDFs contain a positive mechanism not previously discussed in the RH packets: Sakellaridis' relative-trace transfer operators.

In the baby case the local transfer is explicitly

\[
\mathcal G=\mathcal F\circ\iota\circ\mathcal F,
\]

with multiplicative actions normalized to be unitary on \(L^2\). In the relative trace comparison, local relative characters match because the transfer operators preserve \(L^2\) inner products. Global equality is then proved by a Poisson summation theorem on nonstandard Schwartz spaces, with endpoint/irregular distributions retained during continuation.

This has the formal shape sought in the current programme:

1. source-defined local Schwartz spaces and basic vectors;
2. explicit Fourier/birational transfer;
3. local \(L^2\)-isometry before scalar compression;
4. global Poisson sewing;
5. endpoint terms arising from irregular orbits.

It is therefore a useful model for a noncircular form-preserving map.

## Why it does not yet solve the zeta problem

The cited baby case concerns

\[
X=\operatorname{Res}_{E/k}\mathbb G_a,
\qquad
T=U(1),
\qquad
X/T,
\]

and the main comparison concerns torus and Kuznetsov relative trace formulas for \(PGL_2\), producing degree-two period \(L\)-functions. It is not the \(GL_1\) Riemann explicit formula and does not identify its positive \(L^2\) pairing with the completed Weil functional.

Moreover, the global spectral decomposition in the split/regularized setting is described by finite signed measures plus irregular evaluations. Local preservation of \(L^2\) inner products does not make the completed global relative trace positive after analytic continuation.

The exact missing specialization would have to prove all of:

- an orbital-integral space whose global Poisson sum is the Riemann endpoint--gamma--prime formula;
- an explicit transfer preserving one positive \(L^2\) pairing;
- identification of the transferred pairing, not merely its scalar trace, with
  \[
  W(f*g^*);
  \]
- positivity surviving the rational-boundary/irregular-orbit subtraction;
- density and cutoff compatibility on the Gaussian composite closure.

No such specialization was found in prior research or the web search.

## Comparison with Burnol and Connes--Consani

Burnol supplies positive finite-place cuspidal conductor spectra and unconditional short-support Weil positivity. Connes--Consani supply unconditional archimedean/windowed form results and semilocal scaling quotients. Existing audits show that neither construction controls the global cross-window interaction kernel.

Sakellaridis supplies precisely the missing *kind* of map—an explicit \(L^2\)-preserving transfer compatible with Poisson sewing—but for a different trace formula. Transporting that architecture to the \(GL_1\) zeta quotient is a genuine new research question, not an available theorem.

## Sharp candidate theorem

Seek a zeta-semiloal transfer

\[
\mathcal G_\zeta:
\mathcal S_{\mathrm{arith}}
\longrightarrow
L^2(\mathcal X)
\]

constructed from Fourier transform, inversion, and the rational diagonal, such that

\[
W(f*g^*)
=
\langle\mathcal G_\zeta f,\mathcal G_\zeta g\rangle
\]

before any zero-side spectral expansion.

The first falsifier is Burnol's off-diagonal prime resolvent: if the proposed transfer sends every prime displacement to an independent positive diagonal channel, it cannot reproduce the oscillating cut density. The transfer must retain source/readout polarization or irregular-boundary coupling.

## Search evidence

- `pnpm pdf:search 'relative trace formula'`
- `pnpm pdf:search 'Poisson summation'`
- `pnpm pdf:search 'Plancherel formula'`
- Sakellaridis, *Beyond Endoscopy for the Relative Trace Formula II*, especially pp. 7, 11, 15, 21, 41, and the global spectral decomposition.
- Fresh OpenAlex searches for Connes--Consani, Burnol, Poitou--Odlyzko, and co-Poisson constructions found no published zeta specialization with the required positive identity.

## Disposition

Relative-trace transfer is the first newly located external architecture that obtains local positive pairing preservation and global Poisson compatibility from one explicit transform. It expands the constructor vocabulary, but currently remains a model: its zeta/Weil specialization and positivity through irregular completion are unconstructed.
