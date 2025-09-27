# Termination Critera in Shor's Algorithm

This repository contains a Python implementation of [Shor's Algorithm](https://arxiv.org/abs/quant-ph/9508027), a quantum algorithm for integer factorization. The project features a command-line interface (CLI), an Anaconda environment YAML for easy setup, and the ability to collect statistics about the algorithm's termination criteria.

## Features

- Implementation of Shor’s Algorithm for factoring integers.

- Statistics collection on termination criteria (success/restart).

- CLI for user-friendly execution.

- Uses `numpy`, ``sympy``, and ``pandas`` for calculations and data analysis.

## Requirements

- [Anaconda](https://anaconda.org/) or [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)

- Packages from ``environment.yml`` (Python 3.13)

## Setup

1. Create and activate the Conda environment:
````bash
conda env create -f environment.yml
conda activate shors_termination_analysis
````

2. Run with CLI tool:

````
python -m shors_termination_analysis.cli [-h] [-n [NUMBERS ...]] [-i ITERATIONS] [-o OUTPUT_DIR] [-fn FILENAME] [-s]

options:
  -h, --help            show this help message and exit
  -n, --numbers [NUMBERS ...]
  -i, --iterations ITERATIONS
  -o, --output_dir OUTPUT_DIR
  -fn, --filename FILENAME
  -s, --save
