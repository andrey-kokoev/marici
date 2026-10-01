# Comparison routes and quartic readout descent

## Records: rebracketing preserves content and retains history

The independent Cartesian comparison constructor extends to operands of unequal
arities. This extension permits the five binary bracketings of four ordered
factors. Each leaf retains its factor ID; each internal record retains its
ordered parent pair. Decode/encode transports between bracketings reconstruct
exactly the same named primitive tuple.

The checker exhausts12^4=20736 full-relation arrow quadruples through all five
bracketings:103680 reconstructions. Factor exchanges together with rebracketing
give120 routes; their named content also agrees. The five ordered bracketings
have distinct recorded parent histories.

This establishes content-level route equivalence. Identifying those histories
operationally is a policy choice. A history-sensitive observable can distinguish
them and must declare that dependence.

## Which quartics descend?

Under independent signs and balanced-tree exchanges, the previous rank4 basis
was A=sum x_i^4, B=x0^2*x1^2+x2^2*x3^2, and
C=(x0^2+x1^2)*(x2^2+x3^2). A coefficient-weighted readout

    alpha*A + b*B + c*C

descends across all paired factor routes only if b=c. Changing the pairing
changes B while B+C=sum_(i<j) x_i^2*x_j^2 remains fixed. Testing a state where
two nonzero coordinates are siblings in one pairing and separated in another
forces equality of the two coefficients.

Thus fully exchange/rebracketing-invariant quartics in this class have the form

    F(x)=alpha*sum_i x_i^4 + beta*sum_(i<j) x_i^2*x_j^2.

The two coefficients remain free. Restricting admissible routes to a retained
tree permits distinct sibling and cross-block coefficients instead.

## One associative composition law

Let Q(x)=sum x_i^2. A composite interface carrying (Q,F) can use

    (Q,F) * (R,G) = (Q+R, F+G+beta*Q*R).

Its associator vanishes by the exact identity

    beta*Q*R + beta*(Q+R)*S
      = beta*R*S + beta*Q*(R+S).

Starting with (x_i^2,alpha*x_i^4) at each leaf produces the descended quartic
above for every binary bracketing. Interchanging operands also preserves it.
A coupling chosen by the current tree depth fails even ordered rebracketing;
the checker supplies an explicit counterexample.

There is an additive coordinate:

    H = F - (beta/2)*Q^2,
    H(comparison) = H(left)+H(right).

The bilinear merge term is a coboundary of this coordinate change. Composition
coherence therefore does not by itself distinguish a physical interaction from
a nonlinear readout of additive retained data. That requires specifying which
observable and coordinate normalization the system physically uses.

## Differential return agreement

The descended readout has gradient

    dF/dx_i = 4*alpha*x_i^3 + 2*beta*x_i*(Q-x_i^2).

Recursive differentiation gives this same vector on all tested routes. With
a chosen Euclidean coordinate metric, its least-change DIFFERENTIAL return is

    delta_x = delta_F * gradient(F) / ||gradient(F)||^2

when the gradient is nonzero. It satisfies the requested linearized increment
and is route-independent. A finite nonlinear target needs a separate solver;
this formula does not claim exact finite replacement of F.

## Structural result and next link

Retained histories and content-equivalent comparison routes can coexist.
Readouts insensitive to those histories must satisfy a composition law; the
quartic example reduces to two coefficients and an associative interface.

The next quantitative link is to induce the orientation-coordinate metric from
the retained member or comparison-cell edit cost. The present return test chooses
Euclidean coordinates. Connecting the two metrics will determine whether the
same route-independent return is obtained from actual retained-record updates.

## Verification

    python research/nima/checkers/check_comparison_route_coherence.py

103680 reconstruction checks,120 routes with explicit histories,9720 exact
quartic/gradient checks over81 states, differential return constraints,
associator identities, an additive-coordinate identity and depth-dependent
negative controls. Alpha=3/2 and beta=5/3 are test coefficients; the algebraic
composition proof applies to arbitrary rational coefficients.
