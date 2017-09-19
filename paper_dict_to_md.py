
def paper_dict_to_md(papers):
    date = papers['date']
    file_name = date + "-daily-DL-paper.md"
    f = open(file_name, "w")

    header = '---\n' \
             'layout: post\n' \
             'title: \"' + date + ' 오늘의 페이퍼\"\n' \
             'subtitle: 오늘의 딥러닝 논문\n' \
             'date: ' + date + '\n' \
             'categories: Machine-learning\n' \
             'cover: https://user-images.githubusercontent.com/6357456/30470074-9b04e2fc-99f3-11e7-9c89-869dc06cc8f3.png\n' \
             'tag:    [AI, machine-learning, deep-learning, paper, trend]\n' \
             '---\n\n'

    f.write(header)

    paper_list = papers['paper_list']

    print(paper_list)

    for detail in paper_list:
        title = detail['title']
        author = detail['author']
        subject = detail['subject']
        pdf = detail['pdf']

        f.write('## ' + title + '<br>\n')
        f.write('국문 : ' + '' + '<br>\n')
        f.write('저자 : ' + author + '<br>\n')
        f.write('키워드 :' + '' + '<br>\n')
        f.write('pdf : <https://arxiv.org' + pdf + '><br>\n')
        f.write('요약 : ' + '' + '<br>\n\n\n')

    f.close()

