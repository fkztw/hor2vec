## hor2vec  
  
```  
 _               ____  
| |__   ___  _ _|___ \__   _____  ___  
| '_ \ / _ \| '__|__) \ \ / / _ \/ __|  
| | | | (_) | |  / __/ \ V /  __/ (__  
|_| |_|\___/|_| |_____| \_/ \___|\___|  
```  
  
Change your pure text arrangement to what you want it to be  
  
---  
  
## Usage  
  
```  
usage: hor2vec [-h] [-s SEP] [-ld {l2r,r2l}] [-wd {t2b,b2t}] [input]  
  
positional arguments:  
  input                 The file contains puretext to be re-arranged. If not  
                        been given in the command, will use the stdin as  
                        input.  
  
optional arguments:  
  -h, --help            show this help message and exit  
  -s SEP, --sep SEP, --seprator SEP  
                        The seperator between lines. Default is '', you can  
                        use ' ', '|' or any other strings.  
  -ld {l2r,r2l}, --line-direction {l2r,r2l}  
                        The reading direction of each line. Default is 'l2r'  
                        (left to right), you can choose 'r2l' (right to left).  
  -wd {t2b,b2t}, --word-direction {t2b,b2t}  
                        The reading direction of each word. Default is 't2b'  
                        (top to bottom), you can choose 'b2t' (bottom to top).  
```  
