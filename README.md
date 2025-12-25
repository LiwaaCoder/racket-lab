# racquet-lab

**racquet-lab** is a Python library that bridges the gap between Tennis Equipment Physics and Software Engineering. It provides tools to calculate advanced racket properties like Recoil Weight and MGR/I (Maneuverability Index), and simulates racket customization with scientific accuracy.

## Features

- **Recoil Weight Calculation**: Determine a racket's resistance to "recoil" (angular acceleration) upon ball impact.
- **MGR/I (Maneuverability Index)**: Calculate the efficiency of a racket's swing dynamics based on pendulum physics.
- **Scientific Customization**: Simulate adding lead tape (mass) at specific positions and instantly get updated specifications (Balance, Swingweight, Recoil Weight) using the Parallel Axis Theorem.
- **Immutability**: The `Racket` class is immutable, ensuring safe calculations without side effects.
- **Recommendation Engine**:
    - **Tension Calculator**: Suggests optimal tension based on string material, head size, and player profile.
    - **Similarity Search**: Finds matching rackets using weighted Euclidean distance.

## Installation

```bash
pip install racquet-lab
```
*(Or clone the repository and run `pip install .`)*

## Usage

### 1. Basic Specifications
```python
from racquet_lab.racket import Racket

# Initialize a standard player's racket
# Mass: 305g, Balance: 32cm, Swingweight: 290 kg·cm²
racket = Racket("Pure Aero", mass_g=305, balance_cm=32.0, swingweight=290)

print(f"Recoil Weight: {racket.recoil_weight():.2f}")
print(f"MGR/I: {racket.mgr_i():.2f}")
```

### 2. Customization (Adding Weight)
Simulate adding 4 grams of lead tape at the 12 o'clock position (approx. 70cm from handle).

```python
# Add 4g at 70cm
customized_racket = racket.customize(mass_added_g=4, position_cm=70)

print(f"Original SW: {racket.swingweight}")
print(f"New SW: {customized_racket.swingweight}")
print(f"New Balance: {customized_racket.balance_cm:.2f} cm")
```

### 3. Advisor
```python
from racquet_lab.advisor import StringsAdvisor, StringMaterial, PlayerProfile

player = PlayerProfile(has_injury_history=True)
tension = StringsAdvisor.suggest_tension(StringMaterial.POLYESTER, 100, player)
print(f"Suggested Tension: {tension} lbs")
```

## Physics Background

### Recoil Weight
Formula: $SW - Mass_{kg} \times (Balance_{cm} - 10)^2$

### MGR/I
A ratio derived from double pendulum physics that describes how easily a racket can be maneuvered to generate racket head speed. Typical values range from 20.0 to 21.5.

## Development

Run tests:
```bash
python -m unittest discover tests
```
