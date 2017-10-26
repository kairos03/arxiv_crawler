# Copyright kairos03. All Right Reserved.


def paper_dict_to_md(paper_bunch, header_out=True):
    """paper dict transform to markdown

    Markdown file's name is automatically created by this rule -- YYYY-MM-DD-daily-DL-paper.md

    :param paper_bunch: paper information dict
    :param header_out: if True write header

    """
    date = paper_bunch['date']
    file_name = date + "-daily-DL-paper.md"
    f = open(file_name, "w")

    if header_out:
        header = '---\n' \
                 'layout: post\n' \
                 'title: \"' + date + ' 오늘의 페이퍼\"\n' \
                 'subtitle: 오늘의 딥러닝 논문\n' \
                 'date: ' + date + '\n' \
                 'categories: Machine-learning\n' \
                 'cover: https://goo.gl/5pYNGp\n' \
                 'tag:    [AI, machine-learning, deep-learning, paper, trend]\n' \
                 '---\n\n'

        f.write(header)

    for paper_list in paper_bunch['paper_list']:

        print(paper_list)
        cls = paper_list['class']
        f.write('## ' + cls + '<br>\n')

        for papers in paper_list['papers']:
            title = papers['title']
            author = papers['author']
            subject = papers['subject']
            pdf = papers['pdf']

            f.write('### ' + title + '<br>\n')
            f.write('국문 : ' + '' + '<br>\n')    # TODO auto translation
            f.write('저자 : ' + author + '<br>\n')
            f.write('키워드 :' + '' + '<br>\n')   # TODO auto keyword extraction
            f.write('pdf : <https://arxiv.org' + pdf + '><br>\n')
            f.write('요약 : ' + '' + '<br>\n\n\n')    # TODO auto summarize

    f.close()
