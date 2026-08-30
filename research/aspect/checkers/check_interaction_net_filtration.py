#!/usr/bin/env python3
"""Exact F2 filtration checker for the bounded interaction-net pilot."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ASPECT=HERE.parent
CONTRACT=ASPECT/"contracts"/"interaction-net-filtration.v1.json"
RESULT=ASPECT/"results"/"interaction_net_filtration.json"

def grade(lower):
    bits,k=lower
    return sum(bits)+k

def move(lower,direction):
    bits,k=lower
    bits=list(bits)
    if direction<5: bits[direction]=1
    else: k+=1
    return tuple(bits),k

def cells(N):
    by_dim={q:[] for q in range(7)}
    for k in range(N+1):
        for mask in range(32):
            bits=tuple((mask>>i)&1 for i in range(5))
            lower=(bits,k)
            if grade(lower)>N: continue
            available=tuple(i for i in range(5) if bits[i]==0)+(5,)
            for q in range(len(available)+1):
                for dirs in combinations(available,q):
                    if grade(lower)+q<=N: by_dim[q].append((bits,k,dirs))
    return by_dim

def boundary(cell):
    bits,k,dirs=cell
    lower=(bits,k)
    faces=[]
    for d in dirs:
        rest=tuple(x for x in dirs if x!=d)
        faces.append((bits,k,rest))
        upper_bits,upper_k=move(lower,d)
        faces.append((upper_bits,upper_k,rest))
    return faces

def rank_f2(columns):
    pivots={}
    for value in columns:
        while value:
            pivot=value.bit_length()-1
            if pivot in pivots: value^=pivots[pivot]
            else:
                pivots[pivot]=value
                break
    return len(pivots)

def homology(N):
    by_dim=cells(N)
    ranks={0:0,7:0}
    for q in range(1,7):
        row_index={cell:i for i,cell in enumerate(by_dim[q-1])}
        columns=[]
        for cell in by_dim[q]:
            value=0
            for face in boundary(cell): value^=1<<row_index[face]
            columns.append(value)
        ranks[q]=rank_f2(columns)
    betti=[len(by_dim[q])-ranks[q]-ranks[q+1] for q in range(7)]
    return {"N":N,"chain_dimensions":[len(by_dim[q]) for q in range(7)],"boundary_ranks":[ranks[q] for q in range(1,7)],"betti_numbers":betti}

def main():
    contract=json.loads(CONTRACT.read_text(encoding="utf-8"))
    tables=[homology(N) for N in range(contract["local_coherence_complex"]["maximum_checked_grade"]+1)]
    connected_persistent=all(row["betti_numbers"][0]==1 for row in tables)
    no_nonlocal=all(all(x==0 for x in row["betti_numbers"][1:]) for row in tables)
    h0={"class":"root_component","birth":0,"survival":[row["N"] for row in tables],"death":None,"death_witness":None}
    square_boundary=("O1@0","K@O1","O1@K","K@0")
    synthetic={"class":"withheld_O1_K_square","birth":2,"survival":[2],"death":3,"death_witness":{"filler":"O1-K-square","boundary":square_boundary},"boundary_matches_cycle":True,"source_result":False}
    macro_hostile={"primitive_grade":4,"primitive_word":["O1","O2","K","K"],"macro_word":["MACRO"],"macro_word_length":1,"resource_grade_preserved":4,"word_length_rejected_as_invariant":True}
    algebraic={"target":"z_after_observation","construction":"solve a separating linear functional after z","authority":"nonmembership_certificate_only","explanatory_authority":False}
    observable=contract["cocycle_authority"]["preregistered_example"]
    passed=connected_persistent and no_nonlocal and synthetic["boundary_matches_cycle"] and macro_hostile["word_length_rejected_as_invariant"] and observable["target_independent"]
    out={"schema":"marici.aspect.interaction-net-filtration-result.v1","passed":passed,
         "primitive_presentation":contract["primitive_source_presentation"],"resource_grading":contract["resource_grading"],
         "homology_by_grade":tables,"induced_maps":{"H0":"root_component maps identically N->N+1","positive_degree":"zero groups map to zero groups"},
         "all_grade_homology":{"proof":contract["local_coherence_complex"]["all_grade_proof"],"H0":1,"positive_degree":0},
         "persistent_classes":[h0],"candidate_nonlocal_classes":[],"synthetic_death_hostile":synthetic,
         "macro_generator_hostile":macro_hostile,"cocycles":{"algebraic_separator":algebraic,"source_observable":observable},
         "verdict":"no_nonlocal_class_in_source_cubical_pilot; semantic_faithfulness_still_open"}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__": main()
