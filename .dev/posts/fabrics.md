Title: Про фреймворки
Slug: fabrics
Date: 2016-04-13
Category: library
Tags: frameworks, fun, Braithwaite
Summary: Несколько статей о пробемах сложности и фреймворков



## Про фреймворки

<small>
_**Оригинал:** <http://discuss.joelonsoftware.com/default.asp?joel.3.219431> (BenjiSmith)
<br>
**Перевод:** <https://habrahabr.ru/post/141477/> (truezemez)_
</small>

Я собираюсь сделать Java-веб-приложение (да, это будет Java, по некоторым причинам, которые сейчас озвучивать не хочу). В процессе работы, я оцениваю кучу J2EE portlet-enabled JSR-compliant MVC role-based CMS web service application container фреймворков.

После кучи потраченного времени на прочтение документации, я уже готов выколоть себе глаза.

***

Давайте представим, что я решил сделать шкафчик для специй.

Я уже делал небольшие поделки из дерева и думаю, что знаю, что мне нужно: немного дощечек и несколько базовых инструментов: рулетка, пила, уровень и молоток.

Если бы я строил целый дом, а не просто шкафчик для специй, то мне все также требовались бы рулетка, пила, уровень и молоток (не считая остального).

Итак, я иду в магазин за инструментами и спрашиваю продавца, где я могу найти молоток.

— Молоток? — спросил он. — Никто уже давно не покупает молотки. Это старомодно.

Я был очень удивлен и спросил почему.

— Ну, проблема молотков в том, что их очень много видов. Кувалды, столярные молотки, с круглым бойком и т.д. Что если Вы купите один тип молотка, а потом поймете, что Вам нужен другой? Вам придется покупать отдельный молоток для следующей задачи. Как выяснилось, большинство людей хотят иметь один молоток, который бы справлялся со всеми типами задач, с которыми можно столкнуться.

— Хммммм. Ну, звучит разумно. Можете показать мне такой Универсальный Молоток?

— Нет. Мы их больше не продаем. Они устарели.

— Серьезно? С Ваших слов я понял, что Универсальный Молоток – это технология будущего.

— Как выяснилось, если сделать только один тип молотка, способный выполнять те же задачи, что и все виды молотков, тогда он будет не очень хорош для каждой из них. Забивать гвозди кувалдой не очень эффективно. И если Вы хотите убить свою бывшую девушку, то ничто не заменит молотка с круглым бойком.

— Верно. Но если никто больше не покупает Универсальные Молотки и если Вы больше не продаете все старомодные типы молотков, то какие же молотки Вы продаете?

— Вообще-то, мы не продаем никакие молотки.

— Но…

— Наши исследования показали, что людям совсем не нужен Универсальный Молоток. Всегда лучше использовать нужный тип молотка для работы. Поэтому, мы начали продавать фабрики молотков, способные создать любой молоток, какой Вам нужен. Все что Вам нужно — это укомплектовать фабрику рабочими, запустить механизм, купить сырье, оплатить расходы и — БАЦ — у Вас есть именно такой молоток, какой Вам нужен.

— Но мне как-то не хочется покупать фабрику молотков…

— Это хорошо. Потому что мы их больше не продаем.

— Но Вы же только что сказали…

— Мы обнаружили, что большинству людей не нужна целая фабрика. Некоторым людям, например, никогда не понадобится молоток с круглым бойком. (Может у них нет бывших девушек. Или они убили их ледорубом.) Поэтому, нет смысла кому-либо покупать фабрику молотков, которая может произвести любой тип молотка.

— Да, похоже на то.

— Вместо этого мы начали продавать чертежи фабрик молотков, позволяющие нашим клиентам построить их собственные фабрики молотков, специально разработанные для производства только тех типов молотков, которые им нужны.

— Дайте угадаю. Вы их больше не продаете.

— Нет. Конечно же нет. Как выяснилось, люди не хотят строить целую фабрику, только ради того, чтоб произвести пару молотков. Оставьте строительство профессионалам, вот что я всегда говорю.

— И здесь я с вами соглашусь.

— Ага. Поэтому мы прекратили продавать эти чертежи и начали продавать фабрики фабрик молотков. Каждая фабрика фабрик молотков строится для Вас экспертами своего дела, и вам не нужно волноваться о деталях постройки фабрики. Вы получаете все преимущества обладания собственной фабрикой молотков, производящей молотки для ваших потребностей.

— Ну, это как-бы, не совсем…

— Я знаю что Вы скажете! Мы их уже больше не продаем. По каким-то причинам, довольно мало людей покупали фабрики фабрик молотков, поэтому мы придумали новое решение проблемы.

— Угу.

