from django.shortcuts import render,redirect

# Create your views here.

#from polls.models import camtelclient
from polls.models import output
from polls.models import title
#from polls.forms import clientform
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
import csv, io
import logging
import datetime
from django.contrib import messages
from datetime import timedelta

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



#def login(request):
#	context = {}
#	logout(request)
#	username = password = ''
#	if request.POST:
#		username = request.POST['username']
#		password = request.POST['password']

#		user = authenticate(username=username, password=password)
#		if user is not None:
#			if user.is_active:
#				login(request, user)
#				return HttpResponseRedirect(reverse("polls:index"))
#	return render(request, "login.html", context)

@login_required
def index(request):
    data = {}
    if "GET" == request.method:
        return render(request, "index.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("polls:index"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("polls:index"))
        
        csv_file.seek(0)
        file_data = csv_file.read().decode("utf-8")
        io_string = io.StringIO(file_data)

        csv.register_dialect('myDialect', delimiter = ",", quoting=csv.QUOTE_NONE)

        #lines = file_data.split("\n")
        #loop over the lines and save them in db. If error , store as string and then display
        reader = csv.reader(io_string, dialect='myDialect')

        count = 1
        n = 0
        begin1 = []
        for column in reader:
        	if "Title" in column[0]:
        		request.session['title'] = column[1]
        		_, created = title.objects.update_or_create(Title=request.session['title'])
        		next(reader)     
        		next(reader)        
        		next(reader)        
        		next(reader)
        		next(reader)        
        		next(reader)        
        		next(reader)        
        		next(reader)        
        		next(reader)  
        		print(column)      
        	if "NaN" in column[1]:
        		begin = []
        		begin.append(column[0])
        		begin1.append(begin[0])
        		end = next(reader)
        		if "NaN" not in end[1]:
        			begin_date = datetime.datetime.strptime(begin1[n].replace('\"',''), "%Y-%m-%d %H:%M:%S")
        			end_date = datetime.datetime.strptime(end[0].replace('\"',''), "%Y-%m-%d %H:%M:%S")
        			diff = end_date - begin_date
        			_, created = output.objects.update_or_create(Number=count, DateDeCoupure=begin_date, DateDeRetablisement=end_date, Duree = diff)
        			count = count + 1
        			n = len(begin1)
        		else:
        			#begin1.append(begin[0])
        			next(reader)
        			nexts = next(reader)
        			if "NaN" not in nexts[1]:
        				begin_date = datetime.datetime.strptime(begin1[n].replace('\"',''), "%Y-%m-%d %H:%M:%S")
        				end_date = datetime.datetime.strptime(nexts[0].replace('\"',''), "%Y-%m-%d %H:%M:%S")
        				diff = end_date - begin_date
        				_, created = output.objects.update_or_create(Number=count, DateDeCoupure=begin_date, DateDeRetablisement=end_date, Duree = diff)
        				count = count + 1
        				n = len(begin1)

        	#data_dict = {}
        	#data_dict["Date"] = column[0]
        	#data_dict["Inbound"] = column[1]
        	#data_dict["col2_cdefa"] = column[2]
        	#data_dict["Outbound"] = column[3]
        	#data_dict["col4_cdeff"] = column[4]
        	#data_dict["col5_cdefa"] = column[5]
        	#data_dict["col6_cdefbb"] = column[6]
        	#try:
        	#	form = clientform(data_dict)
        	#	if form.is_valid():
        	#		form.save()         
        	#	else:                 
        	#		logging.getLogger("error_logger").error(form.errors.as_json())                                              
        	#except Exception as e:
        	#	logging.getLogger("error_logger").error(repr(e))                    
        	#	pass
    except Exception as e:
    	logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
    	messages.error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("polls:index"))
