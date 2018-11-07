from django.shortcuts import render
from django.views.generic import CreateView
from cadastroaluno.models import Inscricao
from cadastroaluno.forms import InscricaoForm

def home(request):
        return render(request,'index.html')

#Criação dos cadastros (Aluno,Professor,Disciplina)
class Aluno(CreateView):
        template_name = 'cadastro.html'
        model = Inscricao
        fields = 'nome','email','cpf','idade','telefone','curso'
        

class Professor(CreateView):
        template_name = 'professor.html'
        model = Inscricao
        fields = 'nome','email','telefone','cargo','Disciplina'

class Disciplina(CreateView):
        template_name = 'disciplina.html'
        model = Inscricao
        fields = 'Disciplina','professor','mensalidade','ano','coordenador','semestre'

