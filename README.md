# Sphere Volume Approximation

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Matplotlib](https://img.shields.io/badge/Render-Matplotlib-orange)

## Abstract

This repository contains a Python-based visualization tool that demonstrates the relationship between numerical precision and geometric resolution. By computing the volume of a sphere using arbitrary-precision arithmetic (`mpmath`), the script simultaneously renders a 3D wireframe mesh that evolves from a low-polygon approximation to a high-fidelity sphere.

The project serves as a visual metaphor for mathematical convergence, mapping the decimal precision of the calculated volume to the vertex density of the 3D object.

## Demo

![Uploading sphere_volume-ezgif.com-video-to-gif-converter.gif…]()



> *Figure 1: Visual output demonstrating the convergence of mesh resolution (polygons) alongside the increasing decimal precision of the calculated volume.*

## Mathematical Context

The program calculates the volume $V$ of a sphere with radius $r$ using the standard formula:

$$V = \frac{4}{3} \pi r^3$$

To demonstrate high-precision computing, the script utilizes the **mpmath** library to compute $\pi$ and the resulting volume to 100 decimal places. As the computation progresses, the visualization updates the mesh resolution $R$ based on the percentage of digits revealed ($P$):

$$R_{current} = R_{min} + P \times (R_{max} - R_{min})$$

Where $R_{min} = 4$ and $R_{max} = 60$.

## Installation

Ensure you have Python 3.8+ installed. This project requires `ffmpeg` for video rendering.

### 1. Clone the Repository
https://github.com/Aucco1/Volume-Of-a-Sphere.git
gh repo clone Aucco1/Volume-Of-a-Sphere

### 2. Install Python Dependencies
pip install numpy matplotlib mpmath

## Configuration

Parameters can be adjusted directly in the script constants:

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `RADIUS` | 5 | The geometric radius of the sphere. |
| `MAX_PRECISION` | 100 | The number of decimal places to calculate. |
| `TOTAL_FRAMES` | 150 | The duration of the animation in frames. |

## License

This project is open-source and available under the [MIT License](LICENSE).
