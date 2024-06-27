#########################
### DICTIONARY SEARCH ###
#########################

### Thông tin phiên bản
## Python 3.12.4
## PyPI 24.1

### Thư viện (libraries)
## Standard
import os, webbrowser

## 3rd-party
import requests, lxml
from bs4 import BeautifulSoup

### User-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

### Thông báo (messages)
NO_WORD_FORMS_FOUND = "No word forms found for this word."

### Cảnh báo (warnings)
WARNING = "WARNING: Please search for word forms using the base form of the word."

### Mã lỗi (errors)
CONNECTION_ERR = "Error: Unable to access the website. Please check your internet connection or try again later."
UNKNOWN_WORD_ERR = "Error: The word is not in the dictionary."
CMD_NOT_FOUND_ERR = "Error: Command not found. Type 'help' for more information."
WF_SYNTAX_ERR = "Error: Incorrect syntax. Type 'wf --help' for usage information."
DF_SYNTAX_ERR = "Error: Incorrect syntax. Type 'df --help' for usage information."

### Bảng trợ giúp (help)
CMD_HELP = '''
Commands:
  wf [word]: Get word forms from the Longman Dictionary.
  df [word]: Open the definition of the word on the Cambridge Dictionary website.
  [command] --help: Show the detailed usage of a command.
  clear: Clear the entire screen.
  exit: Exit the program.
  help: Show this help message.'''

WF_HELP = '''
Usage: wf [word | --help]
Arguments :
            word    Get word forms from the Longman Dictionary.
  --help, -h, -?    Show this help message.'''

DF_HELP = '''
Usage: df [word | --help]
Arguments:
            word    Open the definition of the word on the Cambridge Dictionary website.
  --help, -h, -?    Show this help message.'''

### Hàm (functions)
def wf(word):
    url = f"https://www.ldoceonline.com/dictionary/{word}"
    
    try:
        response = requests.get(url, headers=headers)
    except:
        print(CONNECTION_ERR)
        return None
    
    response.raise_for_status()
    if response.url == f"https://www.ldoceonline.com/spellcheck/english/?q={word}&entrySet=B":
        print(UNKNOWN_WORD_ERR)
        print(WARNING)
        return None
    
    soup = BeautifulSoup(response.content, 'lxml')
    word_forms_div = soup.find('div', class_='wordfams')
    
    if not word_forms_div:
        print(NO_WORD_FORMS_FOUND)
        print(WARNING)
        return None
    
    word_forms = {}
    current_pos = None
    
    for element in word_forms_div.children:
        if element.name == 'span' and 'pos' in element.get('class', []):
            current_pos = element.text.strip().strip('()').capitalize()
            word_forms[current_pos] = []
        elif element.name in ['span', 'a'] and 'w' in element.get('class', []):
            form_word = element.text.strip()
            if current_pos:
                word_forms[current_pos].append(form_word)
        elif element.name == 'span' and 'opp' in element.get('class', []):
            opposite_word = element.text.strip().replace('!', '').strip()
            if current_pos:
                word_forms[current_pos][-1] += f" {opposite_word}"

    return {pos: forms for pos, forms in word_forms.items() if forms}

def df(word):
    url = f"https://dictionary.cambridge.org/vi/dictionary/english/{word}"
    
    try:
        response = requests.get(url, headers=headers)
    except:
        print(CONNECTION_ERR)
        print()
        return None
    
    response.raise_for_status()
    if response.url == 'https://dictionary.cambridge.org/vi/dictionary/english/':
        print(UNKNOWN_WORD_ERR)
        print()
        return None
    
    webbrowser.open_new_tab(url)

### Chương trình (main)
while True:
    cmd_line = input(">>> ").lower()
    args = cmd_line.split()
    if not args:
        continue
    
    if args[0] == "wf":
        if len(args) != 2:
            print(WF_SYNTAX_ERR)
            continue
        if args[1] in ["--help", "-h", "-?"]:
            print(WF_HELP)
        else:
            word_forms = wf(args[1])
            if word_forms:
                for pos, forms in word_forms.items():
                    forms_str = ', '.join(forms)
                    print(f"{pos}: {forms_str}")
    elif args[0] == "df":
        if len(args) != 2:
            print(DF_SYNTAX_ERR)
            continue
        if args[1] in ["--help", "-h", "-?"]:
            print(DF_HELP)
        else:
            df(args[1])
            continue
    elif args[0] in ["cls", "clr", "clrscr", "clear"]:
        os.system("cls")
        continue
    elif args[0] == "exit":
        break
    elif args[0] == "help":
        print(CMD_HELP)
    else:
        print(CMD_NOT_FOUND_ERR)
    print()