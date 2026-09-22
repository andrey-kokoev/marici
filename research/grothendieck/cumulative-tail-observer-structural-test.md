# Cumulative-tail observer: the obstruction is incompatible mass scheduling

## Structural reduction

For ordered cells with cumulative capacities c_i and objective weights w_i,
consider max sum w_i x_i subject to x_i>=0 and sum_{j<=i}x_j<=c_i.
Let

    h_i = max(0, w_i, ..., w_n), c_0=0.

The exact optimum is sum (c_i-c_{i-1}) h_i. This is not an unconstrained
cellwise maximization: capacity first available at i can only be spent at i
or later. Allocate each increment c_i-c_{i-1} to a future maximizer of h_i,
or leave it unused when h_i=0. This is an explicit feasible primal witness.
The nonnegative, nonincreasing sequence h majorizes w and supplies the dual:

    sum w_i x_i <= sum h_i x_i <= sum (c_i-c_{i-1}) h_i.

Thus the future running envelope preserves all objective-relevant cumulative
compatibility for this finite problem. It is objective-relative, not a
universal observer for arbitrary later functionals.

## Continuous fixed-kernel test

Use the actual combined kernel K_plus+K_minus, the existing N=1e6 finite
prime evidence, and the unchanged Chebyshev capacity. Whole-cell interval
weights and capacities at right endpoints give an outer discrete problem.
Atoms placed at right endpoints under lower capacities give a feasible
continuous primal construction. An analytic exponential bound controls the
infinite suffix. This yields a certified finite approximation sandwich;
it does NOT establish an exact finite representation of the continuum
extremum.

At mesh 1/512 (25,695 cells), approximately:

- joint cumulative minimum: [-3.082390241e-7, -3.072285239e-7];
- pointwise-relaxed minimum: [-3.085384466e-7, -3.065314048e-7].

The intervals overlap. The strict-gap DPC is therefore UNRESOLVED, not
corroborated and not refuted. The primal and dual agree exactly for each
finite surrogate, not across the continuous approximation sandwich.
No new midpoint classification is asserted.

## What explains whether compression loses information?

In Abel form, minimizing the tail pointwise selects A=M wherever K'>0
and A=0 wherever K'<0. This relaxed optimizer is compatible with a
nondecreasing cumulative measure only if those choices can be realized
without removing previously accumulated mass.

A single-valley kernel, decreasing then increasing to zero, illustrates
why a strict gap is NOT automatic: choose A=0 before the valley and A=M
after it. This is a feasible cumulative schedule (with a permitted atom at
the valley), and it attains the pointwise relaxed extremum. When the switch
is at the initial excluded endpoint, the same statement is about an
approachable infimum. This observation is not a certified shape theorem
for the actual fixed kernel.

By contrast, discrete weights (-1,1,-1) with capacities (1,2,3) give a
pointwise prefix relaxation of -5 but a cumulative optimum of -3. The
relaxation wants prefix masses (1,0,3), which would erase already allocated
mass. This strict-loss control passes exact rational arithmetic.

The synthesis is consequently sharper than 'dependencies improve bounds':
**a discarded dependency matters precisely when an extremizing continuation
tries to violate it.** Provenance can likewise be redundant when the old
operational observer already preserves the relevant distinction. A shared
measure is structurally necessary for the model, but need not change this
particular objective's extremum.

## Reproduction and scope

    uv run --with python-flint python research/grothendieck/checkers/check_cumulative_tail_observer.py

Artifact: `results/cumulative-tail-observer.json`.
Checks include owning artifact hashes, exact finite primal feasibility,
matching primal/dual values, envelope inequalities, interval kernel bounds,
and the strict-loss control. There is no independent implementation of the
interval kernel evaluation. The admissible measures are a continuous
Chebyshev relaxation, not necessarily prime-realizable measures.

The next structural discriminator is a certified sign-order description of
the COMBINED kernel derivative: does the relaxed optimum require a forbidden
M-to-zero reset? This is more informative than further mesh refinement or
assuming that the two separate kernels' sign changes imply a strict gap.
