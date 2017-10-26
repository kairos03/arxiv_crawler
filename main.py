# Copyright kairos03. All Right Reserved.

import crawler
from encoder import paper_dict_to_md

# today with header
paper_dict_to_md(crawler.get_papers(0), header_out=True)

# yesterday without header
paper_dict_to_md(crawler.get_papers(1), header_out=False)
