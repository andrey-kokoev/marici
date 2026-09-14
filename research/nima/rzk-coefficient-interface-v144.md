# v144: all-degree L2 integral lattice

The D28 denominator observation is now upgraded to an all-degree symbolic
argument for the actual labelled p/q formulas.

Because `u^2=0`, every required power of `L1` and `L2+/-` has an integral u0
part and at most a half-integral u1 part; only exponents 0,1,2 occur. The
potentially dangerous explicit `3/2` terms are harmless:
`(3/2) d_b k` and `(3/2) d_a k` both have integral coefficients because the
relevant derivatives of k are even. All remaining operations have integer
coefficients.

Hence in every degree the lattice retaining the original u0 sector and taking
`u/2` as the square-zero u1 generator contains every labelled p/q column. This
is now a proved denominator/lattice theorem, not cutoff extrapolation.

The remaining integral L2 task is the relation-kernel/Bockstein Smith
presentation in this lattice.

`rzk/172-l2-all-degree-integral-lattice.rzk.md` passes all eight declarations
without assumptions.
