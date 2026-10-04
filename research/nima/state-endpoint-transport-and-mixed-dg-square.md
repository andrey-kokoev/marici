# Independent state-index transport and its mixed DG square

## Question and result

Does the existing shared-leg source contain changes of one state index, rather than only diagonal XOR reanchoring?

**Yes, within the declared free DG model.** The existing leg witnesses change either state index independently. Their mixed routes have the same endpoints but differ by the boundary of an existing degree-two product. Thus q=i XOR j is preserved by the diagonal subgroup, not by all available source comparisons.

The exact audit passed 64 left changes, 64 right changes, 256 mixed squares, and 512 comparisons with the canonical reference witnesses. The mixed boundary is nonzero for all 144 squares in which both indices change. No additional generator was introduced.

SCC obligation: attachment transport and mixed route compatibility on the actual shared-leg DG presentation. This is not an assertion that the formal leg witnesses are physical interventions or that their adjunctions have been derived from the universal stable source.

## Source-native witnesses

In `checkers/check_shared_leg_dg_realization.py`, the state block has degree-zero maps

\[
x_i:A\to V_{\rm mid},\qquad y_j:V_{\rm mid}\to B,
\qquad D_{ij}=y_jx_i.
\]

Here V_mid is the intermediate object type, not the finite label group. Degree-one witnesses satisfy

\[
\delta h_i=x_i-x_0,\qquad \delta k_j=y_j-y_0,
\]

with h_0=k_0=0. For i'=i XOR g and j'=j XOR h, set

\[
a=h_{i'}-h_i,\qquad b=k_{j'}-k_j.
\]

The existing typed composites

\[
L_{i\to i';j}=y_ja,\qquad R_{j\to j';i}=bx_i
\]

obey

\[
\delta L=D_{i'j}-D_{ij},\qquad
\delta R=D_{ij'}-D_{ij}.
\]

These are degree-one comparison witnesses for actual shared-leg composites. They are not newly postulated endpoint morphisms in a physical carrier.

In origin/displacement coordinates o=i and q=i XOR j, left and right index changes give

\[
L_g:(o,q)\mapsto(o\oplus g,q\oplus g),\qquad
R_h:(o,q)\mapsto(o,q\oplus h).
\]

Their equal-parameter composite preserves q. Either one separately changes q when its parameter is nonzero. The earlier diagonal audit therefore tested a restricted family, not an isolation theorem for the q-fibers.

## The mixed square is filled, not strictly equal as a witness chain

Define the two composite witnesses

\[
K_{LR}=y_ja+bx_{i'},\qquad
K_{RL}=bx_i+y_{j'}a.
\]

Both have boundary D_(i',j')-D_(i,j). The existing degree-two product is

\[
F=ba.
\]

The DG Leibniz rule gives

\[
\delta F=(y_{j'}-y_j)a-b(x_{i'}-x_i)=K_{RL}-K_{LR}.
\]

This boundary is nonzero whenever both indices change in the tested free model. Hence natural leg-route witnesses do not commute strictly, even though their endpoint changes do. They have an explicit higher comparison already supplied by the source products. No assertion about all higher coherence degrees follows from checking this square.

## Relation to strict canonical reanchoring

The reanchoring checker uses a particular reference witness route

\[
H_{ij}=H_{00}+k_jx_i+y_0h_i.
\]

Its direct difference is

\[
\kappa=H_{i'j'}-H_{ij}.
\]

The natural leg routes compare with it through existing fillers:

\[
K_{LR}-\kappa=\delta(k_ja),\qquad
K_{RL}-\kappa=\delta(k_{j'}a).
\]

Thus the [strict XOR reanchoring result](reanchoring-xor-dg-action.md) and the present nonzero mixed boundary are compatible. Canonical differences telescope exactly; alternative leg routes retain additional degree-two comparison data.

The existing `reanchor` function can select any state anchor, including one in a different q-fiber. Fresh checks verify direct/staged current-payload equality for these cross-fiber choices too. Retained operation histories are still distinct.

## Disposition and next boundary

Problem: identify source-native cross-q transport. Conjecture: the existing independent leg witnesses supply it. Rival: only diagonal transport exists, or independent updates require an absent mixed filler. Falsifier: exact endpoint boundary and mixed-route comparison using the actual generators. Disposition: both independent transports exist, and the mixed filler is the existing product ba; strict equality of the natural mixed witnesses is rejected.

The search for cross-q comparison witnesses is therefore closed for this declared model. Their existence does not select a distinguished q or identify the direct reference with the marked primitive edge. It also does not extend the lattice readout to the mixed filler. The next comparison must preserve the distinction between canonical reference differences and natural leg-route witnesses, rather than discarding their nonzero boundary discrepancy.

## Verification

```text
python research/nima/checkers/check_state_endpoint_transport.py
```

The dependency-free checker reruns the baseline reanchoring audit and uses its actual maps, witnesses and differential. Result: `results/state-endpoint-transport.json`. Execution receipt: `structured_command_execution:e_25120_1790953710456090700_150`, exit code 0.

All 144 nondegenerate mixed boundaries are retained as deliberate counterexamples to strict natural-leg commutation. The identities involving canonical reference fillers hold for all 256 choices, including identity changes.

This packet and checker remain local and uncommitted. No commit, push, or deployment was performed.
