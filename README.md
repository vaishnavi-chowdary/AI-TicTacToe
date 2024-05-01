# AI Tic-Tac-Toe Algorithm Exploration 🤖🎮

Welcome to the AI Tic-Tac-Toe Algorithm repository! This project explores the implementation and comparison of various AI algorithms for the classic game of Tic-Tac-Toe. Dive into different strategic approaches and witness their performance in gameplay scenarios. 🚀🔍

---

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Algorithms and Techniques](#algorithms-and-techniques)
  - [Temporal Difference Learning](#temporal-difference-learning)
  - [Rollout Policy Adaptation (Monte Carlo)](#rollout-policy-adaptation-monte-carlo)
  - [Sparse Sampling (Tree Search)](#sparse-sampling-tree-search)
- [Evaluation Criteria](#evaluation-criteria)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Running the Main Script](#running-the-main-script)
  - [Running Individual Algorithm Scripts](#running-individual-algorithm-scripts)
- [Results and Visualizations](#results-and-visualizations)
- [YouTube Links for Algorithm Demonstrations](#youtube-links-for-algorithm-demonstrations)
- [Contribution](#contribution)

---

## Project Overview 🌟
<a name="project-overview"></a>
The primary goal of this project is to develop and evaluate three distinct AI agents for playing Tic-Tac-Toe, each employing a unique algorithmic strategy. The agents use the following techniques:

1. **Temporal Difference Learning** 🧠
2. **Rollout Policy Adaptation (Monte Carlo)** 🎲
3. **Sparse Sampling (Tree Search)** 🌳

Explore how these AI agents perform in terms of learning speed, efficiency, and adaptability across different game scenarios. 📊

---

## Repository Structure 📂
<a name="repository-structure"></a>
The repository contains the following key files and components:

- `main.py`: Main entry point for executing and comparing the AI algorithms.
- `temporallearning.py`: Implementation of the Temporal Difference Learning algorithm.
- `monteclaro.py`: Implementation of the Rollout Policy Adaptation (Monte Carlo) algorithm.
- `sparsesampling.py`: Implementation of the Sparse Sampling (Tree Search) algorithm.
- `Tic Tac Toe.pdf`: PowerPoint presentation providing an overview of the project. 📄

---

## Algorithms and Techniques 🧩
<a name="algorithms-and-techniques"></a>
### Temporal Difference Learning
<a name="temporal-difference-learning"></a>
- **Description**: Utilizes reinforcement learning principles to make optimal moves by updating value estimates based on immediate and future rewards.
- **Key Concepts**: Reinforcement Learning, Q-Learning.
- **YouTube Link**: Watch a detailed demonstration of the Temporal Difference Learning algorithm in action: [Temporal Difference Learning Algorithm](https://www.youtube.com/watch?v=L64E_NTZJ_0) 📺

### Rollout Policy Adaptation (Monte Carlo)
<a name="rollout-policy-adaptation-monte-carlo"></a>
- **Description**: Employs random simulations (rollouts) to approximate the value of actions, aiding in decision-making for optimal moves.
- **Key Concepts**: Monte Carlo Simulations, Rollout Policy Adaptation.
- **YouTube Link**: Explore how the Rollout Policy Adaptation algorithm works through this interactive demonstration: [Rollout Policy Adaptation (Monte Carlo) Algorithm Demo](https://www.youtube.com/watch?v=PsxnVsCplYc) 📹

### Sparse Sampling (Tree Search)
<a name="sparse-sampling-tree-search"></a>
- **Description**: Efficiently explores the search space by selectively evaluating potential moves, ideal for games with large state spaces.
- **Key Concepts**: Tree Search, Exploration vs. Exploitation.
- **YouTube Link**: Learn more about Sparse Sampling (Tree Search) and its application in Tic-Tac-Toe: [Sparse Sampling (Tree Search) Algorithm Demo](https://www.youtube.com/watch?v=0Ey02HT_1Ho) 🎥

---

## Evaluation Criteria 📊
<a name="evaluation-criteria"></a>
The project evaluates AI agent performance using the following criteria:

- No. of Episodes
- Regret
- Average Total Rewards per Episode
- Win Rate
- Learning Speed
- Adaptability
- Efficiency

---

## Getting Started 🚀
<a name="getting-started"></a>
To explore and run the AI Tic-Tac-Toe algorithms locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/vaishnavi-chowdary/AI-TicTacToe.git
    ```
   
2. Install dependencies:
   ```bash
   pip install matplotlib pygame
    ```
   ---

## Usage ℹ️
<a name="usage"></a>
### Running the Main Script
<a name="running-the-main-script"></a>
To execute and compare the different AI algorithms across multiple Tic-Tac-Toe games, run the `main.py` script:

```bash
python main.py
```

This script orchestrates the execution of algorithms, displays game outcomes, evaluation metrics, and generates visualizations for performance comparison.

### Running Individual Algorithm Scripts
<a name="running-individual-algorithm-scripts"></a>
Alternatively, run individual algorithm scripts to observe their behavior independently:

```bash
python temporallearning.py
python monteclaro.py
python sparsesampling.py
```

---

## Results and Visualizations 📊📈
<a name="results-and-visualizations"></a>
### Evaluation Metrics

The AI agents were evaluated based on several key metrics to assess their performance in playing Tic-Tac-Toe:

1. **No. of Episodes**
2. **Regret**
3. **Average Total Rewards per Episode**
4. **Win Rate**
5. **Learning Speed**
6. **Adaptability**
7. **Efficiency**

### Visualizations

#### Tic Tac Toe Board

![Board](https://i.ibb.co/wpWSYPd/board.jpg)
*Figure 1: Tic Tac Toe.*

#### Win Rate Comparison

![Efficiency Comparison](https://i.ibb.co/KKx5RLv/individual-graph.jpg)
*Figure 2: Comparison of efficiency over number of game plays among indvidual AI algorithms.*

#### Combined Performance Metrics

![Combined Metrics](https://i.ibb.co/d0q86kd/combined-graph.jpg)
*Figure 3: Combined performance metrics of AI agents.*

---

## YouTube Link for Algorithm Demonstration 📹
<a name="youtube-links-for-algorithm-demonstrations"></a>
For a more interactive understanding, check out this YouTube link demonstrating the gameplay and decision-making process of each AI algorithms:

[AI Tic Tac Toe Algorithm Demo](https://www.youtube.com/watch?v=1EEoXy5rEIY)
  
---

## Contribution 🤝
<a name="contribution"></a>
This project was created by @vaishnavi-chowdary and @Kajaganesh. Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---
Copyright © 2024 Vaishnavi Chowdary Kommi

