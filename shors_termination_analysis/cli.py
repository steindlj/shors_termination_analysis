import argparse
from data import DEFAULT_TEST_SET
from .core import shors_algorithm
from .analysis import analyze_statistics

def run_on_set(test_set: list[int], iterations: int) -> None:
    """Run Shor's algorithm analysis on specified test set with defined iteration count."""
    statistics = []
    for n in test_set:
        for _ in range(iterations):
            statistics.append(shors_algorithm(n))
        analyze_statistics(statistics, n)
        statistics.clear()

def main() -> None:
    """Prepare test set, parse arguments, and run analysis on chosen numbers."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--numbers', nargs='*', type=int, default=DEFAULT_TEST_SET)
    parser.add_argument('-i', '--iterations', type=int, default=1000)
    args = parser.parse_args()

    run_on_set(args.numbers, args.iterations)

if __name__ == '__main__':
    main()
