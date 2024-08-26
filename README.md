# SCAMP5 Compiler

## Introduction

The SCAMP5 Compiler is designed to transform Python code into assembly code executable on the SCAMP5 processing architecture. This project includes libraries for code transformation, simulation, and image processing capabilities tailored for the SCAMP5 environment.

## Features

- **Code Transformation:** Converts Python scripts into assembly code specific to SCAMP5 devices.
- **Image Processing Simulation:** Facilitates the development and testing of image processing algorithms on a simulated SCAMP5 environment.
- **Extensible Framework:** Easily extendable to incorporate new instructions and functionalities into the compiler framework.

## Installation

### Prerequisites

Make sure the following software is installed on your system:

- Python 3.x
- opencv-python
- numpy
- matplotlib

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/SCAMP5-Compiler.git
   cd SCAMP5-Compiler
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Directory Structure

SCAMP5-Compiler/  
├── src/ - Source code directory  
│   ├── transfor_tool.py - Main transformation tool  
│   └── ...  
├── lib/ - Libraries for simulation and transformation  
│   ├── ast_tool.py - AST visitor and assembly generator  
│   └── sim/ - Simulation library for SCAMP5 operations  
│       └── sim_py/ - Python-based SCAMP5 simulation library  
├── example/ - Example scripts and usage scenarios  
│   ├── median_filter.py - Median filtering example  
│   └── ...  
└── requirements.txt - Python dependencies  


### Usage

#### Converting Python Code to SCAMP5 Assembly

**Run the Conversion Tool:**

```bash
python src/transfor_tool.py -path example/your_script.py -o output/your_output.asm

```

Use the `-path` option to specify the path to the input Python file and `-o` to specify the path for the output assembly code file.

**Running Simulations**

1. Execute Example Scripts:

```bash
python example/median_filter.py
```

This script will launch a simulation of the SCAMP5 platform, allowing you to observe the effects of the median filter algorithm.

### Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bug reports and feature requests.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.
