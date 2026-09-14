# The four-cusp flow must be read on the middle route difference

## Question

How can the four critical vertices produce the antisymmetric mixed detector without arbitrarily selecting one wall against the physical symmetry?

## Claim boundary

This packet determines the algebraic routing forced by the existing two commuting wall swaps. It does not yet identify the primitive half-difference with an admitted physical period record.

## Four critical vertices

The total-energy discriminant has four critical values

\[
E_0=0,
\qquad E_x=2x,
\qquad E_y=2y,
\qquad E_{xy}=2(x+y).
\]

They form the coherence square underlying the pyramid:

\[
E_0\longrightarrow E_x\longrightarrow E_{xy},
\qquad
E_0\longrightarrow E_y\longrightarrow E_{xy}.
\]

The two middle routes carry the labelled wall transports \(T_1\) and \(T_2\). On the canonical symmetric mixed state \(s_+=g_{101}+g_{110}\),

\[
T_1s_+=-s_-,
\qquad
T_2s_+=s_-,
\]

where \(s_-=g_{101}-g_{110}\).

## Correct information flow

The useful information is not the common endpoint value. Since \(T_1\) and \(T_2\) commute, completing both routes to \(E_{xy}\) gives the same diagonal transport and preserves the symmetric line. Endpoint equalization therefore erases the distinction.

The information must instead be read on the middle relative edge:

\[
\delta_{m mid}(s_+)
=
\frac{T_2s_+-T_1s_+}{2}
=s_-.
\]

Although the formula contains \(1/2\), the numerator is exactly \(2s_-\). Thus the half-difference is integral and primitive on the canonical symmetric source line. It is a primitive-closure operation, not rational rescaling of an arbitrary vector.

After this middle readout,

\[
s_-
\longmapsto
\frac1{4xy}(e_2-e_4)
-rac{2}{4x^3y^3(x+y)}v_{\rm alg},
\]

so the second primitive coordinate is nonzero away from its pole locus.

## Role of the missing coherence datum

The missing datum is the relative comparison that retains the difference between the two middle transports before endpoint descent. Its role is analogous to a transgression: a commuting endpoint square has zero ordinary path defect, while its normalized middle-edge difference carries the primitive odd class.

Accordingly, the flow must:

1. enter at \(E_0\) on the canonical symmetric mixed source;
2. split into the \(E_x\) and \(E_y\) arms;
3. apply the separately labelled transports \(T_1\) and \(T_2\);
4. take the primitive half-difference at the middle level;
5. send that odd class through the marked algebraic extension and \(v_{\rm alg}\) readout;
6. only afterward compare or descend toward \(E_{xy}\).

Taking the sum at the middle level reproduces the Bunch–Davies diagonal response. Waiting until the apex makes the two complete paths equal. Both orders lose the odd class.

## Disposition

The four vertices need not select one wall absolutely. They can produce the detector equivariantly by comparing the two labelled middle arms. The remaining theorem is that this primitive middle-route half-difference is carried by the physical relative-period/readout complex rather than only by the integral monodromy module.

Verification:

- `research/voevodsky/checkers/check_four_cusp_middle_route_difference.py`
- `research/voevodsky/results/four_cusp_middle_route_difference.json`
