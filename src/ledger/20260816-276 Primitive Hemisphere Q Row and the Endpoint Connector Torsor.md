# Primitive Hemisphere Q Row and the Endpoint Connector Torsor

Date: 2026-08-16  
Status: proved in the finite integral coefficient/carrier model. The literal
six-functor endpoint comparison cells and physical mapping fibre remain open.
No epistemic-graph admission is claimed.

Entry 275 corrects the former factor-two source obstruction: each labelled
octahedral hemisphere maps to the primitive relative long-facet row

\[
[-1,1,1],
\]

whose Smith form is \([1]\). This fixes the based generic \(Q\)-coefficient
sheetwise, but it does not fix the endpoint pointing.

The degree-correct unsplit endpoint row remains

\[
d_1=\begin{bmatrix}1&-1&-1&-1&-1\end{bmatrix}
:
P_{\rm sh}\oplus P_{\rm road}^{\rm or}\longrightarrow\mathbb Z_{\rm or}.
\]

For example, the two integral cycles

\[
z_+=(1,0,1,0,0),\qquad z_-=(0,1,-1,0,0)
\]

both lie in \(\ker d_1\). The primitive hemisphere row constrains neither
choice of endpoint comparison cell. On reflection cochains, changing an
integral sheet lift changes the coefficient by \(2a\), so the remaining
component invariant is \(b\bmod2\). Combining the independent primitive
\(Q\) row with this endpoint row gives Smith factors

\[
[1,2].
\]

Thus the hemisphere construction saturates the \(Q\) image but does not
select either point of the endpoint-fixed \(\mathbb Z/2\)-torsor. In
particular, it proves neither \(p_{\partial,Q}=0\) nor
\(p_{\partial,Q}=1\). The missing datum is still the pair of spatially
derived endpoint comparison cells in the same correspondence category as
the normalization-sheet map and the based literal entry143 \(Q\)-leg.

## Certificate

- `research/voevodsky/check_octahedral_hemisphere_endpoint_connector_torsor.rs`

~~~json
{
  "claim": "The primitive sheetwise hemisphere Q row and the endpoint reflection connector are independent finite rows; the former has Smith factor 1 while the latter retains Smith factor 2.",
  "status": "proved_scoped_finite_independence_and_nonselection",
  "scope": "finite integral coefficient/carrier complex after entry 275; literal six-functor BC excluded",
  "combined_snf": [1, 2],
  "hemisphere_Q_image": "saturated Z",
  "endpoint_component_torsor": "Z/2",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined",
  "D8_and_Jordan": "not testable before the pointed mapping fibre",
  "minimal_next_datum": "Derive both endpoint comparison cells and their based qSigma compatibility from one normalization/log-excess correspondence into literal entry143."
}
~~~
