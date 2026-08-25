"""Finite witness for typed constructor-tree closure."""


def rank2(columns):
    if not columns:
        return 0
    if all(x == 0 for col in columns for x in col):
        return 0
    first = next(col for col in columns if col != [0, 0])
    if any(first[0] * col[1] != first[1] * col[0] for col in columns):
        return 2
    return 1


constructors = {
    "unary_seed": {
        "inputs": ("A",),
        "output": "C",
        "authorized": True,
        "apply": lambda a: [a, 0],
    },
    "binary_join": {
        "inputs": ("A", "B"),
        "output": "C",
        "authorized": True,
        "apply": lambda a, b: [0, a * b],
    },
    "same_bytes_undeclared": {
        "inputs": ("A", "B"),
        "output": "C",
        "authorized": False,
        "apply": lambda a, b: [0, a * b],
    },
}


def compile_node(constructor_id, typed_inputs):
    spec = constructors[constructor_id]
    signatures = tuple(t for t, _ in typed_inputs)
    if signatures != spec["inputs"]:
        return {"code": "signature_mismatch", "node": constructor_id}
    if not spec["authorized"]:
        return {
            "code": "undeclared_authority_constructor",
            "node": constructor_id,
            "claimed_output": spec["output"],
        }
    return (spec["output"], spec["apply"](*(v for _, v in typed_inputs)))


unary = compile_node("unary_seed", [("A", 1)])
binary = compile_node("binary_join", [("A", 1), ("B", 1)])
rejected = compile_node("same_bytes_undeclared", [("A", 1), ("B", 1)])
mismatch = compile_node("binary_join", [("B", 1), ("A", 1)])

assert unary == ("C", [1, 0])
assert binary == ("C", [0, 1])
assert rank2([unary[1]]) == 1
assert rank2([unary[1], binary[1]]) == 2
assert rejected["code"] == "undeclared_authority_constructor"
assert mismatch["code"] == "signature_mismatch"
assert constructors["same_bytes_undeclared"]["apply"](1, 1) == binary[1]

print("unary word-closure rank:", rank2([unary[1]]))
print("authorized constructor-tree rank:", rank2([unary[1], binary[1]]))
print("same numerical output rejected as:", rejected["code"])
print("wrong ordered signatures rejected as:", mismatch["code"])
print("PASS: typed authorized trees, not free words or output bytes, generate the carrier")
