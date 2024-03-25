from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EForm

# Create your views here.

def greet(t):
	return HttpResponse("Good Evening to All..")

def demo(c,v="rajesh"):
	return HttpResponse(f"Good Evening: {v}")

def b(request,y):
	return HttpResponse("Hello User {}".format(y))

def st(request,r,a):
	return HttpResponse(f"<h1>Username: {a}</h1><h3>Age: {r}</h3>")

def em(request,en,sa,dg):
	return HttpResponse(f"<h3>Employee Name: {en}<br/>Salary: {sa}<br/>Designation: {dg}</h3>")

def cpp(request,cmp,ename):
	return HttpResponse(f"<h3>Company: <span style='background-color:green;color:white;padding:5px'>{cmp}</span></h3><h3>Employee Name: <span style='color:yellow'>{ename}</span></h3>")

def fy(request,d):
	return HttpResponse(f"<script>alert('Hi Welcome {d}')</script><h1>Username: {d}</h1>")

def dd(request):
	return HttpResponse("<html><title>Sample</title><body>Sample HTML Structure response</body></html>")

def hk(request):
	return render(request,'da.html')

def fbn(request,c):
	return render(request,'wv.html',{'t':c})

def std(request,rn,sn,sb,sy,cg):
	q = {'a':rn,'b':sn,'c':sb,'d':sy,'e':cg}
	return render(request,'st.html',q)

def fm(request):
	if request.method == "POST":
		a = request.POST['ed']
		b = request.POST['en']
		c = request.POST['ea']
		d = request.POST['edg']
		return render(request,'edata.html',{'edd':a,'ename':b,'eage':c,'edes':d})
	return render(request,'emp.html')

def btp(request):
	return render(request,'bt/empy.html')

def eda(request):
	z = Employee.objects.all()
	if request.method == "POST":
		y = Employee(epid=request.POST['eid'],ename=request.POST['en'],esal=request.POST['es'],edesg=request.POST['ede'])
		y.save()
		return redirect('/d/')
	return render(request,'bt/emform.html',{'ep':z})

def emup(request,g):
	k = Employee.objects.get(id=g)
	if request.method == "POST":
		k.epid = request.POST['eppid']
		k.ename = request.POST['epn']
		k.esal = request.POST['eps']
		k.edesg = request.POST['epde']
		k.save()
		return redirect('/d/')
	return render(request,'bt/stupdate.html',{'dc':k})

def edl(request,q):
	z = Employee.objects.get(id=q)
	if request.method == "POST":
		z.delete()
		return redirect('/d/')
	return render(request,'bt/stdlte.html',{'de':z})

def edd(request):
	if  request.method == "POST":
		b = EForm(request.POST)
		if b.is_valid():
			b.save()
			return redirect('/')
	b = EForm()
	return render(request,'bt/emplist.html',{'t':b})