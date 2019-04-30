+++
title = "Post: Website"
date = 2018-02-19T14:35:20+01:00
draft = false

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = []
categories = []

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
# Use `caption` to display an image caption.
#   Markdown linking is allowed, e.g. `caption = "[Image credit](http://example.org)"`.
# Set `preview` to `false` to disable the thumbnail in listings.
[header]
image = ""
caption = ""
preview = true

+++

As I said on my homepage I want this site to be a place to keep the kind of snippets I always forget. So to begin, I'll put here the info relevant for the site itself.

Firstly, this site is built by Hugo, not Jekyll (which I know lots of other people are using). I installed Hugo with <a href="https://brew.sh/">Homebrew</a>, which is a great package manager for mac computers. To do this I type:

<code>brew install hugo</code>

The site's progress is easily documented and tracked with git, which can also be obtained from <a href="https://brew.sh/">Homebrew</a>. I have a Github account, which allows for open access contributions to my work and even provides the domain, as you can see from the address bar.

With Hugo I use **Academic**, a framework to help create a nice website quickly. They have a good [demo](https://themes.gohugo.io/theme/academic/) of what you can get in less than 10 minutes.

**Academic Kickstart** is a minimal template to start a new website (which i'm still using) by following the simple steps below.

[![Screenshot](https://raw.githubusercontent.com/gcushen/hugo-academic/master/academic.png)](https://github.com/gcushen/hugo-academic/)

1. Clone (or [download](https://github.com/sourcethemes/academic-kickstart/archive/master.zip)) the *Academic Kickstart* repository with Git: 

       <code>git clone https://github.com/sourcethemes/academic-kickstart.git My_Website</code>
    
2. Initialise the theme:

       <code>cd My_Website</code>
       <code>git submodule update --init --recursive</code>

3. Read the [Quick Start Guide](https://sourcethemes.com/academic/docs/) to learn how to add content, customise the site, and deploy it.

From this point I can write to the files on my computer, which are easy to read, modify and create. 

These changes can be viewed locally before I make anything public, which is great because I can work on it while offline and I can check I didn't do too much damage before I upload anything!

This can be done by typing

<code>hugo server</code>

and then opening <a href="http://localhost:1313" rel="nofollow">localhost:1313</a> in my web browser.

When I'm ready I use Hugo to build the files, I go to the public directory, add the changes, comment on the changes and push to the repository.

The commands for this are:

<code>hugo</code>

<code>cd public</code>

<code>git add .</code>

<code>git commit -m "explanation of most recent changes"</code>

<code>git push</code>

Then it takes about 10 minutes before the site updates to the most recent version.

The original author of Academic Kickstart is [George Cushen](https://georgecushen.com). It is released under the [MIT](https://github.com/sourcethemes/academic-kickstart/blob/master/LICENSE.md) license, Copyright 2017.
