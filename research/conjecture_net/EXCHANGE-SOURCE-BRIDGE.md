# Retained exchange source → metric-spectral realization

Implementation: `exchange_source_bridge.py`.
Contract: `contracts/exchange-source-bridge.v1.json`.

## Source discovery changes the target

The existing six exchange port updates are **reversible involutions**, not dissipative maps. Their mismatch metric G=K^-1 is positive, and `T_i^T G T_i=G`. The exported encoder E and decoder D satisfy ED=DE=I22 and

`E raw_i D=I16 direct_sum T_i`.

Thus a faithful target retains sixteen conserved anchor coordinates plus six evolving mismatch coordinates. Compressing the entire source into the Bool C4 witness would discard information. The bridge uses C16⊕C6 with the transported source metric instead; it does not equate these two sources or derive a universal physical carrier.

The underlying tail/head feature policy, Gram metric and initial preparation remain the **existing conditional adapter premises**. Source provenance is retained, not upgraded to source-only uniqueness or physical selection.

## Faithful coordinate and record bridge

The implementation reads the exported encoder, decoder, reduced updates and metric using exact rationals. It independently reconstructs the raw exchange operators from the original feature rule `f_ab=(e_a tensor e_b)/11`, metric `(10I4+J4) tensor (10I4+J4)` and the actual port registry. It checks the full intertwining square, not only matching endpoint values.

The transported full metric is block diagonal: an anchor metric plus G. Dropping the anchor loses reconstruction, even though it is fixed by every exchange. Dropping mismatch loses the active noncommuting response. The new target retains both.

The actual source port registry determines admissible words. Execution validates all seams before recording any occurrence, retains occurrence identity and before/after state, and maps each matched word to the identical ordered operator product. Repeated executions get distinct batch/occurrence IDs. Numerical inverse reconstruction uses retained history; it does not equate AB with the independently labelled BA port.

The existing six-step and twelve-step ABC cycles have the same source/target but different full exchange actions. Their rank-two difference and the externally supplied AB-record preparation witness remain distinguishable through the bridge. No equality/coherencer is fabricated merely from common endpoints. The mismatch commutator images retain rank six, so the earlier no-go for a faithful global map into commuting fixed gates is not evaded by erasing response.

## Source-generated metric-unitary spectral legs

For an involution T satisfying `T^T G T=G`, multiplying by T proves `T^T G=GT`. Consequently

`Q=(I-T)/2`, `Q^2=Q`, `Q^T G=GQ`.

Q and I-Q are orthogonal projections for the G inner product. The **uniform declared** spectral rule

`U(t)=(I-Q)+exp(-i*pi*t)Q`

therefore gives `U(t)* G U(t)=G`, `U(0)=I`, `U(1)=T` and `i U'(t)=pi Q U(t)` in ordinary complex analysis. These general written identities do not require whitening, square-root approximations or fitted generators. Exact rational phase controls support the algebra; they are not an all-time analytic proof by sampling.

This is a new standard-complex extension of the sourced metric-involution pattern. It is **not** an operational Agda completion implementation on C6, nor is it imported automatically from the Bool kernel certificate. The added continuous parameter is an analytic realization choice, not an independently supplied physical duration or switchable control.

## Metric Hamiltonian realification

For H=pi Q, GH is symmetric. Set x=(q,p),

`E_H(x)=(q^T GHq+p^T GHp)/2`,

`Pi_G=[[0,G^-1],[-G^-1,0]]`,

`Omega_G=Pi_G^-1=[[0,-G],[G,0]]`.

Then `Pi_G grad E_H=(Hp,-Hq)=R(-iH)x`, and the vector-field matrix preserves Omega_G. The checker verifies these identities coefficientwise with the common pi scalar retained symbolically. G=I gives the previous Hamiltonian convention; the sign of the symplectic form is consistent with the displayed Poisson matrix.

## What this synthesizes—and what it does not

The Bool and exchange instances now share a **finite metric-involution → spectral dynamics → retained-record → Hamiltonian** construction pattern. The exchange instance supplies a second, actually noncommuting sourced operation family rather than hypothetical extra C4 actuators.

This is common structural grammar with faithful maps **within each source instance**. A common physical witness, cross-source overlap maps, preparation/measurement authorization, phase-framed coherent actuation and empirical tests remain open. In particular, typed ports do not authorize arbitrary free switching among all six generators. No u(6) physical-control claim follows from their existence.

The source receipt/dependency hashes and primary source code are checked live. This audit recomputes exact finite identities without rerunning the historical SymPy/NumPy producer; it does not claim a fresh kernel proof or new physical admission.

```sh
python research/conjecture_net/check_exchange_source_bridge.py
python research/conjecture_net/test_exchange_source_bridge.py
```
