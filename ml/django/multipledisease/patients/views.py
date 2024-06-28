from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        last=request.POST['lname']
        un=request.POST['uname']
        em=request.POST['email']
        p1=request.POST['psw']
        p2=request.POST['psw1']
        if p1==p2:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email already Exists")
                return render(request,"register.html")
            else:
                 user=User.objects.create_user(first_name=first,
        last_name=last,email=em,username=un,password=p1 )
                 return redirect('login')
        else:
             messages.info(request,"password not matching")
             return render(request,"register.html")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        p1=request.POST['psw']
        user=auth.authenticate(username=uname,password=p1)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('index')
        else:
             messages.info(request,"invalid credentials")
             return render(request,"login.html")
    return render(request,"login.html")


def index(request):
    return render(request,"index.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('index')

def multipledisease(request):
    if request.method=="POST":
        glucose=float(request.POST['glucose'])
        cholesterol=float(request.POST['cholesterol'])
        hemoglobin=float(request.POST['hemoglobin'])
        platelets=float(request.POST['platelets'])
        whiteblood=float(request.POST['whiteblood'])
        redblood=float(request.POST['redblood'])
        insulin=float(request.POST['insulin'])
        bmi=float(request.POST['bmi'])
        sbloodpressure=float(request.POST['sbloodpressure'])
        dbloodpressure=float(request.POST['dbloodpressure'])
        lchol=float(request.POST['lchol'])
        hchol=float(request.POST['hchol'])
        heartrate=float(request.POST['heartrate'])
        creat=float(request.POST['creat'])
        troponin=float(request.POST['troponin'])
        react=float(request.POST['react'])
        import pandas as pd
        df=pd.read_csv(r"static/Disease.csv")
        print(df.head())
        print(df.isnull().sum())
        print(df.dropna(inplace=True))
        
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.heatmap(df.isnull())
        plt.show()
        plt.bar(df["Cholesterol"],df["Hemoglobin"])
        plt.show()
        sns.set_style("darkgrid")
        sns.countplot(df["Hemoglobin"])
        plt.show()
        x=df[["Glucose","Cholesterol","Hemoglobin","Platelets","White Blood Cells","Red Blood Cells","Insulin","BMI","Systolic Blood Pressure"
        ,"Diastolic Blood Pressure","LDL Cholesterol","HDL Cholesterol","Heart Rate","Creatinine","Troponin","C-reactive Protein"]]
        #x=df.drop(["Disease","Hematocrit","Mean Corpuscular Hemoglobin","Mean Corpuscular Volume","Mean Corpuscular Hemoglobin Concentration","Triglycerides","HbA1c","ALT","AST"],axis=1)
        print(x[0:3])
        y=df["Disease"]
        from sklearn.linear_model import LogisticRegression
        log=LogisticRegression()
        log.fit(x,y)
        import numpy as np
        data=np.array([[glucose,cholesterol,hemoglobin,platelets,whiteblood,redblood,insulin,bmi,sbloodpressure,dbloodpressure,lchol,hchol,heartrate,creat,react,troponin]],dtype=object
        )
        pred_dis=log.predict(data)
        print(pred_dis)
        return render(request,"dispredict.html",
        {"glucose":glucose,"cholesterol":cholesterol,"hemoglobin":hemoglobin,"platelets":platelets,
        "whiteblood":whiteblood,"redblood":redblood,"insulin":insulin,"bmi":bmi,"sbloodpressure":sbloodpressure,
        "dbloodpressure":dbloodpressure,"lchol":lchol,"hchol":hchol,"heartrate":heartrate,"creat":creat,"troponin":troponin,"react":react,"prediction":pred_dis})
    return render(request,"disease.html")




def dispredict(request):
    return render(request,"dispredict.html")