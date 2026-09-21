# The fixed scalar adjoint return cannot realize all Xi transmission zeros

## Result

The minimal conservative completion from the preceding packet cannot accommodate all Xi transmission states with a fixed scalar weight w>0 and a fixed real diagonal alpha. Along the unbounded critical-line zeros its return-port residual grows linearly in the ordinate.

This rules out that specific completion. The proof uses the source's Fourier transform and the explicit return row; it places no assumption on zeros away from the critical line.

## 1. Fourier convention and source

Use the unitary Fourier transform with kernel exp(-itq), so D=partial_q becomes multiplication by it. Let Phi be the real completed theta forcing, with its recorded bilateral transform tau(z)=integral exp(-zq)Phi(q)dq. On the imaginary axis,

hatPhi(t)=tau(it)/sqrt(2 pi).

The standard completed theta forcing is Schwartz; the following statement requires precisely that regularity and the transform identity. Denote rho(t)=|hatPhi(t)|^2, a nonnegative Schwartz function.

At tau(i gamma)=0, the equation (D-i gamma)u=Phi has Fourier solution

hat u(t)=hatPhi(t)/(i(t-gamma)).

Smoothness and the zero remove the apparent singularity. The quotient is square integrable and lies in the domain of the multiplier t, so u belongs to H1. The homogeneous equation has no nonzero L2 solution; this identifies the matched finite-energy history uniquely.

## 2. Explicit source return functional

Plancherel gives

<Phi,u>=i M(gamma),

M(gamma)=PV integral_R rho(t)/(gamma-t) dt.

At a source zero, rho vanishes to at least second order and the integral is ordinary after the removable local extension. The principal-value notation allows discussion at arbitrary real gamma.

The scalar return residual from K_(w,alpha) is consequently

r_(w,alpha)(i gamma)=i [M(gamma)+w alpha-w gamma].

Its vanishing requires

alpha=gamma-M(gamma)/w.

This determines the proposed scalar parameter separately at each zero. A single operator requires the right side to be constant over all admitted zeros.

## 3. Source regularity forces M(gamma) to vanish at infinity

For gamma>2 split the t-axis into:

A: |t|<=gamma/2;
B: |t-gamma|<1;
C: the remainder.

On A, |gamma-t|>=gamma/2, giving an absolute bound 2||rho||_1/gamma.

On B, subtract rho(gamma). Its constant contribution has zero symmetric principal value, and the mean value theorem bounds the remainder integral by 2 sup_(|t-gamma|<=1)|rho'(t)|.

On C, |gamma-t|>=1 and |t|>gamma/2, giving the tail bound integral_(|t|>gamma/2)rho(t)dt.

Thus

|M(gamma)| <= 2||rho||_1/gamma
 +2 sup_(|t-gamma|<=1)|rho'(t)|
 +integral_(|t|>gamma/2)rho(t)dt,

which tends to zero. The negative direction follows by reflection. The same estimate applies at zeros without a principal-value qualification.

## 4. Contradiction for a fixed return port

At unbounded positive critical-line zero ordinates gamma_n,

M(gamma_n)+w alpha-w gamma_n = -w gamma_n+w alpha+o(1).

It cannot vanish for all n. The completed-zeta application uses the classical theorem that there are infinitely many critical-line zeros with unbounded ordinate. That theorem is an imported analytic input; this packet does not reprove it or supply a new bibliographic locator.

Therefore no fixed w>0, alpha real in the constructed scalar-port family makes every matched Xi history an eigenstate. This failure already occurs on the critical line, where the real-part confinement test alone is vacuous.

The failure is structural: the forced-history return has a decaying Hilbert-transform response, while the retained scalar state's eigenvalue term grows linearly.

## 5. Consequence for the closure construction

The scalar theta input c=1 is an input port in the Rosenbrock transmission problem. Promoting it to a dynamical positive-energy scalar state introduces the additional term z w. That promotion changes the spectral problem. The computed mismatch identifies the exact change.

Retaining c as a port leads instead to a boundary relation or a larger dynamical attachment. Such a construction must derive its storage and return law from the source. A frequency-dependent alpha(gamma) fitted by the displayed equation would simply encode the desired transmission condition and would not define the fixed operator sought here.

The minimal scalar-state completion has now been excluded by its own source formula.

The prior packet `research/voevodsky/the-minimal-joint-boundary-reservoir-is-a-two-port-weyl-matrix-whose-cross-entry-is-the-evans-observer.md` already identifies the appropriate source/endpoint distinction. Its incidence is J=(B_f,E_0^times), and its matrix response is M=J^times R_z J. The source autocorrelation is M_11, while the endpoint transfer is M_21. Its descriptor weight diag(I,0,0) leaves both ports without artificial spectral mass. The current no-go supplies an additional asymptotic obstruction to promoting the source port to the positive scalar state considered here.

That prior packet explicitly leaves closed-domain realization, the full completed Xi cross-entry comparison, and the distinguished minor estimate open. A positive Weyl matrix alone permits a zero cross-entry. The next derivation must retain the two ports and compute the reciprocal sewing that produces the full Xi mismatch from the one-sided endpoint transfers. Merely renaming M_21 as Xi would skip that calculation.

## 6. Independent finite hostile

A flat spectral density rho=1 on [-1,1] gives, for gamma>1,

M(gamma)=log((gamma+1)/(gamma-1)).

It is strictly decreasing, while gamma increases. Hence gamma-M(gamma)/w is strictly increasing for every w>0; a fixed alpha cannot satisfy the return law at two such ordinates. This fixture is an L2 band-limited source, distinct from completed theta. It exercises the same return-port mechanism without an RH assumption.

## Verification status

Sections 1–4 are analytic derivations under the explicitly listed source regularity and classical zero-existence input. The checker `check_fixed_scalar_return_obstruction.py` verifies the flat-density integral, monotonicity sample, and opposite variation of the two sides. It is a regression test, not a numerical proof about Xi zeros.

Predecessor: `bilateral-arithmetic-attachment-and-the-explicit-conservative-port-residual.md`.
