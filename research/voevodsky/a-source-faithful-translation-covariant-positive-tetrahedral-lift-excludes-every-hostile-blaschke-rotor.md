# A source-faithful translation-covariant positive tetrahedral lift excludes every hostile Blaschke rotor

## Objective

State the exact conditional arithmetic theorem supplied by the hostile-rotor analysis.

The theorem does not construct the missing positive tetrahedral lift. It proves that any such lift, if source faithful and translation covariant, automatically removes every off-axis Krein--Langer defect. Thus the remaining positive-lift theorem has the intended spectral strength and cannot be replaced by a formal positive enlargement.

## Completed reflected multiplier

Let

\[
E(z)
=
\xi(1/2-iz)
+
\xi'(1/2-iz)
\]

in the established Suzuki normalization, and define

\[
\Theta(z)
=
\frac{E^\#(z)}{E(z)}.
\]

Assume \(\Theta\) belongs to the generalized Schur class on the selected half-plane and has Krein--Langer factorization

\[
\Theta
=
B^{-1}S,
\]

where \(S\) is Schur and \(B\) is the Blaschke product of forbidden poles, with no common inner factor.

For a finite divisor packet, \(B\) is finite. For an infinite packet, all statements below are first read on each finite subproduct and then on the observer-localized limit.

## Exact signed kernel

The completed kernel has the decomposition

\[
k_\Theta(z,w)
=
\frac{
k_S(z,w)
-
k_B(z,w)
}
{
B(z)
\overline{B(w)}
}.
\]

On the source core, write its form as

\[
Q_\Theta(f)
=
\|A_Sf\|^2
-
\|A_Bf\|^2.
\]

The hostile feature space is the model space

\[
K_B
=
H^2_+
\ominus
BH^2_+.
\]

Its dimension equals the forbidden divisor multiplicity for finite \(B\).

## Positive-lift hypotheses

Suppose the canonical eight-lattice tetrahedron admits a positive source-rooted lift with the following properties.

### Exact signed readout

The signed Green/trace readout of the positive lift equals \(Q_\Theta\) on the admitted source core. No divisor term is dropped or replaced by its absolute value.

### Douglas realization

There is a contraction

\[
C:
\overline{
\operatorname{ran}A_S
}
\longrightarrow
K_B
\]

such that

\[
A_B
=
CA_S
\]

on the source core.

### Bilateral translation covariance

Real source translations \(\tau_x\) are represented unitarily on the positive bulk:

\[
A_S
\tau_x
=
U_x
A_S,
\qquad
U_x^*U_x=I.
\]

The defect feature is intertwined naturally:

\[
A_B
\tau_x
=
V_x
A_B,
\qquad
CU_x
=
V_xC.
\]

### Source faithfulness

For every finite forbidden divisor packet, translated Gaussian observers detect its full value-and-jet space. Equivalently, \(A_B\) does not annihilate a nonzero finite model-space direction merely by source restriction.

These hypotheses are exactly the external physical positive-lift requirements. Internal addition of an arbitrary orthogonal rotor does not satisfy them.

## One forbidden coordinate

Let

\[
\rho
=
\alpha+i\beta,
\qquad
\beta\ne0,
\]

be one forbidden divisor coordinate. Under translation,

\[
\widehat{
\tau_xf
}(
\rho
)
=

e^{-ix\rho}
\widehat f(
\rho
).
\]

Hence the modulus of this coordinate is multiplied by

\[

e^{x\beta}.
\]

Choose a translated-Gaussian source packet \(f\) whose \(\rho\)-coordinate is nonzero. Contractivity and covariance give

\[
\begin{aligned}
\|V_xA_Bf\|
&=
\|A_B\tau_xf\|\\
&=
\|CU_xA_Sf\|\\
&\le
\|A_Sf\|.
\end{aligned}
\]

The right side is independent of \(x\), while the selected defect coordinate grows like

\[

e^{x\beta}
\]

in one translation direction. Therefore that coordinate must vanish.

Source faithfulness contradicts its vanishing.

Thus no forbidden coordinate with \(\beta\ne0\) can occur.

## Symmetry-completed orbit

For a conjugation/functional-equation pair \(\rho,\bar\rho\), the defect translation matrix has singular values

\[

e^{x\beta},
\qquad

e^{-x\beta}.
\]

Its determinant has modulus one, but its Hilbert operator norm is

\[

e^{|x\beta|}.
\]

Thus the paired rotor is Krein-unitary rather than Hilbert-unitary. Dagger completion does not remove the contradiction.

For the symmetry-completed hostile family, the rank-two model-space rotor is therefore forbidden by the positive covariant lift.

## Finite-packet conclusion

Every finite forbidden Blaschke subproduct must be trivial. Hence

\[
\boxed{
B_{fin}=1.
}
\]

Equivalently, the source-compressed kernel has no finite Krein--Langer negative square.

Since every nonempty discrete forbidden divisor contains a finite nonempty packet, source faithfulness excludes the full locally finite divisor:

\[
\boxed{
B=1
}
\]

provided the factorization and observer-localized infinite-product passage are valid.

## Kernel consequence

With \(B=1\),

\[
\Theta=S
\]

is Schur, and

\[
k_\Theta
=
k_S
\succeq0.
\]

Thus the generalized Schur kernel becomes an ordinary de Branges--Rovnyak kernel.

In the Suzuki specialization, the established Hermite--Biehler equivalence then supplies the corresponding critical-line conclusion.

This final implication inherits every normalization and hypothesis of that equivalence; the hostile theorem does not independently reprove Suzuki's arithmetic identification.

## Tetrahedral interpretation

A hostile rotor gives an exact finite-rank cell on all four signed faces:

1. \(H_{123}\): phase-energy rotor;
2. \(H_{134}\): model-space projection;
3. \(H_{124}\): exact Hardy transport;
4. \(H_{234}\): transported cutoff defect.

A positive tetrahedral filler would have to map its nonunitary translation character contractively into a unitary positive bulk. This is impossible unless the rotor cell is absent.

Therefore the positive eight-lattice tetrahedron is not compatible with a nonzero hostile sub-tetrahedron.

## No circular rotor insertion

Adjoining a positive discrete rotor sector by hand does not prove the theorem. Such a sector carries the same exponentially nonunitary translation character and cannot be a positive unitary subrepresentation under bilateral translations.

It may represent the signed defect in a Pontryagin or affine-clutched model, but it cannot supply the required global positive covariant absorption.

## Remaining theorem reduced

The arithmetic program is reduced to constructing a positive tetrahedral lift satisfying:

\[
\boxed{
\text{exact signed readout}
+
\text{Douglas contractivity}
+
\text{bilateral translation covariance}
+
\text{source faithfulness}.
}
\]

If such a lift is constructed without using the unknown divisor factor \(B\), the forbidden divisor is forced to vanish.

The construction of that lift remains the substantive positivity theorem.

## Scope boundary

This result is conditional on:

1. the declared completed-multiplier normalization;
2. Krein--Langer factorization of the reflected ratio;
3. the Suzuki Hermite--Biehler equivalence in the cited specialization;
4. exact identification of the physical signed readout with the completed kernel;
5. bilateral, not merely semigroup, translation covariance;
6. source faithfulness on every finite divisor packet.

Dropping any of the last three conditions opens a route for a nonfaithful or nonphysical positive model that does not imply the spectral conclusion.

## Disposition

The hostile rotor is now a decisive conditional obstruction:

\[
\boxed{
\text{source-faithful bilateral covariant positive lift}
\Longrightarrow
B=1
\Longrightarrow
k_\Theta\succeq0.
}
\]

For the completed Suzuki multiplier, this is exactly the bridge from a valid physical positive tetrahedral lift to the critical-line statement.
