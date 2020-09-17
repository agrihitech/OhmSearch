# -*- coding: <encoding utf-8> -*-
import logging
from django.views import generic
from . import forms
from django.template.context_processors import csrf
import logging
from django.shortcuts import render
from ohm.forms import SampleForm
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views import View

import sqlite3
import math

def calc(R):
    kind = [ u"",u"単独",u"直列",u"並列"]
    conn = sqlite3.connect('regdb.sqlite3')
    x = conn.cursor()
    y = conn.cursor()

    y.execute("drop table sort");
    com = 'create table sort(rid integer, error1 real, error2 real)'
    y.execute(com)
    com = "select * from registors"
    x.execute(com)
    while True:
        raw = x.fetchone()
        if raw == None:
            break
        error1 = raw[3] - R
        error2 = abs(error1)
        com = "insert into sort values("+str(raw[0])+","+str(error1)+","+str(error2)+")"
        y.execute(com)
    conn.commit()
    com = "select * from sort order by error2 asc limit 10"
    y.execute(com)
    anser = y.fetchall()
    disp = u'<table border="1"><tr><td>回路</td/><td>R1</td><td>R2</td><td>仕上</td><td>誤差</td></tr>'
    for ans in anser:
        com = "select * from registors where id="+str(ans[0])
        x.execute(com)
        reg = x.fetchone()
        disp += "<tr><td>%s</td><td>%g</td><td>%g</td><td>%g</td><td>%g%%</td></tr>" % (kind[reg[4]],reg[1],reg[2],reg[3],ans[2]*100/R)
    disp += "</table>"
    return disp


multi = [0,1e-3,1,1e3,1e6,1e9]
def ohm(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SampleForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            unit = int(form.cleaned_data['select'])
            reg = float(form.cleaned_data['value']) * multi[unit]
            form.message = calc(reg)
        return render(request,
        'ohm/ohmform.html',
        {"form" : form}
        )
    else:
        form = SampleForm
        return render(request,
        'ohm/ohmform.html',
        {"form" : form}
        )
