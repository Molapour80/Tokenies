<i class="fa-sharp fa-light fa-ghost"></i>
# Code Tokenizer

A simple code tokenizer written in Python that processes a string of code and extracts various types of tokens, including integers, floats, identifiers, operators, keywords, delimiters, strings, and comments.

## <i class="fa-sharp fa-regular fa-pen"></i>Features

- Supports multiple token types:
  - Integer
  - Float
  - Identifier
  - Operator
  - Keyword
  - Delimiter
  - String
  - Comment
- Handles single-line and multi-line comments
- Uses regular expressions for tokenization

## <i class="fa-sharp fa-regular fa-download"></i> Requirements

- Python 3
- os
- re



# <i class="fa-sharp fa-regular fa-folder-open"></i>Usage
Usage
'''pytho
from tokenizer import tokenize

code = '''
// This is a comment
ashar arz;
ashar tool;
/*
This is a multi-line comment
*/
arz = begir (ashar);
tool = begir (ashar);
agar(tool == arz) {
    chap("moraba ast");
    chap("masahat");
    chap(arz*arz);
    chap("mohit");
    chap (arz*4);
}
'''

tokens = tokenize(code)
for token_type, value in tokens:
    print('Token: {}, Value: {}'.format(token_type, value))


'''



