# Joint arrow/state probes carrying the matrix comparison response

## Exact coefficient adapter

Use the actual slot matrices C_s and fixed rung4 reference d4 as coefficients
of carrier probe functions psi_s on S4 x S4:

    R_field(g,h) = (1/137) sum_s psi_s(g,h)*(C_s-d4).

For the endpoint-fixing arrow probes and point-fixing state probes, this field
has an exact factorized construction. If X(g),Y(h) are probe-weighted arrow-leg
sums and S(g),T(h) are the state-leg sums, then

    R_field = [Y(h)*X(g)+T(h)*S(g)-N(g,h)*d4]/137,

where N is the sum of active slot-probe indicators. The multiplication order and
the distinct intermediate arrow/state spaces are preserved. The fixture supplies
d4=2I; its physical normalization is not derived by encoding it.

At the identity pair all137 probes equal1. Evaluating there recovers exactly
the original normalized matrix residual. This supplies a specified readout
back to the existing comparison model.

## Decode the two sectors and retain the kernel

Pairs of3-cycles fixing chosen individual states isolate all16 state responses.
Pairs of transpositions fixing chosen endpoint pairs then isolate36 arrow
reversal-class sums after subtracting the known state contributions.

Retain the within-class slot deviations to reconstruct all121 arrow responses.
These have85 independent coefficient directions per scalar response channel.
The full original137 matrix slots, and hence all named mixed rectangles, are
then recoverable.

Kernel retention matters: interchanging two reverse-arrow input maps preserves
the entire endpoint-fixing probe field and its mean, while changing a named
mixed rectangle. This is a valid change of the actual leg maps, not merely an
arbitrary change to independent slot coefficients.

## Probe averaging is not the same as slot averaging

Under uniform carrier averaging, an arrow-slot probe has mean1/144 and a state-
slot probe has mean1/16. Therefore the uniform average of R_field differs from
its identity evaluation. The original equal-slot rule is recovered by the
specified identity readout, not automatically by a uniform carrier ensemble.
This distinction must be respected when deriving an observation metric or
coupling normalization.

## Recursive closure of this probe choice

The initial52-dimensional scalar feature span is not closed under pointwise
multiplication. Two successive product-envelope constructions give

    52 ->113 ->121,

then stabilize. The last space is the tensor square of the11 independent
nonempty fixed-set indicators on one carrier. Adding a global constant reference
channel gives122 dimensions. These are linear feature-envelope dimensions;
they do not count independent physical parameters of the factored matrix data.
This closure is specific to the endpoint-fixing probe choice.

## A faithful marked-context alternative

A second joint adapter retains a reference ordered edge e0 and a state basepoint
k outside its endpoints. Use

    a_e(g)=1[g(e0)=e], e!=e0,
    p_i(g)=1[g(k)=i].

The eleven selected arrow probes and four state probes are jointly independent.
Their121 arrow-pair and16 state-pair products have rank137. An exact rational
decoder recovers every original matrix slot from the resulting field, including
the mean and named mixed defects. The reverse-arrow perturbation that the first
adapter hid is detected by this one.

The marked context transports equivariantly under carrier relabelling. Given
e0, there are two outside state-basepoint choices; the construction does not
select a preferred one. Choosing the state basepoint on e0 instead loses primitive
rank. Faithfulness therefore distinguishes these probe designs without assigning
a physical dynamics to the context.

## A new coherence test: readout versus composition

Faithful decoding is linear but is not automatically multiplicative for
pointwise carrier fields. The checker uses two valid single-leg perturbations
in disjoint rooted arrow contexts. Their pointwise residual product is zero,
while the product of their decoded means is nonzero:

    J(R2 * d4^-1 * R1) != J(R2) * d4^-1 * J(R1).

The mismatch is not caused by a reference change or missing slot data. It is a
failure to commute averaging with same-context multiplication.

Independently pairing slot contexts restores the equality exactly:

    sum_(i,j) w_j*w_i R2_j*d4^-1*R1_i
      = (sum_j w_j R2_j)*d4^-1*(sum_i w_i R1_i).

For arbitrary independently variable coefficient arrays, insisting on such an
all-pairs linear readout forces product weights w_j*w_i by coefficient matching.
This gives a conditional structural reason for an independent-context operation.
Another option is to retain the explicit multiplicativity defect as coherence
data. The test does not choose between those policies or derive the tower's
family generator from either one.

## Synthesis outcome

A joint observation can now reproduce the actual comparison response. There
are two checked implementations: an unmarked lossy probe map with complete
kernel records, and a faithful marked-context map. Their carrier averaging and
recursive product behaviour differ.

The next transport condition is precise: specify how comparison composition
crosses the probe/readout adapter. Independent contexts or retained coherence
corrections can make the resulting diagram accountable. Context selection and
the physical rung4 measurement law remain required inputs; no fine-structure or
other constant is derived by the feature counts.

## Verification

    python research/nima/checkers/check_joint_probe_response_adapter.py

Exact matrix-field factorization on all576 carrier pairs, explicit state/arrow
decoding,85 retained kernel directions, a valid hidden-leg perturbation,
identity versus uniform readouts, two feature-closure rounds, rank137 marked
adapter and exact decoder, marked-context covariance, and a multiplicativity
counterexample repaired by independent slot pairing.
