from bottle import route, run, error, request
import re

def redirect(data):
    return('<meta http-equiv="refresh" content="0;url=' + data + '" />')

def table_p(d, d2):
    alltable = 'style="'
    celstyle = 'style="'
    rowstyle = 'style="'
    row = ''
    cel = ''

    table_w = re.search("&lt;table\s?width=((?:(?!&gt;).)*)&gt;", d)
    table_h = re.search("&lt;table\s?height=((?:(?!&gt;).)*)&gt;", d)
    table_a = re.search("&lt;table\s?align=((?:(?!&gt;).)*)&gt;", d)
    if(table_w):
        alltable += 'width: ' + table_w.groups()[0] + ';'
    if(table_h):
        alltable += 'height: ' + table_h.groups()[0] + ';'
    if(table_a):
        if(table_a.groups()[0] == 'right'):
            alltable += 'float: right;'
        elif(table_a.groups()[0] == 'center'):
            alltable += 'margin: auto;'
            
    table_t_a = re.search("&lt;table\s?textalign=((?:(?!&gt;).)*)&gt;", d)
    if(table_t_a):
        if(table_t_a.groups()[0] == 'right'):
            alltable += 'text-align: right;'
        elif(table_t_a.groups()[0] == 'center'):
            alltable += 'text-align: center;'

    row_t_a = re.search("&lt;row\s?textalign=((?:(?!&gt;).)*)&gt;", d)
    if(row_t_a):
        if(row_t_a.groups()[0] == 'right'):
            rowstyle += 'text-align: right;'
        elif(row_t_a.groups()[0] == 'center'):
            rowstyle += 'text-align: center;'
        else:
            rowstyle += 'text-align: left;'
    
    table_cel = re.search("&lt;-((?:(?!&gt;).)*)&gt;", d)
    if(table_cel):
        cel = 'colspan="' + table_cel.groups()[0] + '"'
    else:
        cel = 'colspan="' + str(round(len(d2) / 2)) + '"'   

    table_row = re.search("&lt;\|((?:(?!&gt;).)*)&gt;", d)
    if(table_row):
        row = 'rowspan="' + table_row.groups()[0] + '"'

    row_bgcolor_1 = re.search("&lt;rowbgcolor=(#[0-9a-f-A-F]{6})&gt;", d)
    row_bgcolor_2 = re.search("&lt;rowbgcolor=(#[0-9a-f-A-F]{3})&gt;", d)
    row_bgcolor_3 = re.search("&lt;rowbgcolor=(\w+)&gt;", d)
    if(row_bgcolor_1): 
        rowstyle += 'background: ' + row_bgcolor_1.groups()[0] + ';'
    elif(row_bgcolor_2):
        rowstyle += 'background: ' + row_bgcolor_2.groups()[0] + ';'
    elif(row_bgcolor_3):
        rowstyle += 'background: ' + row_bgcolor_3.groups()[0] + ';'
        
    table_border_1 = re.search("&lt;table\s?bordercolor=(#[0-9a-f-A-F]{6})&gt;", d)
    table_border_2 = re.search("&lt;table\s?bordercolor=(#[0-9a-f-A-F]{3})&gt;", d)
    table_border_3 = re.search("&lt;table\s?bordercolor=(\w+)&gt;", d)
    if(table_border_1):
        alltable += 'border: ' + table_border_1.groups()[0] + ' 2px solid;'
    elif(table_border_2):
        alltable += 'border: ' + table_border_2.groups()[0] + ' 2px solid;'
    elif(table_border_3):
        alltable += 'border: ' + table_border_3.groups()[0] + ' 2px solid;'
        
    table_bgcolor_1 = re.search("&lt;table\s?bgcolor=(#[0-9a-f-A-F]{6})&gt;", d)
    table_bgcolor_2 = re.search("&lt;table\s?bgcolor=(#[0-9a-f-A-F]{3})&gt;", d)
    table_bgcolor_3 = re.search("&lt;table\s?bgcolor=(\w+)&gt;", d)
    if(table_bgcolor_1):
        alltable += 'background: ' + table_bgcolor_1.groups()[0] + ';'
    elif(table_bgcolor_2):
        alltable += 'background: ' + table_bgcolor_2.groups()[0] + ';'
    elif(table_bgcolor_3):
        alltable += 'background: ' + table_bgcolor_3.groups()[0] + ';'
        
    bgcolor_1 = re.search("&lt;bgcolor=(#[0-9a-f-A-F]{6})&gt;", d)
    bgcolor_2 = re.search("&lt;bgcolor=(#[0-9a-f-A-F]{3})&gt;", d)
    bgcolor_3 = re.search("&lt;bgcolor=(\w+)&gt;", d)
    if(bgcolor_1):
        celstyle += 'background: ' + bgcolor_1.groups()[0] + ';'
    elif(bgcolor_2):
        celstyle += 'background: ' + bgcolor_2.groups()[0] + ';'
    elif(bgcolor_3):
        celstyle += 'background: ' + bgcolor_3.groups()[0] + ';'
        
    st_bgcolor_1 = re.search("&lt;(#[0-9a-f-A-F]{6})&gt;", d)
    st_bgcolor_2 = re.search("&lt;(#[0-9a-f-A-F]{3})&gt;", d)
    st_bgcolor_3 = re.search("&lt;(\w+)&gt;", d)
    if(st_bgcolor_1):
        celstyle += 'background: ' + st_bgcolor_1.groups()[0] + ';'
    elif(st_bgcolor_2):
        celstyle += 'background: ' + st_bgcolor_2.groups()[0] + ';'
    elif(st_bgcolor_3):
        celstyle += 'background: ' + st_bgcolor_3.groups()[0] + ';'
        
    n_width = re.search("&lt;width=((?:(?!&gt;).)*)&gt;", d)
    n_height = re.search("&lt;height=((?:(?!&gt;).)*)&gt;", d)
    if(n_width):
        celstyle += 'width: ' + n_width.groups()[0] + ';'
    if(n_height):
        celstyle += 'height: ' + n_height.groups()[0] + ';'
        
    text_right = re.search("&lt;\)&gt;", d)
    text_center = re.search("&lt;:&gt;", d)
    text_left = re.search("&lt;\(&gt;",  d)
    if(text_right):
        celstyle += 'text-align: right;'
    elif(text_center):
        celstyle += 'text-align: center;'
    elif(text_left):
        celstyle += 'text-align: left;'
        
    alltable += '"'
    celstyle += '"'
    rowstyle += '"'

    return([alltable, rowstyle, celstyle, row, cel])

