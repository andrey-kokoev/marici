# Finite multibin quantum bath dilation

Owner: `marici.Aspect`

Strength: finite-cutoff theorem.

## Bounded question

Can the one-frequency-bin loss dilation be composed across labelled frequency
bins, and can a single shared bath replace the orthogonal bin baths while
preserving the same scalar attenuation data?

## Source, ports, and constructor order

The source consists of three labelled system frequency modes and three
orthogonal bath modes. The frame fixes the bin ordering before any matrix is
formed. The typed ports are three system inputs, three bath inputs, and their
corresponding outputs. Constructor order is frequency-bin declaration,
system-bath mixing within each bin, frequency-resolved detection, then bath
trace. No continuum identification is made before this finite constructor.

Let \(T=\operatorname{diag}(3/5,5/13,8/17)\) and
\(L=\operatorname{diag}(4/5,12/13,15/17)\). Exact passivity gives

\[
TT^{\mathsf T}+LL^{\mathsf T}=I_3.
\]

Therefore all three output commutators are conserved and distinct bins remain
canonically independent. System photon number is dissipated into the bath;
total number is conserved by the underlying direct sum of two-port unitaries.

## Shared-bath hostile

Replacing \(L\) by the single column
\((4/5,12/13,15/17)^{\mathsf T}\) preserves every diagonal norm. A scalar
attenuation audit therefore passes in all three bins. But the off-diagonal
entries of \(L L^{\mathsf T}\) are nonzero, so distinct output bins acquire
forbidden cross-commutators. One shared bath is not a valid diagonal,
frequency-preserving quantum completion.

This eliminates the shared-bath branch only under the declared diagonal
system transfer. Correlated baths remain admissible when paired with the
matching non-diagonal system scattering; that is a different constructor.

## Detector and noise

The detector is frequency resolved and observes only the system outputs. A
vacuum bath contributes no mean counts but remains necessary for commutator
preservation. A diagonal thermal bath contributes the positive matrix
\(L\operatorname{diag}(n_j)L^{\mathsf T}\); the exact checker uses occupations
\(0,1/2,2\) and records distinct nonnegative added-noise values.

## Completion gate

Three bins establish neither a continuum nor a causal material spectral
density. Completion requires a declared refinement sequence, convergence of
the transfer and noise kernels, preservation of the canonical commutator in
the limit, Kramers-Kronig compatibility, and a source-derived
fluctuation-dissipation law. The present packet supplies no material-specific
microscopic authority.

Run:

```powershell
python research/aspect/checkers/finite_multibin_quantum_bath_dilation.py
```
