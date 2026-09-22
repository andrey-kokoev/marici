# Time-bin recalibration gives a finite-horizon near-optimal cubic observer

## Result

The finite-horizon implementation target is closed in the bounded-integral measurement model:

- 76 nonuniform time bins on [0,64];
- continuous piecewise-linear filters, with rational coefficients and normalizers;
- exactly recalibrated observer norm at most 1.04 times the FULL optimum;
- rational implementation norm upper bound at most 1.03 times that optimum, with separately certified calibration defects;
- the same 449 existing analytical blocks, and exact cancellation on all 268 zero source columns;
- no point-sampling, field-BV, or additional source-tail assumptions.

The rational norm upper bound is

    3.45349579 * 10^537 w_seam^2.

The two source calibration errors are below 0.00036 and 0.00076 per w_seam^2. At total independent response/joint-filter error 10^(-540), the positive margin remains greater than 0.05 w_seam^2 after calibration.

The acquisition values are bounded weighted BIN INTEGRALS, not point samples. Experimental ability to achieve the stated absolute noise remains an external requirement. No measurement data have been fabricated.

## 1. Recalibrate instead of reproducing the previous waveform

The earlier astronomical time estimate concerned uniformly reproducing a particular frequency-step filter to absolute error 10^(-540). That is unnecessary. A new bounded test can be calibrated on the actual prepared-window family, while preserving the exact same-window cancellation on all 270 source columns.

Write c=O(e,0), v=(0,0,0,e,0), e(u)=exp(-3u). Any common one-feature test theta with

    theta(c)=C_theta>0, theta(v)=h_theta>0

has actual prepared-window value

    n_theta(F)=sqrt(2) X_F [C_theta+h_theta(mu_F-L)].

The 192 private corrections cancel as identities of actual ordered window pairs, independently of theta. Thus the 256 target blocks and reserved positive block retain the exact source coefficient pattern.

With exact gains, the observer is feasible on the entire source corner:

    gain_x=S_x/[64 n_theta([2,20])n_theta([20,420])],
    gain_0=S_0/[n_theta(A_1)n_theta(B_1)].

For the constructed filter, |gain_0|<|gain_x|. Since ||theta||<=1, |gain_x| is an upper bound on its full response-dual norm. Comparing this bound with the certified full optimum gives the factor 1.04.

Rational gains approximate these two exact values. Their smaller reported norm is not used to pretend that a calibration defect improves the exact optimization problem.

## 2. Fit the damped bulk profiles using exact Euler-line moments

For either actual bulk label f, let g(u)=exp(-u)f(u), u>=0. For c, these profiles have Laplace transforms -H_+ and -H_- from the full-optimum certificate. The signs are the prescribed compression and negative-leakage signs.

Use thirteen exponential basis functions exp(-lambda_i u), with

    lambda_i=2^i, i=-3,...,10, i!=1.

The omission of lambda=2 avoids a removable divided difference at q=s. No spectral information is discarded: these functions are only a candidate test basis.

Their Gram matrix and moments are

    G_ij=1/(lambda_i+lambda_j),
    m_i=-H_+(3/2+lambda_i) or -H_-(3/2+lambda_i).

Acb evaluates the exact all-prime Euler-line formulas. An Arb solve proposes coefficients; the builder rounds them to dyadic rationals. All subsequent validation is for those actual rational coefficients, not an assumption that the rounded vector remains an exact orthogonal projection.

If k=sum_i a_i exp(-lambda_i u), then

    ||k||^2=a^T G a, <g,k>=a^T m.

The fitted projection responses are approximately 0.49061409 and 0.63646201. Existing all-prime bulk-norm enclosures rigorously control the remaining fitting error.

## 3. The finite time-bin filters

Use the initial interval [0,2^(-12)] and the eighteen dyadic intervals [2^j,2^(j+1)], j=-12,...,5. Divide each into four equal bins. This gives 76 bins, with widths between 2^(-14) and 8, ending at H=64.

At every node, round k's value to a multiple of 2^(-40). Set the final value at H to zero. Interpolate linearly and extend by zero beyond H; call the resulting function b. No value of the measured field at a node is required.

Its norm is evaluated exactly from rational coefficients:

    ||b||^2=sum_bins Delta (b_left^2+b_left*b_right+b_right^2)/3.

A rational nu strictly above ||b|| makes b/nu contractive. The filter is continuous at H and piecewise linear. Multiplying by exp(-u) puts its unweighted-pairing test in the admitted unrestricted-trace graph space. Thus it is an actual graph test, not just an abstract element of the response dual.

For each weak coordinate, perform the same construction from exp(-4u). Its source response is computed by elementary exponential integration. The endpoint test remains the prescribed swapped endpoint vector divided by a rational norm upper bound.

