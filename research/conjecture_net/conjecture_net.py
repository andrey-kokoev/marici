"""Static signed conjecture nets and exhaustive simple-path enumeration.

The signs are polarities, not times: E_ab is a local relation a -> b.
Wires preserve polarity. Forks and joins are polarity-preserving structural
agents. No causal or signal-propagation semantics is assumed.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Sign(Enum):
    PLUS = "+"
    MINUS = "-"


class Exploration(Enum):
    PP = "++"
    PM = "+-"
    MP = "-+"
    MM = "--"

    @property
    def source(self) -> Sign:
        return Sign(self.value[0])

    @property
    def target(self) -> Sign:
        return Sign(self.value[1])


@dataclass(frozen=True)
class Agent:
    name: str
    kind: str
    exploration: Exploration | None = None
    sign: Sign | None = None

    def ports(self) -> tuple[str, ...]:
        if self.kind in {"origin", "terminal"}:
            return ("p",)
        if self.kind == "exploration":
            if self.exploration is None:
                raise ValueError(f"{self.name}: missing exploration type")
            return ("p", "a")
        if self.kind in {"fork", "join"}:
            if self.sign is None:
                raise ValueError(f"{self.name}: structural agent needs a sign")
            return ("p", "a0", "a1")
        raise ValueError(f"{self.name}: unknown kind {self.kind}")

    def port_sign(self, port: str) -> Sign:
        if port not in self.ports():
            raise ValueError(f"{self.name}: unknown port {port}")
        if self.kind == "exploration":
            assert self.exploration is not None
            return self.exploration.source if port == "p" else self.exploration.target
        if self.sign is None:
            raise ValueError(f"{self.name}: endpoint needs a sign")
        return self.sign

    def local_steps(self) -> tuple[tuple[str, str], ...]:
        if self.kind in {"origin", "terminal"}:
            return ()
        if self.kind == "exploration":
            return (("p", "a"),)
        if self.kind == "fork":
            return (("p", "a0"), ("p", "a1"))
        if self.kind == "join":
            return (("a0", "p"), ("a1", "p"))
        raise AssertionError


Port = tuple[str, str]


@dataclass
class Net:
    agents: dict[str, Agent]
    wires: tuple[tuple[Port, Port], ...]
    origin: Port
    terminal: Port

    def _agent(self, port: Port) -> Agent:
        name, label = port
        if name not in self.agents or label not in self.agents[name].ports():
            raise ValueError(f"unknown port {port}")
        return self.agents[name]

    def validate(self) -> None:
        occupied: set[Port] = set()
        if self._agent(self.origin).kind != "origin":
            raise ValueError("origin port is not on an origin agent")
        if self._agent(self.terminal).kind != "terminal":
            raise ValueError("terminal port is not on a terminal agent")
        for left, right in self.wires:
            la, ra = self._agent(left), self._agent(right)
            if left in occupied or right in occupied:
                raise ValueError("interaction-net linearity violated: port has multiple wires")
            if la.port_sign(left[1]) != ra.port_sign(right[1]):
                raise ValueError(f"polarity mismatch on wire {left}--{right}")
            occupied.update((left, right))

    def paths(self) -> list[tuple[Port, ...]]:
        """Enumerate all simple directed local-traversal paths."""
        self.validate()
        adjacency: dict[Port, list[Port]] = {}
        def edge(a: Port, b: Port) -> None: adjacency.setdefault(a, []).append(b)
        for a, b in self.wires:
            edge(a, b); edge(b, a)       # wires preserve polarity, not direction
        for agent in self.agents.values():
            for source, target in agent.local_steps():
                edge((agent.name, source), (agent.name, target))
        found: list[tuple[Port, ...]] = []
        def visit(at: Port, used: frozenset[Port], path: tuple[Port, ...]) -> None:
            if at == self.terminal:
                found.append(path); return
            for nxt in adjacency.get(at, ()):
                if nxt not in used:
                    visit(nxt, used | {nxt}, path + (nxt,))
        visit(self.origin, frozenset({self.origin}), (self.origin,))
        return found

    def path_words(self) -> list[tuple[str, ...]]:
        words=[]
        for path in self.paths():
            seen=[]
            for name, _ in path:
                e=self.agents[name].exploration
                if e is not None and (not seen or seen[-1][0] != name):
                    seen.append((name,e.value))
            words.append(tuple(value for _,value in seen))
        return words

    @staticmethod
    def compose_word(word:tuple[str,...])->str:
        if not word:raise ValueError("empty path word has no declared polarity")
        source=word[0][0];target=word[0][1]
        for step in word[1:]:
            if step[0]!=target:raise ValueError(f"ill-typed path word {word}")
            target=step[1]
        return source+target

    def path_composites(self)->list[str]:
        return [self.compose_word(word) for word in self.path_words()]

    def coherence_classes(self)->dict[str,list[tuple[str,...]]]:
        """Parallel paths grouped by their composite in the thin sign category."""
        classes:dict[str,list[tuple[str,...]]]={}
        for word in self.path_words():classes.setdefault(self.compose_word(word),[]).append(word)
        return classes
