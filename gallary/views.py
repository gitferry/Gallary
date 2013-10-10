# coding=utf-8
from django.shortcuts import render_to_response
from students.models import Student

Catagory_CHOICES = ['学习之星', '科技先锋', '训练标兵', '才艺明星']
QuDui_CHOICES = ['一区队', '二区队', '三区队', '四区队']

def index(request):
    StudyImage = Student.objects.filter(catagory = "0").order_by("time")[:4]
    ScienceImage = Student.objects.filter(catagory = "1").order_by("time")[:4]
    TrainImage = Student.objects.filter(catagory = "2").order_by("time")[:4]
    TalentImage = Student.objects.filter(catagory = "3").order_by("time")[:4]

    for item in StudyImage:
    	item.url = "/info?id=" + str(item.id)

    for item in ScienceImage:
    	item.url = "/info?id=" + str(item.id)

    for item in TrainImage:
    	item.url = "/info?id=" + str(item.id)
    
    for item in TalentImage:
    	item.url = "/info?id=" + str(item.id)

    return render_to_response('index.html', locals())

def studyList(request):
	List = Student.objects.filter(catagory = "0").order_by("time")
	for item in List:
		item.url = "/info?id=" + str(item.id)
		item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
		item.catagory = Catagory_CHOICES[int(item.catagory)]
	study = True
	title = '学习之星'
	return render_to_response('list.html', locals())

def scienceList(request):
	List = Student.objects.filter(catagory = "1").order_by("time")
	for item in List:
		item.url = "/info?id=" + str(item.id)
		item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
		item.catagory = Catagory_CHOICES[int(item.catagory)]
	science = True
	title = '科技先锋'
	return render_to_response('list.html', locals())

def trainList(request):
	List = Student.objects.filter(catagory = "2").order_by("time")
	for item in List:
		item.url = "/info?id=" + str(item.id)
		item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
		item.catagory = Catagory_CHOICES[int(item.catagory)]
	train = True
	title = '训练标兵'
	return render_to_response('list.html', locals())

def talentList(request):
	List = Student.objects.filter(catagory = "3").order_by("time")
	for item in List:
		item.url = "/info?id=" + str(item.id)
		item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
		item.catagory = Catagory_CHOICES[int(item.catagory)]
	talent = True
	title = '才艺明星'
	return render_to_response('list.html', locals())

def allList(request):
	List = Student.objects.order_by("time")
	for item in List:
		item.url = "/info?id=" + str(item.id)
		item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
		item.catagory = Catagory_CHOICES[int(item.catagory)]
	all = True
	title = '所有分类'
	return render_to_response('list.html', locals())

def info(request):
	pid = request.GET.get('id')
	item = Student.objects.filter(id = int(pid))[0]
	item.QuDui = QuDui_CHOICES[int(item.QuDui) - 1]
	if not item:
		raise Http404
	return render_to_response('info.html', locals())