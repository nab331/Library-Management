from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Type,book,Issued
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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
         query=request.GET.get("q")
         if query:
             queryset_list=Issued.objects.filter(ISBN=query)
             issued = queryset_list
             return render(request, "student_dash.html",
                           context={'issued':issued,'currentuser': currentuser, 'currentType': currentType,
                                    'query_list': queryset_list})

         issued = Issued.objects.filter(userName=currentuser)
         return render(request, "student_dash.html", context={'issued':issued ,'currentuser':currentuser,'currentType':currentType,})


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
            bookform = forms.CreateBook(request.POST)

            if issueform.is_valid():
                q_isbn = issueform.cleaned_data.get('ISBN')
                q_username = issueform.cleaned_data.get('userName')

                isbn_found = False
                user_found = False

                for a_book in book.objects.all():
                    if a_book.ISBN==q_isbn:
                        isbn_found=True
                        break

                for a_user in Type.objects.all():
                    if a_user.userName==q_username:
                        user_found=True
                        break

                if user_found and isbn_found:

                    book_change = book.objects.get(ISBN=q_isbn);
                    book_change.bookcount=book_change.bookcount-1;
                    book_change.save()

                    issueform.save()
                    return redirect("dash:staff_dash")

                else:
                    print ("Not Found")



            if request.POST.get("id",""):
                id = request.POST.get("id")
                Issued.objects.get(IssueID=id).delete()
                return redirect("dash:staff_dash")

            if request.POST.get("id2",""):
                id = request.POST.get("id2")
                all_book = book.objects.all()
                return render(request, "dash/booklist_staff.html",
                              context={'all_book': all_book, 'currentuser': currentuser, 'currentType': currentType})

            if bookform.is_valid():
                bookform.save()
                return redirect("dash:staff_dash")






                #print "\n\n\n\n\n\n\n"
                #print form['username'].value();


        bookform = forms.CreateBook()
        issueform = forms.CreateIssued()
        issuedbooks = Issued.objects.all().order_by('-Issued_date');
        return render(request, 'dash/staff_dash.html', {'bookform':bookform,'currentuser':currentuser,'issuedbooks':issuedbooks,'issueform':issueform,'currentType':currentType})


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

            if request.POST.get("id",""):
                id = request.POST.get("id")
                print (id)

                Type.objects.get(userName=id).delete()
                User.objects.get(username=id).delete()
                # return redirect("dash:admin_dash")



        form = UserCreationForm()
        userform = forms.CreateType()

        return render(request, 'dash/admin_dash.html', { 'Users':Users,'form':form,'userform':userform,'currentuser':currentuser,'currentType':currentType})



@login_required(login_url='/accounts/login')
def book_list(request):
    currentuser = request.user.username
    currentType = Type.objects.get(userName=currentuser).userType

    if currentType != 'student':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    else:
        query = request.GET.get("q")
        if query:
            queryset_list = book.objects.filter(ISBN=query)

            if not queryset_list.exists():
                    queryset_list=book.objects.filter(title=query)

            if not queryset_list.exists():
                    queryset_list=book.objects.filter(author=query)

            all_book=queryset_list

            return render(request, "dash/book_list.html",
                          context={'query_list':queryset_list,'all_book': all_book, 'currentuser': currentuser, 'currentType': currentType})

        all_book = book.objects.all()
        return render(request, "dash/book_list.html",
                      context={'all_book': all_book, 'currentuser': currentuser, 'currentType': currentType})


@login_required(login_url='/accounts/login')
def users_list(request):
    currentuser = request.user.username
    currentType = Type.objects.get(userName=currentuser).userType

    if currentType != 'student':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    else:
        query = request.GET.get("q")
        if query:
            queryset_list = Type.objects.filter(userName=query)
            users=queryset_list
            return render(request, "dash/users_list.html",
                          context={'users': users, 'currentuser': currentuser, 'currentType': currentType,'query_list':queryset_list})
        users=Type.objects.all()
        return render(request, "dash/users_list.html",
                      context={'users': users, 'currentuser': currentuser, 'currentType': currentType})