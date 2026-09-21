# Ordered Volterra shell receiver: exact tails, admitted inverses, and a failed full-history gate

## Result

There is a concrete analytic algebra receiver built directly from the shell forcings. It reproduces all four degree-one Clark tails, preserves chronological products in its declared algebra order, and admits every finite event word and its comparison inverse without a small-increment hypothesis.

It nevertheless fails the requested full-history comparison:

- it kills reverse-ordered shell products;
- for the actual two-route arithmetic comparison it has D^2 nonzero but D^3=0, whereas the universal history has d^3 nonzero;
- its natural positive Hilbert pullback has an explicitly nonzero comparison-invariance residual.

This is a tested candidate and an exact obstruction to using that candidate as the faithful terminal-isometric Clark bridge. It is not a construction or refutation of the prescribed full Clark metric.

## 1. Source-derived operators and the four-tail readout

Fix finitely many disjoint increasing shells I_i within [0,R], and let

`f_i(x)=1_(I_i)(x) Phi(x)`.

Assume Phi is real and bounded on this finite interval, as for the completed smooth forcing. On H=L2([0,R]) define

`T_i psi(x)=integral_x^R f_i(t) psi(t) dt`.

These are bounded Volterra operators. Their images lie in H1([0,R]), with weak derivative -f_i psi and value zero at R. Extending the output by zero beyond R therefore gives an H1 half-line function.

For p_j(t)=t^j, j=0,1, the shell tails are exactly

`G_(i,sigma,j)(z;x)=exp(-sigma i z x) T_i[exp(sigma i z t) p_j(t)](x)`.

All multiplication operators in this formula are bounded on the finite interval. Endpoint evaluation is applied only after T_i, on its H1 output. No endpoint delta or ambiguous trace is introduced.

Thus the degree-one source, including both moment channels, is the same source as in `clark-sewing-tests-the-arithmetic-history-metric-through-the-full-kernel.md`. The existing endpoint matrix, mixed integration-by-parts identities, and forcing reservoir apply to these recovered tails. The construction does not replace their full divided-difference kernel by a Hilbert Gram matrix.

The new choice is the **higher-word receiver**: a tensor word is evaluated as T_(i_1)...T_(i_n). Its iterated integration region is x<t_1<...<t_n<R, so its algebra order agrees with the chronological ordering of the integration variables. Source/target arithmetic labels remain separate; this algebra evaluation alone does not supply the boundary-cocone attachment map.

## 2. An analytic source domain admitting all event inverses

Give V the l1 chamber norm and let M=max_i ||f_i||_infinity, with rho=RM>0. For v in V write f_v=sum_i v_i f_i and T_v=sum_i v_i T_i.

For any v_1,...,v_n, the iterated kernel and Schur's test give

`||T_(v_1)...T_(v_n)|| <= rho^n/n! product_k ||v_k||_1`.

Indeed its absolute kernel is bounded by

`product_k ||f_(v_k)||_infinity (t-x)^(n-1)/(n-1)!`,

whose row and column integrals are bounded by R^n times that product divided by n!.

Define the factorial-weighted analytic tensor algebra

`A_rho = {h : sum_n rho^n/n! ||h_n||_projective < infinity}`.

Since (n+m)!>=n!m!, these weights are submultiplicative. A_rho is a unital Banach algebra, and tensor polynomials are norm dense. The displayed operator estimate gives a unique bounded extension of tensor evaluation

`pi:A_rho -> B(L2([0,R]))`.

For every chamber vector v, without a size restriction,

`sum_n ||(-v)^n||_(A_rho) <= exp(rho ||v||_1)`.

Hence the geometric event inverse belongs to A_rho, and

`pi((1+v)^(-1))=(I+T_v)^(-1)`.

Finite event histories, their inverses, and comparison cocycles are therefore admitted. Their coefficients agree with the corresponding universal formal histories.

This is a **proper analytic subalgebra**, not a continuous evaluation of all degree-completed H(V). Arbitrary sufficiently fast-growing coefficients are excluded. Also, T_i^n is nonzero for every n when its shell forcing is positive; the receiver does not factor through one finite jet. Its norm continuity therefore does not contradict the formal-degree continuity theorem in `full-formal-history-obstructs-a-positive-clark-receiver.md`.

## 3. The price of ordered integration

For increasing disjoint shells,

`T_i T_j=0 whenever i>j`.

To see this, the outer integration variable lies in I_i, beyond the support endpoint of I_j, where T_j psi vanishes. Endpoints of adjacent shells do not affect this L2 identity.

Thus pi is not faithful. Tensor histories permit arbitrary ordered chamber words, including inverse/comparison terms, whereas this Volterra receiver retains only spatially nondecreasing words. Spatial shell order and abstract history order must not be identified silently.

There is also no Hilbert-star compatibility with eventwise comparison unitarity: the adjoint of T_i is a lower-triangular integral operator, not the upper-triangular series -T_i+T_i^2-.... No such compatibility was assumed in defining pi.

