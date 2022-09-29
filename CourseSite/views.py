from django.http import HttpResponse
import datetime

def saludo(request):

	return HttpResponse("Esta es la vista Django")

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