// Each input shard consists of rows: four-deletion mask, followed by all legal supports on that parent. Obtain via four_deletion_probe --supports.
use std::{
    collections::HashMap,
    env,
    fs::File,
    io::{BufRead, BufReader},
};
include!("ramsey312_forced_class_test.rs");
fn main() {
    let mut audit = env::var("RAMSEY_FORCED_MATRIX")
        .ok()
        .map(|f| ForcedAudit::from_matrix(&f));
    let mut dom = HashMap::new();
    for f in env::args().skip(1) {
        for line in BufReader::new(File::open(f).unwrap()).lines() {
            let l = line.unwrap();
            let mut nums = l.split_whitespace().map(|x| x.parse::<u64>().unwrap());
            let mask = nums.next().unwrap();
            let v: Vec<_> = nums.collect();
            assert!(
                mask.count_ones() == 4
                    && v.windows(2).all(|w| w[0] < w[1])
                    && v.iter().all(|&x| x & mask == 0)
            );
            assert!(dom.insert(mask, v).is_none())
        }
    }
    assert_eq!(dom.len(), 270725);
    assert_eq!(dom.values().map(Vec::len).sum::<usize>(), 5470805);
    let mut stat = [0u64; 6];
    let mut cores = 0;
    let mut examples = 0;
    for i in 0..52 {
        for j in 0..i {
            for k in 0..j {
                for l in 0..k {
                    for m in 0..l {
                        let b = [1 << i, 1 << j, 1 << k, 1 << l, 1 << m];
                        let d = b.iter().fold(0, |p, v| p | v);
                        let mut row = vec![];
                        for &a in &b {
                            let par = &dom[&(d ^ a)];
                            for &s in par {
                                row.push((s & !a, a));
                            }
                        }
                        row.sort_unstable();
                        let (mut p, mut best) = (0, 0);
                        let mut forced: [Vec<u64>; 5] = Default::default();
                        let mut ambiguous = vec![];
                        while p < row.len() {
                            let x = row[p].0;
                            let mut compatible = 0;
                            while p < row.len() && row[p].0 == x {
                                compatible |= row[p].1;
                                p += 1
                            }
                            let n = compatible.count_ones() as usize;
                            best = best.max(n);
                            if n == 4 && audit.is_some() {
                                forced[b.iter().position(|v| v & compatible == 0).unwrap()].push(x)
                            }
                            if audit.is_some() && n < 4 {
                                ambiguous.push((x, d ^ compatible));
                            }
                            if n == 5 {
                                examples += 1;
                                println!("{m},{l},{k},{j},{i},{x}")
                            }
                        }
                        if let Some(a) = audit.as_mut() {
                            a.test(d, b, forced, ambiguous)
                        }
                        stat[best] += 1;
                        cores += 1;
                    }
                }
            }
        }
    }
    if let Some(a) = audit {
        a.summary()
    }
    assert_eq!(cores, 2598960);
    eprintln!("cores={cores} max-compatible-hist={stat:?} five-way-supports={examples}")
}
