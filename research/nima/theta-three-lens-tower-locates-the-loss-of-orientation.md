# The three-lens tower locates the loss of RH orientation

## Recognition

Kitaev's three route-effect lenses are exactly the three algebraic levels that have appeared in the theta programme:

1. additive current;
2. invertible scalar transport;
3. ordered state transformation.

The RH lane has concrete representatives at all three levels.

| Lens | Algebra | Theta representative | Retained information |
|---|---|---|---|
| Additive | additive commutative monoid | endpoint, gamma, primitive, square, and connected logarithmic currents | accumulated scalar increment |
| Scalar multiplicative | \(GL(1,\mathbb C)\) | determinant line, Tate gamma transition, completed scalar section | scalar gain, phase, divisor |
| Ordered transformation | \(\operatorname{End}(V)\) or \(GL(V)\) | reciprocal transport, tail–seam system, ordered port \(S\) | state action, order, domains, commutators |

This is not merely an analogy. The familiar scalar constructions are the decategorifying maps between the lenses.

## Carrier versus evaluator

The Carrier and the coefficient lens perform different jobs. The Carrier supplies the typed route

\[
e_1\longrightarrow e_2\longrightarrow\cdots\longrightarrow e_n
\]

and determines which local operations are composable. The lens supplies the evaluation law for the effects transported along that route:

\[
\begin{aligned}
\text{additive:}&\quad e_1+\cdots+e_n,\\
\text{scalar multiplicative:}&\quad e_1\cdots e_n,\\
\text{ordered transformation:}&\quad e_n\circ\cdots\circ e_1.
\end{aligned}
\]

Thus shared Carrier geometry does not imply shared operational semantics. A commutative additive or scalar lens generally erases route order, whereas an endomorphism lens can retain it through noncommuting composition. More precisely, the Carrier supplies compositional syntax and the lens supplies effect-composition semantics: its identity, cancellation or inversion laws, replay behaviour, order sensitivity, and closed-loop observable.

This gives a finite typing test. If a claimed observable changes under permutation of the route while its declared coefficient law is commutative, it is not an observable of that lens. Conversely, equality after additive or determinant projection is not evidence that two ordered transports agree.

## Downward maps are lossy

For an invertible finite-dimensional operator \(U\), determinant gives

\[
U\longmapsto\det U.
\]

Logarithmic differentiation then gives

\[
\det U
\longmapsto
\partial_z\log\det U
=
\operatorname{Tr}(U^{-1}\partial_zU).
\]

Thus the observational direction is

\[
GL(V)
\longrightarrow
GL(1,\mathbb C)
\longrightarrow
(\mathbb C,+).
\]

The reverse direction is not canonical. An additive current can be integrated and exponentiated only after choosing constants, branches, and normalization. A scalar multiplier cannot reconstruct which state transformation produced it.

Most importantly, determinant kills commutators:

\[
\det(ABA^{-1}B^{-1})=1,
\]

and trace kills additive commutators:

\[
\operatorname{Tr}[A,B]=0.
\]

Therefore ordered noncommutative information is exactly what disappears first.

## RH interpretation

The completed logarithmic derivative lives in the additive lens. It records the exact sum of endpoint, gamma, and prime currents. That establishes provenance.

The completed section \(\Xi\) lives in the scalar multiplicative lens. It records the divisor and reciprocal scalar sewing.

The odd forcing port

\[
S=-2D^{-1}
\]

lives in the ordered transformation lens. It records occurrence order, reciprocal character, dilation degree, domain, and the constant-mode boundary extension.

The persistent gap is now structurally explained:

> The additive and scalar lenses cannot reconstruct the ordered port whose orientation they have erased.

This is why the following routes were necessarily circular or incomplete:

- deriving positivity from the completed logarithmic derivative;
- deriving operator orientation from the scalar functional equation;
- deriving ordered seam data from a determinant or overlap;
- treating matching scalar cumulants as authority for an operator incidence.

They ask a lower lens to recover information discarded by the projection into that lens.

## Correct construction direction

An explanatory RH architecture must be built from the ordered lens downward: source-authorized ordered transport, then its determinant-line section, and finally its additive logarithmic currents. First construct the state action and its domains; then derive its scalar determinant; only afterward take the logarithmic current.

The already completed arithmetic comparison verifies the bottom projection. It does not construct the top object.

## Lens-crossing authority

Every crossing needs its own constructor.

### Ordered to scalar

A determinant, Fredholm determinant, relative determinant, or distinguished overlap requires:

- a declared operator class;
- a domain and completion;
- a determinant-line normalization;
- control of anomalies and boundary modes.

### Scalar to additive

A logarithmic current requires:

- nonvanishing on the local chart;
- a branch or differential formulation;
- endpoint and regularization conventions;
- preservation of source labels before aggregation.

Transporting an equality across either crossing does not authorize an inverse reconstruction.

## Location of the new ordered-port theorem

The relations

\[
DS=SD=-2I,
\]

\[
RSR=-S,
\]

and

\[
U_a^{-1}SU_a=a^{-1}S
\]

belong wholly to the ordered lens. Their scalar shadows do not retain the reciprocal-character exchange or the degree-\(-1\) action.

Grothendieck's Hardy-boundary calculation identifies the archimedean crossing: Fourier transform does not commute with half-line projection, and their commutator supplies a universal boundary operator. It still has no prime labels. The missing arithmetic constructor is a labelled adelic sampling-to-Hardy incidence before scalar determinant formation.

## Cross-sector confirmations

Benincasa's filtered occurrence packet is erased by coarse residue exactly as the odd ordered port is erased by reciprocal trace.

Figueiredo's invisible flavor direction changes the pole signature while vanishing under the physical16 projection. This is another failure of a lower lens to determine a higher one.

Aspect's temporal integrator realizes the ordered port physically, while its measured scalar transfer function is only the multiplicative lens and a metric accumulation is the additive lens.

These parallels do not identify the sectors. They exhibit the same typed loss pattern.

## Finite falsifier for a claimed inverse crossing

Suppose two ordered transformations \(A\) and \(B\) satisfy

\[
\det A=\det B
\]

and have the same logarithmic determinant current, but

\[
A^{-1}B
\]

acts nontrivially on the source state or has a different commutator with reciprocal reflection. Then neither lower lens determines the ordered constructor.

The smallest generic witness is a determinant-one shear. It is invisible in both scalar lenses but changes state transport.

## Disposition

Kitaev's lens typing reveals the architecture we were already encountering without naming it. RH orientation, if source-derived, must originate in the ordered transformation lens. The determinant section and the additive prime currents are its shadows. They can verify a proposed ordered construction, but they cannot generate one.
