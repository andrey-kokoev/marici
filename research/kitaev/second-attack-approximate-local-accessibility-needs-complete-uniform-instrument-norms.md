# Second attack: approximate local accessibility needs complete, uniform, instrument norms

**Owner:** marici.Kitaev  
**Status:** hostile audit and quantitative repair  
**Target:** the approximate extension of the local-accessibility theorem

## 1. Exact theorem survives

Let \(\Phi_L\) be the logical-to-output channel induced by the compiler.

If for every output observable \(O\),

\[
V^*\Phi_L^*(O)V=c(O)I_L,
\]

then \(\Phi_L\) is constant on logical inputs.

No exact counterexample exists without violating the pullback-to-correctable-algebra premise.

The vulnerable step is the proposed approximate extension.

## 2. Pointwise convergence is insufficient

Suppose that for every fixed probe sequence chosen independently of system size,

\[
V_L^*\Phi_L^*(O)V_L
\]

approaches a scalar.

This does not imply that the supremum over all allowed probes approaches zero.

A moving hostile \(O_L\) may track the escaping logical direction at each size:

\[
orall O	ext{ fixed},quad epsilon_L(O)\to0,
\]

while

\[
sup_{|O_L|le1}epsilon_L(O_L)
\not	o0.
\]

Therefore completion stability requires a uniform operator-norm or operational-norm bound, not pointwise convergence on a dense probe list.

This is the same escape mechanism seen in pro-Gram completion and observability constants.

## 3. Marginal channel norm is not context-complete

Let \(\Delta_L=\Phi_L-\mathcal C_L\), where \(\mathcal C_L\) is a constant channel.

Small induced trace norm

\[
|Delta_L|_{1\to1}
\]

controls unassisted logical inputs.

It does not, in a dimension-uniform way, control

\[
|Delta_L\|_\diamond,
\]

which allows an entangled reference system.

In finite dimension one generally pays an input-dimension factor when passing from induced norm to diamond norm. If logical dimension grows, an induced error can vanish while the dimension-amplified complete error does not.

Thus coherent logical localization and arbitrary contextual faithfulness require a completely bounded or diamond-norm certificate.

A marginal-output certificate is sufficient only for the explicitly weaker task of unassisted state discrimination.

## 4. Instrument erasure hostile

An adaptive or postselected compiler is an instrument

\[
\{\Phi_m\}_m,
\qquad
\sum_m\Phi_m=Phi.
\]

The averaged channel \(\Phi\) may be constant on logical inputs while the classical outcome \(m\), or the conditional state in one branch, carries logical information.

Discarding the outcome register erases the very behavior that distinguishes the instrument.

Therefore the output behavior must include:

- branch probabilities;
- the classical outcome register;
- conditional output states;
- success and failure flags;
- feed-forward dependencies.

Channel-level constancy does not imply instrument-level constancy.

## 5. Postselection and success probability

Let a successful branch have subnormalized map \(S_L\) and success probability

\[
p_L(\rho)=\operatorname{tr}S_L(\rho).
\]

Normalization divides by \(p_L(\rho)\). Small subnormalized differences can become order-one conditional differences when success probability vanishes.

A uniform approximate obstruction must require

\[
p_L(\rho)\ge p_0>0
\]

for every admitted logical input, or report the success-probability cost explicitly.

Rare-event localization is not uniform compilation.

## 6. Subsystem-code typing

For a subsystem code, correctable local observables need not compress to scalars on the whole code space. They can act on a gauge subsystem:

\[
V^*OV=I_L\otimes O_G.
\]

The conclusion “logical output is constant” follows only after:

- fixing or quantifying over the gauge input;
- requiring no logical–gauge correlation imports information;
- typing the output claim as logical, not gauge, accessibility.

A scalar compression test applied to a subsystem code is unnecessarily strong and may misclassify valid gauge behavior.

## 7. Uniform quantitative theorem candidate

Let \(\mathcal A_{C,L}\) be the complete backward causal algebra of the output instrument.

Require a matrix-level correctability bound \(\varepsilon_L\) for that algebra and a completely bounded causal-tail approximation \(\delta_L\).

Then the logical output instrument should be close, in the corresponding diamond or strategy norm, to one that factors through no logical information, with a bound of the form

\[
operatorname{dist}_{\mathrm{context}}
\le
C(\varepsilon_L+\delta_L),
\]

where \(C\) is independent of system size, logical dimension, ancillary dimension, and branch count.

For postselected outputs, the conditional bound must also include the uniform success floor.

The exact norm and constant remain to be derived for each process type.

## 8. Process-type hierarchy

The required norm follows the claimed behavior:

- states: trace norm;
- channels without references: induced trace norm;
- channels under arbitrary ancillas: diamond norm;
- instruments: diamond norm on the classical–quantum output;
- multi-round strategies: strategy or comb norm;
- reusable devices: behavioral metric over sequential contexts;
- completions: uniform bound in the completed process norm.

Using a lower-level norm for a higher-level claim is a typing error.

## 9. Decisive hostile suite

1. **Moving probe:** each fixed probe vanishes, but the maximizing probe depends on \(L\).
2. **Ancilla activation:** induced norm vanishes while complete norm remains bounded away from zero.
3. **Outcome erasure:** averaged channel is constant but instrument outcomes reveal the logical state.
4. **Rare branch:** conditional distinguishability is large with vanishing success probability.
5. **Gauge leakage:** output depends on gauge and is misreported as logical information.
6. **Branch proliferation:** each branch error is small but the total instrument error accumulates.
7. **Comb activation:** one-round diamond distance vanishes but a multi-round strategy separates the devices.
8. **Completion escape:** every finite process norm is controlled while the uniform constant diverges.

## 10. SCC correction

The certificate must state:

```json
{
  "claim_process_type": "state | channel | instrument | comb | reusable",
  "comparison_norm": "...",
  "complete_ancilla_stability": "proved | failed | open",
  "uniform_over_system_size": "true | false",
  "moving_probe_supremum": "...",
  "classical_outcome_retained": "true | false",
  "success_probability_floor": "...",
  "gauge_subsystem_treatment": "...",
  "causal_tail_bound": "...",
  "contextual_error_bound": "..."
}
```

## 11. Present conclusion

The exact causal-algebra theorem is stable.

The naive approximate DPC is not. It becomes defensible only after replacing marginal, pointwise error by a uniform context-complete norm on the full instrument or process type.

The next quantitative theorem must therefore be formulated as continuity of the entire source-to-behavior distributive cell in the appropriate complete process norm.