— Когда мы сделали шаг назад и посмотрели глобально на инфраструктуру инструментов, мы обнаружили что люди разочарованы, т.к. им нужно управлять фабрикой фабрик молотков и произведенной фабрикой молотков. Это довольно обременительно, в случае если вам еще нужно управлять фабрикой фабрик рулеток, фабрикой фабрик пил, фабрикой фабрик уровней, не говоря уже о производстве пиломатериалов. Взглянув на ситуацию, мы поняли, что это слишком сложно для тех, кто просто хочет сделать шкафчик для специй.

— Да. Это уж точно.

— Поэтому, на этой неделе мы представим единую фабрику фабрик фабрик инструментов, чтобы каждую фабрику фабрик инструментов Вы могли произвести с помощью одной, объединенной фабрики. Фабрика фабрик фабрик будет производить только те фабрики фабрик инструментов, какие Вам нужны, и каждая из этих фабрик фабрик будет производить фабрику, основанную на Ваших требованиях к инструменту. Окончательный набор инструментов, полученных в результате этого процесса, будет идеален для вашего конкретного проекта. У Вас будет именно тот молоток, который вам нужен, и рулетка, подходящая именно под эту задачу, и все это по нажатию одной кнопки (конечно вам придется немного поработать с конфигурацией, чтобы заставить все это работать именно так как вам надо).

— Так у вас нет никаких молотков? Совсем никаких?

— Нет. Если Вы по-настоящему хотите высококачественный, промышленно разработанный шкафчик для специй, вам нужно нечто более продвинутое, нежели обычный молоток из магазина.

— И что, все сейчас так делают? Все используют единую фабрику фабрик фабрик инструментов, всякий раз, когда им нужен молоток?

— Да.

— Ладно… Я кажется понял, что мне нужно делать. Если сейчас это делается таким образом, будет, наверное, лучше и мне научиться так делать.

— Очень хорошо!

— Эта вещь идет с документацией, верно?


## Остерегайтесь Тьюринговской трясины

<small>
_**Оригинал:** <http://weblog.raganwald.com/2004/10/beware-of-turing-tar-pit.html> (Reginald Braithwaite)
<br>
**Перевод:** <https://habrahabr.ru/post/139535/> (tangro), Николай Волков_
</small>


> ...в которой всё возможно, но ничего конкретного нельзя сделать просто.
> -- <cite>Алан Перлис [^Perlis]</cite>

[^Perlis]: <span>Алан Джей Перлис (англ. Alan Jay Perlis; 1 апреля 1922 — 7 февраля 1990) — американский учёный в области компьютерных технологий, известен своими работами в области языков программирования и как первый лауреат премии Тьюринга (в 1966 году, согласно цитате, «за его влияние в области передовых методов программирования и создание компиляторов». Имеется в виду его работа в группе, разработавшей язык программирования Алгол).</span>

Что такое Тьюринговская трясина? Это состояние, в котором программа становится столь могущественной, столь обобщенной, что усилия по решению с её помощью какой-либо конкретной задачи равны или превосходят затраты на написание с нуля программы, которая решает только данную задачу.

Я частенько страдаю от желания пойти поплавать в этой трясине. Начинается всё с необходимости решить какую-то конкретную проблему. Я смотрю на существующие инструменты и вижу в каждом из них свои недостатки. И вот, забыв о первоначальной задаче, я уже набрасываю архитектуру универсального инструмента, который будет решать общий класс подобных задач, будет невероятно гибким, универсальным и… 

(Особенно опасна эта трясина для разработчиков языков программирования. Есть огромный соблазн урезать язык до самого маленького, самого элегантного ядра аксиом.)

> Я думаю, язык программирования должен быть большей частью самоопределяем. Спецификация языка должна быть разделена на 2 части: небольшое ядро операторов (которые выполняют роль аксиом) и остальная часть языка, которая, как теоремы, определяется в терминах аксиом.
> -- <cite>Пол Грэм</cite>

Опасность трясины в том, что вместо решения проблемы вы начинаете разрабатывать инструмент для создания решений проблем. И чем шире круг задач, в которых он пытается быть полезным, тем менее полезным он окажется в каждой конкретной задаче. 

В моем случае, я часто ловлю себя на том, что при "программировании снизу вверх", пытаюсь изобрести идеальный язык программирования для реализации программы, которую я пытаюсь написать. Когда я вдруг обнаруживаю себя работающим над спецификацией нового языка программирования, я понимаю, что попал в трясину. Пора остановиться и передохнуть.

Привлекательность Тьюринговской трясины в том, что она кажется потенциальным решением всех проблем. Инструмент, который решает любые задачи общими методами — что может быть лучше? Например, VisiCalc[^vc]: это приложение действительно превратило своих пользователей в программистов!

