The website [robertolofaro.com](https://robertolofaro.com) is my main publishing venue.

The Kaggle dataset [Articles publication metadata and AI access](https://www.kaggle.com/datasets/robertolofaro/articles-publication-metadata-and-ai-access) contains metadata to ease access to articles via scraping, robots, and AI scraping.

This directory contains, for each article, two files:

* file_<id of the article>_abstract.txt ("Abstract")
* file_<id of the article>_content.txt ("Content")

The <b>Abstract</b> file contains the following information:
* id of the article (number)
* breadcrumbs that you can see also on the website
* title as on the website
* a short one-paragraph presentation of the article (available also within the Kaggle dataset)

The <b>Content</b> file contains the actual content of the article, reformatted as a markdown text (with few exceptions for images), i.e. each URL is converted in [text]\(url)
