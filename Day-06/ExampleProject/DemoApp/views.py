from django.shortcuts import render
from django.http import HttpResponse
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