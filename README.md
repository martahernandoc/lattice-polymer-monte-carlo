# lattice-polymer-monte-carlo
Monte Carlo simulations of self-avoiding walks and polymer translocation on a 2D lattice.
# Lattice Polymer Models: Monte Carlo Simulations

## Overview

This project investigates the statistical and dynamical properties of **self-avoiding walks (SAWs)** on a two-dimensional square lattice.

The aim is to study polymer configurations using different numerical methods and explore their application to simplified models of RNA ejection and translocation through a nanopore.

The project was developed as part of the *M1 Physique Fondamentale / Physique Appliquée* programme at Université Paris Cité and Sorbonne Université (2025–2026).

## Numerical Methods

Three main approaches are explored:

### 1. Exact Enumeration

- Recursive generation of all possible self-avoiding walks for a given chain length.
- Calculation of the total number of configurations, Z(N).
- Computation of the mean squared end-to-end distance, ⟨r²⟩.
- Study of the scaling relation ⟨r²⟩ ~ N^(2ν).

The computational cost increases rapidly with chain length, limiting this method to relatively small polymers (N ≤ 15).

### 2. Rosenbluth Sampling

- Sequential growth of self-avoiding polymer chains.
- Random selection among available lattice sites.
- Assignment of Rosenbluth weights to account for the number of available growth directions.
- Estimation of the mean squared end-to-end distance for longer chains.

This method allows the exploration of larger chain lengths, although statistical fluctuations become important.

### 3. Monte Carlo Simulations

Two types of Monte Carlo moves are investigated:

- **Local moves:** random displacement of individual monomers while preserving chain connectivity and self-avoidance.
- **Slithering snake moves:** removal of one end monomer and addition of a new monomer at the opposite end.

Their efficiency is compared through relaxation and first-passage observables.

## Polymer Translocation Through a Pore

A separate simulation illustrates the dynamics of a self-avoiding polymer confined within a two-dimensional square lattice.

The polymer evolves through slithering snake moves and can escape through a pore in the confining boundary. Its evolution is visualised using an animation.

This model provides a qualitative illustration of polymer ejection dynamics.

## Results

The main observable is the mean squared end-to-end distance:

⟨r²⟩ ~ N^(2ν)

For two-dimensional self-avoiding walks, the theoretical value is ν = 3/4.

The project obtained the following estimates:

| Method | Estimated ν |
|---|---:|
| Exact enumeration | 0.73 |
| Rosenbluth sampling | 0.70 |
| Monte Carlo (slithering snake) | 1.46 |

The exact enumeration result is consistent with the theoretical prediction. Rosenbluth sampling gives a reasonable estimate, with larger statistical fluctuations.

The Monte Carlo estimate is not reliable: incomplete thermalisation and strong correlations between successive configurations introduce significant bias.

## Technologies

- Python
- NumPy
- Matplotlib
- Monte Carlo methods
- Numerical simulation
- Statistical physics

## Current Limitations and Future Work

The project is an exploratory implementation and some components remain incomplete.

Potential improvements include:

- Improving Monte Carlo sampling and thermalisation.
- Investigating temporal correlations between configurations.
- Implementing pruning and enrichment techniques for Rosenbluth sampling.
- Extending the analysis of polymer translocation dynamics.

## Author

Marta Hernando Conde

Physics undergraduate student

Universidad Complutense de Madrid
