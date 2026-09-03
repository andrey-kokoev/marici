# Preconditioned-spline convention sensitivity atlas

## Question

Which executable convention changes preserve or reverse the certified finite sign?

## Claim boundary

These are rival computations, not source-authorized conventions. They discriminate future convention maps; they do not select one.

## Atlas

The baseline tuple uses arithmetic coefficient `-2`, argument `log(p^m)`, all five shifts, the `D_N` term, constant `-(gamma+log pi)f(0)`, and kernel shift `n+1/4`. Its Gram interval is

\[
[1.1790450740\times10^{-5},1.1906013635\times10^{-5}],
\]

strictly positive.

Changing only the arithmetic coefficient from `-2` to `+2` gives

\[
[-8.3861655491,-8.3861654335],
\]

strictly negative. Omitting the four noncentral shifts gives

\[
[-5.0468111245,-5.0468110090],
\]

strictly negative. Omitting `D_N` gives

\[
[0.6584601561,0.6584602480],
\]

strictly positive but separated from the baseline by more than four orders of magnitude.

Replacing the prime-power argument `log(p^m)` by `2 log(p^m)`, while retaining the supported enumeration, changes the prime contribution to `1.9215658261`; combined with the certified baseline archimedean interval this gives approximately

\[
[-2.2715110533,-2.2715109377],
\]

strictly negative.

The exact interval for `(gamma+log pi)f(0)` is concentrated at `4.74146935895`. Omitting the negative constant therefore shifts the baseline to approximately `4.7414812`, while reversing its sign shifts it to approximately `9.4829505`; both remain positive but are not normalization-equivalent to the baseline.

## Evidence

- Baseline and deliberate rivals: `research/nima/results/preconditioned_spline_weil.json`
- Double-log prime execution: `structured_command_execution:e_4616_1788287832863525700_25`
- Constant-term execution: `structured_command_execution:e_4616_1788287861357580800_26`
- Results summary: `structured_command_execution:e_4616_1788287906797750400_27`

## Disposition

The finite sign is convention-sensitive: arithmetic-sign, shift-family, and log-argument changes reverse it; constant and `D_N` changes preserve positivity while changing scale. The exact-moment and tail functions now accept a quarter-grid kernel shift. With all other conventions fixed, `delta=1/2` gives `[0.06197034055,0.06197039934]` and `delta=3/4` gives `[0.43248138311,0.43248141267]`. Both preserve positivity but change its scale; execution: `structured_command_execution:e_4616_1788288225615497700_28`. The `delta=1/4` regression remains `[1.1790450740e-5,1.1906013635e-5]` after full execution `structured_command_execution:e_4616_1788288332424490900_29`.
