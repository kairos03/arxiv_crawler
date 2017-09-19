# arxiv crawler

crawl todays arxiv ai paper and transform to markdown file.

## How to run?
just run `main.py`
```bash
$ python main.py
```

## detail of file
### crawler
crawling arxiv page and return `papers` dict

### paper_dict_to_md
using `papers` dict make markdown file with jekyll header

### main
main file
it just call two above functions

