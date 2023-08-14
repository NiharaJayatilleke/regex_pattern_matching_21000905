import pattern_matching as pm

def main():

    #TEST CASE 1
    # Read pattern and text from files (pattern1.txt, text1.txt)
    with open('./test data/pattern1.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text1.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch1.output)
    with open('./test data/patternmatch1.output', 'w') as output_file:
        output_file.write(str(output) + '\n')


    #TEST CASE 2
    # Read pattern and text from files (pattern2.txt, text2.txt)
    with open('./test data/pattern2.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text2.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch2.output)
    with open('./test data/patternmatch2.output', 'w') as output_file:
        output_file.write(str(output) + '\n')


    #TEST CASE 3
    # Read pattern and text from files (pattern3.txt, text3.txt)
    with open('./test data/pattern3.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text3.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch3.output)
    with open('./test data/patternmatch3.output', 'w') as output_file:
        output_file.write(str(output) + '\n')
    

    #TEST CASE 4
    # Read pattern and text from files (pattern4.txt, text4.txt)
    with open('./test data/pattern4.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text4.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch4.output)
    with open('./test data/patternmatch4.output', 'w') as output_file:
        output_file.write(str(output) + '\n')

    

    #TEST CASE 5
    # Read pattern and text from files (pattern5.txt, text5.txt)
    with open('./test data/pattern5.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text5.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch5.output)
    with open('./test data/patternmatch5.output', 'w') as output_file:
        output_file.write(str(output) + '\n')


    #TEST CASE 6
    # Read pattern and text from files (pattern6.txt, text6.txt)
    with open('./test data/pattern6.txt', 'r') as pattern_file:
        pattern = pattern_file.read().strip()
    with open('./test data/text6.txt', 'r') as text_file:
        text = text_file.read().strip()

    output = pm.regex_search(text, pattern)

    # Write True if pattern was found and False if not found to the output file (patternmatch6.output)
    with open('./test data/patternmatch6.output', 'w') as output_file:
        output_file.write(str(output) + '\n')

if __name__ == "__main__":
    main()
