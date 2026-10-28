# Oscillator test: three source fibers do not force a literal triangle

## Frozen question

Apply the Berry candidate's source-index restriction at `group-from` to a source with no preselected tetrahedral geometry. Does a three-fiber cut preserve the physical domain and expose a literal triangle of its primitive ports?

The cut operation is imported unchanged from `check_berry_fibration_cut.py`. The literal-port-triangle criterion is an interpretation under test, not a definition established by the operator's proposal. SCC obligation: forward realization and readout descent, including retained noise input.

## Independent source

Use the existing Markov oscillator input-output equations. Vertices are external input u, bath input b, oscillator amplitude a and external output y. With positive real coupling amplitudes g,h (rates g^2,h^2), define

    chi = 1 / ((g^2+h^2)/2 - i delta),
    a = chi (g u + h b),
    y = u - g a.

The primitive coefficient graph has four edges:

    u -> a : g chi
    b -> a : h chi
    a -> y : -g
    u -> y : 1.

These are direct dependencies of the supplied equations. Route composition multiplies coefficients and parallel contributions add. The triangular subgraph therefore represents interference, not equality of its two routes.

The row reader computes all paths independently and obtains r=1-g^2 chi and q=-gh chi. Symbolic simplification proves |r|^2+|q|^2=1 for this declared model. The existing fixture is g=1,h=2,delta=0, giving r=3/5,q=-4/5.

## All four three-fiber cuts

Include the output's empty source fiber, as required by the existing marked grouping convention. Enumerate all four choices of three source fibers:

| Selected fibers | Retained primitive support | r,q at resonance | Commutator weight |
| --- | --- | --- | --- |
| u,b,a | Whole four-vertex graph | 3/5, -4/5 | 1 |
| u,b,y | Oscillator-to-output edge missing | 1, 0 | 1 |
| u,a,y | Literal triangle, bath omitted | 3/5, 0 | 9/25 |
| b,a,y | Bath-to-oscillator-to-output chain | 0, -4/5 | 16/25 |

Every cut retains exact marked serialization/deserialization. Only the first preserves both response and noise. The literal triangle loses the bath and fails the commutator. The second row is a useful stronger control: commutator preservation alone does not establish preservation of the response law.

## Disposition

**Rejected:** the interpretation that selecting three source-index fibers automatically exposes a faithful literal three-port triangle in an arbitrary physical coefficient graph. The Berry example benefited from its already tetrahedral line geometry.

**Survives:** the same marked-fibration cut mechanism can retain the oscillator's complete response/noise domain; it has three nonempty source fibers but four incident ports. No coefficient was fitted and no tetrahedron was supplied.

This distinction prevents an overclaim in either direction. Counting three fibers is not a proof of a formed triangle, but a four-port incidence graph is not an obstruction to every structured tetrahedral presentation. The operator's broader conjecture remains open. In particular, this test does not eliminate a formed triangle whose vertices are structured presentations rather than primitive physical ports. No replacement grouping or extra edges are introduced to absorb the failed literal interpretation.

The next mathematical issue is now specific: what existing formed-triangle constructor, if any, acts on these retained source fibers while preserving their additive route law and bath port? The result is not grounds for inventing another hierarchy of specification gates or claiming the missing constructor impossible.

## Two successive applications

Operator suggestion: run it twice. Tested the precise re-presentation operation already used here: `group-from` followed by `unpack-reversed` (`TableFibrationCycle.twice`). Applied again to its actual output, this is the kernel's `four` operation.

The first grouping has three nonempty source fibers: u has two rows, b one and a one. Its reassembled output exchanges the endpoints of all four rows. The second grouping has two nonempty fibers: a has two rows and y two. Its reassembled output is exactly the original four-row table. Reading the intermediate stage with the retained endpoint-exchange marker preserves both response and noise; ignoring that marker gives zero external input-to-output transfer.

Thus two applications of this particular operation recover the source rather than create a new three-port support. This does not test two applications of a different WG generative/promotion rule, nor a triangle made of the successive structured presentations. It narrows what the current implementation can answer; it does not reject the operator's suggestion for the tower generally. Fresh exact execution: `structured_command_execution:e_42200_1792520169315919200_28`, exit zero.

## Verification

`uv run --with sympy python research/strominger/checkers/check_oscillator_fibration_cut.py` produced a passing exact test receipt at `research/strominger/results/oscillator-fibration-cut/verification.json`. Pass means the displayed identities and predicted counterexample were verified, not that the triangle conjecture passed. The source report and source checker were read; neither owner producer nor a physical experiment was rerun. The current general-amplitude formula is independently evaluated, avoiding the historical checker's fixture-only q implementation outside its admitted rates.
