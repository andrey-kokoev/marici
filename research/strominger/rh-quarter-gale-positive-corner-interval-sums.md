# Positive-corner Gale intervals can have negative signed mass

## Question

Do variable-size Gale intervals with terminal-positive minimal and maximal corners provide nonnegative local blocks?

## Claim boundary

No. After 343 positive-corner intervals in 99 terminal cases, the first obstruction occurs for base \(\{1\}\), exchanged labels \((i,j)=(0,2)\), and interval

\[
[\{0,1\},\{0,3\}]=\{\{0,1\},\{0,2\},\{0,3\}\}.
\]

Both corners have positive oriented sign, but the exact interval sum is negative:

\[
-21457980561330351524292666045604961034551754347037146615212355760064099145099417305070574911826602836447061581125756866789865721959243649378930942979591386386051439637148828506115701117759656438483980449218560000.
\]

Thus edges, fixed three-term chains, and parity-compatible intervals all fail as universal independent blocks.

## Disposition

The surviving mechanism must permit branching and mass splitting. Test the narrowest such network: restrict transport edges to opposite-parity Gale covers rather than all comparable pairs, and run exact max flow in every terminal case. Success would localize Hall transport to the Hasse graph; failure would quantify the necessity of longer comparable jumps.
