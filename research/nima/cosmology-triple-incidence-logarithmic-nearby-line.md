# The physical triple-wall collision has a canonical logarithmic nearby line

Put

\[
q_3=q_1+q_2+p,
\qquad p=x+y+3z.
\]

For the three ordered logarithmic pair symbols

\[
\omega_{ij}=d\log q_i\wedge d\log q_j,
\]

direct exterior algebra gives

\[
\boxed{
\omega_{23}-\omega_{13}+\omega_{12}
=p\,\frac{dq_1\wedge dq_2}{q_1q_2q_3}.
}
\]

Equivalently, after clearing denominators,

\[
q_1\,dq_2\wedge dq_3
-q_2\,dq_1\wedge dq_3
+q_3\,dq_1\wedge dq_2
=p\,dq_1\wedge dq_2.
\]

## Specialization and transverse class

At \(p=0\), the left side is the Orlik--Solomon circuit relation for three
concurrent affine lines.  Away from the collision the three degree-two pair
symbols are independent; on the collision the circuit removes one direction:

\[
3\longrightarrow2.
\]

The disappearing quotient is therefore canonically rank one.  Its oriented
vector is

\[
\boxed{(1,-1,1)},
\]

and its normalized transverse representative is obtained by dividing the
displayed identity by \(p\) before specializing.

This reproduces the same oriented line previously found in the resolved
principal Čech calculation, but now its provenance is the source wall
arrangement: it is the vanishing direction of the triple-incidence circuit.

## Scope

This constructs the universal logarithmic nearby line of the three-wall
arrangement.

The literal physical coefficient can also be restricted exactly.  On the
triple incidence,

\[
N_{\rm phys}=-\frac{2(x+y)}3,
\]

and

\[
K|_{p=0}
=\frac{64}{729}(x-2y)^2(x+y)^2(2x-y)^2.
\]

Thus the algebraic coefficient is generically nonzero, while the restricted
double cover splits over the function field of the incidence divisor.  Its
squared coefficient is

\[
\frac{6561}{256(x-2y)^4(2x-y)^4},
\]

a rational square.  The nearby object loaded by the form is therefore a
sheet-odd Kummer line rather than a new elliptic carrier.

This still does not show that an invariant \(\mu_2\)-trace or literal physical
chain activates that odd line.  Algebraic loading, deck descent, and Betti
selection remain distinct gates.

The literal-chain support gate can nevertheless be decided.  In the source
physical chamber,

\[
x=X_1>0,\qquad y=X_2>0,\qquad z=X_3>0,
\]

and therefore

\[
p=X_1+X_2+3X_3>0.
\]

The divisor \(p=0\) misses the strict positive chamber.  Its intersection with
the closed nonnegative chamber is only the all-soft origin.  Hence the literal
generic positive chain does not activate this nearby line.  A nonzero physical
period would require a separately derived analytic continuation or an all-soft
specialization; neither follows from the present source.

Horizontality of the algebraic twisted nearby line remains unproved, but it is
no longer a gate for the frozen generic physical contour: that contour has
zero support on the incidence divisor.

## Reproducibility

- `research/nima/checkers/check_cosmology_triple_incidence_logarithmic_identity.py`
- `research/nima/results/cosmology_triple_incidence_logarithmic_identity.json`
- `research/nima/checkers/check_cosmology_triple_incidence_physical_coefficient.py`
- `research/nima/results/cosmology_triple_incidence_physical_coefficient.json`
- `research/nima/checkers/check_cosmology_triple_incidence_positive_chamber_gate.py`
- `research/nima/results/cosmology_triple_incidence_positive_chamber_gate.json`
