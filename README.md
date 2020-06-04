## hor2vec

[![Coverage Status](https://coveralls.io/repos/github/M157q/hor2vec/badge.svg?branch=master)](https://coveralls.io/github/M157q/hor2vec?branch=master)

```
 _               ____
| |__   ___  _ _|___ \__   _____  ___
| '_ \ / _ \| '__|__) \ \ / / _ \/ __|
| | | | (_) | |  / __/ \ V /  __/ (__
|_| |_|\___/|_| |_____| \_/ \___|\___|
```

Change your horizontal pure text to vertical with some options.

---

## Installation

- `hor2vec` doesn't use any third party Python package.
- You can just `git clone` from GitHub, `cd` into cloned `hor2vec` dir, and use `python3 hor2vec ...`.
- You can also install from PyPI with `pip install hor2vec`, after that, you can just use `hor2vec ...`.


### GitHub

`$ git clone https://github.com/M157q/hor2vec`


### PyPI

`$ pip install hor2vec`

---

## Usage

```
usage: hor2vec [-h] [-s SEP] [-ld {l2r,r2l}] [-wd {t2b,b2t}] [-nr] [-fw]
               [input]

positional arguments:
  input                 The file has horizontal pure text to be changed to
                        vertical. If not been given in the command, will use
                        the stdin as input.

optional arguments:
  -h, --help            show this help message and exit
  -s SEP, --sep SEP, --separator SEP
                        The separator between lines. Default is '', you can
                        use ' ', '|' or any other strings.
  -ld {l2r,r2l}, --line-direction {l2r,r2l}
                        The reading direction of each line. Default is 'l2r'
                        (left to right), you can choose 'r2l' (right to left).
  -wd {t2b,b2t}, --word-direction {t2b,b2t}
                        The reading direction of each word/character. Default
                        is 't2b' (top to bottom), you can choose 'b2t' (bottom
                        to top).
  -nr, --no-rotate      If this option has been given, hor2vec won't rotate
                        the input.
  -fw, --full-width     If this option has been given, hor2vec will use
                        fullwidth characters instead of halfwidth characters.
```

### Usage - Docker

- Get the Docker image of `hor2vec`
    - `docker pull M157q/hor2vec`
- Run Docker image and use `stdin` as input
    - `docker run -it --rm M157q/hor2vec`
    - type in the input string
    - Press `Ctrl-D`
    - Get the output
- Run Docker image use local file as input
    - `docker run -it --rm -v $PWD:/srv/work m157q/hor2vec ${FILENAME}`
    - e.g., If you have a file `a` in your current directory:
        - `docker run -it --rm -v $PWD:/srv/work m157q/hor2vec a`
    - Get the output

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
$ python3 hor2vec tests/data/chinese_test_data.txt
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
$ python3 hor2vec -s '|' tests/data/chinese_test_data.txt
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
$ python3 hor2vec -s '|' -ld r2l tests/data/chinese_test_data.txt
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
$ python3 hor2vec -s '|' -ld r2l -wd b2t tests/data/chinese_test_data.txt
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

```
$ python3 hor2vec -nr -ld r2l tests/data/chinese_test_data.txt
　途旅的生陌個一上踏要我
　度溫的伴陪你有記忘會我
　獨孤憾遺最中心下放著試
　　　　　　　　福祝著學
人的敢勇最界世全成變要我
路的好最是都排安切一信相
　　　　　　　　　　見再
```

```
$ python3 hor2vec -nr -ld r2l -wd b2t tests/data/chinese_test_data.txt
　　　　　　　　　　見再
路的好最是都排安切一信相
人的敢勇最界世全成變要我
　　　　　　　　福祝著學
　獨孤憾遺最中心下放著試
　度溫的伴陪你有記忘會我
　途旅的生陌個一上踏要我
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
$ python3 hor2vec tests/data/english_test_data.txt
Iwtbyf Cw?
 aoeor ae
 n  ui n
 t  re
     n
     d
     .
```

```
$ python3 hor2vec -fw tests/data/english_test_data.txt
Ｉｗｔｂｙｆ Ｃｗ？
　ａｏｅｏｒ ａｅ
　ｎ　　ｕｉ ｎ
　ｔ　　ｒｅ
　　　　　ｎ
　　　　　ｄ
　　　　　．
```

```
$ python3 hor2vec -s ' ' tests/data/english_test_data.txt
I w t b y f   C w ?
  a o e o r   a e
  n     u i   n
  t     r e
          n
          d
          .
```

```
$ python3 hor2vec -s ' ' -ld r2l tests/data/english_test_data.txt
? w C   f y b t w I
  e a   r o e o a
    n   i u     n
        e r     t
        n
        d
        .
```

```
$ python3 hor2vec -s ' ' -ld r2l -wd b2t tests/data/english_test_data.txt
        .
        d
        n
        e r     t
    n   i u     n
  e a   r o e o a
? w C   f y b t w I
```

```
$ python3 hor2vec -nr -ld r2l tests/data/english_test_data.txt
      I
   tnaw
     ot
     eb
   ruoy
.dneirf

    naC
     ew
      ?
```

```
$ python3 hor2vec -nr -ld r2l -wd b2t tests/data/english_test_data.txt
      ?
     ew
    naC

.dneirf
   ruoy
     eb
     ot
   tnaw
      I
```

---

## Development

### Install dev dependencies

`pipenv install --dev`

or

`pip install -r requirements-test.txt`

### Testings

`python -m pytest --cov hor2vec/  --cov-report html --cov-report term`
or just
`make test`
