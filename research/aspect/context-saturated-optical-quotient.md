# Context-saturated optical quotient

## The surprise

Two devices can agree on every currently injected probe and still disagree
when one is placed in a cavity. “Same transfer” is therefore not compositional
until the probe domain is saturated under the admitted optical contexts.

Freeze two two-mode transfers, `I` and `diag(1,-1)`, and inject only the first
mode. They act identically. Admit the mode-swap context `X`. The orbit of the
probe under `{I,X}` spans both modes, exposing the hidden sign.

The cavity version is stronger because it needs no new external input. With
amplitude recirculation `1/2`, the effective fields are

```text
(I - X I/2)^(-1) e1       = (4/3, 2/3)
(I - X diag(1,-1)/2)^(-1) e1 = (4/5, 2/5).
```

Direct intensity detection now separates devices that were identical on the
original one-dimensional probe domain. Feedback has synthesized the missing
probe direction internally.

## Global phase becomes a relative record

Standalone operations `I` and `-I` induce the same polarization channel. Put
the whole implementation in one arm of a coherently controlled bypass. The
control exits in the plus state for `I` and the minus state for `-I`; its
X-basis expectations are `+1` and `-1`.

Thus an apparent representation kernel can be activated by enlarging the
context from standalone action to coherent controlled action. This applies to
the `q` versus `-q` spinor sheet only if the laboratory genuinely supplies
coherent control of the implementation. Merely writing a controlled matrix is
not evidence that such a control port exists.

## Route history needs an internal slot

The bare routes `H` then `H` and `X` then `X` both equal `I`. Coherently
controlling either complete box cannot distinguish them: equal operations stay
equal in that context.

But insert the same `Z` operation between the two route elements:

```text
H Z H = X
X Z X = -Z.
```

On the first-mode probe, their endpoint intensity records become `(0,1)` and
`(1,0)`. One fixed internal context distinguishes the histories without a
complete internal log. The price is explicit access to the factorization slot.

This yields three different provenance claims:

- endpoint equivalence on a probe domain;
- contextual equivalence after saturation under allowed external contexts;
- comb or route equivalence when contexts may be inserted at internal slots.

Only the third is a route-compositional test.

## Claim boundary

The checker treats exact lossless two-mode linear optics and a finite declared
context library. It does not establish cavity stability, phase-noise tolerance,
loss robustness, or physical coherent control of an arbitrary unknown device.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_context_saturated_optical_quotient.py
```
