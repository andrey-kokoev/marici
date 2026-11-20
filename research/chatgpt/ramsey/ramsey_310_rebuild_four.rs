// stdin: Exoo's 39-vertex undirected edge list. Optional [start,end) lexicographic core indices.
use std::{
    io::{self, Read},
    sync::atomic::{AtomicUsize, Ordering::Relaxed},
};
fn audit(adj: &[u64; 39], sets: &[u64], layers: &[Vec<u64>], d: u64) -> (usize, usize) {
    let nine: Vec<_> = layers[3].iter().copied().filter(|m| m & d == 0).collect();
    let eight: Vec<_> = layers[2].iter().copied().filter(|m| m & d == 0).collect();
    let opts: Vec<_> = sets
        .iter()
        .copied()
        .filter(|s| s & d == 0 && nine.iter().all(|m| m & s != 0))
        .collect();
    let olds: Vec<_> = (0..39).filter(|i| d >> i & 1 == 1).collect();
    for &i in &olds {
        assert!(opts.contains(&(adj[i] & !d)));
    }
    let mut nb = vec![Vec::new(); opts.len()];
    let mut count = 0;
    for (i, &x) in opts.iter().enumerate() {
        let needs: Vec<_> = eight.iter().copied().filter(|m| x & m == 0).collect();
        for (j, &y) in opts[..=i].iter().enumerate() {
            let r = x & y == 0;
            let b = needs.iter().all(|m| y & m != 0);
            if r || b {
                nb[i].push((j, b as u8 + 2 * r as u8));
            }
        }
    }
    let edge = |i: usize, j: usize| {
        nb[i]
            .binary_search_by_key(&j, |t| t.0)
            .ok()
            .map_or(0, |p| nb[i][p].1)
    };
    for (a, &u) in olds.iter().enumerate() {
        for &v in &olds[..a] {
            let i = opts.iter().position(|s| *s == adj[u] & !d).unwrap();
            let j = opts.iter().position(|s| *s == adj[v] & !d).unwrap();
            assert!(edge(i.max(j), i.min(j)) & (1 << ((adj[u] >> v) & 1)) != 0);
        }
    }
    for i in 0..opts.len() {
        for &(j, ij) in &nb[i] {
            for &(k, jk) in &nb[j] {
                let ik = edge(i, k);
                if ik == 0 {
                    continue;
                }
                for &(l, kl) in &nb[k] {
                    let il = edge(i, l);
                    let jl = edge(j, l);
                    if il * jl == 0 {
                        continue;
                    }
                    count += 1;
                    let ports = [opts[i], opts[j], opts[k], opts[l]];
                    let pairs = [
                        (0, 1, ij),
                        (0, 2, ik),
                        (0, 3, il),
                        (1, 2, jk),
                        (1, 3, jl),
                        (2, 3, kl),
                    ];
                    for mask in 0..64u32 {
                        if pairs
                            .iter()
                            .enumerate()
                            .any(|(t, p)| p.2 & (1 << (mask >> t & 1)) == 0)
                        {
                            continue;
                        }
                        let mut ok = true;
                        for sub in [7u32, 11, 13, 14, 15] {
                            let mut red = 0;
                            let mut n = 0;
                            for (t, &(a, b, _)) in pairs.iter().enumerate() {
                                if sub >> a & sub >> b & 1 != 0 {
                                    red += mask >> t & 1;
                                    n += 1;
                                }
                            }
                            if n == 3 && red == 3 {
                                ok = false;
                                break;
                            }
                            if red == 0 {
                                let union = (0..4)
                                    .filter(|t| sub >> t & 1 != 0)
                                    .fold(d, |a, t| a | ports[t]);
                                if layers[(4 - sub.count_ones()) as usize]
                                    .iter()
                                    .any(|m| m & union == 0)
                                {
                                    ok = false;
                                    break;
                                }
                            }
                        }
                        if ok {
                            println!("WITNESS d={d} ports={ports:?} redmask={mask}");
                        }
                    }
                }
            }
        }
    }
    (opts.len(), count)
}
fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut adj = [0u64; 39];
    let v: Vec<usize> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
    for p in v.chunks_exact(2) {
        adj[p[0]] |= 1 << p[1];
        adj[p[1]] |= 1 << p[0];
    }
    let mut sets = vec![0];
    for (j, r) in adj.iter().enumerate() {
        for i in 0..sets.len() {
            if sets[i] & r == 0 {
                sets.push(sets[i] | 1 << j);
            }
        }
    }
    assert_eq!(sets.iter().map(|s| s.count_ones()).max(), Some(9));
    assert!(adj.iter().all(|s| sets.contains(s)));
    let layers: Vec<_> = (6..=9)
        .map(|k| {
            sets.iter()
                .copied()
                .filter(|s| s.count_ones() == k)
                .collect()
        })
        .collect();
    let mut ds = vec![];
    for i in 0..39 {
        for j in i + 1..39 {
            for k in j + 1..39 {
                ds.push(1 << i | 1 << j | 1 << k);
            }
        }
    }
    let args: Vec<usize> = std::env::args()
        .skip(1)
        .map(|s| s.parse().unwrap())
        .collect();
    let start = *args.first().unwrap_or(&0);
    let end = *args.get(1).unwrap_or(&ds.len());
    let next = AtomicUsize::new(start);
    let max = AtomicUsize::new(0);
    let four = AtomicUsize::new(0);
    std::thread::scope(|scope| {
        for _ in 0..std::thread::available_parallelism().unwrap().get().min(12) {
            scope.spawn(|| loop {
                let i = next.fetch_add(1, Relaxed);
                if i >= end {
                    break;
                }
                let (n, c) = audit(&adj, &sets, &layers, ds[i]);
                max.fetch_max(n, Relaxed);
                four.fetch_add(c, Relaxed);
            });
        }
    });
    println!(
        "range=[{start},{end}) cores={} largest_pool={} compatible_quads={}",
        end - start,
        max.load(Relaxed),
        four.load(Relaxed)
    );
}