All five labels remain present. Their sum is a norm-at-most-one response-dual functional because the carrier has the labelled sum norm.

## 4. Certify the finite-filter response without a time-tail hypothesis on data

Both <k,b> and ||b|| are computed exactly up to Arb arithmetic, using integrals of an exponential times an affine function. Put

    d^2=||k-b||^2=||k||^2-2<k,b>+||b||^2,
    R^2=||g-k||^2=||g||^2-2<g,k>+||k||^2.

The certified all-prime bulk norm supplies an upper bound for R^2. Then

    <g,b>=<g,k>+<k,b>-||k||^2 + error,
    |error|<=R*d.

This bounds the finite filter's source response, including its entire missing time tail. It requires no pointwise tail estimate for arbitrary acquired fields. The measured filter itself is exactly zero after time 64.

The certified bulk interpolation errors are approximately 0.00211706 and 0.00220819 in L2. Summing the normalized bulk responses, endpoint response and weak-even response gives an enclosure printed as

    C_bin=[1.97 +/- 0.00310].

The weak residual response is approximately 0.35355092948. These replace the ideal C_even and h in the actual prepared-window formula. Fresh completed-theta calibration then certifies the two gains and their defects.

## 5. What is acquired

Let phi_j be the continuous nodal hat function, supported on its neighboring bins. The last node's coefficient is zero, so it requires no measurement. For each of the four field labels, acquire

    z_j=integral_0^64 phi_j(u) exp(-u) f(u)du,
    j=0,...,75.

These are bounded L2 functionals. Interior hats have squared L2 norm (Delta_left+Delta_right)/3; the first hat has the analogous one-sided formula. Fields may be rough or singular at zero within their declared L2 domain. Their point values are never evaluated.

Together with the two endpoint coordinates, one feature has 306 elementary measurement coordinates. The filter combines them with its explicit rational weights.

For ordered tensors, there are three supported acquisition interfaces:

1. Directly acquire the one bounded joint theta_bin tensor theta_bin reading per analytical block: 449 final readings.
2. Supply a genuine finite-rank decomposition or certified approximation, and evaluate by bilinear extension.
3. Supply the full joint elementary-integral matrix, not products of marginal readings.

The third option has 306^2=93636 entries per block, or 42042564 entries for all blocks. The 76-bin figure must not be mistaken for 76 scalar measurements of an arbitrary two-slot response. Direct joint filtering or justified low-rank structure avoids materializing that matrix; neither is silently inferred from marginal data.

## 6. Acquisition and arithmetic error

For elementary feature weights w_i and independently bounded scalar errors epsilon_i,

    feature_error <= sum_i |w_i| epsilon_i.

For joint entry errors epsilon_ij,

    joint_error <= sum_ij |w_i w_j| epsilon_ij.

The implemented dense joint API accepts a common absolute entry bound epsilon and returns epsilon*(sum_i |w_i|)^2. This error is not automatically the same as the original response-norm noise budget.

The observer sums errors across the 449 blocks, multiplies by its maximal gain, and retains Arb arithmetic radii. It defaults to 2048 bits because legitimate cancellations can span hundreds of decimal orders. The regression again resolves two readings of size 10^(-193) differing by 10^(-540).

The manifest carries rational filter and gain coefficients and is checked against the certificate's SHA-256 digest. The original conjugate-linear observation convention is implemented by final conjugation, not by changing ordered tensor bilinearity.

## 7. Reproduction and scope

Build and freshly certify:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/build_time_bin_cubic_observer.py

Run independent receiver tests:

    uv run --with python-flint python research/grothendieck/checkers/check_time_bin_cubic_observer.py

Evaluate acquired joint readings:

    uv run --with python-flint python research/grothendieck/checkers/evaluate_time_bin_cubic_observer.py observations.json

The CLI accepts the same 449-reading contract as the earlier receiver. Python APIs additionally expose the hat functions, elementary feature integrals, dense joint matrices, finite-rank tensors and acquisition-error propagation.

Artifacts:

- `results/time-bin-cubic-observer.json`;
- `results/time-bin-cubic-observer-certificate.json`;
- `results/time-bin-cubic-observer-tests.json`.

Tests verify exact rational filter norms, finite-support continuity, an analytic weak-field integral fixture, a nonfactorized joint matrix, error-budget rejection and high-precision cancellation. They are analytical fixtures, not claims of experimental acquisition accuracy.

The supplied vacuum-probe extension theorem remains separate. This degree-two filter does not acquire the new vacuum coordinate, alter its relative attachment, or assert that an adjacent pushout survives. Nor does finite cubic recalibration establish all-depth frame coherence or source summability.
