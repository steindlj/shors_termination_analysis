import pandas as pd
import os

class Analysis:
    def __init__(self, output_dir: str, filename: str):
        os.makedirs(output_dir, exist_ok=True)
        self.filename = os.path.join(output_dir, f"{filename}.csv")
        self.columns = [
            "N", "total_runs", "total_attempts",
            "success: gcd(a, N) > 1", "restart: r is odd",
            "restart: x+-1 mod N = 0", "success: x+-1 mod N != 0"
        ]
        self.df = pd.DataFrame(columns=self.columns)

    def add_run(self, statistics: list[list[int]], n: int) -> None:
        total_counts = [sum(values) for values in zip(*statistics)]
        total_attempts = sum(total_counts)

        summary_row = {
            "N": n,
            "total_runs": len(statistics),
            "total_attempts": total_attempts,
            "success: gcd(a, N) > 1": total_counts[0],
            "restart: r is odd": total_counts[1],
            "restart: x+-1 mod N = 0": total_counts[2],
            "success: x+-1 mod N != 0": total_counts[3],
        }
        self.df = pd.concat([self.df, pd.DataFrame([summary_row])], ignore_index=True)

    def save(self, save_as_file: bool) -> None:
        print(self.df)
        if save_as_file:
            self.df.to_csv(self.filename, index=False)
            print(f"[Saved entire dataframe to '{self.filename}']")