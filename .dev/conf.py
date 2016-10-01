#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

routing = {
    "archive": "/archive/<modification_date>/<title>.html",
    "tag": "/<allow_tag>/<title>.html",
    "article": "/<title>.html",
}


# Tags are allowed for routing (substituted in <allow_tag>)
allow_tags = [
    "project",
]


# Templates rules
# Задается здесь, а не в самих шаблонах, т.к. так проще и нужно редактировать только в одном месте, а не в нескольких.
# Т.к. нет смысла в "пустом" тэге, то в качестве стандартного тэга была выбрана именно пустая строка.
templates = [
    # Template for projects pages
    ("project", "project.html"),

    # "Default" template
    ("", "article.html"),
]
