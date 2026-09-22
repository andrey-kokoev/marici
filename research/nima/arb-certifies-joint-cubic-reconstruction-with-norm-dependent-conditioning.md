# Arb certifies joint cubic reconstruction with norm-dependent conditioning

## Certified result

For the specified 270 private mixed scalar readings on the actual two-feature cubic packet, the exact inverse is now quantitatively certified.

At background 2, spectral point 3i, forcing beta=4 and receiver gamma=2:

- the inverse norm from total scalar l1 error to Q_1 source error is approximately 4*10^18 w_seam, rigorously below 10^19 w_seam;
- consequently total scalar error at most 10^(-27) implies Q_1 reconstruction error below 10^(-8) w_seam;
- the inverse norm to UNWEIGHTED PATH-COEFFICIENT error is instead approximately 10^(136822211.62).

Both maxima occur on

`forgotten(11,13) mixed(5,7) mixed(2,3)`,

whose retained diamonds begin at arithmetic values 286 and 10010.

Thus finite-packet separation is certified, but conditioning depends critically on which source error is meant. Actual-letter weighting cancels the leading tiny-window exponentials; unweighted coefficient reconstruction does not. Even the smaller bound is large, and no experimental acquisition capability is asserted.

## 1. Freeze the acquisition protocol and norms

Use exactly the 270 private rows constructed in `joint-cubic-kernel-survives-vacuum-addition-but-private-mixed-rows-separate.md`. Each row has two retained first-edge slots, one forgotten slot and vacuum coefficient buffers. Test the retained slots with the existing norm-one residual functional kappa and the forgotten slot with the unit vacuum observation.

Let z_j denote the resulting UNscaled scalar reading. The error norm is the TOTAL sum sum_j |e_j|, not a per-row bound. No division by a window amplitude is built into this data norm.

The actual source basis vectors v_j have disjoint marked-path supports and 32 unit-magnitude coefficients each. Write nu_j=||v_j||_Gamma. With E_j>0 the exact scalar response on the private row, the source is

`x=sum_j (z_j/E_j)v_j`.

Therefore the exact operator norms are

`C_R=6!R^6 max_j(nu_j/E_j)`

for Q_R, and

`C_path=32 max_j(1/E_j)`

for the unweighted marked-path coefficient norm. These are norms of the full finite inverse, not of one previously optimized scalar source functional.

## 2. Actual source weights and scalar responses

For a mixed diamond beginning at a with primes p,q, let

`S(a;p,q)=g(a,p)+g(pa,q)+g(a,q)+g(qa,p)`,

where g is the actual H4 norm of the corresponding completed-theta forcing window.

For F=[log a,log(pa)] put

`X_F=integral_F cosh(3x)Phi(x) dx`,

`J_F=integral_F x sinh(3x)Phi(x) dx`,

`K_F=J_F-L X_F`, with `L=xi'(7/2)/xi(7/2)`.

The positive-window bound mu_F>L ensures K_F>0. With h^2=1/[2(3+2)]=1/10, the retained scalar response is sqrt(2)h K_F. Thus, for the two retained diamonds beginning at A and B,

`nu_j/w=2 S_A S_B`, `E_j=(1/5)K_A K_B`,

where w=w_seam remains the original physical constant. Consequently

`C_R/w=7200 R^6 max_j (S_A/K_A)(S_B/K_B)`.

Only the chosen first-edge intervals enter K_A,K_B; all four actual diamond windows enter each S. Confusing these would change the inverse constant.

## 3. Certified integration without tiny-amplitude underflow

The forcing norms use the completed-theta norm enclosures already proved in the worked source certificate. This run computes all 63 required starting-value enclosures.

For residual evaluations use q_0=pi a^2, v=pi exp(2x)-q_0, and q=q_0+v. The scaled theta density Phi(x)dx, after removing exp(-q_0), is

`exp(x/2)[(2q-3)exp(-v)+(32q-12)exp(-3q_0-4v)+positive remainder]`.

