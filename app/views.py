from django.shortcuts import render
import csv

from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_bank(self):
    with open('C:\\Users\\st150\OneDrive\\Desktop\\DjangoProject\\ankit\Scripts\\project41\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data is inserted successfully')


def insert_branch(self):
    with open('C:\\Users\\st150\OneDrive\\Desktop\\DjangoProject\\ankit\Scripts\\project41\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                brn=i[2]
                add=i[3]
                con=i[4]
                cit=i[5]
                dis=i[6]
                stat=i[7]

                BR=Branch(bank_name=BO[0],ifsc=ifs,branch=brn,address=add,contact=con,city=cit,district=dis,state=stat)
                BR.save()


    return HttpResponse('branch data is inserted successfully')





