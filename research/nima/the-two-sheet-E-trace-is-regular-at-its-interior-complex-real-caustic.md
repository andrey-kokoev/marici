# The full E two-sheet trace is regular at its interior complex/real caustic

The unique E fibre discriminant root `e*∈(1/40,1/35)` lies on a **target-regular positive V family**. To test whether this algebraic caustic creates a meromorphic E-form pole, take the exact **double-root inverse source** in the quadratic kernel lift and reduce its coordinates modulo the irreducible caustic quartic.

Exact polynomial-GCD checks show that, at the double source, **all six E weights, `u`, `t−u`, the source gauge pivot, and the target pivot are finite and nonzero**. None of their numerators or denominators shares a caustic-quartic factor. The E intrinsic logarithmic eight-form is therefore **regular** at this coalescence, even though each single-sheet target inverse Jacobian diverges.

For a simple quadratic fold in a transverse target coordinate `r=s²`, a regular source density `f(s) ds` pushes as the paired expression

```
[f(+√r) − f(−√r)]/(2√r) · dr,
```

which is holomorphic at `r=0`. The discriminant root is simple and transverse along the V family, so this applies componentwise to the complete fermionic numerator. **The two-sheet E meromorphic trace has no pole at this interior caustic**, despite E changing from two real nonpositive inverses to two nonreal inverses there. A single inverse-sheet divergence is not a physical image-form singularity.

This is a local all-component regularity statement at this one caustic, not a construction or validation of the global nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_E_caustic_source_pole_intersection.py`; result: `research/nima/results/nine-point-E-caustic-source-pole-intersection.json`.
