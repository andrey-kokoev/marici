# Discrete source-actuator type no-go: WP1037

## Question

Can WP996-style control select the compatible WP1036 labels
\((k,C)=(2,23)\)?

## Object space is not command space

The labels \(k\) and \(C\) specify matter and operator multiplicities. They
therefore label distinct source theories. In the integer lattice, the open
unit ball around \((2,23)\) contains only \((2,23)\), so its authorized local
actuator has rank zero.

Replacing the actuator by \(I_2\) on \(\mathbb R^2\) gives formal rank two but
admits commands such as \((1/2,0)\), which leave the integer source domain.
This is the continuous-relaxation authority error highlighted by Aspect.

## Smallest exact falsifier

Changing \((2,23)\) to \((2,22)\) changes the pole coefficient by
\(6\pi^2/1367\). But it replaces an operator multiplicity; no common source
substrate or actuator executes that change. Distinguishability of the objects
does not create a control arrow between them.

## Aspect gates

The WP1036 packet supplies none of source_control_norm, source_bound_B, or
closed_loop_dual_error. WP997 gives the general actuator-metric theorem;
WP1037 identifies the sharper obstruction here: the proposed controls are
theory labels, not state coordinates.

## Claim boundary

This closes local or continuously relaxed actuation on the integer-label
model. It does not exclude discrete preparation operations inside a larger
common source theory.

## Disposition

Negative. WP996 cannot select WP1036. Reopening requires a common source
substrate whose executable operations realize the integer sectors and whose
cost/support ball is derived before optimization.

Checker: research/flavor/checkers/wp1037_discrete_source_actuator_type_no_go.py

Result: results/wp1037_discrete_source_actuator_type_no_go.json
