from django.shortcuts import render,HttpResponse
from apps.models import*
import hashlib

def index(request):
	return render(request,'index.html')

def about(request):
	viewqurey = image_tb.objects.all()
	return render(request,'about.html',{'viewqurey':viewqurey})
	
def services(request):
	viewqurey = image_tb.objects.all()
	return render(request,'services.html',{'viewqurey':viewqurey})
	
	

def contact(request):
	if request.method =='POST':
		firstname =request.POST['firstn']
		lastname =request.POST['lastn']
		Number =request.POST['phone']
		query=person_tb(first_name=firstname,last_name=lastname,Number=Number)
		query.save()
	return render(request,'contact.html')

def contact1(request):
	if request.method =='POST':
		firstname =request.POST['firstna']
		lastname =request.POST['lastna']
		Number =request.POST['phones']
		email =request.POST['email']
		password =request.POST['passwrd']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()


		query=cust_tb(email=email,password=hashpass,first_name=firstname,last_name=lastname,Number=Number)
		query.save()
	return render(request,'contact1.html')

def login(request):
	if request.method =='POST':
		email =request.POST['email1']
		password =request.POST['passwrd1']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=cust_tb.objects.all().filter(email=email,password=hashpass)
		if check:
			for x in check:
				print("====================================")
				request.session['userid']=x.id
			return render(request,'index.html')
		else:
			return render(request,'registration.html')
			
	return render(request,'registration.html')

def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'index.html')


def myprofile(request):
	if request.session.has_key('userid'):
		uid=request.session['userid']
		viewqurey = cust_tb.objects.all().filter(id=uid)
		return render(request,'myprofile.html',{'viewqurey':viewqurey})
	else:
		return render(request,'registration.html')

def delete(request):
	usid=request.GET['uid']
	vd = cust_tb.objects.all().filter(id=usid).delete()

	viewqurey = cust_tb.objects.all()
	return render(request,'table.html',{'viewqurey':viewqurey})


	

def viewdata(request):
		viewqurey = cust_tb.objects.all()
		return render(request,'table.html',{'viewqurey':viewqurey})


def update(request):
	usid=request.GET['uid']
	vd=cust_tb.objects.all().filter(id=usid)
	print(vd)
	return render(request,'update.html',{'vd':vd})


def updateform(request):
	if request.method =='POST':
		usid=request.GET['uid']
		firstname =request.POST['firstna']
		lastname =request.POST['lastna']
		Number =request.POST['phones']
		email =request.POST['email']
		password =request.POST['passwrd']
		query=cust_tb.objects.all().filter(id=usid).update(email=email,password=password,first_name=firstname,last_name=lastname,Number=Number)
	viewqurey = cust_tb.objects.all()
	return render(request,'table.html',{'viewqurey':viewqurey})
# Create your views here.


def imageget(request):
	if request.method =='POST':
		img= request.FILES['uploadFromPC']
		query=image_tb(image=img)
		query.save()
	return render(request,'images.html')


def imageupload(request):
	if request.method =='POST':
		img= request.FILES['uploadto']
		query=image_tb(image=img)
		query.save()
	return render(request,'image1.html')




from reportlab.pdfgen import canvas 
from django.views.generic import View
from project3.utils import render_to_pdf



def downloadtc(request):
	if request.session.has_key('userid'):
		usid=request.GET['uid']
		users=cust_tb.objects.all().filter(id=usid)
		pdf=render_to_pdf('pdfdownload.html',{'users':users})
		return HttpResponse(pdf,content_type='application/pdf')
	else:
		return render(request,'registration.html')	


def favactor(request):
	if request.session.has_key('userid'):
		if request.method=='POST':
			favactor=request.POST['favactor']
			userid=request.session['userid']
			uid=cust_tb.objects.get(id=userid)
			query=fav_tb(favactor_title=favactor,userid=uid)
			query.save()
		return render(request,'favactor.html')
		
		return render(request,'registration.html')	



def luckyno(request):
	if request.session.has_key('userid'):
		if request.method=='POST':
			luckyno=request.POST['luckyno']
			userid=request.session['userid']
			uid=cust_tb.objects.get(id=userid)
			query=luck_tb(luckyno_title=luckyno,userid=uid)
			query.save()
		return render(request,'luckyno.html')
	return render(request,'registration,html')
