import crawler
from encoder import paper_dict_to_md

# with header
paper_dict_to_md(crawler.get_papers(), header_out=True)

# without header
paper_dict_to_md(crawler.get_papers(), header_out=False)
