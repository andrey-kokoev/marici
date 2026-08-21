# Five-site branch-chain lift gate

## Attack

The codimension-one Kummer branch is the smallest geometric candidate for
the quotient \(C_2\to1\).  Entry 1224's checker identifies the two signs of
one radical by masking its sheet bit, reducing 32 sheet labels to 16.  It
also states that generic deck maps preserve the orientation of the physical
\(u_1,u_2,u_3\) current.

## Result

Those facts do not construct a pushforward of physical relative chains.
Locally write the two generic chains as \(\Gamma_+,\Gamma_-\) and the branch
chain as \(\Gamma\).  Frozen positive-chamber normalization fixes

\[
s(\Gamma_+)=\Gamma.
\]

Set-level coalescence says only that both labels restrict to the same branch
label.  Even retaining positive integral multiplicity leaves, for example,

\[
s_1(\Gamma_-)=\Gamma,
\qquad
s_2(\Gamma_-)=2\Gamma.
\]

Both respect the recorded target label, positivity, and selected
\(\Gamma_+\) normalization.  They differ on the orbit trace and on the full
coefficient--Betti adjunction.

The algebraic adjunction with \(q^*(1)=(1,1)\) uniquely selects \(s_1\),
because it requires both sheet-basis pairings to equal 1.  But the physical
adjunction is precisely the property whose source admission is under test.
Using it to infer \(s_1\) would be circular.

## Verdict

The codimension-one branch gives a genuine quotient of sheet labels, but
not yet a source-authorized relative-chain map.  The missing datum is a map
of relative pairs with boundary compatibility, local degree/intersection
multiplicity, and endpoint or regulator normalization.  Generic deck
orientation does not determine specialization multiplicity.

This strengthens the boundary established by the paired Mackey norm:
multiplicity one is algebraically canonical once adjunction is imposed, but
it is not derivable physically from Entry 1224's cardinalities.

## Verification

`checkers/five_site_branch_chain_lift_gate.py` reads the frozen 32-to-16
branch census and verifies two distinct positive integral chain lifts, only
one of which satisfies the desired full pairing adjunction.
