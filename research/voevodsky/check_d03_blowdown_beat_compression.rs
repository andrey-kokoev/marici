//! Tests whether the actual D03 barycentric blowdown factors into
//! ring-compatible beat-point retractions.

use std::collections::BTreeSet;

const N: u8 = 6;
const MAX_FACE_SIZE: u32 = 3;
const EXCEPTIONAL: u16 = 1 << 9;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Diagonal(u8, u8);

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        Diagonal(a, b)
    } else {
        Diagonal(b, a)
    }
}

fn boundary_edge(d: Diagonal) -> bool {
    d.1 - d.0 == 1 || d == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(a: Diagonal, b: Diagonal) -> bool {
    if a.0 == b.0 || a.0 == b.1 || a.1 == b.0 || a.1 == b.1 {
        return false;
    }
    between(b.0, a.0, a.1) != between(b.1, a.0, a.1)
        && between(a.0, b.0, b.1) != between(a.1, b.0, b.1)
}

fn diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|a| ((a + 1)..N).map(move |b| diagonal(a, b)))
        .filter(|d| !boundary_edge(*d))
        .collect()
}

fn old_faces(ds: &[Diagonal]) -> BTreeSet<u16> {
    (0_u16..(1_u16 << ds.len()))
        .filter(|mask| mask.count_ones() <= MAX_FACE_SIZE)
        .filter(|mask| {
            (0..ds.len()).all(|i| {
                ((i + 1)..ds.len())
                    .all(|j| mask & (1 << i) == 0 || mask & (1 << j) == 0 || !crosses(ds[i], ds[j]))
            })
        })
        .collect()
}

fn blowup_faces(old: &BTreeSet<u16>, d03_bit: u16, x1_bit: u16) -> BTreeSet<u16> {
    let mut result = BTreeSet::new();
    for face in old {
        if face & d03_bit == 0 || face & x1_bit == 0 {
            result.insert(*face);
        } else {
            let remainder = face & !d03_bit & !x1_bit;
            result.insert(remainder | EXCEPTIONAL);
            result.insert(remainder | EXCEPTIONAL | d03_bit);
            result.insert(remainder | EXCEPTIONAL | x1_bit);
        }
    }
    result
}

fn extend_chains(faces: &[u16], chain: &mut Vec<u16>, out: &mut Vec<Vec<u16>>) {
    out.push(chain.clone());
    let last = *chain.last().expect("nonempty chain");
    for next in faces {
        if last != *next && last & *next == last {
            chain.push(*next);
            extend_chains(faces, chain, out);
            chain.pop();
        }
    }
}

fn barycentric(faces: &BTreeSet<u16>) -> Vec<Vec<u16>> {
    let faces: Vec<_> = faces.iter().copied().collect();
    let mut result = Vec::new();
    for face in &faces {
        extend_chains(&faces, &mut vec![*face], &mut result);
    }
    result
}

fn blowdown(face: u16, d03_bit: u16, x1_bit: u16) -> u16 {
    let mut result = face & !EXCEPTIONAL;
    if face & EXCEPTIONAL != 0 {
        result |= d03_bit | x1_bit;
    }
    result
}

fn chain_contains(big: &[u16], small: &[u16]) -> bool {
    small.iter().all(|face| big.contains(face))
}

// The barycentric face order is reverse chain inclusion.
fn leq(left: &[u16], right: &[u16]) -> bool {
    chain_contains(left, right)
}

fn compatible_beat(
    index: usize,
    active: &[bool],
    chains: &[Vec<u16>],
    labels: &[u16],
) -> Option<usize> {
    let uppers: Vec<_> = (0..chains.len())
        .filter(|j| active[*j] && *j != index && leq(&chains[index], &chains[*j]))
        .collect();
    for candidate in &uppers {
        if labels[*candidate] == labels[index]
            && uppers
                .iter()
                .all(|other| leq(&chains[*candidate], &chains[*other]))
        {
            return Some(*candidate);
        }
    }

    let lowers: Vec<_> = (0..chains.len())
        .filter(|j| active[*j] && *j != index && leq(&chains[*j], &chains[index]))
        .collect();
    for candidate in &lowers {
        if labels[*candidate] == labels[index]
            && lowers
                .iter()
                .all(|other| leq(&chains[*other], &chains[*candidate]))
        {
            return Some(*candidate);
        }
    }
    None
}

fn main() {
    let ds = diagonals();
    assert_eq!(ds.len(), 9);
    let d03 = diagonal(0, 3);
    let x1 = diagonal(1, 3);
    let d03_bit = 1 << ds.iter().position(|d| *d == d03).unwrap();
    let x1_bit = 1 << ds.iter().position(|d| *d == x1).unwrap();
    let old = old_faces(&ds);
    assert_eq!(old.len(), 45);
    let blown = blowup_faces(&old, d03_bit, x1_bit);
    assert_eq!(blown.len(), 51);
    let chains = barycentric(&blown);
    let census: Vec<_> = (1..=4)
        .map(|length| chains.iter().filter(|chain| chain.len() == length).count())
        .collect();
    assert_eq!(census, [51, 194, 240, 96]);

    let labels: Vec<_> = chains
        .iter()
        .map(|chain| blowdown(chain[0], d03_bit, x1_bit))
        .collect();
    assert!(labels.iter().all(|label| old.contains(label)));

    let mut active = vec![true; chains.len()];
    let mut removed = 0_usize;
    loop {
        let next = (0..chains.len()).find_map(|index| {
            active[index]
                .then(|| compatible_beat(index, &active, &chains, &labels))
                .flatten()
                .map(|_| index)
        });
        let Some(index) = next else {
            break;
        };
        active[index] = false;
        removed += 1;
    }

    let survivors: Vec<_> = (0..chains.len()).filter(|i| active[*i]).collect();
    let survivor_labels: BTreeSet<_> = survivors.iter().map(|i| labels[*i]).collect();
    assert_eq!(removed, 0);
    assert_eq!(survivors.len(), chains.len());
    assert_eq!(survivor_labels.len(), old.len());
    println!(
        "{{\"claim\":\"The actual D03 barycentric blowdown does not admit even a first equal-label ordinary beat-point removal\",\"status\":\"beat_compression_falsified\",\"barycentric_cells\":{},\"removed_equal_label_beats\":{},\"survivors\":{},\"survivor_label_count\":{},\"target_cells\":{},\"omega_b_perfectness\":\"UNDECIDED\"}}",
        chains.len(),
        removed,
        survivors.len(),
        survivor_labels.len(),
        old.len()
    );
}
