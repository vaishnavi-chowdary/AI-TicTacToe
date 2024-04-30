# 🤖 AI Tic-Tac-Toe Algorithm User Guide 🎮

Welcome to the Tic-Tac-Toe Algorithm repository! This comprehensive guide will help you understand and utilize the included scripts for playing and comparing different Tic-Tac-Toe strategies.

## 📁 Repository Overview

This repository contains various scripts that implement different AI algorithms for playing Tic-Tac-Toe:

1. **`main.py`**:
   - **Description**: This script serves as the main entry point for executing and comparing Tic-Tac-Toe playing algorithms.
   - **Purpose**: It imports and orchestrates functions from other algorithm scripts to demonstrate gameplay and efficiency comparisons.
   - **Usage**: Run this script to observe and analyze the performance of different algorithms across multiple games.

2. **`monteclaro.py`**:
   - **Description**: Implements the Rollout Policy Adaptation algorithm for playing Tic-Tac-Toe.
   - **Strategy**: Utilizes Monte Carlo simulations to make strategic decisions during gameplay.
   - **Usage**: Execute this script independently to witness the Monte Carlo algorithm in action, simulating gameplay scenarios to inform optimal move selection.

3. **`sparsesampling.py`**:
   - **Description**: Implements the Sparse Sampling algorithm for efficient Tic-Tac-Toe gameplay.
   - **Strategy**: Utilizes a tree search approach to explore and exploit specific game states, optimizing decision-making efficiency.
   - **Usage**: Run this script to observe how the Sparse Sampling strategy performs in Tic-Tac-Toe, balancing between exploration and exploitation.

4. **`temporallearning.py`**:
   - **Description**: Implements the Temporal Difference Learning algorithm for adaptive gameplay.
   - **Strategy**: Utilizes reinforcement learning techniques to adapt strategies based on feedback and predicted outcomes.
   - **Usage**: Run this script to observe the adaptive nature of temporal difference learning in Tic-Tac-Toe, where strategies evolve through iterative learning.

## 🚀 Getting Started

Follow these steps to use the scripts in this repository:

1. **Clone the Repository**:
   - Open your terminal or command prompt.
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/vaishnavi-chowdary/AI---Tic-Tac-Toe.git
     ```

2. **Navigate to the Repository Directory**:
   - Use the `cd` command to enter the repository directory:
     ```bash
     cd AI---Tic-Tac-Toe
     ```

3. **Install Dependencies**:
   - Ensure Python is installed on your computer.
   - Install required libraries (such as `matplotlib` and `pygame`) using pip:
     ```bash
     pip install matplotlib
     pip install pygame
     ```

4. **Run Individual Scripts**:
   - Execute each script individually to explore different Tic-Tac-Toe playing strategies:
     ```bash
     python monteclaro.py
     python sparsesampling.py
     python temporallearning.py
     ```

5. **Compare Algorithms with `main.py`**:
   - Run the `main.py` script to compare and visualize the performance of different algorithms:
     ```bash
     python main.py
     ```

## 💡 Understanding the Algorithms

Explore detailed insights into each algorithm included in this repository:

### Monte Carlo Algorithm (`monteclaro.py`)

- **Description**:
  - The Monte Carlo algorithm uses random simulations (rollouts) to estimate move values and make strategic decisions during Tic-Tac-Toe gameplay.
  - It explores various game paths and estimates the likelihood of winning based on simulated game outcomes.

- **Usage**:
  - By executing `monteclaro.py`, you can observe how the Monte Carlo algorithm navigates different Tic-Tac-Toe scenarios to make optimal move selections.

### Sparse Sampling Strategy (`sparsesampling.py`)

- **Description**:
  - The Sparse Sampling algorithm applies a tree search approach to efficiently explore and exploit specific game states in Tic-Tac-Toe.
  - It balances between exploring new moves and exploiting known strategies to optimize decision-making.

- **Usage**:
  - Running `sparsesampling.py` demonstrates how the Sparse Sampling strategy performs in Tic-Tac-Toe gameplay, focusing on decision-making efficiency.

### Temporal Difference Learning (`temporallearning.py`)

- **Description**:
  - Temporal Difference Learning (Q-Learning) is a reinforcement learning approach that adapts strategies based on feedback and predicted outcomes.
  - It learns from game experiences to improve decision-making over time.

- **Usage**:
  - Execute `temporallearning.py` to witness the adaptive nature of temporal difference learning in Tic-Tac-Toe, where strategies evolve through iterative gameplay sessions.

## 🌟 Additional Notes

- Customize parameters or game settings directly within each script to experiment with different configurations.
- Explore the source code of individual scripts (`monteclaro.py`, `sparsesampling.py`, `temporallearning.py`) for deeper insights into implementation details and algorithmic strategies.
- Refer to included comments and documentation within each script for comprehensive understanding and customization options.

---

This user guide provides you with the necessary knowledge to utilize and explore the Tic-Tac-Toe algorithms provided in this repository effectively. Experiment with different strategies, configurations, and comparisons to gain insights into their behaviors and performances. If you have questions or feedback, feel free to reach out!

## Project Overview Presentation

For a detailed high-level overview of this project, please refer to the included PowerPoint presentation (`Tic Tac Toe.pptx`) located in the repository.