def namumark(data):
    data = re.sub('<', '&lt;', data)
    data = re.sub('>', '&gt;', data)
    data = re.sub('"', '&quot;', data)

    data = re.sub("(?:\|\|\r\n)", "#table#<tablenobr>", data)
        
    while(1):
        y = re.search("(\|\|(?:(?:(?:(?:(?!\|\|).)*)(?:\n?))+))", data)
        if(y):
            a = y.groups()
            
            mid_data = re.sub("\|\|", "#table#", a[0])
            mid_data = re.sub("\r\n", "<br>", mid_data)
            
            data = re.sub("(\|\|((?:(?:(?:(?!\|\|).)*)(?:\n?))+))", mid_data, data, 1)
        else:
            break
            
    data = re.sub("#table#", "||", data)
    data = re.sub("<tablenobr>", "\r\n", data)
    
    while(1):
        m = re.search("(\|\|(?:(?:(?:.*)\n?)\|\|)+)", data)
        if(m):
            results = m.groups()
            table = results[0]
            while(1):
                a = re.search("^(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", table)
                if(a):
                    row = ''
                    cel = ''
                    celstyle = ''
                    rowstyle = ''
                    alltable = ''
                    table_d = ''

                    result = a.groups()
                    if(result[1]):
                        table_d = table_p(result[1], result[0])
                        alltable = table_d[0]
                        rowstyle = table_d[1]
                        celstyle = table_d[2]
                        row = table_d[3]
                        cel = table_d[4]
                            
                        table = re.sub("^(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "{| class='wikitable' " + alltable + "\n|- " + rowstyle + "\n| " + cel + " " + row + " " + celstyle + " | ", table, 1)
                    else:
                        cel = 'colspan="' + str(round(len(result[0]) / 2)) + '"'
                        table = re.sub("^(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "{| class='wikitable'\n| " + cel + " | ", table, 1)
                else:
                    break
                    
            table = re.sub("\|\|$",                 "</td> \
                                                </tr> \
                                            </tbody> \
                                        </table>", table)
            
            while(1):
                b = re.search("\|\|\r\n(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", table)
                if(b):
                    row = ''
                    cel = ''
                    celstyle = ''
                    rowstyle = ''
                    table_d = ''

                    result = b.groups()
                    if(result[1]):
                        table_d = table_p(result[1], result[0])
                        rowstyle = table_d[1]
                        celstyle = table_d[2]
                        row = table_d[3]
                        cel = table_d[4]
                        
                        table = re.sub("\|\|\r\n(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "\n|- " + rowstyle + "\n| " + cel + " " + row + " " + celstyle + " | ", table, 1)
                    else:
                        cel = 'colspan="' + str(round(len(result[0]) / 2)) + '"'
                        table = re.sub("\|\|\r\n(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "\n|-\n| " + cel + " | ", table, 1)
                else:
                    break

            while(1):
                c = re.search("(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", table)
                if(c):
                    row = ''
                    cel = ''
                    celstyle = ''
                    table_d = ''

                    result = c.groups()
                    if(result[1]):
                        table_d = table_p(result[1], result[0])
                        celstyle = table_d[2]
                        row = table_d[3]
                        cel = table_d[4]

                        table = re.sub("(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "\n| " + cel + " " + row + " " + celstyle + " | ", table, 1)
                    else:
                        cel = 'colspan="' + str(round(len(result[0]) / 2)) + '"'
                        table = re.sub("(\|\|(?:(?:\|\|)+)?)((?:&lt;(?:(?:(?!&gt;).)*)&gt;)+)?", "\n| " + cel + " | ", table, 1)
                else:
                    break
            table += '\n|}'
            data = re.sub("(\|\|(?:(?:(?:.*)\n?)\|\|)+)", table, data, 1)
        else:
            break

    data = re.sub("(\n<nobr>|<nobr>\n|<nobr>)", "", data)
    data = re.sub('\n', '<br>', data)

    return(data)

@route('/', method=['POST', 'GET'])
def start():
    if(request.method == 'POST'):
        data =  '<html> \
                    <body> \
                        <a href="https://github.com/2DU/NamuMark-Table-To-MediaWiki">깃 허브</a> \
                        <br> \
                        <form action="/" method="POST"> \
                            <textarea style="width: 100%; height: 500px;" name="data">' + request.POST.data + '</textarea> \
                            <br> \
                            <input value="변환" type="submit"> \
                        </form> \
                        <br> \
                        ' + namumark(request.POST.data) + ' \
                    </body> \
                </html>'
    else:
        data =  '<html> \
                    <body> \
                        <a href="https://github.com/2DU/NamuMark-Table-To-MediaWiki">깃 허브</a> \
                        <br> \
                        <form action="/" method="POST"> \
                            <textarea style="width: 100%; height: 500px;" name="data"></textarea> \
                            <br> \
                            <input value="변환" type="submit"> \
                        </form> \
                    </body> \
                </html>'

    return(data)

@error(404)
def error_404(error):
    return(redirect('/'))

run(
    host = '0.0.0.0',
    server = 'tornado',
    port = 3000
)
