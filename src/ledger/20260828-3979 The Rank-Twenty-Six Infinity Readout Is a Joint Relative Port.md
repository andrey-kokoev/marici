# 3979 — The Rank-Twenty-Six Infinity Readout Is a Joint Relative Port

Status: retracted by Entry 3987. The endpoint non-descent premise was a projection artifact.

## Claim

For the physical five-mark rank-twenty-six quotient, the three infinity endpoint functionals do not descend separately, even after retaining every source-derived finite-part correction available through numerator degree seven.

The admissible next object is therefore a joint relative infinity map retaining compact elliptic and endpoint components together.

This is a finite-field theorem at the tested exact fibers, not yet a characteristic-zero global theorem.

## Frozen source expansion

On the chart
[
b=s^{-1},qquad a=t s^{-1},qquad w=W s^{-2},
]
write the five marked denominator factors as
[
q_r=s^{-1}\bigl(l_r(t)+s c_r\bigr).
]

Their product is
[
D(s)=D_0+sD_1+s^2D_2+cdots.
]

The compactified Cayley--Menger branch is
[
overline K=F+s^2G+O(s^4).
]

For a numerator of total degree (5+n), the logarithmic finite-part coefficient is derived from
[
[s^n]\frac{1}{D(s)sqrt{F+s^2G}},
qquad n=0,1,2.
]

Thus the tested grades are:

- degree five: direct logarithmic residue;
- degree six: first denominator finite part;
- degree seven: second denominator finite part plus the first Cayley--Menger correction.

No endpoint coefficient was chosen by solving the desired descent equation.

## Normalization guard

The formal Laurent engine exactly reproduces the independently derived degree-five rows. In the ordered monomial basis (i=0,ldots,5), they are

[
r_0=(-y^{-1},y^{-1},0,0,0,0),
]

[
r_{-1}=(z^{-1},-z^{-1},z^{-1},-z^{-1},z^{-1},-z^{-1}),
]

[
r_infty=(0,0,0,0,-x^{-1},x^{-1}).
]

This guards the branch choices, residue orientations, and infinity Jacobian.

## Exact result

At both primes
[
p=32009,qquad p=32003,
]
at the exact external point
[
(x,y,z)=(2,3,4),
]
the physical quotient has dimension twenty-six.

The number of nonzero raw endpoint coefficients by numerator degree is

[
\begin{array}{c|ccc}
&5&6&7\
hline
t=0&2&3&4\
t=-1&6&7&8\
t=infty&2&3&4
end{array}
]

so the higher finite parts are genuinely present.

For each endpoint, the completed constraint matrix has rank twenty-six, but its augmentation by the source-derived endpoint values is inconsistent. Therefore none of the three completed endpoint functionals descends separately through the physical exact relations.

## Interpretation

The failure is not caused by truncating at the direct degree-five symbol: degrees six and seven have now been included from the frozen compactification.

The narrow surviving architecture is
[
q_infty:
V_{m phys}^{(26)}
longrightarrow
W_{m compact}oplus W_{m endpoints},
]
where only the joint relative cocycle is expected to descend.

It is mistyped to demand independent quotient maps
[
V_{m phys}^{(26)}	o W_{0},qquad
V_{m phys}^{(26)}	o W_{-1},qquad
V_{m phys}^{(26)}	o W_{infty}.
]

The seven-plane comparison remains unauthorized until the compact elliptic component and all endpoint components are assembled into one source-defined primal map.

## Falsifier

Construct the compact elliptic finite-part rows in the same source normalization and append them to the endpoint packet.

Then test the joint primal map before dualization:

[
q_{m target}T=Uq_{m source}.
]

Possible outcomes:

1. The joint packet descends and transports naturally: a typed primal infinity quotient exists and may be dualized to a Leray covector.
2. The joint packet descends but fails cyclic naturality: the proposed source normalization is not occurrence-covariant.
3. The joint packet still fails descent: the present rank-twenty-six source complex omits a required relative boundary or exact-lift component.

No endpoint projector or compact correction may be fitted from the desired cancellation.

## Artifacts

- `research/benincasa/checkers/check_rank26_infinity_order2_endpoint_descent.py`
- `research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32009.json`
- `research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32003.json`

Sequence claim: `seqclaim-9d330000c8a85ec346fe8fa9`.