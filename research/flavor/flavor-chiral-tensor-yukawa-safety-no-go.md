# Direct Chiral-Tensor Yukawa Safety No-Go

## Question

Does the Higgs-like Yukawa that directly contains the anomaly-essential chiral
tensor repair WP803's incidence failure while retaining a perturbative
interacting ultraviolet selector?

## Direct incidence

The generalized chiral theories admit a gauge-fundamental scalar (H) and

\[
y_k T^{ab}\widetilde F^k_a H_b+\text{h.c.},
\]

where (T) is the two-index antisymmetric or symmetric chiral fermion. Its
incidence vector on ((T,\widetilde F,H)) is ((1,1,1)). This passes the direct
chiral-incidence gate that the meson Yukawa failed in WP803.

## Exact fixed-flow audit

At one loop the Yukawa beta function has the form

\[
\beta_{a_H}=a_H(c_1a_g+c_2a_H),
\]

so its nonzero fixed flow has (a_H/a_g=-c_1/c_2). For finite (SU(5)), the
two sign conventions give the exact ratios

\[
\frac{a_H}{a_g}=\frac{24}{5}
\qquad\text{or}\qquad
\frac{a_H}{a_g}=\frac{36}{7}.
\]

Substitution into the two-loop gauge beta function gives

\[
\beta_g^{\rm eff}=a_g^2(b_0+b_1^{\rm eff}a_g).
\]

An interacting ultraviolet fixed point after loss of asymptotic freedom needs
(b_0>0) and (b_1^{\rm eff}<0). The exact conditions are disjoint:

\[
\begin{aligned}
x&>77/20, & x&<1601/1610,\\
x&>101/20, & x&<5107/2254.
\end{aligned}
\]

For each branch the upper bound from the effective two-loop coefficient lies
strictly below the lower bound from loss of asymptotic freedom. Hostile points
just beyond the latter boundary give negative interacting (a_g^*). Thus the
direct chiral-tensor Yukawa does not generate the perturbative safe fixed point
at the admitted order.

## What remains under complete asymptotic freedom

In the asymptotically free region, a fixed-flow ratio can rigidify the relative
decay of (a_H) and (a_g) toward the Gaussian ultraviolet point. It does not
select the normalization along that ray or the transmutation scale. It is a
relative-coupling rigidifier, not a nonzero interacting portal selector.

The published coordinate (a_H=y_H^2/(4\pi)^2) is sign-blind. With one Yukawa
hyperedge, the incidence complex has cycle rank zero, so there is no
rephasing-invariant orientation phase. A Higgs mass remains a free relevant
deformation, and no threshold completion or calibrated physical16 instrument
is provided.

## Contextual partition

Intrinsic fixed-flow probes determine the ratio (a_H/a_g) but retain the ray
coordinate, mass deformation, and detector calibration. On the packet
((r,m,\alpha_{\rm det})), their Jacobian has rank one and a two-dimensional
kernel.

## Classification

- Integer anomaly-complete chiral matter: present.
- Direct portal incidence on the chiral tensor: present.
- Interacting ultraviolet portal selector: absent at admitted order.
- Portal sign or phase: absent.
- RG scale and threshold: unselected.
- Physical16 instrument: absent.

## Smallest exact falsifier

The upper branch simultaneously requires (x>77/20) and
(x<1601/1610). Their positive separation is the smallest exact safety
obstruction. The lower branch has the same contradiction with (101/20) and
(5107/2254).

## Disposition

WP803 and WP804 expose complementary failures. The meson Yukawa can create a
safe fixed point but misses the chiral tensor; the Higgs-like Yukawa contains
the chiral tensor but cannot create the safe fixed point. A positive source
must make the same orientation-sensitive chiral interaction contribute with
the sign needed to generate its own irrelevant fixed-point direction. This
likely requires at least two coupled chiral Yukawa hyperedges, because a single
edge has no invariant phase cycle.

Verification:

- checker: research/flavor/checkers/wp804_chiral_tensor_yukawa_safety_no_go.py
- generated result: research/flavor/results/wp804_chiral_tensor_yukawa_safety_no_go.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp804_chiral_tensor_yukawa_safety_no_go.py
- primary source: [Mølgaard and Sannino](https://arxiv.org/abs/1610.03130)
