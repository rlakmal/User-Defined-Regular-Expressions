
# Horspool String Searching Algorithm

This is a Python implementation of the Horspool string searching algorithm. The Horspool algorithm is used to find occurrences of a pattern string within a given text string. The implementation includes variations of the algorithm to handle different pattern cases, such as wildcard characters and anchor characters.

## Usage

1. download the code files.

2. Modify the text and pattern input files as needed. You can replace the contents of the `textN.txt` and `patternN.txt` files with your own text and pattern strings.


3. Run the `main.py` script to perform the string search and generate output files.

   python assignment_01.py
   compiler ask to enter N value as your file name.
   for example if you need run text5.txt and pattern5.txt set. Then you should input 5. 

4. The output files, named `outputN.txt`, will be generated, showing the positions where the pattern was found in the text.

## Variations

The algorithm includes different variations to handle various pattern cases:

- `horspool(text, pattern, text_file)`: Basic Horspool algorithm to search for exact pattern matches.
- `horspool_dot(text, pattern, text_file)`: Horspool algorithm with support for the `.` wildcard character.
- `horspool_quest(text, pattern, text_file)`: Horspool algorithm to handle patterns containing `?` characters.
- `horspool_begg(text, pattern, text_file)`: Horspool algorithm to handle patterns anchored at the beginning.
- `horspool_end(text, pattern, text_file)`: Horspool algorithm to handle patterns anchored at the end.

## Input Files

- `textN.txt`: Replace `N` with the specific input number. Contains the text in which the pattern is searched.
- `patternN.txt`: Replace `N` with the specific input number. Contains the pattern string to be searched.

## Output

Output files, named `outputN.txt`, are generated for each input pair. These files contain the positions where the pattern was found in the corresponding text.

