# Fixed-sixfold quadratic test: full Hodge norm versus divisor-only blindness

## Question and source

Fresh workbench action: cycle-pairing-faithfulness, independent of the multiplication-filler branch. Use the actual fixed X, polarization E and rational basis (E^3,R,I) of Hdg^3(X,Q) from hodge-explicit-sixfold-candidate-v1.md and hodge-middle-hodge-kernel-v1.md. No new variety or assumption about algebraicity is introduced.

SCC obligations: source pairing and orientation, primitive/Lefschetz decomposition, then readout kernel and phase comparison. The positive pairing is derived from the supplied polarization, not fitted to eliminate a residual.

## Orientation must be fixed first

Put e_j=dx_j wedge dy_j, d=(1,1,1,-1,-1,-3), E=sum d_j e_j and vol_mark=e_1 wedge ... wedge e_6. At the period-chart origin, the complex structure is standard on the three positive coordinate planes and reversed on the three negative planes. Its complex orientation is therefore minus the marked coordinate orientation. Along the path tZ to the selected period, positive-plane nondegeneracy is preserved, so this orientation does not change.

Thus integration over the complex-oriented X gives

    integral vol_mark = -1,
    E^6 = 6! product(d_j) vol_mark = -2160 vol_mark,
    integral E^6 = 2160.

Using plus marked orientation would wrongly make the polarization volume negative. This sign is not an adjustable normalization.

## Exact exterior pairing

Let U=product_wedge (dx_j+i dy_j), R=Re U, I=Im U. Each monomial of R or I contains one form from each coordinate pair, so E wedge R=E wedge I=0. Hence W=span(R,I) is primitive in degree six.

Exterior expansion gives

    R wedge R = I wedge I = 32 vol_mark,
    R wedge I = 0,
    E^3 wedge R = E^3 wedge I = 0.

On (E^3,R,I), the ordinary intersection form is therefore

    B_cup = diag(2160,-32,-32).

It is nondegenerate but indefinite. Over real coefficients it has nonzero isotropic vectors, for example (1,sqrt(135/2),0). This is not a kernel vector. No assertion that this displayed vector is rational is made.

## The actual positive quadratic form

For primitive type (3,3) in degree six, the Hodge-Riemann sign is (-1)^(6*5/2)=-1, so the polarized form is minus the intersection form on W. For the Lefschetz summand Q E^3, the sign is positive. Equivalently, for the Kähler metric with form E, Hodge star acts as +1 on E^3 and -1 on W. This is the standard Lefschetz/Hodge-star identity; the constant forms on the torus are harmonic.

Consequently the positive Hodge norm on the full fixed rational Hodge space is

    q_H(a E^3+bR+cI)=2160 a^2+32 b^2+32 c^2.

Its associated bilinear form has zero radical, and q_H(v)=0 iff v=0. In particular q_H(alpha)=32. There is NO nonzero dark input for this actual full polarized Hodge observer. This rejects that specific binding of the quadratic-dark-mode hypothesis, not every conceivable source readout.

A positive norm is not an injective scalar encoding: q_H(v)=q_H(-v), and entire equal-norm families can share the readout. It detects zero versus nonzero vector, not vector identity, route phase, domain membership or algebraic realizability. The cohomological comparison does not reconstruct a cycle witness.

## A real dark subspace appears under the restricted observer

The divisor-generated degree-six probes span only Q E^3 at the fixed X. Their intersection reader is

    B_div(v)=integral v wedge E^3=2160a.

Its kernel is exactly W. A squared divisor readout is therefore dark on alpha even though alpha has positive full Hodge norm. This is an actual source-derived incomplete observer, not an invented resource flag.

However, divisor products are not all algebraic codimension-three cycles. Kernel membership under B_div is not a proof that no algebraic cycle realizes alpha. Completeness of those probes on all algebraic classes would need a new theorem; on this source that would run into the same unresolved exceptional-cycle question. The positive full norm does not require supplying algebraic probes for R or I: it is a cohomological pairing, so it must not be relabeled algebraic tomography.

## Disposition and next discriminating test

Constructed: exact fixed-source cup matrix, primitive check, polarization sign and positive Hodge norm. Rejected at scope: a nonzero dark mode for the full positive Hodge pairing. Retained: an exact W kernel for divisor-only observation, with NO universal all-cycle conclusion. Raw indefinite self-intersection, positive norm, and scalar phase blindness have been separated.

The next useful comparison is whether a proposed witness-sensitive reader descends through the actual cycle-class map and whether its probe family is source-complete. Do not substitute the finite divisor library for all algebraic cycles or resume confirmation-directed cycle search. The separate multiplication-associator construction remains executable.

Verification: exact exterior arithmetic on twelve generators, all basis cross-pairings, a small rational positive-norm regression, zero/nonzero and phase controls, and wrong-orientation rejection. The full Hodge-space identification and Hodge-Riemann theorem are imported written results; they are not proved by these finite tests. No proof-assistant certification, independent review or Hodge verdict is claimed.
