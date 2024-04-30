"""
Script Name: Main-Algorithm Efficiency Comparison for Tic-Tac-Toe
Description: This script compares the efficiency of three different algorithms (Monte Carlo, Sparse Sampling, Temporal Difference Learning) in playing Tic-Tac-Toe over multiple games.
Author: Vaishnavi Chowdary Kommi
Date: April 26, 2024
"""

# This script imports and runs main functions from separate modules implementing each algorithm:
# Monte Carlo algorithm: `monteclaro`
# Sparse Sampling algorithm: `sparsesampling`
# Temporal Difference Learning algorithm: `temporallearning`

# The efficiency values of each algorithm are collected and plotted to visualize their performance over a series of games. The plot demonstrates the efficiency comparison among the algorithms in strategic decision-making during Tic-Tac-Toe gameplay.

# To use this script:
# 1. Ensure that the required modules (`monteclaro`, `sparsesampling`, `temporallearning`) are installed.
# 2. Run the script to execute each algorithm's main function and generate an efficiency comparison plot.

# Note: This script requires `matplotlib` for plotting. Make sure the necessary dependencies are installed before running the script.



import matplotlib.pyplot as plt
from monteclaro import main as monte_carlo_main
from sparsesampling import main as sparse_main
from temporallearning import main as temporal_main

# Run each algorithm and collect efficiency values
monte_carlo_efficiency = monte_carlo_main()
sparse_efficiency = sparse_main()
temporal_efficiency = temporal_main()

# Plot efficiency values
games = min(len(monte_carlo_efficiency), len(sparse_efficiency), len(temporal_efficiency))
plt.plot(range(1, games + 1), monte_carlo_efficiency[:games], marker='o', label='Monte Carlo')
plt.plot(range(1, games + 1), sparse_efficiency[:games], marker='o', label='Sparse Sampling')
plt.plot(range(1, games + 1), temporal_efficiency[:games], marker='o', label='Temporal Difference Learning')
plt.title('Efficiency Comparison of Algorithms over 5 Games')
plt.xlabel('Game Number')
plt.ylabel('Efficiency')
plt.legend()
plt.grid(True)
plt.show()
