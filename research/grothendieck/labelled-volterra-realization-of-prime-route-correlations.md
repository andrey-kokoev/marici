# Labelled Volterra realization of prime-route correlations

## Result and boundary

The six four-prime probes have a continuous-signal realization on labelled L1 controls, with explicit continuity bounds and exact composition. Ordered unit-mass pulses reproduce the source-route probes independently of pulse shape and width. This realizes an enriched analytical measurement channel, **not** a decoder of the existing aggregate theta signal and not an independently established physical theta instrumentation interface.

Sources:
- `research/nima/prime-cube-faithful-observers-paths-relations-and-nested-reconstruction.md`
- `research/voevodsky/four-prime-correlation-observer-realization-and-minimality.md`

The labels and routes are admitted arithmetic source data. This construction does not generate primes from a bare coherence object.

## 1. Domain and operation

Fix an ordered compact interval I=[0,T]. Its coordinate orders source events; no physical-time interpretation is asserted. For each directed cube edge e retain a complex control x_e in L1(I). Let a_i,b_i be the six ordered edge pairs in Voevodsky's packet. Put

A_i(t) = integral_0^t x_{a_i}(s) ds,

B_i(t) = integral_0^t x_{b_i}(r) A_i(r) dr.

These are absolutely continuous, solve A_i'=x_{a_i}, B_i'=x_{b_i}A_i with zero initial conditions, and are unique by integration. In particular

B_i(T) = integral_{s<r} x_{a_i}(s)x_{b_i}(r) ds dr.

The integral exists by Fubini and the product L1 bound. A_i is uniformly bounded by ||x_{a_i}||_1, so the second differential equation has an L1 right-hand side. This is the continuous analogue of the thirteen-coordinate homogeneous observer, with its constant coordinate fixed to one.

## 2. Bounds and approximation

For every i,

|B_i(x)| <= ||x_{a_i}||_1 ||x_{b_i}||_1.

For two controls x,y, expanding the product gives

|B_i(x)-B_i(y)| <= ||x_{a_i}-y_{a_i}||_1 ||x_{b_i}||_1
                  + ||y_{a_i}||_1 ||x_{b_i}-y_{b_i}||_1.

Thus the six-output map is locally Lipschitz on the labelled L1 direct sum. Piecewise-constant approximations converge in output whenever they converge in that norm. This does not require discontinuous evaluation of a control at an event time.

The map is quadratic on controls, not linear. Its linearization is the bounded functional

K_i -> integral_{s<r} K_i(s,r) ds dr

on L1(I x I). A route-mixture measurement retains

K_i = sum_p c_p x^p_{a_i} tensor x^p_{b_i},

not the tensor square of the summed controls. The readout has norm at most one on each such L1 kernel channel. This specifies exactly which second-order information the enriched analytical source must retain.

## 3. Source-derived pulse embedding

For a directed route p=(e_1,...,e_k), choose successively ordered, disjoint interval supports and functions h_j with integral one supported there. Set x_e=sum_{j:e_j=e} h_j. They may be smooth compactly supported pulses; positivity is unnecessary for the exact identity. Then

B_i(x^p)= number of occurrences of a_i before b_i in p.

Proof: expand the double integral over the pulse supports. A pair of supports contributes one when the first precedes the second, zero when it follows. The selected first and second edge families are disjoint, so a pulse never pairs with itself. This also realizes repeated-event words. Unit pulse mass and strict support ordering, not a fitted energy identity, imply the result.

Different ordered pulse choices have the same six outputs. Hence this readout is independent of those choices, although the control embedding itself is not canonical. One can choose unit-width slots and a fixed smooth unit bump for a representative.

For all 168 admissible cube paths with nonnegative unit pulses, each selected pair occurs at most once. Consequently the linear readout from the path-counting source has the previously proved norms 2 on all routes and 1 on full routes. No corresponding norm is claimed in an unspecified physical source metric.

## 4. Composition and the mixture distinction

Concatenate labelled controls x followed by y. Denote the second-channel mass by M_b(y). Splitting the ordered integration triangle at the join gives

A(x*y)=A(x)+A(y),

B_i(x*y)=B_i(x)+A_i(x) M_{b_i}(y)+B_i(y).

This is precisely the source signature composition law. For route combinations X,Y the linear extension has the coefficient-sum factors:

B_i(Y composed X)=lambda(Y) B_i(X)+A_i(X) M_{b_i}(Y)+lambda(X) B_i(Y).

It is essential to distinguish a linear source mixture from physical superposition of its controls. In general B(sum c_p x^p) is not sum c_p B(x^p); it contains additional cross terms. The implementation and checker include a one-panel counterexample.

## 5. Exact constant-panel implementation

For constant first/second controls a,b on a panel of width d, the exact update is

A_new=A_old+d a,

B_new=B_old+d b A_old+(d^2/2) b a.

The last term is required when both controls are present simultaneously. Applying the discrete event update blindly on such panels would omit it and violate subdivision invariance.

Implementation: `research/grothendieck/correlation_volterra_observer.py`.

Exact checker: `research/grothendieck/checkers/check_correlation_volterra_observer.py`.

The checker compares all 168 source paths with the existing streaming observer, tests every path cut, varying rational pulse widths, overlapping signed-channel subdivision, and the equal-edge collision. The continuum estimates above are analytic proofs, not consequences of those finite tests.

## 6. What this closes, and the next actual gate

Closed: a bounded kernel-channel realization and continuous L1 control realization of the six source probes, with an exact compositional pulse adapter. The positive route mixtures 0123+1032 and 0132+1023 have identical edge counts but different enriched outputs, with difference (1,0,0,0,0,0).

Not closed: construction of these channels from the independently prescribed physical theta source. Any observation factoring only through additive edge/interval data still identifies that collision and cannot supply these outputs, even by a nonlinear deterministic decoder.

The next interface must expose either labelled pre-aggregation controls or their route-conditioned ordered two-point kernels, prove continuity in its own source norm, and commute with source concatenation. It must not substitute the tensor square of an averaged theta signal for the averaged route tensor. This is a concrete acceptance test for the analytical adapter, not another abstract coherence requirement.