## 4. Exact actual-route comparison in the receiver

For the two prime routes from 2 to 12, merge the relevant consecutive chamber intervals into

- u: [log 2,log 4],
- v: [log 4,log 6],
- w: [log 6,log 12].

Here u,v,w now denote their Volterra operators, and w is the sum of the two original chamber operators on its interval. The independently prescribed event products are

`S_left=(1+u)(1+v+w)`,

`S_right=(1+u+v)(1+w)`.

They correspond respectively to the routes adding 2 then 3 and 3 then 2. Their difference is vw-uv. Reverse spatial products satisfy vu=wu=wv=0.

Set

`A=u(1+u)^(-1)`, `B=v(1+v)^(-1)`,

`D=S_left^(-1) S_right-1`.

Using the reverse-product relations and convergent event inverse series gives exactly

`D=Bw-Av(1+w)`,

`D^2=-AvBw`,

`D^3=0`.

For example, left multiplication by (1+v+w)^(-1) sends vw to Bw and leaves every term beginning with A unchanged, because vA=wA=0. Expanding the resulting D squared leaves only -AvBw; multiplying again gives zero since its final w kills either possible initial A or B.

If Phi is positive almost everywhere on these three intervals, D^2 is nonzero. The kernel of A within its shell is

`f_u(t) exp(-integral_x^t f_u(s) ds)`

for x,t in that shell, with the corresponding lower-endpoint formula when x lies before it. This kernel is positive; B has the same property. Applying AvBw to the positive vacuum 1 gives a nonzero positive function inside the first shell.

Thus the analytic receiver kills the specific nonzero universal d^3 established by the preceding checker, not merely some unrelated reverse word. Increasing the analytic jet order does not repair this loss.

## 5. The natural positive metric fails by a visible residual

Let J send (1,d,d^2) to (1,D1,D^2 1) in L2([0,R]). For positive forcing on the three shells these functions are linearly independent:

- 1 is nonzero on the last shell, where the other two vanish;
- D1 is nonzero on the middle shell, where D^2 1 vanishes;
- D^2 1 is nonzero on the first shell.

Consequently Q=J*J is positive definite. Since D^3=0, multiplication by 1+D acts on these columns through

`U=[[1,0,0],[1,1,0],[0,1,1]]`.

Using indices 0,1,2, the residual satisfies

`(U* Q U-Q)_(1,2)=Q_(2,2)=||D^2 1||_2^2>0`.

This is an exact failure of terminal-invariant isometry for this natural metric. It does not rely on fitting an invariant matrix or numerical near-zero decisions.

### Exact constant-forcing fixture

For three unit shells [0,1], [1,2], [2,3] with f_i equal to their indicators, direct integration gives

`D1(x)=-1-exp(-1)+2exp(x-1)` on [0,1],

`D1(x)=1-exp(x-2)` on [1,2], and zero on [2,3];

`D^2 1(x)=-exp(-1)(1-exp(x-1))` on [0,1], and zero elsewhere.

Therefore the residual entry is

`(-exp(2)+4exp(1)-1)/(2exp(4))>0`.

Its positivity also follows immediately from its integral as a nonzero squared norm. The checker independently evaluates the integral operators piecewise before computing this Gram matrix.

This positive L2 pullback is a candidate carrier metric only. It is **not** lambda_Clark, and its scalar entries must not be substituted for the prescribed full-kernel couplings.

## 6. What survives and what the next receiver must change

Survives:

- exact four-tail readout with a correct first-order domain;
- a specified analytic algebra and bounded evaluation;
- all finite arithmetic event inverses and comparison identities;
- a nonzero image of d^2 and explicitly retained mixed ordered integrals.

Fails:

- faithfulness to the full tensor history, already at d^3;
- a terminal-invariant natural positive metric;
- identification of any higher-word form with the prescribed Clark sewing functional.

Keeping the original tensor history beside pi(h) would preserve storage, but a form read only from pi(h) would still miss ker pi. This is the same distinction between faithful storage and a nondegenerate observable form encountered in the fixed-port obstruction.

The next source-compatible receiver must avoid annihilating abstract history words merely because their spatial shell labels decrease. One possible architecture is a retained ordered history register coupled to the Volterra tail readout. Its cross-degree observation must be derived from the full Clark sewing; an orthogonal tensor register alone still fails the previously established invariant-metric gate. No such coupled observation is constructed here.

## 7. Verification

`uv run --with sympy python research/voevodsky/checkers/check_ordered_volterra_history_receiver.py`

Passed:

- the exact comparison formulas in ordered quotient jets through degree eight;
- nonzero comparison square and zero cube in that quotient;
- independent direct piecewise Volterra evaluation of the fixture columns;
- exact Gram and nonzero invariance-residual calculation.

Certificate: `results/ordered-volterra-history-receiver.json`.

The all-order operator identities and analytic bounds are proved above, not inferred from finite jets. The fixture uses constant forcing, not a replacement normalization for completed theta. No numerical positivity claim about the arithmetic Clark kernel is made.
