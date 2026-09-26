# Triple comparisons require specified higher coherence, not automatic loop erasure

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverTriangleCoherence.agda`; retained log: `results/agda-triangle-coherence.log`. The check rebuilds the imported circle-cover regression. No previous whole-programme receipt is asserted fresh for this file.

Given comparisons p:x=y, q:y=z and r:x=z, the extra triangle datum is c:p·q=r. The new module proves that such a c makes transport along the two-edge route agree with transport along the direct route.

For actual local contents u,v,w, agreement witnesses a:transport(p,u)=v and b:transport(q,v)=w compose to a route witness. A base cell c converts that route witness to one with the direct route's endpoints. If a direct agreement witness d was independently supplied, compatibility is a further equality between the converted route witness and d. This condition is defined explicitly; the canonical choice of d satisfies it by reflexivity. We have NOT proved that every chosen d is compatible, nor yet constructed dependent three-patch descent from this condition.

## Two checked counterexamples in one configuration

Use three index comparisons at the same base: p=refl, q=refl, r=the nontrivial circle loop. All three comparisons exist, but no triangle p·q=r exists (otherwise the loop would equal reflexivity).

Now let the observer see only Unit at every index. Both routes have equal observed results, nevertheless the structural triangle remains impossible. Observational equality for a coarse observer does not certify equality of the actual comparisons.

## Qualification to the programme

A network of three edges is allowed to contain nontrivial loop action. A triangle cell is required ONLY when the overlap specification includes a filled triangle. Adding a filling to every cycle would change the structure and wrongly erase legitimate loop information. This corrects any suggestion that pairwise observations must always satisfy a triangle equation regardless of their support geometry.

The result continues the direction-free model: edge orientation chooses notation for comparison, not a temporal execution order. It also makes observer limitations concrete: an observer may genuinely fail to distinguish a structural obstruction.

Next construct an explicit filled-triangle observation support and its dependent gluing/elimination rule, retaining local, edge and two-dimensional witnesses. This will test the proposed compatibility condition against actual descent rather than merely its well-typed statement. General covers and all higher coherence remain outside this finite step.
