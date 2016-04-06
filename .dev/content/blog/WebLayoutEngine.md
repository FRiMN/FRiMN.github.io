Title: WebLayoutEngine
Date: 2016-03-05 23:50
Category: projects
Tags: wle, js
Illustration: cover3.jpg
Summary: Концепции для WebLayoutEngine

[Downloadable File]({attach}/downloads/archive.zip)

# Концепт
1. Простое API
    - `gtk.Table(rows=5, columns=5, homogeneous=False)`
    - `tableH.attach(lw, 0,1, *label_row)`
    - `vd.show()`
2. При удалении родителя удаляются и все его потомки
3. Темы определяют внешний вид элементов
4. Явное отображение/скрытие элементов: `show()`, `hide()`
5. Политики изменения размеров
6. Политики пустого пространства
7. Все виджеты располагаются в пространстве согластно их политикам размеров и пустого пространства
8. Все компановщики занимают всё доступное пространство родительского компановщика (или его части)
9. Все виджеты и компановщики должны быть внутри корневого компановщика `Root`
10. Каждый виджет имеет уникальный id

# Сайзеры/Компоновщики/Контейнеры (Менеджеры компоновки)
1. **Grid/Table** - размещение виджетов в сетке
2. **HBox** - размещение виджетов горизонтально
3. **VBox** - размещение виджетов вертикально
4. **Box** - размещение виджета на весь размер
5. **Dialog/Message/Echo** - всплывающий виджет, висящий поверх других виджетов; может быть модальным
6. **Frame** - группировка виджетов с общим заголовком (подписью) *надо?*

## Виджеты
1. **Progress**
    - *Text*
    - *TextAlignment* [0,1]
    - *Value* [0,1]
2. http://www.opennet.ru/docs/RUS/gtk-reference/TextWidget.html
3. http://www.opennet.ru/docs/RUS/gtk-reference/GtkSpinButton.html
4. http://www.opennet.ru/docs/RUS/gtk-reference/GtkTreeView.html
5. **Separator**
6. http://www.opennet.ru/docs/RUS/gtk-reference/GtkRange.html
7. **Entry/LineEdit** -- поле ввода
8. **TextEdit**
9. **Label**
10. http://doc.crossplatform.ru/qt/4.6.x/widget-classes.html

***

# Tests

## Render 100 elements 1000 times

<table class="table">
    <thead>
        <tr>
            <th>Render engines</th>
            <th style="text-align:right">Chrome</th>
            <th style="text-align:right">Firefox</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>WebLayoutEngine</td>
            <td align="right">1351.226ms</td>
            <td align="right">1467.81мс</td>
        </tr>
        <tr>
            <td>React</td>
            <td align="right">5323.632ms</td>
            <td align="right">6826.2мс</td>
        </tr>
        <tr>
            <td>Underscore</td>
            <td align="right">1435.358ms</td>
            <td align="right">1395.74мс</td>
        </tr>
        <tr>
            <td>Mustache</td>
            <td align="right">1391.363ms</td>
            <td align="right">1375.35мс</td>
        </tr>
    </tbody>
</table>

## Render 1 element 1000 times

<table class="table">
    <thead>
        <tr>
            <th>Render engines</th>
            <th style="text-align:right">Chrome</th>
            <th style="text-align:right">Firefox</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>WebLayoutEngine</td>
            <td align="right"></td>
            <td align="right">57.2мс</td>
        </tr>
        <tr>
            <td>React</td>
            <td align="right"></td>
            <td align="right">323.38мс</td>
        </tr>
        <tr>
            <td>Underscore</td>
            <td align="right"></td>
            <td align="right">6349.43мс</td>
        </tr>
        <tr>
            <td>Mustache</td>
            <td align="right"></td>
            <td align="right">61.36мс</td>
        </tr>
    </tbody>
</table>

## Render 1000 element 1000 times

<table class="table">
    <thead>
        <tr>
            <th>Render engines</th>
            <th style="text-align:right">Chrome</th>
            <th style="text-align:right">Firefox</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>WebLayoutEngine</td>
            <td align="right"></td>
            <td align="right">28719.16мс</td>
        </tr>
        <tr>
            <td>React</td>
            <td align="right"></td>
            <td align="right">67917.41мс</td>
        </tr>
        <tr>
            <td>Underscore</td>
            <td align="right"></td>
            <td align="right">16363.67мс</td>
        </tr>
        <tr>
            <td>Mustache</td>
            <td align="right"></td>
            <td align="right">13594.38мс</td>
        </tr>
    </tbody>
</table>
