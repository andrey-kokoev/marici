# Finite-mesh escape fields have a certified end-to-end L2 budget

## Result

A finite piecewise-exponential field now approximates the normalized finite-prime response with a certified GLOBAL ordinary-L2 error.

For the raw receiver prior ||f||_D1<=M, M>0, use

    P=100000, R=8, mesh width delta=1/100, N=800,
    profile tail length S=16.

Suppose the 800 source cell averages are supplied with discrete L2 error at most 0.001M. The finite field constructed below satisfies

    ||P^(-1/2)T_P E_+f - finite_field||_2 <0.74M,

even allowing an additional independently bounded global L2 evaluation error of 0.0005M. No zero endpoint trace is imposed.

The bound includes the already certified finite-prime/profile error, source truncation, averaging, coefficient noise, and both profile tails. The script recomputes the underlying Arb cutoff certificate rather than trusting a stored decimal.

A concrete nonzero-trace exponential input produces an artifact with 800 exact rational coefficients. Its actual profile discretization error is independently enclosed below 0.000091 by integrating exponential polynomials, not by sampling a response grid.

## 1. Approximate the source in a norm the profile maps control

More generally, let gamma>1/2 and

    ||f||_Dgamma^2=integral_0^infinity exp(2gamma x)
                                   (|f(x)|^2+|f'(x)|^2)dx <=M^2.

Divide [0,R] into N equal cells of width delta=R/N. Write c_j for the true cell mean and ctilde_j for its supplied approximation. Assume

    eta^2=delta sum_j |ctilde_j-c_j|^2

is bounded. Define g to equal ctilde_j on cell j and zero outside [0,R]. Orthogonal cell averaging and the cell Poincare--Wirtinger inequality give

    ||f-g||_L2(R_+) <= M[exp(-gamma R)+delta/pi]+eta,
    ||g||_2 <= M+eta.

The spatial tail follows from the source weight. The averaging estimate uses the derivative of the actual f, not a derivative of the step function g. The discrete noise norm is exactly the L2 norm of the coefficient error field.

The surrogate g need not belong to the original strong source domain. We apply ONLY the bounded profile maps J_- and J_+ to it, not the arithmetic operator T_P. The latter remains applied to the original admissible f throughout the theorem.

Both profile convolution kernels have L1 norm two. Therefore

    ||E_P E_+f-E_P E_+g||_2 <=4||f-g||_2.

This is forward propagation of independently supplied SOURCE cell data. No recovery of those averages from arithmetic outputs is inferred.

## 2. A finite analytic mesh, not an unevaluated convolution

Put x_j=j delta and q=exp(-delta/2). The exact nodal values A_j=J_-E_+g(x_j) and B_j=J_+E_+g(x_j) satisfy

    A_0=0, A_(j+1)=q A_j+2ctilde_j(1-q),
    B_N=0, B_j=q B_(j+1)+2ctilde_j(1-q).

Inside cell j, for 0<=s<=delta,

    A(x_j+s)=exp(-s/2)A_j+2ctilde_j[1-exp(-s/2)],
    B(x_j+s)=exp(-(delta-s)/2)B_(j+1)
                       +2ctilde_j[1-exp(-(delta-s)/2)].

Outside [0,R], their only nonzero pieces are

    A(t)=A_N exp(-(t-R)/2), t>=R,
    B(t)=B_0 exp(t/2), t<=0.

Thus finitely many coefficients determine the entire exact pair of profiles. No numerical convolution or arbitrary interpolation rule is required.

Retain A only on [0,R+S], and B only on [-S,R]; set them to zero elsewhere. Call these finite-window functions A^fin and B^fin. Their translated sum is

    F_(P,R,N,S)(u)=A^fin(u+log P)+B^fin(u-log P).

This is a finite piecewise-exponential representation on the union of two shifted meshes and two truncated tail cells. Overlaps are summed; they are not assumed disjoint. The prime cutoff and its shift log P remain the prescribed ones.

## 3. Exact profile-tail control

The discarded tails have norms

    ||A-A^fin||_2=|A_N|exp(-S/2),
    ||B-B^fin||_2=|B_0|exp(-S/2).

Cauchy--Schwarz in the defining integrals gives |A_N|,|B_0|<=||g||_2. Hence

    ||E_P E_+g-F_(P,R,N,S)||_2
       <=2exp(-S/2)(M+eta).

One may instead use the sharper data-dependent value exp(-S/2)(|A_N|+|B_0|) after enclosing the nodal recurrences. The uniform theorem does not require such an improvement.

## 4. Compose every error in the same ordinary-L2 norm

Let c_P be an independently certified cutoff/profile coefficient on unrestricted half-line H1 balls:

    ||P^(-1/2)T_P E_+f-E_P E_+f||_2 <=c_P M.

The preceding Arb theorem certifies c_P<0.72 at P=100000. If a numerically realized field differs from the exact finite representation by at most epsilon_eval in global L2, then

    total error <=c_P M
       +4M[exp(-gamma R)+delta/pi]+4eta
       +2exp(-S/2)(M+eta)+epsilon_eval.

All terms now have the same target norm. The formula does not add a pointwise error tolerance to an L2 budget without a conversion.

For gamma=1, R=8, delta=0.01, S=16, eta<=0.001M and epsilon_eval<=0.0005M, Arb encloses the displayed bound using the conservative c_P=0.72 by

    0.73924584214003 M <0.74M.

The source mesh and tail part before the optional evaluation error is approximately 0.01874584214M. The cutoff error dominates this particular certified budget; finer meshing alone is not claimed to reduce that bound.

The finite exact representation needs no additional evaluation error in its mathematical definition. A software renderer or sampled measurement claiming to realize it must independently justify any epsilon_eval it uses.

## 5. Concrete finite-field artifact and independent fixture check

Use

    f(x)=sqrt(2/5)exp(-2x).

Its weighted D_1 norm is exactly one and its trace is nonzero. It is an admitted raw receiver input, not an asserted theta window or arithmetic kernel source.

The script encloses all exact cell averages with Arb. It proposes rational coefficients with denominator 100000000, then independently certifies their collective error with interval arithmetic. Floating-point rounding is used only to propose those rationals; no sign or error conclusion depends on it.

The artifact records their 800 integer numerators, denominator, mesh, exact symbolic recurrences, support endpoints and output shifts. It therefore determines an actual finite field rather than a list of unchecked floating samples.

For this input the exact profiles are

    J_-E_+f(t)=(2/3)sqrt(2/5)[exp(-t/2)-exp(-2t)], t>=0,
    J_-E_+f(t)=0, t<0,

    J_+E_+f(t)=(2/5)sqrt(2/5)exp(-2t), t>=0,
    J_+E_+f(t)=(2/5)sqrt(2/5)exp(t/2), t<0.

On each mesh or tail cell, the difference from the finite representation is an exponential polynomial. Its squared integral is a finite sum of elementary exponential integrals, enclosed directly by Arb. Infinite remaining tails are integrated analytically. The sum of the two profile-error norms is enclosed near

    0.00009090186816335.

This also bounds their translated-sum error, without dropping an overlap cross term. The coefficient-data error is below 8.16e-9. These are additional fixture checks, not substitutes for the uniform prior-ball proof.

## 6. Source operations and other certificates remain separate

Nima's convex-height projections preserve the actual path-source operations. The receiver cell-averaging map here is NOT asserted to preserve those operations, ideal powers, or prepared-letter compatibility. It is only an approximation device inside the bounded linear profile calculation.

Likewise Voevodsky's prior-controlled tower and attachment certificates concern specified source quotients and finite labelled observers. This theorem approximates a raw receiver field from a stated receiver prior and cell data. It does not turn response noise into source coefficients, identify arbitrary noisy data with a source, or assign a derived class to the mesh surrogate.

The arithmetic response, all included prime powers, fixed gamma term, and endpoint conventions are unchanged. The finite field approximates the existing normalized finite response; it is not a new all-prime subtraction or an ordinary-L2 limit of unnormalized responses.

## Reproduction and artifacts

    uv run --with python-flint python research/grothendieck/checkers/certify_finite_escape_field.py

The command first reruns the 192-bit Arb cutoff certificate. It then writes:

- `research/grothendieck/results/finite-escape-field.json`: exact finite field representation;
- `research/grothendieck/results/certified-finite-escape-field.json`: rigorous error enclosures and checked inequalities.

Input:

`research/grothendieck/arb-certifies-uniform-escape-on-unrestricted-half-line-prior-balls.md`.
