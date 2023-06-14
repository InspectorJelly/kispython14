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
    tt = x
    for row in tt:
        row_buff = row[1]
        row[0], row[1] = row[0].split("&")
        row.insert(1, row_buff)
        # tt.append(row)
    return tt


def data_change(x):
    tt = x
    for row in tt:
        dat = row[0][2:4] + "/" + row[0][5:7] + "/" + row[0][8:10]
        row[0] = dat
    return tt


def at_change(x):
    tt = x
    for row in tt:
        row[2] = row[2].replace("[at]", "@")
    return tt


def name_change(x):
    tt = x
    for row in tt:
        st = row[1].split(" ")
        name = ""
        name += st[0][0] + "." + st[1] + " " + st[2]
        row[1] = name
    return tt


def main(x):
    res = add_col(x)
    res = data_change(x)
    res = at_change(x)
    res = name_change(x)
    return res
