from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Type,book,Issued
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .import forms
########################################################################
@login_required(login_url='/accounts/login')
def student_dash(request):
    currentuser = request.user.username
    currentType = Type.objects.get(userName=currentuser).userType

    if currentType!='student':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

    else:
        all_book = book.objects.all()
        return render(request, "dash/book_list.html", context={'all_book': all_book,'currentuser':currentuser,'currentType':currentType})


########################################################################

@login_required(login_url='/accounts/login')
def staff_dash(request):
    currentuser = request.user.username;
    currentType = Type.objects.get(userName=currentuser).userType

    if currentType!='staff':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

    else:


        if request.method == 'POST':
            issueform = forms.CreateIssued(request.POST)
            if issueform.is_valid():
                issueform.save()
                return redirect("dash:staff_dash")

            if request.POST.get("id",""):
                id = request.POST.get("id")
                Issued.objects.get(IssueID=id).delete()
                return redirect("dash:staff_dash")




                #print "\n\n\n\n\n\n\n"
                #print form['username'].value();



        issueform = forms.CreateIssued()
        issuedbooks = Issued.objects.all().order_by('-Issued_date');
        return render(request, 'dash/staff_dash.html', {'currentuser':currentuser,'issuedbooks':issuedbooks,'issueform':issueform,'currentType':currentType})


###########################################################################

@login_required(login_url='/accounts/login')
def admin_dash(request):

    #users = TypeTable.objects.all().order_by('date');

    currentuser = request.user.username;
    currentType = Type.objects.get(userName=currentuser).userType

    if currentType!='admin':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html',{'form':form})

    else:
        Users = Type.objects.all().order_by('-date');
        if request.method == 'POST':
            userform = forms.CreateType(request.POST)
            form = UserCreationForm(request.POST)



            if form.is_valid() and userform.is_valid():
                form.save()

                #temp instance to add user to type Type table
                instance = userform.save(commit=False)
                instance.userName = form['username'].value()
                instance.save()
                return redirect("dash:admin_dash")

                #print "\n\n\n\n\n\n\n"
                #print form['username'].value();


        form = UserCreationForm()
        userform = forms.CreateType()

        return render(request, 'dash/admin_dash.html', { 'Users':Users,'form':form,'userform':userform,'currentuser':currentuser,'currentType':currentType})
