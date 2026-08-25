# The strongest coherent proper task fails three physical fields (WP85)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## One task identity

Use the exact three-branch spectral pinching task from WP78 throughout:

\[
T_E:(H_u,H_d)\mapsto(H_u,E_{H_u}(H_d)),\qquad
E_{H_u}(H_d)=\frac13\sum_{k=0}^2D_{H_u}^kH_dD_{H_u}^{-k}.
\]

Here `D_Hu` is the order-three spectral phase operator defined covariantly by
the nondegenerate eigenspaces of `H_u`. No certificate is borrowed from a
different readout task.

## Package fields

1. **Proper operation and attribute — passes mathematically.** The image is
   `[H_u,H_d]=0`, a proper weak-basis-invariant locus. The task descends and is
   counterfactually total on the nondegenerate domain.
2. **Independent normalization — passes mathematically.** Uniform weights
   `1/3` are fixed by the finite group average, not by the IR fit.
3. **Independent physical authority — fails.** The source declares neither
   this channel nor a bath/coupling that generates it.
4. **Task-specific instrument — fails.** Required resources are a spectral-
   frame coupling, three-branch compiler, uniform random source, timing, and
   discard/reset channel. None is declared.
5. **Repeatability/degradation — algebraic half passes, physical half fails.**
   `T_E^2=T_E`, so substrate error is exactly zero after one ideal use. But no
   apparatus trajectory or degradation/reset bound exists; absent data are
   untyped, not zero.
6. **Own ensemble prediction — fails.** The predeclared image predicts
   commuting nondegenerate Gram operators and hence zero physical mixing.
   The fitted flavor domain has nonzero mixing; WP66 records that the locus
   does not survive the ensemble.

## Result

This is the closest task-identity-coherent package currently available. It is
a complete mathematical selector specification but not a physical flavor
constructor. Its irreducible missing cut is physical source authority,
task-specific implementation/repeatability, and ensemble survival. Changing
the target to fit the ensemble would create a new task and trigger WP84
certificate noninheritance.

Verification: `uv run --with sympy python
research/flavor/checkers/wp85_pinching_coherent_task_package.py`.