[^vc]: **VisiCalc** -- первая программа для редактирования таблиц (а-ля *Excel*). <http://www.bricklin.com/visicalc.htm>

> В программировании всё, что мы делаем, является всего-лишь частным случаем более общей проблемы. И иногда мы осознаём это слишком быстро.
> -- <cite>Алан Перлис [^Perlis]</cite>

Попытка понять отношение вашей конкретной проблемы и общего класса подобных проблем может действительно помочь увидеть некоторые скрытые ранее детали, и найти ряд замечательных моментов «Ага!».

Таким образом, я верю, что в идеальном случае вы должны быть всегда готовы пройтись по краю Тьюринговской трясины, но в то же время иметь железную силу воли, чтобы не свалиться в неё. 

Лично у меня подобной силы воли нет, и, что еще хуже, есть огромное любопытство. Для хоть какой-то борьбы с этим всем я придумал ряд эвристик по определению края трясины:

1. **Помните мысль Алана Кэя**: *«Мы стараемся сделать простые вещи простыми, а сложные — возможными»*. Когда решение общей задачи делает сложные вещи возможными — это хорошо. Но не ценой потери простоты простых вещей.
2. **Сколь бы высоко вы не летали в облаках теории, время от времени спускайтесь на грешную землю**. Лично я всегда имею в наличии определенное количество пожеланий пользователей и регулярно возвращаюсь к ним с вопросом «а поможет ли этот восхитительный виджет решить вот эту банальную практическую проблему?».
3. **Eat your own dog food/go round trip on an infrequent basis**. Okay, you’re convinced you need to run your application inside a special purpose virtual machine. Fine. Pick one small operation and make it work. Program for your virtual machine, end to end. Don’t skip any of the steps. It’s better to go thin (few functions) and deep (use the entire stack) than to go wide and shallow. If your VM is a pain in the rump, you’ve discovered something. (This is a cornerstone of Ken Schwaber’s Scrum methodology).
4. **Не занимайтесь самобичеванием, когда вдруг обнаружите, что всё-таки погрязли в трясине**. Даже если Вы начали решать проблему А и вдруг обнаружили себя решающим общий класс задач С, который даже не включает А, снова вспомните Алана Кэя: *«Успешная технология создаёт проблемы, которые только она и может решить»*. Не будьте сразу уверенными в том, что создали что-то ненужное. Если осталось немного — закончите и посмотрите, что вышло. Вы никогда не узнаете, полезная ли получилась штука, пока не начнёте пользоваться.


> Уверены ли вы, что все эти свистелки и дуделки, все эти восхитительные средства, составляющие ваш «мощный язык программирования», на самом деле являются частью решения проблемы, а не частью самой проблемы?
> -- <cite>Эдсгер Дейкстра</cite>

Аминь.

### Комментарий переводчика

Тьюринговская трясина на самом деле встречается чаще, чем кажется. И ладно бы в неё затягивало лишь великие академические умы, решающие задачи вселенского масштаба. Но нет — универсальные инструменты стараются создавать все! Каждая программа по записи DVD зачем-то обзаводится своими аудио\видео\фото-редакторами, средствами создания обложек, плеерами и конверторами. Каждый мессенджер считаем своим долгом поддерживать все возможные протоколы связи, вплоть до электронной почты, социальных сетей, СМС, бумажных писем и отправки сообщений внеземным цивилизациям. Все операционки лезут на все типы устройств, каждый кодек-пак включает в себя тонну хлама, документация на некоторые консольные программы [^mplayer] имеет по 150 страниц формата А4 и пару тысяч ключей командной строки. Каждый второй сайт в интернете обрастает мхом из погоды\гороскопов\знакомств\работы\чатов\форумов. Стараясь привлечь лишнего пользователя новой фичей, программы и сайты теряют десяток других, которые заколебались выискивать в образовавшейся куче хлама то рациональное зерно, ради которого когда-то эта программа или сайт были выбраны.

[^mplayer]: Например, [документация](http://www.mplayerhq.hu/DOCS/man/en/mplayer.1.html) *Mplayer*

Серебряных пуль нет. Лично мне единственным способом не скатится из полезного узконаправленного средства в разрозненный набор малофункциональной чуши кажется система плагинов. Хорошими примерами являются современные браузеры, некоторые онлайн-игры, IDE и другие модульные программы (я уверен — вы сможете дополнить список), которые, оставаясь весьма аскетичными в своей основе, дают тем не менее возможность сотворить боевой комбайн любого уровня сложности.
Перед тем как добавить в свою программу новую фичу — подумайте, а нужна ли она хотя бы четверти пользователей? Если нет — может быть стоит просто вывести наружу API и дать возможность желающим написать и подключить плагин? 