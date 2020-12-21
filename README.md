# ***PyPep_Toolbox***

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Git](https://img.shields.io/badge/-Git-black?style=flat-square&logo=git)
-----
**PyPep toolbox** includes the basic yet important sequence tools that help the researchers to formulate within stipulated time.It includes operations like-
- addition
- multiplying with an integer
- counting of amino acids 
- overlapping and non-overlapping subsequences
- molecular weight
- charge at a given pH, etc.
and all these embedded to the **sequencer** which outputs for each calculated outputs from the given inputs.

There are two parts - **CLI toolbox and GUI toolbox.**
- For nerdy experience, pypep-cli provides a high-level commandline interface for the peptide sequence management system. 
- For a decent gui experience, pypep-gui can be used for easy understanding and handling of the data. It is intended as an end user interface and enables some options better suited for interactive usage by default compared to more specialized laboratory tools like spectrophotometer and others.

#### Download the files and see the instructions (demo) here: [PyPep webpage](https://suvankarpioneer.github.io/eurymedons/)
-----
# Installation - 
The `requirements.txt` file contains all the required libraries to be installed.

Use `pip install -r requirements.txt` to install the required dependencies(Or pip3).

The python version is to be more than 3.0.0

Extra modules needed are -
  * Tkinter (installing ttk)
  * simple_term_menu
  * biopython
  
 Use `pip install libname` to install the apps.
 
 Steps after extracting the zip file - 
  * Go to the project folder and start with the development environment with conda or venv.
  * Run `python pypep-cli.py` for using the CLI.
  * Run `python pypep-gui.py` -> for running the GUI app.
-----
**Features of PyPep GUI** -
An example for a quick demo: In the pattern field input a sequence(LKHAKHAKGTADAL).
In the input fields place a required subsequence or amino acid(AKH or A).
In the integer field put any integer to get multiplied with the sequence(say 4)
Then click the buttons to get required outputs.

- [Sequencer] - Outputs the permutations of the sequences with given amino
	                    inputs.
- [Amino count] - Returns the number of amino acids. In case a given amino
	                    acid, it's count is returned.
- [Amino percentage] - Same as amino count except it returns the percentage.
- [Add] - Adds two input sequences. (right of main sequence)
- [Add on left] - Adds the second input sequence to the left.
- [Multiply] - multiplies the sequence with given input integer.
- [Complement] - returns the complement of the sequence.
- [Compare] - Compares two sequences on their equality
- [Non-overlapping count] - returns count of non-overlapping subsequence.
- [Overlapping count] - returns count of overlapping subsequence.
- [Contains] - returns if the sequence contains the input subsequence.
- [find] - Finds the input amino acid or subsequence.
- [Molecular weight] - returns the molecular weight of the sequence
- [Isoelectric point] - returns the isoelectric_point.
- [Charge at given pH] - returns the charge of the sequence at input pH.
- [Molar Extinction Coefficient] - returns the molar_extinction_coefficient
	                          of the sequence.
- Also the cli toolset exports the output data to a text file if needed.
