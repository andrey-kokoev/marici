# Direct compact transitions and anchor charts

## Result and scope

Compact reference packets can now change reference and completion anchor **without constructing the 144-block operator core** on the selected-spanning domain.

The direct implementation validates and temporarily reconstructs 36 complex coordinates together with a positive normalization rho. It evaluates the new scalar observations and, where needed, only the three products defining a completion column. This avoids the large intermediate; it does not claim to avoid field reconstruction or prove an asymptotic complexity bound.

The verified full-core route remains an independent oracle and the explicit fallback outside this domain. No original field, amplitude anchor, physical d or fixed-2x2 realization is supplied to the direct interface.

## Dependencies and unchanged contracts

The construction uses [sharp reference fibers](reference-quadratic-fibers-v1.md), [reference transitions](field-reference-transitions-v1.md) and [retained transport](reconstruction-aware-tower-v1.md).

The retained-carrier portion of the old validator has been factored into `verify_carrier`. Both old and direct interfaces use it to check context, leaf labels, endpoint roles, family membership, masses, means, numerical route histories and presentations. The old full-packet validator still performs its original certificate and fallback checks after that shared validation; it is not weakened.

`DirectPacket` has its own chart type. It retains the fiber certificate and the earlier reference-probe conditioning certificate. A completion column may use any explicitly selected nonzero coordinate, whereas the earlier `SharpPacket` format uses a canonical first nonzero coordinate. Conversion back to `SharpPacket` restores that convention directly, without an operator core.

## Anchor charts

For an ambiguous or unresolved missing triple at reference r, a chart anchored at selected coordinate (e,j) stores

```
b_r[i] = c_r[i] conjugate(c_e[j]),    i=0,1,2.
```

The chart is valid when e differs from r and c_e[j] is nonzero. If the selected reconstruction has representative y=lambda c and rho=|lambda|^2, the missing representative is

```
y_r[i] = rho b_r[i] / conjugate(y_e[j]).
```

All 411 measurements are regenerated and checked after completion. The scalar data alone cannot validate a unique phase choice on an ambiguous fiber; the retained column is part of the packet's actual information.

### Direct anchor transition

For another selected nonzero coordinate (f,k),

```
b'_r = b_r conjugate(y_f[k]) / conjugate(y_e[j]).
```

The common scale and phase cancel in the ratio. Thus identity, inverse and composition laws follow by multiplication of these ratios. The carrier and all scalar values remain unchanged.

A zero anchor is rejected rather than divided through. An anchor equal to the excluded reference is not in the selected chart and is also rejected.

## Weak-anchor diagnostics

Each completion chart records the invariant coordinate strength

```
s = |y_e[j]|^2 / rho = |c_e[j]|^2.
```

The checker declares a squared-strength threshold 1/1000 before the audit. This is a coordinate diagnostic in the supplied corner frame, not a source-selected physical scale or a complete inverse condition number.

A weak but nonzero anchor remains algebraically valid and is flagged. The implementation can select the strongest available selected coordinate by exact algebraic comparison, with deterministic tie-breaking. If all coordinates are weak, that choice is still flagged weak; a large gain is not declared free.

The checker scales the original canonical anchor by 10^-6, verifies its weak status, switches to a stronger chart, and verifies that the scalar carrier and prior reference-probe warning are unchanged. Better anchor selection does not repair weak probe information elsewhere in the decoder.

## Direct reference transition

For a new reference s:

1. Validate the source carrier, certificates and completion chart.
2. Reconstruct a temporary complete representative y and positive rho.
3. Evaluate the P/Q/C scalar comparisons for s and divide their quadratic values by rho.
4. Apply the existing sharper missing-triple classifier to the target observations.
5. Keep no column when the target is unique; otherwise form only the three products for a selected target anchor.
6. Recompute target certificates and rebuild the retained numeric presentation at the same rung and policy.

No full outer-product packet is formed. A provisional three-value column may be used to certify the target fiber and then discarded if uniqueness is proved.

The target chart defaults to the strongest selected coordinate. A caller may instead request a particular valid destination anchor for a nonunique target. If the old anchor becomes the newly excluded arrow, it is not silently carried over: the target must use another selected anchor, or no anchor if it is unique.

## Exact composition and chart conventions

For fixed source and destination charts, the direct transition is determined by the same field modulo common phase. Consequently direct and multistep transitions produce identical complete destination packets. The checker verifies reference and anchor identity, round-trip and cocycle laws.

A chart convention matters: changing a reference back with the default strongest-anchor rule need not restore an arbitrarily chosen noncanonical anchor. To assert literal packet equality for that round trip, request the original destination anchor. Otherwise the results are equivalent charts, not necessarily identical encodings. Tests cover both canonical defaults and explicitly fixed noncanonical endpoints.

These are maps of complete compact representations, not merely equality of terminal means. Numerical route histories are preserved. Anchor/reference operation paths may be recorded separately; direct and composite operation histories are not claimed identical. No absolute phase connection or holonomy theorem is introduced.

## Retained transport compatibility

For both retained-promotion policies, direct reference change commutes with:

- vertical indexing;
- horizontal two-stage retained promotion;
- the complete numerical route to rung 4.

The transport lift validates the resulting carrier while preserving its reconstruction and anchor certificates. These checks compare complete packet trees and completion columns. They do not identify numerical rung positions with native field grades.

## Explicit fallback boundary

A source carrying the full selected-span fallback is outside the direct chart interface and remains on the verified old route.

Likewise a reference change can remove the only selected triple contributing a third independent direction. The checker constructs such a field: the source selected arrows span C3, but excluding the essential arrow leaves span two. The direct call raises `FullFallbackRequired` and leaves its source packet untouched. The independent old route produces the target with its 144-block fallback.

This is a deliberate boundary, not a fabricated compact target. Extending direct transport to selected-span-deficient packets would require another reconstruction theorem or an explicitly larger retained record.

## Verification against the large representation

The checker first prepares its full-core oracle results, then disables eleven full-core/legacy-bridge entry points during all direct checks. Any attempted call fails and is counted. It observes **zero such calls**.

Within that guarded region it verifies:

- agreement with the earlier route for all twelve reference marks, after conversion to the canonical compact convention;
- reference and anchor composition laws;
- a round trip with an explicitly chosen noncanonical anchor;
- a reference change that excludes the old anchor;
- weak-to-strong anchor repair without changing scalar data;
- six retained-transport compatibility squares;
- rejection of selected-span failures, zero/excluded anchors, corrupted columns, stale certificates, invalid references and a nonpositive threshold.

Guarding known entry points is a regression check in addition to the implementation's explicit construction: the direct module creates scalar readouts and three-value columns, never a 144-block array. The temporary field representation is acknowledged rather than described as a no-reconstruction algorithm.

## Reproduction

```
python research/strominger/checkers/check_direct_compact_transitions.py
```

Receipt: `research/strominger/results/direct-compact-transitions/verification.json`. All previous reconstruction, transport and transition checks are freshly replayed. Production and viewer code are unchanged.
