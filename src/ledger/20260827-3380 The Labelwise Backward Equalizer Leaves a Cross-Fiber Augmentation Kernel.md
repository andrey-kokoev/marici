# The Labelwise Backward Equalizer Leaves a Cross-Fiber Augmentation Kernel

For every `p`-free base `m`, the valuation-chain transform satisfies the exact
labelwise identity

\[
(1+q)R_m-qA_m-q^2B_{m,2}=(1-q^2)F_m.
\]

The global scalar readout is the augmentation `F=sum_m F_m`. A global zero
therefore kills only that sum, not each fiber. With `d` retained `p`-free
bases, a `(d-1)`-dimensional cross-fiber cancellation space remains. The
minimal witness is `(F_1,F_2)=(1,-1)`.

Thus labelwise retention repairs the rank-one dagger obstruction, but
componentwise zero-state equalizers are unauthorized. The final mate cell
must contain a source-derived comparison acting on the augmentation kernel,
and must be natural under cutoff restriction.

This gives the final coherence cell its own internal tower: scalar mate,
labelwise mate, augmentation-kernel comparison, sesquilinear Ward form, and
completion coherence.

Research packet:
`research/grothendieck/the-labelwise-backward-equalizer-leaves-a-cross-fiber-augmentation-kernel.md`

Exact checker:
`research/grothendieck/checkers/check_labelwise_equalizer_augmentation_kernel.py`

The checker passes 6/6 gates.
