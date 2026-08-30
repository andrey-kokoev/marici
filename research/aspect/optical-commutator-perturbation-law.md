# Optical commutator perturbation law

The odd-intersection record is invariant under the smallest structural
transport that preserves the source pair: a common change of target basis,
independent scalar rephasing of each primitive, and use of the actual inverse
of every transported primitive.

Write

    X' = exp(i beta) U X U inverse
    Z' = exp(i alpha) U Z U inverse.

Then the balanced signal word is

    Z' X' Z' inverse X' inverse
      = U (Z X Z inverse X inverse) U inverse
      = minus identity.

The scalar phases cancel and centrality removes the common basis change.
Consequently every target state retains control record X equal to minus one,
Y equal to zero, and magnitude one. This is the positive transport law.

The smallest coherent breaking direction is one unmatched relative-phase
parameter. Replace only the forward Z by

    Z epsilon = diagonal(1, minus exp(i epsilon))

while retaining the old inverse Z in the return half. The signal word becomes

    diagonal(minus one, minus exp(i epsilon)).

For every nonzero epsilon modulo a full turn it is not central. The rail-one
target has Y equal to minus sin(epsilon), while rail zero still has Y equal to
zero. Thus one scalar mismatch simultaneously breaks the zero-Y prediction
and target-state independence.

The preregistered finite falsifier uses epsilon equal to 0.01 radians. It is a
source-level algebraic falsifier, not an assertion about an apparatus noise
floor. A physical run must separately preregister its uncertainty threshold.

This law concerns the reversible toric logical pair only. It neither constructs
interaction-net O or K lifts nor promotes the optical realization to the
interaction-net quotient.
