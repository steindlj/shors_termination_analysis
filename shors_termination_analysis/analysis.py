def analyze_statistics(statistics: list[list[int]], n: int) -> None:
    """Compute and print analysis of the collected statistics."""
    total_counts = [sum(values) for values in zip(*statistics)]
