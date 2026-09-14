# Sealed-label natural arithmetic-coupling thought experiment

## Question

Can a preregistered inference procedure distinguish a source-derived arithmetic shell generator from retrospective mode relabeling and free per-mode attenuation?

## Claim boundary

The thought experiment can test source-label identifiability and reject inadequate inference rules on synthetic exact data. It does not test the categorical fact that a compatible faithful probe distinguishes its inputs. It asks whether the probe and its arithmetic labels arise from independently declared source structure. It cannot establish that any physical source carries the required generator. A surviving procedure defines the evidential burden for a future candidate; synthetic success is not physical evidence.

## Bold conjecture

A finite source-natural candidate is identifiable when it supplies, independently of attenuation data:

1. a physical mode space \(H\);
2. a source-derived operator \(K\) with integer eigenspaces \(H_j\);
3. an embedding \(\iota(e)\in H_{j(e)}\) of consecutive-prime edges;
4. a controlled attenuation depth \(s\) whose contraction is \(V_s=e^{-sK}\);
5. a detector \(\widetilde C\) with \(\widetilde C\iota=C_{\rm history}\).

With \(t=e^{-s}\), the first four objects imply

\[
V_s\iota=\iota D_t,
\qquad D_t(e)=t^{j(e)}.
\]

The coordinate \(s\) is attenuation depth, not physical time.

## Named rivals

- `response_sorted_labels`: infer shell labels by sorting measured attenuation;
- `permuted_shells`: use the right integer spectrum with a wrong source assignment;
- `free_mode_gains`: fit one response coefficient per mode and setting;
- `frequency_order`: replace source shells by carrier-frequency order;
- `nonlinear_exponents`: use an unrelated exponent family such as \(j^2\).

The free-gain rival can interpolate a finite observed table but has no held-out prediction without additional structure. Its training fit is therefore not evidence for arithmetic coupling.

## Sealed envelopes

### Envelope A: source declaration

Before response data are exposed, freeze the consecutive-prime pairs, edge incidence, shell map, candidate \(K\), embedding, detector, and allowed coordinate transports.

### Envelope B: calibration

Expose only initial shells and settings. Calibration may identify one common attenuation parameter. It may not alter shell labels or introduce a gain per held-out shell.

### Envelope C: held-out tests

Reveal new shells, settings, cycles, and a transported second realization. Score predictions without refitting the source declaration.

## Exact synthetic world

At cutoff \(N\), use consecutive-prime shells

\[
(2,3),(3,5),(5,7),(7,11)
\]

with edges \(kp_j\to kq_j\) whenever the target is at most \(N\). Let \(\partial\) be the incidence matrix and let \(F\) be an exact basis of \(\ker\partial\). The true generator is diagonal with entry \(j(e)\) on edge \(e\).

Use the exact settings

\[
\frac56,\quad\frac34,\quad\frac7{10},\quad\frac23.
\]

The first two shells and first two settings form calibration data. The remaining shells and settings are held out.

## Risky consequences

The conjecture requires all of the following:

- the true source map predicts held-out shell responses exactly;
- attenuation composes as \(D_tD_u=D_{tu}\);
- a nontrivial shell permutation fails against fixed source labels;
- nonlinear exponents fail on held-out shells;
- response-sorted labels can fit after relabeling, demonstrating that response alone is nonidentifying;
- unmodulated exact cycles remain in \(\ker\partial\);
- the stacked modulated boundary responses detect the finite cycle basis;
- a simultaneous source-coordinate permutation preserves the result only when transported through \(K\), \(\iota\), and the detector.

## Strongest falsification attempt

Give the rival access to every measured attenuation eigenvalue but withhold source labels. It can sort those values and declare the resulting order to be arithmetic. This reconstructs the finite response table, so attenuation observations alone cannot distinguish the true shell assignment from a conjugate permutation. The exact residual is missing independent source identification of \(K\)'s eigenspaces.

Then restore the sealed source labels. A wrong permutation predicts the wrong response on at least one held-out shell. This separates source-natural identification from retrospective fit.

## Acceptance

The synthetic checker passes only if it exhibits both sides:

1. the natural-generator world satisfies held-out, composition, transport, and cycle-detection tests;
2. response-only relabeling remains observationally degenerate until the sealed source declaration is restored, after which the declared hostile rivals fail.

If the checker cannot produce the response-only degeneracy, it has not tested the central identifiability obstruction. If a hostile rival survives fixed labels and held-out tests, revise the conjecture rather than narrowing the test after inspection.

## Disposition

This thought experiment operationalizes the distinction between compiled and source-natural coupling. Its surviving target is a physical candidate carrying an independently measurable integer generator and prime-edge incidence. No such candidate is supplied here.
