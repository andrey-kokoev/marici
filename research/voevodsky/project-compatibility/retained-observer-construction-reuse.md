# Reuse an existing positive construction: retain the observer, contract discrepancies

## Search result, not a new framework

The proposed search for a positive common construction has a direct antecedent:

`research/voevodsky/consistency-complexes-retract-to-corrected-observers-while-discrepancies-kill-synchronized-classes.md`, sections2–6, already proves an explicit source-equivariant deformation retraction of corrected frame-consistency complexes. It separates horizontal consistency from vertical depth extensions and retains nonsplit source extension classes. Its input is Nima's `frame-discrepancy-observers-form-a-compatible-consistency-tower.md`.

The prior theorem is stronger than another generic obstruction taxonomy. We reuse its algebraic identities below rather than present them as new mathematics. The current readout synthesis already contains the ingredients of both examples; the contribution here is the explicit common construction and its non-promotion boundary.

## The existing reusable construction

In the declared additive category, suppose the supplied maps have types

    i: V -> P, r: P -> V, d: P -> D, h: D -> P

and satisfy

    r i = 1, d i = 0, d h = 1, r h = 0,
    i r + h d = 1.

Then `(r,d):P -> V direct_sum D` is an isomorphism with inverse `(i,h)`. The complex `[P --d--> D]` decomposes as `V[0]` plus the contractible complex `[D --1--> D]`. Thus the full consistency complex retains V, whereas discrepancy-only observation d kills i(V).

For an independently declared readout O on V, `O r` recovers O on realized packets: `O r i=O`. No claim is made that this defines the intended physical reading on arbitrary incompatible packets. Different off-image splittings may agree on all realized data.

This is a sufficient construction, not a necessary condition for readout descent. Non-split sources can still preserve a particular observation; the weaker readout-relative contract remains relevant there.

## Independently sourced finite instances

### Spectral observer

Use the existing spectral checker and its source representative, without changing its coefficients:

    i(x)=(Ax,Bx), r(y,z)=B^(-1)z,
    d(y,z)=y-AB^(-1)z, h(w)=(w,0).

B is the retained invertible direct-score port. All five identities hold over the declared rational/real coefficients, including at the tensor-only wall. No formal acyclicity of the ordinary 3->6 cone is inferred: the specified 3->6->3 augmented complex is the split object.

### Integral fs/Kato realized packet

The existing physical pullback checker supplies the primitive cycle and detector rows r,c,r with c-r=d1. Their actual primitive detector image is `(1,1,1)`. On the resulting homology packet, use

    i(n)=(n,n,n), r(a,b,c)=a,
    d(a,b,c)=(a-b,b-c), h(u,v)=(0,-u,-u-v).

All five identities hold over Z; neither3 nor a support normal is inverted. The retraction uses a retained labelled primitive coordinate, not the scalar trace. The construction is on the already realized homology packet, not a new proof of fs/Kato geometry, a chain-level comparison of the full source complexes, or a physical realization of arbitrary triples.

The algebraic off-image h is displayed to verify the decomposition. It is NOT asserted to be a source-authorized physical constructor, a canonical equivariant map for an unspecified ambient action, or a new geometric coefficient sector.

## Hostile tests and limits of universality

- Discrepancy-only extraction is zero on both source images. Compatibility residuals cannot replace the retained observer.
- In the integral example, scalar trace followed by mod3 is also zero on the primitive image. Replacing the labelled coordinate by that scalar destroys the intended information.
- The spectral instance uses B inverse over its declared field. This does not license inverting3 in the integral supported sector.
- The two V objects need not be identified. A shared contraction pattern is not a physical cross-sector map.
- The earlier corrected-frame theorem has source-equivariance and product/inverse-limit continuity under its own hypotheses. Those hypotheses do not automatically transfer to these two examples. Uniform analytic bounds, summable source realization and physical extraction remain separate.

The surviving common construction is therefore **retained-observer contraction of a witnessed split consistency complex**. Its algebraic reuse is established on these packets; universal physical-core promotion is not. This respects `docs/cross-sector-falsification.md`: an algebraically selected discrepancy section cannot silently become a source-authorized physical operation.

## Programme consequence

Do not open another generic common-construction or obstruction-classification branch. There is already a positive construction to reuse. A stronger claim must identify the actual source action and completion under which these particular i,r,d,h remain admitted and continuous, or produce a counterexample. Merely rerunning the finite split identities would add no new completion theorem.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_retained_observer_reuse.py`

The audit reuses the two existing source checkers, computes the five identities symbolically, verifies the integral coefficients and the hostile scalar loss, and records hashes. It neither changes owner artifacts nor promotes a physical source theorem from finite matrix checks.
