# Contractible-kernel comparison: positive certificate

## Question

Can a positive equivalence certificate use exact fibre models and their contractions without requiring a scalar-linear ambient chain splitting?

## Claim boundary

`agda/ContractibleKernelComparison.agda` proves that a map whose every fibre is a retract of a supplied contractible type has contractible fibres. Its `KernelFibreCertificate` records the model, contraction, encoding, decoding, and retraction equation for every target point. Thus it does not infer surjectivity from a trivial kernel. `AdmissibleKernelComparison` separately retains the forward map's caller-supplied admissibility proof; no admissibility predicate on a chain-level inverse or ambient splitting is required.

Positive regression: identity on the two-point marking type has this certificate, without selecting one boundary. Negative regression: the previously exhibited split readout cannot have such a certificate. Neither theorem has holes or postulates.

This is the derived-mapping-space core, NOT a formal construction of derived A-modules, homology, or the polynomial node comparison. Raw chain-module kernels cannot be substituted for these fibre models. A future source instantiation must construct the derived map, establish the fibre model from the exact sequence with kernel [J -> J], and justify that its chosen derived probes detect equivalences. Merely declaring a predicate named A-linearity supplies none of those facts.

For the supplied branch comparison, distinguish three operations: (1) the A-linear forward comparison and A-linear contraction of its kernel; (2) the resulting inverse in the derived A-category; (3) a representative ambient R-linear splitting and homotopy. The third is optional computational data, not an A-linear chain section demanded by this certificate. Conversely, existence of an R-linear section alone supplies neither exact fibre models nor an A-linear derived equivalence. No formal theorem identifying the source map with this abstract certificate is claimed.

## Disposition

Targeted Agda 2.8.0.1/Cubical 0.9 check passed, exit 0, without warnings, retaining `--safe --cubical --guardedness`:

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ContractibleKernelComparison.agda"
```

The initial check found product notation unavailable from Prelude; using its explicit Sigma form repaired the scope error, and the rerun passed. Shell fallback was explicitly authorized for Agda. No aggregate rebuild or dependency installation. No analytic interface changed. New owned paths are the module and this packet; no Git operations, commit, or push.

Do not elaborate another generic certificate layer in lieu of the missing source instantiation. The next positive mathematical work requires an actual complex/exact-sequence model and scalar-action interpretation, not stronger names for these parameters.
