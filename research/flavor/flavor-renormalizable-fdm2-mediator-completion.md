# A renormalizable mediator realizes the FDM-2 Yukawa map (WP90)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Source fields and CP

Extend `FDM-2` by a complex gauge-singlet flavon `S=x+i y` and one heavy
vectorlike down-type mediator `D_L,D_R`. CP acts by `y->-y` and complex
conjugation. All source coefficients below are real.

Use the renormalizable nonnegative scalar potential

\[
V=(x^2+y^2-1)^2+(x^2-y^2-7/25)^2+(x-4/5)^2.
\]

It is CP invariant, has degree at most four, and its exact zero set is

\[
(x,y)=(4/5,+3/5),\ (4/5,-3/5).
\]

Thus the two global vacua are CP conjugates with
`<S>_+=4/5+3i/5` and `<S>_-=<S>_+^*`. A CP-symmetric quench and bath induce
equal vacuum probabilities; the WP88 orientation coin is the spontaneous
vacuum outcome rather than an independently inserted sign source.

## Renormalizable mediator Lagrangian

The flavor interactions are

\[
-\mathcal L\supset
\bar Q_LY_0H d_R+\bar Q_L a H D_R
-\bar D_L S b\,d_R+M\bar D_LD_R+\text{h.c.}
\]

with real `Y0,a,b,M`. Every displayed interaction has operator dimension at
most four. Eliminating the heavy mediator at tree level gives the exact Schur
complement

\[
Y_d^{\rm eff}=Y_0+\frac{\langle S\rangle}{M}a b.
\]

Consequently the two vacua produce complex-conjugate Yukawa matrices without
a sparse texture or generation-space reference.

## Exact nonzero-CP witness

For

\[
Y_0=\operatorname{diag}(1,2,4),\quad
a=(1,2,3)^T,\quad b=(2,1,1),\quad M=1,
\]

and `H_u=diag(1,4,9)`, the checker obtains

\[
\det[H_u,H_d^+]=1152i,\qquad
\det[H_u,H_d^-]=-1152i.
\]

The spectra are nondegenerate and CP-even Gram invariants agree. This is an
explicit renormalizable realization of the WP89 quotient map and proves that
the selected vacuum union supports physical mixing and CP violation.

## Instrument and remaining empirical boundary

The task-specific instrument is now a CP-symmetric thermal quench of `S`,
followed by overdamped relaxation through the cooled bath and mediator-induced
Yukawa readout. Exact symmetry enforces the ideal `1/2,1/2` vacuum law. The
finite coin-bias and bath-degradation bounds remain those of WP88.

This closes the renormalizable representation gate inside the proposed model.
It does not establish that the singlet, vectorlike quark, or quench apparatus
exists in nature; their masses, collider bounds, and finite-temperature
nucleation dynamics remain empirical successor tests.

Verification: `uv run --with sympy python
research/flavor/checkers/wp90_renormalizable_fdm2_mediator.py`.
