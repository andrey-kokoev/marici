# Segmented unchanged-copy transport has a synchronized reference-mode plane

**Strength:** conditional finite graded construction and exact invariant-subspace identities. Positive structural transport result; not two independent photons, a physical evolution, a derived preparation or a formal outcome admission.

[Previous retained-word test](RETAINED-WORD-TRANSPORT.md) · [Checker](check_segmented_copy_transport.py) · [Receipt](results/segmented-copy-transport.v1.json)

## 1. A different existing source operation

The preceding additive and repeated-primitive multiplicative readouts failed. They do not exhaust the existing retained-path operations.

The [retained path ledger](../../nima/retained-path-family-composition-synthesis.md) also supplies **unchanged-copy extension**: concatenate a retained path with a compatible right operand whose coefficient is one. Its coefficient remains the starting path's coefficient, while both operands and the complete word stay registered.

We use that actual API on each composite, rather than assigning a new coefficient to a photon-labelled output. In the existing primitive order

    (a,b,c,d,e,f,g,h,i,j)
      =(AB,BC,CD,DE,EA,AEp,EpDp,DpC,CB,BA),

the two displayed-edge readouts become

    q1 = (a,b,i,c,e,a),
    q2 = (f,h,i,i,j,a).

For example, CE=(CD,DE) inherits c, not c+d or c*d; DE appears as a registered neutral extension operand. This operation does **not** consume the supplied d coordinate as the extension coefficient. The original primitive input d must remain a separate residual; similarly g is not used as the coefficient of the EpDp extension in ADp.

The resulting linear Q:Q^10→Q^12 has rank eight. Keeping the residuals (d,g) restores rank ten. This is lossless bookkeeping with retained provenance, not a claim of a physical isometry. Neutral extension operands are explicit supplied records.

## 2. Derive the invariant image before selecting photon modes

Construct K directly from endpoint-compatible continuation of the two supplied displayed triangle pairs, with their pair labels retained. K is block diagonal with the two actual six-occurrence endpoint-incidence matrices. There are twenty allowed macro-transitions in total. No spectrum or desired mode is fitted into K.

The image of Q is characterized by four equalities:

    q1[5]=q1[0],  q2[5]=q1[0],
    q2[2]=q1[2],  q2[3]=q1[2].

Not every Qx remains in this image under K. Exact compatibility checks give:

- after one step, require b=h and e=j;
- after two steps, additionally require a=f and c=i;
- these four conditions suffice at every further step.

In source-coordinate form, the maximal stable readout therefore satisfies

    f=a, h=b, c=i, j=e.

Its dimension is **four**; unused d,g remain residual input directions, not extra output dimensions. The checker verifies maximality through constraint ranks and separately gives an invariant embedding, so this is not merely stability observed for a few iterates.

On the common source roles (a,b,i,e), the induced matrix is derived from endpoint incidence:

    M = ((0,0,1,1),
         (1,0,0,0),
         (1,1,0,0),
         (0,0,1,0)).

If H embeds these roles into the twelve displayed occurrences, then

    K H = H M.

This construction precedes the comparison with the reference photon plane.

## 3. Positive result: synchronized reference-mode transport

Now compare with the independently recorded reference plane and its existing step

    T = ((-1/2,1/2),(-3/2,-1/2)),   T^3=I.

The four-dimensional common-role carrier contains the rational plane

    (a,b,i,e) = (-s,(s+t)/2,s,-(s+t)/2).

Writing its embedding as Z, the exact identity is

    M Z = Z T.

With the same shared-edge relabellings used in both earlier audits, HZ is exactly the pair of reference frames with parameters

    (s,t,u,v) = (s,t,s,t).

Thus both proposed output patterns support the **same synchronized two-parameter mode**, and its macro-continuation returns after three steps. The checker verifies K(HZ)=(HZ)T and K^3(HZ)=HZ directly.

There is also a maximality statement. The instantaneous intersection of im Q with the direct sum of the two reference planes is three-dimensional: only u=s is initially required. Requiring continuation to remain compatible adds v=t. The largest invariant reference-plane sector is therefore **two-dimensional**, not four-dimensional.

This is a genuine change from the previous shortcuts: the synchronized mode is nonzero and survives continuation. It is nevertheless one common mode displayed twice, not a construction of independently variable photon outputs or a tensor-product two-photon state. The input restrictions and selection of this mode still require preparation; generic primitive coefficients do not satisfy them.

## 4. A finite controller makes the segmentation explicit

One macro-edge uses either one or two primitive arrows. To implement the chosen dictionary without hiding this grading, construct a finite controller with:

- twelve boundary states, one for each pair-labelled macro-edge ready to execute;
- six internal states, one for each length-two composite in progress;
- every transition labelled by its actual owner-labelled primitive arrow.

A length-one word executes its primitive arrow and reaches a permitted next boundary state. A length-two word executes its first arrow into its own internal state, then its second arrow into a permitted next boundary state. All twenty macro-transitions arise this way; the checker verifies the endpoints of every micro-transition.

With boundary and internal coordinates separated, the primitive-step matrix is

    P = ((A,B),
         (D,0)).

The exact first-return generating transfer to the boundary is

    F(z)=z A + z^2 B D,
    A+B D=K.

Here z records primitive step count, not physical energy or time. Evaluating at z=1 forgets elapsed lengths and recovers one macro-event's endpoint incidence. It does not identify P with K. For example, two micro-steps have boundary block A^2+BD: two short macro-events and one long macro-event are different histories.

The reference plane's three-macro-step return is not a three-micro-step return for the checked boundary-only initialization. All pair, path and segment data must remain available before any such timing interpretation.

### What the controller adds

After the first AB inside composite AC=(AB,BC), the underlying primitive graph also allows BA at the intermediate B. The controller excludes that premature branch because it is still executing AC and must next take BC. Pair labels also restrict which displayed graph is followed.

These are explicit dictionary/context restrictions. They are not implied by unconstrained endpoint extension of the glued primitive graph. The checker independently constructs that unrestricted primitive endpoint operator N and verifies

    Q N J != (HZ) T,

where J supplies the synchronized input plane. N itself is only a combinatorial operator on the supplied glued registry, not an identified physical dynamics. The mismatch prevents silently treating the conditional macro construction as a native same-step evolution theorem.

## 5. Current disposition and next gate

**Constructed:** using the existing unchanged-copy operation, a source-labelled, segmentation-aware finite controller and an event-level continuation that preserves a synchronized reference-mode plane.

**Still supplied, not derived:**

1. the candidate's vertex identifications and macro dictionary;
2. the pair/context controller and its exclusion of intermediate exits;
3. neutral extension payloads and the correlated input/mode preparation;
4. physical clock, source metric, filled faces and independent output sectors.

The next meaningful test is to **derive or reject this boundary controller and synchronized preparation from existing source operations**, including the cost and retained record of branch selection. It would be circular to choose the controller or preparation solely to obtain the desired photon modes. A larger carrier or environment may be needed, but its operation must be specified rather than inferred from the successful small matrix.

The original work-net frontier and physical photon-channel gate remain open. No pinned contract, source-owner receipt or formal outcome is promoted. No physical annihilation or ratio 372 is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_segmented_copy_transport.py
python research/scattering/seed-composition/check_segmented_copy_transport.py --check
python research/scattering/seed-composition/check_retained_word_transport.py --check
python research/scattering/seed-composition/check_incidence_audit.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All matrices, source hashes, controller transitions, constraint ranks and the unrestricted primitive defect are recorded in the new receipt. The checker uses exact rational arithmetic, reuses the actual retained-path implementation, and writes only its own receipt; `--check` compares without writing.
