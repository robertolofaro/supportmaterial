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

As a further experiment to ease access, I also made available on Huggingface [a model with different approaches to store metadata](https://huggingface.co/spaces/robertolofaro/articles).

For now the model will search across all the 350+ article (it is "frozen" in content as of the article [Organizational Support 17: Reusing lessons from the past to improve processes with AI](https://robertolofaro.com/index.php?page=651)), and you can try:
* different approaches to associate metadata (Chroma, FAISS_hnsw, Qdrant)
* parameters to affect the way the model provides responses

The option to select a specific category is currently not active- for the time being, the aim is to collect feed-back so that can improve the "system prompt" that guides the answer to users' questions.

Plan: to update this model (as others already released on [my Huggingface profile](https://huggingface.co/robertolofaro)) on a quarterly basis, while I will revise the "system prompt" weekly.

Currently all the models that posted on Huggingface share these characteristics:
* their system prompt restricts to using only the material provided during the training
* the underlying model is Qwen3.5-4B

As for the content:
* some are provided with all the files downloadable, including scripts to use it without a GPU
* some just with an Huggingface "space" that uses the Q4_K_M.gguf version

Any feed-back is welcome.
