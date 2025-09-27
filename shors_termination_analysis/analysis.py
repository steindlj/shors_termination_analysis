import pandas as pd
import os

class Analysis:
    def __init__(self, output_dir: str, filename: str):
        """Initialize an Analysis instance for storing and saving results.

        Args:
            output_dir (str): Directory where the CSV file will be stored.
            filename (str): Base name (without extension) for the output file.
        """
        os.makedirs(output_dir, exist_ok=True)
        self.filename = os.path.join(output_dir, f"{filename}.csv")
        self.columns = [
            "N", 
            "Iterations", 
            "Runs",
            "Success (gcd(a;N)>1)", 
            "Restart (odd r)",
            "Restart (x+-1 mod N = 0)", 
            "Success (x+-1 mod N /= 0)"
        ]
        self.df = pd.DataFrame(columns=self.columns)

    def add_run(self, statistics: list[list[int]], n: int) -> None:
        """Aggregate results from a set of Shor's algorithm runs.

        Args:
            statistics (list[list[int]]): A list of per-iteration statistics. 
                Each inner list contains counts for different termination outcomes.
            n (int): The integer N that was factorized.
        """
        total_counts = [sum(values) for values in zip(*statistics)]
        total_attempts = sum(total_counts)
        summary_row = {
            "N": n,
            "Iterations": len(statistics),
            "Runs": total_attempts,
            "Success (gcd(a;N)>1)": total_counts[0],
            "Restart (odd r)": total_counts[1],
            "Restart (x+-1 mod N = 0)": total_counts[2],
            "Success (x+-1 mod N /= 0)": total_counts[3],
        }
        self.df = pd.concat([self.df, pd.DataFrame([summary_row])], ignore_index=True)

    def save(self, save_as_file: bool) -> None:
        """Display and optionally save the collected results.

        Args:
            save_as_file (bool): If True, saves the DataFrame to CSV.
        """
        print(self.df)
        if save_as_file:
            self.df.to_csv(self.filename, index=False)
            print(f"[Saved entire dataframe to '{self.filename}']")