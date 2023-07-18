---
blogpost: true
date: 2016-03-13
category: tutorial
tags: bugs, js
language: Russian
---

Slug: dark_side_javascript
Cover: cover4.jpg
Color: #564a4e
FocalPoint: 25%
Summary: Баги и малоизвестные особенности JavaScript
Modified: 2016-04-21


# Тёмная сторона JavaScript

## typeof null

Это оффициально признанный баг [^MDN:null], не фиксищейся для поддержки совместимости со старым кодом [^type-detection] [^C-null].
`typeof null` возвращает `"object"`, однако **null** не является объектом [^MDN:null], и что хуже, не ведёт себя как объект.

```js
typeof null     // "object"

var z = null;   // null
z.prop = 1      // TypeError: z is null
```

Если мы заглянем в код библиотеки underscore.js [^underscore], то увидим такую функцию как `isObject()`, как раз правильно проверяющую на тип объекта.

```js
// версия 1.6.0 (2014)
_.isObject = function(obj) {
    return obj === Object(obj);
};

// версия 1.8.3 (2015)
// соответствует lodash
_.isObject = function(obj) {
    var type = typeof obj;
    return type === 'function' || type === 'object' && !!obj;
};

_.isObject(null)    // false
```

А также функцию `isNull()` проверяющую на соответствие `null` (тоже самое в lodash):

    :::js
    _.isNull = function(obj) {
        return obj === null;
    };

    _.isNull(null)      // true
    _.isNull({})        // false
    _.isNull(undefined) // false
    _.isNull(NaN)       // false


## Что есть NaN?

Возможно вы не знаете, но `NaN` является числом [^ECMA262] *(и не важно, что **NaN** акроним от **Not a Number**)*,
просто это число никогда не равно самому себе [^type-detection][^underscore][^MDN:isNaN].

    :::js
    typeof NaN  // "number"

    NaN === NaN // false

В underscore.js есть пример проверки на `NaN` [^underscore] (тоже самое в lodash):

    :::js
    _.isNaN = function(obj) {
        return toString.call(obj) === '[object Number]' && obj !== +obj;
    };

    _.isNaN(NaN)    // true

Есть также встроенная функция **isNaN()**, но она работает некорректно [^MDN:isNaN]:

    :::js
    isNaN(NaN)          // true
    isNaN(undefined)    // true
    isNaN({})           // true
    isNaN(new Date().toString())   // true
    isNaN("words")      // true

В новом стандарте *ECMAScript 6 (Harmony)* предложена новая функция `Number.isNaN()` избавленная от этих недостатков. Вот её полифилл [^MDN:Number.isNaN]:

    :::js
    Number.isNaN = Number.isNaN || function(value) {
      return typeof value === 'number' && isNaN(value);
    }



## Операторы сложения и вычитания

Преобразование типов в JavaScript реализовано по-разному для операторов сложения и вычитания:

    :::js
    []+[]   // ""
    []+{}   // "[object Object]"

    []-[]   // 0
    []-{}   // NaN

    var l = ['a','b','c']
    var o = {'q':1, 'w':2, 'e':3}

    l+l     // 'a,b,ca,b,c'
    l-l     // NaN
    o+o     // '[object Object][object Object]'
    o-o     // NaN

    var L = [22]

    L-[]    // 22
    []-L    // -22
    +L      // 22
    L+L     // '2222'
    L-L     // 0
    L+[]    // '22'
    -L      // -22
    100-L   // 78
    100+L   // '10022'

Обратите внимание, что в некоторых случаях, когда массив является одним из операндов оператора вычитания, массив может быть преобразован к числу **автоматически**.


## Арифметика null

Преобразования осуществляемые при арифметических операциях и сравнениях `>` `>=` `<` `<=`, и при проверке равенства `==` -- различны. Алгоритм проверки равенства для **undefined** и **null** в спецификации прописан отдельно [^es5]. В нём считается, что они равны между собой, но эти значения не равны никакому другому значению [^types].

Из-за этого **null** ведёт себя странно при сравнении:

    :::js
    > null >= 0
    true

    > null <= 0
    true

    > null > 0
    false

    > null < 0
    false

    > null == 0
    false

А значение **undefined** вообще «несравнимо»:

    :::js
    > undefined > 0
    false

    > undefined == 0
    false

    > undefined < 0
    false

    > undefined >= 0
    false

    > undefined <= 0
    false


## Пустой блок кода

Пустой блок кода `{}` в одних случаях может вести себя как **null**, а в других -- как "ничего", хотя сам по себе интерпритируется как **undefined**.

    :::js
    > undefined
    undefined

    > {}
    undefined

    > {}+1    // {} -- null?
    1

    > undefined+1
    NaN

    > {}+'1'    // {} -- wtf??!
    1

    > undefined+'1'
    "undefined1"

    > {}+null    // {} -- null?
    0

    > undefined+null
    NaN


## Обход массива

Существует несколько способов обойти массив. Одни из них обходят массив как массив, а другие как объект [^arrayloop].

    :::js
    var list = []
    list[0] = "x"
    list[100] = "y"
    list[10000] = "z"

    > list.forEach(function(item) { console.log(item) })
    x
    y
    z

    > for (var i = 0; i < list.length; i++) { console.log(item) }
    x
    undefined
    ...
    undefined
    y
    undefined
    ...
    undefined
    z

    > for (var key in list) {
        if (
            // Здесь мы проверяем что ключ взят не из цепочки прототипов
            list.hasOwnProperty(key) &&
            // Тут, что это числовой ключ, поскольку, хотя разряженный
            // массив практически не отличается от объекта мы по прежнему
            // используем только числовые ключи
            /^0$|^[1-9]\d*$/.test(key) &&
            // Здесь мы проверяем что ключ не выходит за пределы допустимые
            // для ключей массива 2^32 - 2. Это число, согласно спецификации,
            // максимальный из возможных индексов массива
            key <= 4294967294
        ) {
            console.log(list[key])
        }
    }
    x
    y
    z



[^type-detection]: [javascript.info](http://javascript.info/tutorial/type-detection)
[^C-null]: [The history of “typeof null”](http://www.2ality.com/2013/10/typeof-null.html)
[^ECMA262]: [Спецификация ECMA-262, п. 4.3.20 и 8.5](http://www.ecma-international.org/ecma-262/5.1/Ecma-262.pdf)
[^es5]: [Документация EcmaScript 5, п. 11.9.3](http://es5.github.io/x11.html#x11.9.3)
[^underscore]: [Аннотированный код underscore.js](http://underscorejs.org/docs/underscore.html)
[^MDN:null]: [Документация MDN по **null**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/null)
[^MDN:isNaN]: [Документация MDN по **isNaN()**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
[^MDN:Number.isNaN]: [Документация MDN по **Number.isNaN()**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
[^types]: [Преобразование типов для примитивов](https://learn.javascript.ru/types-conversion)
[^arrayloop]: [Способы обхода массива](http://www.developersonthe.net/ru/qa/question_id/63-Obhod-elementov-massiva-Kak-eto-sdelat-v-JavaScript/)
