from django.shortcuts import render
import mysql.connector as msc
# Create your views here.
conn=msc.connect(host="*****",user="****",password="*****",database="****")
c=conn.cursor()
r=0
def admin(request):
    return render(request,"admin.html")
def info(request):
    return render(request,"info.html")
def tab(request):
    c.execute("create table if not exists info(rollno int primary key,name varchar(50),dob varchar(50),city varchar(50),email varchar(50),school varchar(50))")
    c.execute("create table if not exists marks(rollno int,subjects varchar(50),marks varchar(50),foreign key fk(rollno) references info(rollno))")
    conn.commit()
    rollno=request.GET.get("rno")
    name=request.GET.get("name")
    dob=request.GET.get("dob")
    city=request.GET.get("city")
    email=request.GET.get("email")
    scl=request.GET.get("scl")
    c.execute("insert into info values({},'{}','{}','{}','{}','{}')".format(rollno,name,dob,city,email,scl))
    conn.commit()
    s1=request.GET.get("sub1")
    s2=request.GET.get("sub2")
    s3=request.GET.get("sub3")
    s4=request.GET.get("sub4")
    s5=request.GET.get("sub5")
    sub=s1+","+s2+","+s3+","+s4+","+s5
    m1=request.GET.get("mk1")
    m2=request.GET.get("mk2")
    m3=request.GET.get("mk3")
    m4=request.GET.get("mk4")
    m5=request.GET.get("mk5")
    p1=request.GET.get("md1")
    p2=request.GET.get("md2")
    p3=request.GET.get("md3")
    p4=request.GET.get("md4")
    p5=request.GET.get("md5")
    marks=m1+","+p1+":"+m2+","+p2+":"+m3+","+p3+":"+m4+","+p4+":"+m5+","+p5
    c.execute("insert into marks values({},'{}','{}')".format(rollno,sub,marks))
    conn.commit()
    return render(request,"sucess.html")
def main(request):
    return render(request,"main.html",{"ch":0})
def adlog(request):
    conn=msc.connect(host="localhost",user="root",password="india",database="cbse")
    c=conn.cursor()
    i=request.POST.get("ID")
    p=request.POST.get("pass")
    c.execute("select * from admin where id='{}' and pass='{}'".format(i,p))  
    a=c.fetchone()
    conn.close()
    if a==None:
        return render(request,"main.html",{"ch":1})
    return render(request,"admin.html")
def mindex(request):
    return render(request,"mindex.html")
def search(request):
    conn=msc.connect(host="localhost",user="root",password="india",database="cbse")
    c=conn.cursor()
    global r
    s=str(request.GET.get("rnos"))
    r=s
    c.execute("select * from info where rollno={}".format(s))
    a=c.fetchone()
    n=a[1]
    d=a[2]
    c=a[3]
    e=a[4]
    s=a[5]
    conn.close()
    return render(request,"mindex.html",{"n":n,"d":d,"c":c,"e":e,"s":s})
def mod(request):
    conn=msc.connect(host="localhost",user="root",password="india",database="cbse")
    c=conn.cursor()
    global r
    n=str(request.GET.get("n"))
    d=str(request.GET.get("d"))
    x=str(request.GET.get("c"))
    e=str(request.GET.get("e"))
    s=str(request.GET.get("s"))
    c.execute("update info set name='{}',dob='{}',city='{}',email='{}',school='{}' where rollno={}".format(n,d,x,e,s,r))
    conn.commit()
    conn.close()
    return render(request,"admin.html")
def sera(request):
    return render(request,"search.html")
def ser(request):
    n=int(request.GET.get("rno"))
    conn=msc.connect(host="localhost",user="root",password="india",database="cbse")
    c=conn.cursor()
    c.execute("select * from marks where rollno={}".format(n))
    a=c.fetchone()
    r=a[0]
    s=a[1].split(",")
    return render(request,"search.html",{"l":a})
