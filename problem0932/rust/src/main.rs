extern crate core;

use code_timing_macros::time_function;
use rayon::iter::ParallelIterator;

fn is_2025(i: u128) -> bool {
    let s = i.to_string();
    let n = s.len();
    if n < 2 {
        return false;
    }
    for k in 1..n {
        let (s1, s2) = s.split_at(k);

        if s2.starts_with('0') {
            continue;
        }

        if let (Ok(n1), Ok(n2)) = (s1.parse::<u128>(), s2.parse::<u128>()) {
            if n1 != 0 && n2 != 0 && (n1 + n2) * (n1 + n2) == i {
                return true;
            }
        }
    }
    false
}

#[time_function]
fn main() {
    const UPPER: u128 = (10_000_000_000_000_000 as u128).isqrt();
    let found: Vec<u128> = <_ as rayon::iter::IntoParallelIterator>::into_par_iter(1u128..=UPPER)
        .filter_map(|i| {
            let sq = i * i;
            if is_2025(sq) { Some(sq) } else { None }
        })
        .collect();

    println!("Result: {}", found.iter().sum::<u128>());
}
