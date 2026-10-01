# Recursive extension through an invertible reference

## A return bridge using retained data

Declare a reversible-reference sector: the retained d:A->B has a strict inverse
r:B->A. Adjoin that inverse to the shared-leg DG path model, with

    delta(r)=0, r*d=id_A, d*r=id_B.

These relations respect the differential because d is closed. This is an added
invertibility assumption, tested explicitly; equal matrix dimensions alone do
not supply it. The construction uses no independent carrier copies and keeps A
and B as distinct endpoint types.

For any two graded records in Hom(A,B), define the one repeated operation

    Q star P = Q*r*P.

It is associative, degree-additive and has the retained d as its degree-zero
unit. The Leibniz differential extends to it. Existing two-leg paths can now be
concatenated through the return bridge, removing the previous depth-two bound.

## Comparison and reference propagation

For degree-zero comparisons C_i=d+rho_i, the reference propagates to d*r*d=d.
The composite residual is exactly

    rho_new = rho1+rho2+rho2*r*rho1.

Equivalently, normalized deviations e_i=r*rho_i satisfy

    1+e_new=(1+e2)*(1+e1).

The checker applies the same record law twice, retaining the original direct
reference and the full path expressions. If delta(h_i)=C_i-d, the two routes

    H_first=h2*r*C1+h1,
    H_second=C2*r*h1+h2

have the required composite boundary. Their difference is delta(h2*r*h1).
Thus the earlier higher-witness law is now applicable to the actual common
Hom(A,B) comparisons via the declared bridge.

## Genuine higher extension

Three existing degree-one witnesses give a nonzero degree-three cube
h3*r*h2*r*h1, with the correct signed boundary and boundary-of-boundary zero.

Starting with one original rectangle witness K=k_j*h_i, repeating the same
higher-product operation twice gives

    K, K*r*K, (K*r*K)*r*(K*r*K),

of degrees2,4,8. All three have nonzero tested responses and correct boundaries.
The last expression contains eight witness occurrences but only the original
two witness labels. Degree and occurrence doubling therefore require no new
independent parameters. This is a generated compositional extension, not the
independent relational-product construction with proposed class counts1,2,4.
It also does not derive the selected family-grouping rule from composition.

## A typed commutator

Both composition orders are now well-typed. Their difference is

    C2*r*C1-C1*r*C2 = rho2*r*rho1-rho1*r*rho2.

Reference and linear terms cancel. A nonzero exact example is checked. This
supplies the reverse composition that the earlier curvature analogy lacked,
within the reversible-reference sector. Identifying this order defect with a
physical curvature still requires a connection, transformation law and physical
observable. The test establishes endpoint-basis covariance of the bridge and
all higher responses, not a gauge-field identification.

## Scope and remaining choices

The reference inverse is determined once an invertible d is given. Singular d
is rejected; no pseudoinverse is substituted. A homotopy-inverse or partial-return
version would need its own unit witnesses, support rules and coherence checks.

The extension admits many words. It supplies a closure operation but does not
select which words to promote, which comparisons to schedule, or what measure
and cost to assign to them. In particular, no homology-doubling, conserved norm
budget or numerical coupling follows from the degree counts.

The next structural test is whether the carrier's retained round-trip data
justify a strict inverse, or instead require a witnessed weaker return. That
choice determines whether this recursive closure applies to the intended tower.

## Verification

    python research/nima/checkers/check_reference_bridge_recursive_extension.py

Exact rational and formal-path tests: strict inverse reductions, unit laws,
two recursive record applications, both witness routes, graded Leibniz signs,
a nonzero cube, degree2/4/8 products, boundary-of-boundary zero, dependency reuse,
zero-input control, typed commutator, endpoint-basis covariance and rejection of
a singular reference. The original shared-leg checker runs as a prerequisite.
