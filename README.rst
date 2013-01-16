Introduction
============

When dealing with blog, people are used to Wordpress. 
This addon provide management screens for Plone to help people
from wordpress to use administrate their website.

Let's start with /wp-admin

How to install
==============

You can install this addon as any other Plone addons. Please follow the
offical documentation_.

This addon do not has setup for Plone. You can just add it to the buildout
and hit /wp-admin where you want.

If you are looking for further integration you should check the addon
`cirb.blog <https://github.com/CIRB/cirb.blog>`

Features
========

Dashboard page
--------------

This page display many widgets that let you see what's up in your blog.

summary
~~~~~~~

* total number of published blog posts
* total number of comments
* last drafts

quickpress
~~~~~~~~~~

You can add a news item very quickly (title, body, tags and image)

add box
~~~~~~~

Big blue button to add a new news item (using the Plone add form) plus a
quickupload form to upload images to media folder.

draft
~~~~~

this widget give you a direct access into Plone to your current blog posts into
draft state.

recent comment
~~~~~~~~~~~~~~

this widget give you a direct access into Plone to last comment

Upload page
-----------

This page let you browse the media folder and manage existing content. You
can rename, delete or modify any image from this page without going to Plone.

Blogs page
----------

This page let you browse current blog posts and manage them. You can rename,
delete any posts from this page without going to Plone. You also has a direct
access to the Plone edit form.


Credits
=======

Companies
---------

|cirb|_ CIRB / CIBG

* `Contact CIRB <mailto:irisline@irisnet.be>`_

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. |cirb| image:: http://www.cirb.irisnet.be/logo.jpg
.. _cirb: http://cirb.irisnet.be
.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
