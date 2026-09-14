from conjecture_net import Agent, Exploration, Net, Sign


def example() -> Net:
    # Two + to + paths: E++ and the polarity round trip E+- ; E-+.
    agents={
        "O":Agent("O","origin",sign=Sign.PLUS),
        "F":Agent("F","fork",sign=Sign.PLUS),
        "A":Agent("A","exploration",Exploration.PP),
        "B":Agent("B","exploration",Exploration.PM),
        "C":Agent("C","exploration",Exploration.MP),
        "J":Agent("J","join",sign=Sign.PLUS),
        "T":Agent("T","terminal",sign=Sign.PLUS),
    }
    wires=(
        (("O","p"),("F","p")),
        (("F","a0"),("A","p")), (("A","a"),("J","a0")),
        (("F","a1"),("B","p")), (("B","a"),("C","p")),
        (("C","a"),("J","a1")), (("J","p"),("T","p")),
    )
    return Net(agents,wires,("O","p"),("T","p"))


def test_enumerates_all_compatible_paths():
    assert example().path_words()==[("++",),("+-","-+")]


def test_composes_parallel_paths_coherently():
    n=example()
    assert n.path_composites()==["++","++"]
    assert n.coherence_classes()=={"++":[("++",),("+-","-+")]}


def test_rejects_polarity_mismatch():
    n=example(); agents=dict(n.agents)
    agents["C"]=Agent("C","exploration",Exploration.PP)
    bad=Net(agents,n.wires,n.origin,n.terminal)
    try:bad.validate()
    except ValueError as e:assert "polarity mismatch" in str(e)
    else:raise AssertionError("expected polarity mismatch")


def test_rejects_implicit_fanout():
    n=example();n.wires += ((("F","a0"),("C","a")),)
    try:n.validate()
    except ValueError as e:assert "linearity" in str(e)
    else:raise AssertionError("expected linearity violation")


if __name__=="__main__":
    test_enumerates_all_compatible_paths();test_composes_parallel_paths_coherently();test_rejects_polarity_mismatch();test_rejects_implicit_fanout();print("passed")
