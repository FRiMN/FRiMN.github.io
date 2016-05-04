Title: Генерация соли
Slug: generate_hash_string
Date: 2016-05-04
Category: tutorial
Tags: sh, unix, password, hash
Summary: Генерация строк из случайной последовательности символов (соли и т.п.)


## Формат хэша пароля

Можно встретить следующий вариант хранения паролей:

    $id$salt$encrypted

где:

- *id* -- алгоритм хэширования
    + **1** -- MD5
    + **2** -- blowfish
    + **5** -- SHA-256
    + **6** -- SHA-512
- *salt* -- соль
- *encrypted* -- результат применения алгоритма хэширования к паролю и соли

### Пример

    $1$vTsHxl6j$dFvR.mqYF/SP3kysqCM/s/

`dFvR.mqYF/SP3kysqCM/s/` -- хэш md5 (`1`) от парольной фразы с солью `vTsHxl6j`.


## openssl rand

Генерирует псевдослучайную последовательность символов

```sh
# generates a base64 encoded 32 chars length random string
$ openssl rand -base64 32
CJ/a0JsZlStDceTGtwfVkInUwJZ6rl7PnNtysz0/Kb8=
```


## pwgen

Генерирует псевдослучайную последовательность символов удобную для запоминания

```sh
# generate 2 passwords of 8 chars length each
$ pwgen -nA 8 2
aafaba3w mee6esho
```


## apg

Генерирует псевдослучайную последовательность символов удобную для запоминания и произношения

```sh
$ apg -n1 -t -a0
WoonMirg; (Woon-Mirg-SEMICOLON)
```


## makepasswd

Генерирует псевдослучайную последовательность символов, а также шифрует пароли с солью

```sh
# generates 2 passwords of 20 chars each
$ makepasswd --char 20 --count 2
pdfvDKXNth144SEtcGpJ
m5Qoe1PQQBFDd69qJYSz

# ************************

# encrypt a password (instead of generating)
$ echo 'secret-password' > /tmp/pwd.txt

# аналогично --cryptsalt 0
$ makepasswd --clearfrom /tmp/pwd.txt --crypt
secret-password   hXY1bRcse3XNk
$ makepasswd --clearfrom /tmp/pwd.txt --crypt
secret-password   EmUq/db.hXCT.

$ makepasswd --clearfrom /tmp/pwd.txt --crypt --cryptsalt 1
secret-password   aaBoSGSDWKUC2
$ makepasswd --clearfrom /tmp/pwd.txt --crypt --cryptsalt 1
secret-password   aaBoSGSDWKUC2

$ makepasswd --clearfrom /tmp/pwd.txt --crypt-md5
secret-password   $1$CQz7qJqd$Io6ZfCeXdP0gKWYa3/CMm0
$ makepasswd --clearfrom /tmp/pwd.txt --crypt-md5
secret-password   $1$vTsHxl6j$dFvR.mqYF/SP3kysqCM/s/
```



[^coelhorjc]: [How to generate (random) and store (key-derived) passwords in Linux (using pwgen/apg/makepasswd/mkpasswd and crypt/bcrypt/scrypt)](https://coelhorjc.wordpress.com/2015/04/07/how-to-generate-random-and-store-key-derived-passwords-in-linux-using-pwgenapgmakepasswdmkpasswd-and-cryptbcryptscrypt/)