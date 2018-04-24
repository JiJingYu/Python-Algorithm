from collections import defaultdict


N = int(input())
table = defaultdict(lambda :defaultdict(lambda :[]))
for i in range(N):
    id = input()
    title = input()
    author = input()
    keyword = {x for x in input().split()}
    publisher = input()
    year = input()

    table['title'][title].append(id)
    table['author'][author].append(id)
    table['publisher'][publisher].append(id)
    table['year'][year].append(id)
    for key in keyword:
        table['keyword'][key].append(id)

M = int(input())
Querys = []
M_d = {1:'title', 2:"author", 3:"keyword", 4:"publisher", 5:"year"}
search_results = []

for i in range(M):
    tmp = input()
    query_type = M_d[int(tmp[0])]
    query_info = tmp.split(':')[-1][1:]
    search_result = []
    # search_result.append(tmp)
    if query_type == 'keyword':
        search_result.extend(table['keyword'][query_info])
    else:
        search_result.extend(table[query_type][query_info])
    if search_result!=[]:
        search_result = sorted(search_result)
        search_result.insert(0, tmp)
    else:
        search_result = [tmp, "Not Found"]
    search_results.append(search_result[:])

for search_result in search_results:
    for it in search_result:
        print(it)


"""
3
1111111
The Testing Book
Yue Chen
test code debug sort keywords
ZUCS Print
2011
3333333
Another Testing Book
Yue Chen
test code sort keywords
ZUCS Print2
2012
2222222
The Testing Book
CYLL
keywords debug book
ZUCS Print2
2011
6
1: The Testing Book
2: Yue Chen
3: keywords
4: ZUCS Print
5: 2011
3: blablabla
"""
