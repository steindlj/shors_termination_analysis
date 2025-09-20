import argparse
from .data import DEFAULT_TEST_SET
from .core import shors_algorithm
from .analysis import Analysis

def run_on_set(test_set: list[int], iterations: int, output_dir: str, filename: str, save: bool) -> None:
    """Run Shor's algorithm analysis on specified test set with defined iteration count."""
    print(f"Executing Shor's algorithm for {test_set}")
    statistics = []
    analysis = Analysis(output_dir, filename)
    for n in test_set:
        for _ in range(iterations):
            statistics.append(shors_algorithm(n))
        analysis.add_run(statistics, n)
        statistics.clear()
    analysis.save(save)

def main() -> None:
    """Prepare test set, parse arguments, and run analysis on chosen numbers."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--numbers', nargs='*', type=int, default=DEFAULT_TEST_SET)
    parser.add_argument('-i', '--iterations', type=int, default=1000)
    parser.add_argument('-o', '--output_dir', type=str, default=".")
    parser.add_argument('-fn', '--filename', type=str, default="data_analysis")
    parser.add_argument('-s', '--save', action="store_true")
    args = parser.parse_args()

    run_on_set(args.numbers, args.iterations, args.output_dir, args.filename, args.save)

if __name__ == '__main__':
    main()
