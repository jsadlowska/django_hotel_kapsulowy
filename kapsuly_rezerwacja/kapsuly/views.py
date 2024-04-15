from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from kapsuly.models import Kapsula, Rezerwacja
from django.db import transaction
from kapsuly.forms import KapsulaForm
from kapsuly_rezerwacja.forms import SignUpForm

# Create your views here.

class KapsulaListView(ListView):
    model = Kapsula
    template_name = "index.html"
    queryset = Kapsula.objects.all()
    context_object_name = "object_list"

    def get_queryset(self):
        return self.queryset.filter(rezerwacja=None)

    def get_context_data(self, **kwargs):
        context = super(KapsulaListView, self).get_context_data(**kwargs)
        context["form"] = KapsulaForm(self.request.POST or None)
        return context

    def post(self,*args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            standard = self.request.POST["standard"]
            poziom = self.request.POST["poziom"]
            plec = self.request.POST["plec"]


            if standard != "":
                self.object_list = self.object_list.filter(standard=standard)
            if poziom != "":
                self.object_list = self.object_list.filter(poziom=poziom)
            if plec != "":
                self.object_list = self.object_list.filter(plec=plec)


            context[self.context_object_name] = self.object_list

        return render(self.request, self.template_name, context)

class KapsulaDetailView(DetailView):
    model = Kapsula
    template_name = "detail.html"

class RezerwacjaListView(ListView):
    model = Rezerwacja
    template_name = "rezerwacja.html"

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form': form})

@transaction.atomic
def reserve(request, kapsula_id):
    kapsula = Kapsula.objects.get(id=kapsula_id)
    if not kapsula.is_reserved:
        rez = Rezerwacja(kapsula=kapsula)
        rez.save()
    return redirect("index")

@transaction.atomic
def unreserve(request, rezerwacja_id):
    try:
        rez = Rezerwacja.objects.get(id=rezerwacja_id)
    except Rezerwacja.DoesNotExist:
        pass
    else:
        rez.delete()
    return redirect("index")