The remainder is bounded by

`2q*81 exp(-8q_0-9v)/[1-(4/3)^4 exp(-7q)]`.

Integrate this density against x sinh(3x)-L cosh(3x) on 2048 complete interval cells through v=32. The integrand is positive. Every actual prime-multiplier window extends beyond that core, so adding the positive infinite tail bound gives an enclosure for each needed finite window without equating their exact integrals.

For the tail use H_0=1+16 exp(-3q_0)/[1-(3/2)^4 exp(-5q_0)] and Q=q_0+32. The scaled X and J tails are bounded respectively by

`2pi^(-7/4)H_0 exp(-32)(Q^3+3Q^2+6Q+6)`,

`2pi^(-7/4)H_0 exp(-32)(Q^4+4Q^3+12Q^2+24Q+24)`.

Their combination J_tail+|L|X_tail bounds the K tail. There are 31 required residual starting values.

L is enclosed using the absolutely convergent prime-power expansion at 7/2 through 4096, with its explicit integral majorant beyond that cutoff. The result is near 0.13668993, and the required global positive-window inequality is checked rigorously.

All calculations use Arb at 192 bits. The common exp(-pi a^2) factor is cancelled between S and K for the Gamma ratios. For unweighted coefficient conditioning, logarithms retain that exponential contribution instead of printing an astronomically long coefficient.

## 4. The certified worst column

The checker evaluates enclosures for every one of the 270 ratios. The LOWER endpoint for the identified worst column exceeds the UPPER endpoints of all other columns, separately for both error norms. Thus the maximizer is certified, not selected using approximate midpoint ordering.

The saved Q_1 inverse ball per w is

`[4e18 +/- 1.53e17]`,

with upper/lower ratio below 1.5. The unweighted path inverse satisfies

`log10(C_path) in [136822211.62 +/- 0.00830]`.

The same-column maximum is particular to this fixed protocol and packet. No claim is made that it persists under a different spectral point, source norm, background or selected row family.

## 5. Error guarantee and its limitations

For any scalar perturbation e in this finite data space,

`Q_R(reconstructed source error)<=C_R ||e||_1`,

and C_R=R^6 C_1. In particular ||e||_1<=10^(-27) guarantees Q_1 error below 10^(-8)w.

The inverse uses exact E_j. If an implemented reconstruction uses approximate constants Ehat_j, its effective exact-coordinate residual is

`(E_j/Ehat_j)(z_j+e_j)-z_j`.

Acquisition, calibration and numerical inversion errors must jointly bound this residual before applying the theorem. The Arb enclosures certify the mathematical inverse norm; they do not themselves provide that implementation-error budget or guarantee that 10^(-27) acquisition precision is available.

Also, a small Q_1 error need not preserve a highly amplified diagnostic functional, small individual source coefficients, or a stronger common-path norm. Those require their own forward or inverse constants. The unweighted path inverse above makes this distinction quantitative.

## 6. Consequence for the broader conjecture

We have now proved finite-packet injectivity and a certified finite reconstruction bound for a specified joint observation protocol. This closes neither uniform conditioning across packets nor stable recovery in the full intersection topology.

The large contrast between the two norms is substantive. A source norm which measures actual forcing amplitudes discounts extremely late, tiny windows; an unweighted coefficient norm asks that their coefficients still be recovered accurately. Neither objective may be silently substituted for the other.

The next general theorem must specify the target source topology and the acquisition error norm before claiming stable all-depth reconstruction. The calculations here do not yet rule out a better sensor design, but they show that injectivity alone is inadequate evidence of useful recovery.

## Reproduction

`uv run --with python-flint --with sympy python research/nima/checkers/certify_joint_cubic_reconstruction.py`

Artifact: `research/nima/results/certified-joint-cubic-reconstruction.json`.

The run freshly repeats the 270-column exact kernel audit, encloses all required forcing and residual moments with complete-theta and integration tails, certifies both maximizing columns, and saves every row's conditioning enclosure.
