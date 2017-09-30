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
  
## Installation  
  
### GitHub  
  
`$ git clone https://github.com/M157q/hor2vec`  
  
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
  
---  
  
## Examples  
  
### Chinese  
  
```  
$ cat tests/data/chinese_test_data.txt  
我要踏上一個陌生的旅途  
我會忘記有你陪伴的溫度  
試著放下心中最遺憾孤獨  
學著祝福  
我要變成全世界最勇敢的人  
相信一切安排都是最好的路  
再見  
```  
  
```  
$ python hor2vec tests/data/chinese_test_data.txt  
我我試學我相再  
要會著著要信見  
踏忘放祝變一  
上記下福成切  
一有心　全安  
個你中　世排  
陌陪最　界都  
生伴遺　最是  
的的憾　勇最  
旅溫孤　敢好  
途度獨　的的  
　　　　人路  
```  
  
```  
$ python hor2vec -s '|' tests/data/chinese_test_data.txt  
我|我|試|學|我|相|再  
要|會|著|著|要|信|見  
踏|忘|放|祝|變|一|  
上|記|下|福|成|切|  
一|有|心|　|全|安|  
個|你|中|　|世|排|  
陌|陪|最|　|界|都|  
生|伴|遺|　|最|是|  
的|的|憾|　|勇|最|  
旅|溫|孤|　|敢|好|  
途|度|獨|　|的|的|  
　|　|　|　|人|路|  
```  
  
```  
$ python hor2vec -s '|' -ld r2l tests/data/chinese_test_data.txt  
再|相|我|學|試|我|我  
見|信|要|著|著|會|要  
　|一|變|祝|放|忘|踏  
　|切|成|福|下|記|上  
　|安|全|　|心|有|一  
　|排|世|　|中|你|個  
　|都|界|　|最|陪|陌  
　|是|最|　|遺|伴|生  
　|最|勇|　|憾|的|的  
　|好|敢|　|孤|溫|旅  
　|的|的|　|獨|度|途  
　|路|人|　|　|　|  
```  
  
```  
$ python hor2vec -s '|' -ld r2l -wd b2t tests/data/chinese_test_data.txt  
　|路|人|　|　|　|  
　|的|的|　|獨|度|途  
　|好|敢|　|孤|溫|旅  
　|最|勇|　|憾|的|的  
　|是|最|　|遺|伴|生  
　|都|界|　|最|陪|陌  
　|排|世|　|中|你|個  
　|安|全|　|心|有|一  
　|切|成|福|下|記|上  
　|一|變|祝|放|忘|踏  
見|信|要|著|著|會|要  
再|相|我|學|試|我|我  
```  
  
### English  
  
```  
$ cat tests/data/english_test_data.txt  
I  
want  
to  
be  
your  
friend.  
  
Can  
we  
?  
```  
  
```  
$ python hor2vec tests/data/english_test_data.txt  
Iwtbyf Cw?  
 aoeor ae  
 n  ui n  
 t  re  
     n  
     d  
     .  
```  
  
```  
$ python hor2vec -s ' ' tests/data/english_test_data.txt  
I w t b y f   C w ?  
  a o e o r   a e  
  n     u i   n  
  t     r e  
          n  
          d  
          .  
```  
  
```  
$ python hor2vec -s ' ' -ld r2l tests/data/english_test_data.txt  
? w C   f y b t w I  
  e a   r o e o a  
    n   i u     n  
        e r     t  
        n  
        d  
        .  
```  
  
```  
$ python hor2vec -s ' ' -ld r2l -wd b2t tests/data/english_test_data.txt  
        .  
        d  
        n  
        e r     t  
    n   i u     n  
  e a   r o e o a  
? w C   f y b t w I  
```  
