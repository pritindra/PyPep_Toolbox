# ***PyPep_Toolbox***

# Technologies used
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Git](https://img.shields.io/badge/-Git-black?style=flat-square&logo=git)
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

Features of PyPep GUI -
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
