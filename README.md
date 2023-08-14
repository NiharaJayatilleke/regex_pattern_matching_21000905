# regex_pattern_matching_21000905
N.Y Jayatilleke 21000905 <br/><br/>
## Implementation of Regular Expressions Pattern Matching Using the Knuth-Morris-Pratt Algorithm. <br/><br/>

I have used the Python programming language to implement the following regular expressions, <br/>
•	^ - start of line <br/>
•	$ - end of line <br/>
•	| - OR operator <br/>

Here I have used the Knuth-Morris-Pratt Algorithm to implement regular expressions in pattern matching. The algorithm will output a boolean result, 'True' if the pattern was found and 'False' if the pattern was not found.
The output is displayed in the patternmatch.output files of the relevant test cases. <br/><br/>

## Instructions to run the program <br/>
1) First, clone this repository to your local desktop and intsall `Python3` compiler.<br/>
2) After obtaining the code, run the source code 'main.py' to which the patternmatching.py source code has been imported<br/> 
3) I have included many text cases in the 'test data' folder which each include a pair of text and pattern along with the output such as text1.txt, pattern1.txt and patternmatch1.output <br/>
4) Replace any test case (1/2...) with  your string in text#.txt and the respective pattern in pattern#.txt which you wish to run. <br/>
5) you can obtain the results in the repective patternmatch.output (patternmatch#.output) file <br/>
6) If you want to add a new test case without changing the current test cases you can do so by adding files text7.txt, pattern7.txt and patternmatch7.output with relevant content to the 'test data' folder.</br>
Next add the following code to main.py

```python
    #TEST CASE 7
    # Read pattern and text from files (pattern7.txt, text7.txt)
    with open('./test data/pattern7.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text7.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch7.output)
    with open('./test data/patternmatch7.output', 'w') as output_file:
        output_file.write(str(output) + '\n')
```

7) You can repeat step 6 to add more new test cases (8, 9, ...) </br></br>
##
For further details and usage instructions, refer to the individual code files and comments within the repository.




