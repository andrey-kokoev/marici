# Theta parity-channel transport and an absolute-noise obstruction

## Results

Grothendieck's eighteen two-point and six four-point coordinates admit an exact parity-channel readout. The two-point kernel is precisely the six-dimensional block-parity space previously found with labelled edges.

The completed calculation supplies:

1. exact transported parity readouts and the hidden-space projector;
2. a visible-baseline subtraction formula for the four-point coordinates;
3. the analytical noise Gram of these readouts in the declared theta metric;
4. high-precision Gram diagnostics with independent quadrature checks;
5. a rigorous lower bound: every exact decoder of the normalized parity channels from the two-/four-point theta response has operator norm greater than 10^67000 in the unweighted direct-sum L² metric.

The algebraic reconstruction is exact. Its absolute-noise stability depends critically on the theta atom amplitudes.

## 1. Exact source and measurement coordinates

Use the same ordered twenty-four full routes as `research/grothendieck/results/minimal-theta-four-point-completion.json`. Let

\[
y=\begin{pmatrix}y_2\\y_4\end{pmatrix}=M c,
\qquad M\in\operatorname{Mat}_{24}(\mathbb Z),\quad\det M=1.
\]

Here y₂ consists of the eighteen selected interval tensor coordinates and y₄ of the six selected fourth-degree coordinates. The checker reconstructs M directly from the event-segmented interval signatures and checks it against the recorded inverse.

Index the six parity blocks by ordered pairs of unordered pairs:

\[
((0,1),(2,3)),\ ((0,2),(1,3)),\ ((0,3),(1,2)),
\]
\[
((1,2),(0,3)),\ ((1,3),(0,2)),\ ((2,3),(0,1)).
\]

Let K have the corresponding four-route alternating sums as columns. Then

\[
K^T K=4I_6,
\qquad B=K^T/2,
\qquad P=KK^T/4.
\]

B gives orthonormal source parity coordinates and P is the route-counting orthogonal hidden-space projector. The entire two-point tensor map annihilates K and has rank eighteen. Thus its kernel equals im K.

The transported readout is

\[
\boxed{b=Bc=R_2y_2+R_4y_4,\qquad (R_2\ R_4)=BM^{-1}.}
\tag{1}
\]

All entries are exact rationals, recorded in `research/voevodsky/results/theta-hidden-channel-transport.json`.

## 2. Isolating the six hidden channels

Let M₄ be the last six rows of M and put Q=M₄K. Direct calculation gives

\[
Q=\begin{pmatrix}
1&0&0&0&0&0\\
1&1&0&0&0&0\\
0&1&1&0&0&0\\
0&1&0&1&0&0\\
0&1&1&1&1&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]

Its determinant is one, and

\[
R_4=2Q^{-1}.
\]

Define the visible prediction matrix

\[
S=-\tfrac12 Q R_2.
\]

Then

\[
\boxed{b=2Q^{-1}(y_4-Sy_2).}
\tag{2}
\]

Sy₂ is exactly the fourth-degree readout of the route-counting visible component (I−P)c. Thus y₄−Sy₂ isolates the hidden contribution before the final change to orthonormal parity coordinates.

The hidden route packet is

\[
c_{hidden}=\tfrac12 Kb.
\]

In measurement coordinates the projector is

\[
\Pi=MPM^{-1}
=\begin{pmatrix}0&0\\-S&I_6\end{pmatrix}.
\tag{3}
\]

The checker verifies Π²=Π and

\[
\Pi^T W=W\Pi,
\qquad W=M^{-T}M^{-1}.
\]

W is the transported route-counting metric. The unweighted measurement-coordinate metric and the physical theta-response metric are distinct metric choices. Orthogonality in (3) is asserted for W.

## 3. Analytical readout and its noise Gram

The fifteen logarithmic interval atoms have endpoints

\[
2,4,6,10,12,14,20,28,30,42,60,70,84,140,210,420.
\]

Use the source atom

\[
\Phi_1(v)=e^{v/2}(2\pi^2e^{4v}-3\pi e^{2v})e^{-\pi e^{2v}}
\]

and

\[
H_i(s)=\int_{\log a_i}^{\log b_i}\Phi_1(v)\Phi_1(v+s)\,dv,
\qquad s\ge0.
\]

Let H synthesize these atoms into L²(ds), let G=H*H, and let L=G⁻¹H*. The imported finite independence theorem gives LH=I. The tensor measurement is

\[
\Theta_r=H^{\otimes r}K_r.
\]

Let P₂ and P₄ select the declared coordinate tuples. The exact analytical parity readout is

