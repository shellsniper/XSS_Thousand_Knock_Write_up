#/usr/bin/env python
# _*_ coding:utf-8 _*_
# this python file is used to listen flag while your site under XSS attack
from flask import Flask, request

xss = Flask(__name__)


@xss.route('/')
def index():
    flag = request.args
    for i,j in flag.items():
        print('Flag is:' + j)
    return str()


if __name__ == "__main__":
    xss.run(host="0.0.0.0")
