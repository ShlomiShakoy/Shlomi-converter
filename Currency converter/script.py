import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def homehtml():
    return render_template("page.html")

@app.route('/convert', methods=['GET','POST'])
def convert():
    if request.method=="POST":
        select_from = request.form.get('from')
        select_to = request.form.get('to')
        amount=request.form.get('amount')
        from_to_str=f"From {select_from} to {select_to}"
        with open("C:\\Users\\IMOE001\\Dropbox\\PC\\Desktop\\Currency converter\\currencies.txt") as f:
            while True:
                curr_cursor=f.tell()
                line=f.readline()
                if line.__contains__(from_to_str):
                    curr_cursor_end=curr_cursor+16
                    f.seek(curr_cursor_end)
                    line_to_float=f.readline()
                    number=float(line_to_float)
                    amount_int=float(amount)
                    total=number*amount_int
                    break
        return render_template("page.html", total_change=f'After converting {amount} {select_from} to {select_to}: {total}')

if __name__=='__main__':
    app.run(debug=True)