\[
\boxed{
\mathcal T(\Theta_2,\Theta_4)
=R_2P_2 L^{\otimes2}\Theta_2
 +R_4P_4 L^{\otimes4}\Theta_4.
}
\tag{4}
\]

Let ℓ_i be the i-th coefficient functional of L. Their Gram is G⁻¹. Hence the Gram of the selected degree-r product functionals is

\[
(D_r)_{\alpha\beta}
=\prod_{j=1}^r(G^{-1})_{\alpha_j\beta_j}.
\]

For the direct-sum norm on L²((0,∞)²) ⊕ L²((0,∞)⁴),

\[
\boxed{
\mathcal T\mathcal T^*
=R_2D_2R_2^T+R_4D_4R_4^T.
}
\tag{5}
\]

This computes the absolute-noise amplification of the specific selected-coordinate implementation on the full observation space. The rigorous lower bound in section 6 applies to every exact parity decoder on the admitted source image.

## 4. Stable evaluation of the atom Gram

Direct floating-point evaluation underflows on most of these atoms. We factor out their dominant exponent before integrating.

Put r=e^(2s), A=a², B=b², and c=π(1+r). Substitution t=e^(2v) gives

\[
H_{[a,b]}(s)=\frac{\pi^2}{2}r^{5/4}
\int_A^B t^{3/2}(2\pi t-3)(2\pi rt-3)e^{-ct}\,dt.
\tag{6}
\]

It is a linear combination of upper incomplete gamma functions of orders 5/2,7/2,9/2. Define F_i(r) by

\[
H_i(s)=e^{-\pi(1+r)a_i^2}F_i(r).
\]

The implementation evaluates exp(x)Γ(q,x) using the half-integer recurrence beginning with sqrt(π)exp(x)erfc(sqrt(x)). Finite upper endpoints are retained exactly in this formula.

Normalize temporarily by H_i(0), writing h_i=H_i/H_i(0). With z=π(a_i²+a_j²)(r−1),

\[
\langle h_i,h_j\rangle
=\frac1{2\pi(a_i^2+a_j^2)}
\int_0^\infty e^{-z}
\frac{F_i(r)F_j(r)}{F_i(1)F_j(1)r}\,dz.
\tag{7}
\]

Gauss–Laguerre quadrature is therefore performed on moderate scaled quantities. Physical norms and dual norms are restored logarithmically.

The checker uses 65 decimal digits and quadrature orders 24,48,72. The largest relative Gram change from 48 to 72 is approximately 8.4×10⁻⁵⁵. A separate direct scaled integral verifies the incomplete-gamma formula on three representative atoms. These are high-precision convergence diagnostics, not interval enclosures.

## 5. Numerical conditioning in the declared metric

The unit-norm atom correlation Gram has

\[
\lambda_{min}\approx2.6311114845\times10^{-7},
\quad\lambda_{max}\approx8.3404260045,
\]

and condition number approximately 3.169925×10⁷.

The physical atom norms have a vastly larger range. Selected base-10 logarithms are:

| interval lower endpoint | log₁₀ ||H_i||₂ |
|---:|---:|
| 2 | −8.18785 |
| 10 | −265.93429 |
| 60 | −9811.89902 |
| 70 | −13358.87585 |
| 140 | −53469.73446 |
| 210 | −120323.11925 |

For the six parity outputs in the stated order, the computed log₁₀ norms of their analytical readout functionals are approximately

\[
10251.7166,\quad10948.7454,\quad21425.6304,
\]
\[
12366.5942,\quad24152.0373,\quad67109.6623.
\]

The largest selected product functional comes from the fourth-degree tuple (0,3,11,13). Formula (5), together with max diagonal ≤ λ_max ≤ trace, gives numerically coincident displayed brackets

\[
\log_{10}\|\mathcal T\|\approx67109.6623.
\tag{8}
\]

The result file retains the separate lower/upper computations and every quadrature refinement. The equality of displayed digits indicates extreme dominance by the last channel; it is not an assertion of an exact equality between the two bounds.

## 6. A rigorous lower bound independent of quadrature

The large amplification is already forced by the source response, independently of the particular coordinate inverse.

### A bound on one interval response

For v≥log 2, Φ₁(v) is positive and

\[
\Phi_1(v)\le2\pi^2e^{9v/2}e^{-\pi e^{2v}}.
\]

Enlarge the upper endpoint to infinity. Using t=e^(2v), r=e^(2s), A=a², and c=π(1+r),

