# qRB microstep 109: finite linking-block convergence

Let `J_alpha` be finite regulated linking operators and `J_link` the bounded operator on the completed orbit. A sufficient convergence criterion is:

1. a dense core `E` in `H_orb`;
2. pointwise form convergence
   
   $$
   \langle J_\alpha u,v\rangle
   \to
   \langle J_{\rm link}u,v\rangle
   $$

   for every `u,v` in `E`;
3. a uniform operator bound
   
   $$
   \sup_\alpha\|J_\alpha\|<\infty.
   $$

Then the finite linking blocks converge weakly on the whole orbit, and strongly if the corresponding quadratic norms also converge.

The cofinal diagonal already supplies pointwise convergence on a countable core. The missing ingredient for convergence to the fixed bounded operator is uniform boundedness of the finite linking blocks in the orbit norm.

Status: finite-to-fixed-orbit convergence criterion isolated.
