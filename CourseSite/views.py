from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):

	ext_file = open("/home/car10s/Documentos/Python/Django/CourseSite/CourseSite/templates/template1.html")
	tmpl = Template(ext_file.read())
	ext_file.close()

	context = Context()
	doc = tmpl.render(context)
	return HttpResponse(doc)

def getDate(request):

	_date = datetime.datetime.now()
	doc = """
	<html>
		<body>
			<h1>
			Fecha y hora actuales %s
			</h1> 
		</body>
	</html>""" % _date

	return HttpResponse(doc)

def calculateAge(request, age, year):

	period = year - 2022
	futureAge = age + period

	doc = "<html><body><h2>En el año %s tendras %s años</h2></body></html>"%(year,futureAge)

	return HttpResponse(doc)