\[
H_{[a,b]}(s)
\le2\pi^4r^{9/4}\int_A^\infty t^{7/2}e^{-ct}\,dt.
\]

Since (A+z)^(7/2)≤A^(7/2)exp(7z/(2A)),

\[
\int_A^\infty t^{7/2}e^{-ct}\,dt
\le\frac{A^{7/2}e^{-cA}}{c-7/(2A)}.
\]

Use e^(2s)≥1+2s and c≥2π to obtain

\[
H_{[a,b]}(s)
\le\frac{2\pi^4a^7}{2\pi-7/(2a^2)}
e^{-2\pi a^2}e^{-(2\pi a^2-9/2)s}.
\]

Therefore

\[
\|H_{[a,b]}\|_2
\le\frac{2\pi^4a^7e^{-2\pi a^2}}
{(2\pi-7/(2a^2))\sqrt{4\pi a^2-9}}
<(2a)^7e^{-2\pi a^2},
\qquad b>a\ge2.
\tag{9}
\]

For the last inequality, π<4 and π>3 suffice: the first denominator exceeds 5, the square-root denominator exceeds 1, and 512/5<128. The right side decreases with a for a≥2.

### A unit hidden source packet

Take

\[
u=K_{:,5}/2.
\]

It has unit route norm and Bu=e₅. Its four routes first traverse labels {2,3} in either order and then {0,1} in either order. With actual primes (2,3,5,7), their edge starting labels are bounded below coordinatewise by

\[
(2,10,70,140).
\]

The full two-point tensor annihilates u, which the exact checker verifies. Its fourth-degree response is a signed half-sum of four product functions. By (9) and the triangle inequality,

\[
\|\Theta_4(u)\|
<2\prod_{a\in\{2,10,70,140\}}(2a)^7e^{-2\pi a^2}.
\tag{10}
\]

Here Σa²=24604 and the polynomial prefactor is

\[
2(16\cdot2\cdot10\cdot70\cdot140)^7<10^{50}.
\]

Use the rational bounds π>157/50 and log 10<2303/1000. They have elementary certificates: the Machin arctangent identity with alternating-series bounds proves the former, and the first seventeen positive terms of exp(2303/1000) already exceed 10, proving the latter. The checker verifies these rational inequalities and

\[
2\frac{157}{50}\cdot24604
>67050\frac{2303}{1000}.
\]

Consequently

\[
\boxed{\|(\Theta_2(u),\Theta_4(u))\|<10^{-67000}.}
\tag{11}
\]

Every exact linear parity decoder T must send this response to e₅. Hence

\[
\boxed{\|T\|>10^{67000}.}
\tag{12}
\]

This is an analytic lower bound with exact rational certificates. It requires no numerical Gram estimate and holds even when the decoder is defined only on the admitted finite source-response image.

The positive and negative parts of u are each mixtures of two routes with coefficient 1/2, hence each has total mass one. Thus (11) also describes two normalized positive mixtures whose parity coordinates differ by one while their two-/four-point responses are extremely close in this norm.

## 7. Implications for the measurement architecture

The exact channel identification is complete: equations (1)–(4) turn the selected theta measurements into the six source parity channels, and equation (3) supplies the transported projector.

The raw unweighted theta metric makes some admitted source differences exponentially small. Detector rescaling changes the response units and the corresponding noise metric together. A stable implementation therefore needs a declared gain/noise model, a source-weighted metric with justified operational meaning, or a different source-level correlation channel.

The unit determinant certifies exact coefficient recovery. Equations (8) and (12) quantify the separate absolute-noise question in the specified analytical metric. The lower bound applies to the whole admitted reconstruction problem, while (8) evaluates the particular selected-coordinate implementation.

The source must still supply event-segmented, route-conditioned multipoint responses. This work computes the exact decoder and its metric behavior once those responses are available.

## Verification and files

Exact transport and norm-obstruction certificate:

```
uv run --with sympy python research/voevodsky/checkers/check_theta_hidden_channel_transport.py
```

Scaled analytical diagnostics:

```
uv run --with mpmath python research/voevodsky/checkers/check_theta_hidden_channel_gram.py
```

Results:

- `research/voevodsky/results/theta-hidden-channel-transport.json`
- `research/voevodsky/results/theta-hidden-channel-gram-diagnostics.json`

The exact checker verifies the source matrix, full two-point kernel, transported readout, projector identities, baseline subtraction, and the rational inequalities supporting (12). The analytical checker reports its precision, quadrature refinements, scaled-formula comparison, normalized Gram, and physical readout norms. Only the explicitly labelled diagnostics depend on floating/high-precision numerical quadrature.
