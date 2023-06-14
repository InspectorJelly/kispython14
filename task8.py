def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def add_col(x):
    tt = []
    for row in x:
        row_buff = row[1]
        row_new = row[0].split("&")
        row_new.insert(1, row_buff)
        tt.append(row_new)
    return tt


def data_change(x):
    tt = []
    for row in x:
        dat = row[0][2:4] + "/" + row[0][5:7] + "/" + row[0][8:10]
        row[0] = dat
        tt.append(row)
    return tt


def at_change(x):
    tt = []
    for row in x:
        row[2] = row[2].replace("[at]", "@")
        tt.append(row)
    return tt


def name_change(x):
    tt = []
    for row in x:
        st = row[1].split(" ")
        name = st[0][0] + "." + st[1] + " " + st[2]
        row[1] = name
        tt.append(row)
    return tt


def main(x):
    res = remove_duplicates(x)
    res = add_col(res)
    res = data_change(res)
    res = at_change(res)
    res = name_change(res)
    return res


x = [['2001.12.03&evgenij92[at]yahoo.com', 'Евгений М. Вечевев'], ['2001.12.03&evgenij92[at]yahoo.com', 'Евгений М. Вечевев'], ['1999.03.26&mitibin62[at]yahoo.com', 'Адель Б. Митибин'], ['1999.11.04&komizidi12[at]rambler.ru', 'Макар Т. Комициди'], ['2000.11.18&gordej74[at]gmail.com', 'Гордей Ч. Касев']]
print(x)
print(main(x))


def main(args):
    result = []
    for i in args:
        row = []
        splt = i[0].split('&')
        row.append(splt[0][2:].replace('.', '/'))
        fio = i[1].split()
        row.append(fio[0][0] + '.' + fio[1] + ' ' + fio[2])
        row.append(splt[1].replace('[at]', '@'))
        if not row in result:
            result.append(row)
    sorted_data = result
    return sorted_data
