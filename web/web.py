#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实验品，可删除
import web

urls = (
    '/users?(.+)', 'get_user'
)
app = web.application(urls, globals())


class get_user:
    def GET(self, user):
        data = web.input()
        return ("Hello, " + data.name + ".Welcome to Gupao! ")

if __name__ == '__main__':
    app.run()
