# Tangent dynamics of the four ground sectors — iteration 3

## Result

The constrained Hamiltonian from `spinor-constrained-leads.md` has three matter oscillation frequencies at each of its four source-related ground sectors:

    0.00611206580804,
    2.00611206580804,
    2.04974201753714.

These are numerical frequencies in the model's clock units, not measured particle gaps or quantum excitation energies. The matter Hessian is positive in the six real projective tangent directions. The full twelve-dimensional linearized system also has three neutral cyclic-angle directions and three conjugate momentum directions forming zero-frequency Jordan chains.

Thus there is no exponential linear instability in these checks. There is secular angle drift when conserved lead momenta are perturbed. A single point on the ground torus must not be called asymptotically stable; there is no dissipation.

## Canonical tangent chart

At a normalized ground vector p, choose a four-by-three complex matrix U satisfying

    U†U=I, U†p=0.

Use real canonical coordinates v=(x,y) with

    delta psi=U(x+i y)/sqrt(2)=T v,
    T=[U,iU]/sqrt(2),
    J=[[0,I],[-I,0]].

This removes both norm and common phase. For nonlinear checks the normalized projective chart is (p+Uz)/||p+Uz||; its inverse is z=U†psi/(p†psi). The chart is local where p†psi is nonzero.

Let S be the four-by-three matrix with upper block I and last row (-1,-1,-1), so delta ell=S m respects the charge constraint. Let theta denote the three cyclic angle perturbations. At the stationary point define

    mu=p†[K p+(beta/4)diag(rho+ell)p],
    A=K+(beta/4)diag(2rho+ell)-mu I,
    D=(beta/4)diag(p^2).

The real Hessian blocks are

    H=2 Re[T† A T+T† D conjugate(T)],
    M=2 Re[T† (beta/4)diag(p) S],
    L=(5 beta/4) S^T S.

The subtraction of mu is essential: this is the constrained energy Hessian, not the unconstrained ambient Hessian.

## Coupled quadratic Hamiltonian

The second-order energy is

    H2=(v^T H v)/2+v^T M m+(m^T L m)/2.

It is independent of theta. The equations are

    vdot=J(Hv+M m),
    theta_dot=M^T v+L m,
    mdot=0.

In each fixed-momentum sector (m=0), the eigenvalues of JH are three imaginary conjugate pairs. All four addresses produce the same frequencies to numerical precision. The smallest Hessian eigenvalue is about 0.00611009464; the small positive mode must not be discarded as an exact rotational zero mode.

For nonzero constant m, shift to the displaced matter center

    v_center=-H^-1 M m.

The remaining angle velocity at that center is

    theta_dot=R m,
    R=L-M^T H^-1 M.

The Schur complement R is positive in all four checks. Its coordinate eigenvalues need not match between addresses: choosing the fourth lead as the reference angle makes the coordinate basis nonorthogonal under permutations. Positivity and the full canonical spectrum, not these Euclidean coordinate eigenvalues, are the invariant statements.

The full Hamiltonian is positive transverse to the ground-angle torus. The linear generator has rank 9 and its square rank 6. Its zero eigenvalue has algebraic multiplicity six and geometric multiplicity three: exactly three length-two Jordan chains. The drift is ordinary conserved-momentum motion along cyclic coordinates, not evidence for an unstable matter mode or a transition to a different lead sector.

## Checks and limits

    uv run --with numpy --with scipy python research/voevodsky/checkers/check_spinor_tangent_dynamics.py

Results: `results/spinor_tangent_dynamics.json`.

For all four rays the checker constructs the analytic Hessian and independently finite-differences the full projective vector field, including angle velocities and lead momentum perturbations. Maximum entrywise Jacobian discrepancies are below 9e-12. It checks positive Hessian/Schur eigenvalues, frequency agreement, generator ranks and all three explicit Jordan-chain relations.

These are double-precision checks, not rational interval certificates. The preceding ground-state classification remains the source for the global minimum; this calculation characterizes local dynamics. It neither quantizes the classical theory nor introduces cross-sector tunneling.

## Next

Completed in `spinor-finite-dynamics.md`: full slow-period and lead-drift trajectories, amplitude/error scaling, solver refinement and the observable/phase-history contract.

Original next step: test finite-amplitude trajectories against this tangent model, especially its slow matter mode and momentum-induced angle drift. Specify the observables and phase/holonomy histories retained by the state-space construction before attempting a quantum or transition model.
