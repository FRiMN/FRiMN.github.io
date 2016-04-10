Title: Тёмная сторона JavaScript
Slug: dark_side_javascript
Date: 2016-03-13 21:50
Modified: 2016-04-08
Category: tutorial
Tags: bugs, js
Cover: /images/cover4.jpg
Illustration: cover.jpg
FocalPoint: 25%
Summary: Баги и малоизвестные особенности JavaScript



## typeof null

Это оффициально признанный баг [^MDN:null], не фиксищейся для поддержки совместимости со старым кодом [^type-detection][^C-null].
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

```js
_.isNull = function(obj) {
    return obj === null;
};

_.isNull(null)      // true
_.isNull({})        // false
_.isNull(undefined) // false
_.isNull(NaN)       // false
```


## Что есть NaN?

Возможно вы не знаете, но `NaN` является числом [^ECMA262] *(и не важно, что **NaN** акроним от **Not a Number**)*, 
просто это число никогда не равно самому себе [^type-detection][^underscore][^MDN:isNaN].

```js
typeof NaN  // "number"

NaN === NaN // false
```

В underscore.js есть пример проверки на `NaN` [^underscore] (тоже самое в lodash):

```js
_.isNaN = function(obj) {
    return toString.call(obj) === '[object Number]' && obj !== +obj;
};

_.isNaN(NaN)    // true
```

Есть также встроенная функция **isNaN()**, но она работает некорректно [^MDN:isNaN]:

```js
isNaN(NaN)          // true
isNaN(undefined)    // true
isNaN({})           // true
isNaN(new Date().toString())   // true
isNaN("words")      // true
```

В новом стандарте *ECMAScript 6 (Harmony)* предложена новая функция `Number.isNaN()` избавленная от этих недостатков. Вот её полифилл [^MDN:Number.isNaN]:

```js
Number.isNaN = Number.isNaN || function(value) {
  return typeof value === 'number' && isNaN(value);
}
```


http://javascript.info/tutorial/memory-leaks
https://learn.javascript.ru/memory-leaks
https://www.smashingmagazine.com/2012/11/writing-fast-memory-efficient-javascript/
http://www.html5rocks.com/en/tutorials/speed/v8/
http://www.developersonthe.net/ru/qa/question_id/63-Obhod-elementov-massiva-Kak-eto-sdelat-v-JavaScript/
http://olmokhov.livejournal.com/21523.html


## Преобразование типов

```js
[]+[]   // ""
[]+{}   // "[object Object]"
{}+[]   // 0
{}+{}   // NaN

[]-[]   // 0
[]-{}   // NaN
{}-[]   // -0
{}-{}   // NaN
```

Там где вначале строки стоит `{` -- там левая фигурная скобка рассматривается как начало блока кода.


[^type-detection]: [javascript.info](http://javascript.info/tutorial/type-detection)
[^C-null]: [The history of “typeof null”](http://www.2ality.com/2013/10/typeof-null.html)
[^ECMA262]: [Спецификация ECMA-262, п. 4.3.20 и 8.5](http://www.ecma-international.org/ecma-262/5.1/Ecma-262.pdf)
[^underscore]: [Аннотированный код underscore.js](http://underscorejs.org/docs/underscore.html)
[^MDN:null]: [Документация MDN по **null**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/null)
[^MDN:isNaN]: [Документация MDN по **isNaN()**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/isNaN)
[^MDN:Number.isNaN]: [Документация MDN по **Number.isNaN()**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)
[^MDN:Array.length]: [Документация MDN по **Array.length**](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Array#Relationship_between_length_and_numerical_properties)




```js
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
```


https://learn.javascript.ru/while-for

Последняя запятая в массивах объектов, проверить на разряженных массивах
