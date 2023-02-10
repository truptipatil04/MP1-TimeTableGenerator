from django.shortcuts import render, redirect
from .lectureplanner import LecturePlanner
from .models import Subject, Room, Batch, Time
from .forms import SubjectForm, RoomForm, BatchForm, TimeForm

def startplanning(data):
	lecture = LecturePlanner(data['batches'][:3], data['rooms'], data['subjects'], data['time_period'][:4], 4)
	Timetable = lecture.planner()
	for i in Timetable:
		print(i)
	return Timetable

def inputdata():
    subjects = []
    for i in Subject.objects.all():
        x = i.subject
        subjects.append(x)

    batches = []
    for i in Batch.objects.all():
        x = i.batchName
        y = int(i.batchCapacity)
        z = [x, y]
        batches.append(z)

    rooms = []
    for i in Room.objects.all():
        x = i.roomName
        y = int(i.roomCapacity)
        z = [x, y]
        rooms.append(z)

    time_period = []
    for i in Time.objects.all():
        x = i.timePeriod
        time_period.append(x)

    return { "subjects": subjects, 'batches': batches, 'rooms': rooms, 'time_period': time_period }

def displayTimetable(request):
    data = inputdata()
    Timetable = startplanning(data)
    # for i in Timetable:
    #     for j in i:
    #         print(j, end="    ")
    #     print()
    # print("Timetable")
    return render(request,"displayTimetable.html", {'timetable':Timetable})

def subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            print("Subject Form Saved")
            return redirect("ttg:displaySubject")
        else:
            form = SubjectForm()
            print("Form not valid")
            return render(request, "subject.html", {"form": form})
    else:
        form = SubjectForm()
        print("Form not saved")
        return render(request, "subject.html", {"form": form})

def room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("ttg:displayRoom")
        else:
            form = RoomForm()
            print("Form not valid")
            return render(request, "room.html", {"form": form})
    else:
        form = RoomForm()
        print("Form not saved")
        return render(request, "room.html", {"form": form})

def batch(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect("ttg:displayBatch")
        else:
            form = BatchForm()
            print("Form not valid")
            return render(request, "batch.html", {"form": form})
    else:
        form = BatchForm()
        print("Form not saved")
        return render(request, "batch.html", {"form": form})

def time(request):
    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved")
            return redirect('ttg:displayTime')
        else:
            form = TimeForm()
            print("Form not valid")
            return render(request, "time.html", {"form": form})
    else:
        form = TimeForm()
        print("Form not saved")
        return render(request, "time.html", {"form" : form})


def displaySubject(request):
    return render(request, "displaySubject.html", {"posts" : Subject.objects.all()})

def displayRoom(request):
    return render(request, "displayRoom.html", {"posts" : Room.objects.all()})

def displayTime(request):
    return render(request, "displayTime.html", {"posts" : Time.objects.all()})

def displayBatch(request):
    return render(request, "displayBatch.html", {"posts" : Batch.objects.all()})


def deleteSubject(request,pk):
    s=Subject.objects.get(subject=pk)
    if request.method=='POST':
        s.delete()
        return redirect('ttg:displaySubject')
    context={
        "post": s
    }
    return render(request,'deleteSubject.html',context)

def deleteRoom(request,pk):
    r = Room.objects.get(roomName=pk)
    if request.method=='POST':
        r.delete()
        return redirect('ttg:displayRoom')
    context={
        "post": r
    }
    return render(request,'deleteRoom.html',context)

def deleteTime(request,pk):
    t = Time.objects.get(timePeriod=pk)
    if request.method=='POST':
        t.delete()
        return redirect('ttg:displayTime')
    context={
        "post": t
    }
    return render(request,'deleteTime.html',context)

def deleteBatch(request,pk):
    b = Batch.objects.get(batchName=pk)
    if request.method=='POST':
        b.delete()
        return redirect('ttg:displayBatch')
    context={
        "post": b
    }
    return render(request,'deleteBatch.html',context)