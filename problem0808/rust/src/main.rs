
use miller_rabin::is_prime;
use primes::{PrimeSet, Sieve};

fn reverse_digits(mut n: u64) -> u64 {
    let mut reversed = 0;
    while n > 0 {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    reversed
}

fn main() {
    let mut pset = Sieve::new();
    let mut count = 0;
    let mut sum = 0;

    for prime in pset.iter() {
        let val = prime * prime;
        let val_rev = reverse_digits(val);
        if val != val_rev {
            let square = val_rev.isqrt();
            if square * square == val_rev && is_prime(&square, 5) {
                println!(
                    "Found #{}: {}^2 = {} and {}^2 = {}",
                    count + 1, prime, val, square, val_rev
                );
                count += 1;
                sum += val;
                println!("Count {} - Sum {}", count, sum);
                if count == 50 {
                    break;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::reverse_digits;

    #[test]
    fn reverse_zero() {
        assert_eq!(reverse_digits(0), 0);
    }

    #[test]
    fn reverse_single_digit() {
        assert_eq!(reverse_digits(7), 7);
    }

    #[test]
    fn reverse_trailing_zeros() {
        assert_eq!(reverse_digits(1200), 21);
    }

    #[test]
    fn reverse_palindrome() {
        assert_eq!(reverse_digits(1221), 1221);
    }

    #[test]
    fn reverse_large_number() {
        let n = 123456789012345678u64;
        let rev = 876543210987654321u64;
        assert_eq!(reverse_digits(n), rev);
    }
}