# A tool crafted for Weather analysis

## Introduction

I always loved to scrape websites in order to grab some data quickly in an elegant way. As a side-project, I reverse-engineered [theweathernetwork.com](www.theweathernetwork.com) because I
wanted a clean json/xml or whatever-you-want-that-deliver-data in a friendly way for programmers. I know there is a [RSS](http://legacyweb.theweathernetwork.com/rss/) feed but it's too much verbose for me. If you look at the code, they
are using abusively AJAX calls and some tricky javascript files inclusions. This was a cool challenge for me and I finally found the API.

## The project

The goal is to realize an ecosystem built around a data miner. The script will be executed on a regular basis, let's say, *12* times a day. The theweathernetwork's server returns a huge json
string so we will have to setup a database to wrap up all those datas with well-chosen datatypes. This ecosystem could be a bunch of useful functions which perform data
analysis.


## Collaboration

To get enrolled, juste send an email to <mailto:richerlariviere@gmail.com>

## License

The MIT License (MIT)

Copyright (c) 2015 richerlariviere

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
