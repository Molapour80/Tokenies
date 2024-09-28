import re
import os

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Token types
TOKEN_INTEGER = 'INTEGER'
TOKEN_FLOAT = 'FLOAT'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_DELIMITER = 'DELIMITER'
TOKEN_STRING = 'STRING'
TOKEN_COMMENT = 'COMMENT'

# Regular expressions for token patterns
INTEGER_PATTERN = r'\b\d+\b'
FLOAT_PATTERN = r'-?\b\d+\.\d+\b|\b\d+\.\d+e[+-]?\d+\b'
IDENTIFIER_PATTERN = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b|\bbegir\b|\bachap\b|\bsahih\b'
OPERATOR_PATTERN = r'[+\-*/%]|==|!=|<=|>=|<|>|='
KEYWORD_PATTERN = r'\b(if|else|while|for|in|range|break|continue|def|return|chap|agar|begir|sahih|ashar)\b'
DELIMITER_PATTERN = r'[,.:;!?(){}\[\]]'
STRING_PATTERN = r'"(?:[^"\\]|\\.)*"'
COMMENT_PATTERN = r'//.*?$|/\*.*?\*/'

def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        # Skip whitespace
        if code[position].isspace():
            position += 1
            continue
        
        # Token for comments
        match = re.match(COMMENT_PATTERN, code[position:], re.MULTILINE)
        if match:
            value = match.group(0)
            tokens.append((TOKEN_COMMENT, value))
            position += len(value)
            continue

        # Integer token
        match = re.match(INTEGER_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_INTEGER, int(value)))
            position += len(value)
            continue

        # Float token
        match = re.match(FLOAT_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_FLOAT, float(value)))
            position += len(value)
            continue

        # Identifier token
        match = re.match(IDENTIFIER_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_IDENTIFIER, value))
            position += len(value)
            continue

        # Operator token
        match = re.match(OPERATOR_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_OPERATOR, value))
            position += len(value)
            continue

        # Keyword token
        match = re.match(KEYWORD_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_KEYWORD, value))
            position += len(value)
            continue

        # Delimiter token
        match = re.match(DELIMITER_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_DELIMITER, value))
            position += len(value)
            continue

        # String token
        match = re.match(STRING_PATTERN, code[position:])
        if match:
            value = match.group(0)
            tokens.append((TOKEN_STRING, value))
            position += len(value)
            continue

        # Invalid token
        raise ValueError(f'Invalid token at position {position}: "{code[position]}"')

    return tokens

# Sample code for tokenization
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
agar(tool!= arz){
    chap("mostatil ast");
    chap("masahat");
    chap(arz*tool);
    chap("mohit");
    chap (arz*2+tool*2)
}
'''

try:
    tokens = tokenize(code)
    for token_type, value in tokens:
        print('Token: {}, Value: {}'.format(token_type, value))
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")
