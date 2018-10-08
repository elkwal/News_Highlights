Feature
========

- Built with Python 3.7
- Shows 'news sources', 'news articles' and sorted by relevancy
- Styled using Bootstrap
- Handles external get posts and requests from API
- Get news articles from several sources


Installation
========

   $ go through all steps.



API Object Reference
========

## Classes: `Source, Articles`


**Arguments:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `category` | string | No | Returns the articles from this topic only and sorted by relevancy. | `(empty string)`  |
| `news_source` | integer | No | Returns the articles from this news source only. | `(user's choice)` |



## Class: `Source`

Each `Source` has the following properties

- **name** - news source name
- **id** - news source unique id

## Class: `Articles`

Each `Article` has the following properties

- **id** - unique id of the article
- **title** - the title of the article itself
- **description** - the article itself and what it is about
- **published time** - time when it was submitted
- **image url** - image url for image tags
- **url** - url to website for full article

Tests
========

To run the tests locally just do:

   $ cd app
   $ python3.7 test_classes.py


The tests are run on a local test server.

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
