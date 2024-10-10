from django.shortcuts import get_object_or_404, render
from .models import Notice, Patron, Person, CommitteeMember,Book
from django.shortcuts import render, redirect
from .forms import NoticeForm,PatronForm, PersonForm, CommitteeMemberForm,BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from cloudinary import uploader

# Create your views here.
def index(request):
    # return render(request,'qflapp/index.html')
    notices = Notice.objects.all()  # Fetch all notices from the database
    return render(request, 'qflapp/index.html', {'notices': notices})

def patrons_page(request):
    patrons = Patron.objects.all().order_by('-date_posted')
    return render(request, 'qflapp/patrons.html', {'patrons': patrons})


def committeemember_page(request):
    # Get all distinct years and ensure they are sorted
    years = sorted(set(CommitteeMember.objects.values_list('year', flat=True)))

    # If a year is passed as a query parameter, use it. Otherwise, use the largest year
    year = request.GET.get('year') or (max(years, key=int) if years else None)

    # If there's no year (i.e., no data), initialize an empty list of members
    if year:
        committeemembers = CommitteeMember.objects.filter(year=year).order_by('order')
    else:
        committeemembers = []

    return render(request, 'qflapp/committeemembers.html', {
        'committeemembers': committeemembers,
        'years': years,
        'selected_year': year,  # Pass the selected or default year
    })

def books_page(request):
    # books = Book.objects.all().order_by('-code')
    # return render(request, 'qflapp/books.html', {'books': books})
    # Get the selected language from the query parameters
    selected_language = request.GET.get('language', None)  # Default to None if no language is selected
    
    if selected_language:
        # Filter books by the selected language
        books = Book.objects.filter(language=selected_language).order_by('-code')
    else:
        # If no language is selected, show all books
        books = Book.objects.all().order_by('-code')

    return render(request, 'qflapp/books.html', {
        'books': books,
        'selected_language': selected_language,  # To keep track of the selected language
    })

##########################################################################################################################

# View to list all notices
@login_required
def notice_board(request):
    notices = Notice.objects.all().order_by('-date_posted')
    return render(request, 'qflapp/notice_board.html', {'notices': notices})

# View to add a new notice
@login_required
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice-board')  # Redirect to the notice board
    else:
        form = NoticeForm()
    return render(request, 'qflapp/add_notice.html', {'form': form})

# View to delete a notice
@login_required
def delete_notice(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    if request.method == 'POST':
        notice.delete()
        return redirect('notice-board')  # Redirect to the notice board
    return render(request, 'qflapp/delete_notice.html', {'notice': notice})

@login_required
def edit_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice-board')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'qflapp/edit_notice.html', {'form': form, 'notice': notice})

#########################################################################################################################

# View to list all patrons
@login_required
def patron_board(request):
    patrons = Patron.objects.all().order_by('-date_posted')
    return render(request, 'qflapp/patron_board.html', {'patrons': patrons})

# View to add a new patron
@login_required
def add_patron(request):
    if request.method == 'POST':
        form = PatronForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patron-board')  # Redirect to the patron board
    else:
        form = PatronForm()
    return render(request, 'qflapp/add_patron.html', {'form': form})

# View to delete a patron
@login_required
def delete_patron(request, patron_id):
    patron = Patron.objects.get(id=patron_id)
    if request.method == 'POST':
        patron.delete()
        return redirect('patron-board')  # Redirect to the notice board
    return render(request, 'qflapp/delete_patron.html', {'patron': patron})

@login_required
def edit_patron(request, patron_id):
    patron = get_object_or_404(Patron, id=patron_id)
    if request.method == 'POST':
        form = PatronForm(request.POST, instance=patron)
        if form.is_valid():
            form.save()
            return redirect('patron-board')
    else:
        form = PatronForm(instance=patron)
    return render(request, 'qflapp/edit_patron.html', {'form': form, 'patron': patron})

#########################################################################################################################

# Views for login and logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a success page
        else:
            return render(request, 'qflapp/login.html', {'error': 'Invalid username or password'})
    return render(request, 'qflapp/login.html')

def custom_logout(request):
    logout(request)  # Log the user out
    return redirect('index')  # Redirect to the home page or desired page
#########################################################################################################################

# View to list all persons
@login_required
def person_board(request):
    persons = Person.objects.all().order_by('-id')
    return render(request, 'qflapp/person_board.html', {'persons': persons})

# View to add a new person
@login_required
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            form.save()
            print(f"Uploaded file URL: {request.person.photo.url}")  # Log the Cloudinary file URL
            return redirect('person-board')  # Redirect to the person board
    else:
        form = PersonForm()
    return render(request, 'qflapp/add_person.html', {'form': form})

# View to delete a person
@login_required
def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('person-board')  # Redirect to the notice board
    return render(request, 'qflapp/delete_person.html', {'person': person})

@login_required
def edit_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person-board')
    else:
        form = PersonForm(instance=person)
    return render(request, 'qflapp/edit_person.html', {'form': form, 'person': person})

#########################################################################################################################

# View to list all committee_members
@login_required
def committeemember_board(request):
    year = request.GET.get('year', None)  # Get the selected year from query params
    if year:
        committeemembers = CommitteeMember.objects.filter(year=year)
    else:
        committeemembers = CommitteeMember.objects.all()

    # Get distinct years to populate the dropdown
    years = set(CommitteeMember.objects.values_list('year', flat=True))  # Use set to ensure uniqueness
    return render(request, 'qflapp/committeemember_board.html', {
        'committeemembers': committeemembers,
        'years': sorted(years),
        'selected_year': year,  # To keep track of the selected year
    })

# View to add a new committeemember
@login_required
def add_committeemember(request):
    if request.method == 'POST':
        form = CommitteeMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('committeemember-board')  # Redirect to the committeemember board
    else:
        form = CommitteeMemberForm()
    return render(request, 'qflapp/add_committeemember.html', {'form': form})

# View to delete a committeemember
@login_required
def delete_committeemember(request, committeemember_id):
    committeemember = CommitteeMember.objects.get(id=committeemember_id)
    if request.method == 'POST':
        committeemember.delete()
        return redirect('committeemember-board')  # Redirect to the notice board
    return render(request, 'qflapp/delete_committeemember.html', {'committeemember': committeemember})

@login_required
def edit_committeemember(request, committeemember_id):
    committeemember = get_object_or_404(CommitteeMember, id=committeemember_id)
    if request.method == 'POST':
        form = CommitteeMemberForm(request.POST, instance=committeemember)
        if form.is_valid():
            form.save()
            return redirect('committeemember-board')
    else:
        form = CommitteeMemberForm(instance=committeemember)
    return render(request, 'qflapp/edit_committeemember.html', {'form': form, 'committeemember': committeemember})

#########################################################################################################################

# View to list all book
@login_required
def book_board(request):
    books = Book.objects.all().order_by('-code')
    return render(request, 'qflapp/book_board.html', {'books': books})

# View to add a new book
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        print('form received')
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('book-board')  # Redirect to the book board
        else:
            print('Form is not valid')
            print(form.errors)  # Print form errors to the console
    else:
        form = BookForm()
    return render(request, 'qflapp/add_book.html', {'form': form})

# View to delete a book
@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book-board')  # Redirect to the notice board
    return render(request, 'qflapp/delete_book.html', {'book': book})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-board')
    else:
        form = BookForm(instance=book)
    return render(request, 'qflapp/edit_book.html', {'form': form, 'book': book})

#########################################################################################################################