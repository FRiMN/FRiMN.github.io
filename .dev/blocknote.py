#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import os
import datetime
from jinja2 import Template
import markdown
import click
import conf


@click.group()
def cli():
    pass


@click.command()
def make():
    """ Generate HTML from mk files and templates """
    # TODO: cleaning dir
    posts = traverse_dir()
    make_html(posts)
    make_index(posts)


@click.command()
def serve():
    """ Simple dev web server """
    # TODO: untached (daemonized)
    # TODO: also use simpleHTTPServer
    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor

    reactor.listenTCP(8000, Site(File("..")))
    reactor.run()


cli.add_command(make)
cli.add_command(serve)


def traverse_dir():
    # traverse root directory, and list directories as dirs and files as files
    posts = []
    for root, dirs, files in os.walk("./posts"):
        for filename in files:
            post = {}
            full_path = os.path.join(root, filename)
            with open(full_path) as f:
                lines = f.readlines()
                meta_flag = True
                post['text'] = ""
                for line in lines:
                    if line == "\n" and len(post['text']) == 0:
                        meta_flag = False
                        continue

                    if meta_flag:
                        key, val = line.split(":", maxsplit=1)
                        key = key.lower().strip()
                        val = val.strip()

                        if key == "tags":
                            tags = val.split(",")
                            strip_tags = []
                            for tag in tags:
                                strip_tags.append(tag.strip())
                            strip_tags.append("")
                            post['tags'] = list(set(strip_tags))
                            # print('--', full_path, post['tags'])
                        else:
                            post[key] = val
                    else:
                        post["text"] = post["text"] + line
            post['text'] = markdown.markdown(post['text'], extensions=[
                'markdown.extensions.footnotes',
                'markdown.extensions.codehilite(css_class=highlight)',
            ])
            if 'slug' in post:
                filename = post['slug']
            else:
                filename = post['title']
            post['url'] = "/{}.html".format(filename)
            post['_source_path'] = full_path
            posts.append(post)
    return posts


def make_html(posts):
    for template_tag, template_file in conf.templates:
        # print('=>', template_tag)
        template_path = "./templates/{}".format(template_file)
        done_posts = []
        try:
            with open(template_path) as t:
                template = Template( "".join(t.readlines()) )
                for post in posts:
                    if '_status' in post and post['_status'] == 'done' or 'draft' in post['tags']:
                        if 'draft' in post['tags']:
                            print("\033[35mSkip\033[39m generate HTML for \033[33m{}\033[39m ({})".format(post['title'], post['_source_path']))
                            posts.remove(post)
                        continue
                    print("Generate HTML for \033[33m{}\033[39m ({} --> {})".format(post['title'], post['_source_path'], post['url']))

                    if template_tag in post['tags']:
                        # print(template_tag, '::', post['tags'])
                        post['tags'].remove("")
                        html = template.render(
                            article=post,
                            datetime=datetime.datetime.strptime
                        )

                        url = "..{}".format(post['url'])
                        # print("\t{}".format(url))
                        with open(url, "w") as h:
                            print(html, file=h)

                        # print('\tdone')
                        post['_status'] = 'done'
                    # print('\tdone?')
                # print('end posts')
        except FileNotFoundError:
            print("\033[31mError:\033[39m template \033[33m{}\033[39m not found.".format(template_path))


def make_index(posts):
    template_path = "./templates/index.html"
    try:
        with open(template_path) as t:
            template = Template( "".join(t.readlines()) )
            print("Generate \033[33mindex.html\033[39m")
            html = template.render(
                articles=posts,
                datetime=datetime.datetime.strptime
            )
            with open("../index.html", "w") as h:
                print(html, file=h)
    except FileNotFoundError:
        print("\033[31mError:\033[39m template \033[33m{}\033[39m not found.".format(template_path))


if __name__ == '__main__':
    cli()
