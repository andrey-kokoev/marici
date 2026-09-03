# Global labeled-center regularity

## Question

Is the principal center globally a regular codimension-three intersection with an oriented wall basis?

## Claim boundary

Locally, yes. For

`l1=U`, `l2=V`, `l3=U+V+P`,

the coefficient determinant is one and

`(l1,l2,l3)=(U,V,P)`

because `P=l3-l1-l2`. Hence wherever `U,V,P` are regular parameters, the center is a regular codimension-three embedding and the labeled conormals form an oriented basis.

The available artifacts establish this on the normal slice through the exceptional `P2`. They do not materialize the global carrier atlas, global ideal sheaf, smoothness along the entire center, or transition cocycle. Rank-26 transport is a relation-module theorem and does not supply those geometric data.

Conditionally, if the three parameters are global along a smooth center, the relative ambient-star `HomotopyLift` globalizes.

## Disposition

Local regularity and orientation pass; global carrier descent remains unproved. The next leaf must inspect the authoritative carrier definition and its principal ideal directly.

## Verification

- `research/voevodsky/check_cosmology_global_labeled_center_regularity.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
