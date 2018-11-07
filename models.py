from django.db import models

#Modelo Base para o cadastro
class Inscricao(models.Model):
        #Cadastro Aluno e possíveis Fields
        nome = models.CharField(max_length=100,blank=True)
        cpf = models.CharField( max_length=11,blank=True)
        idade = models.PositiveIntegerField(blank=True, null=True)
        email = models.EmailField(blank=True)
        telefone = models.CharField(max_length=20, blank=True)
        
        #Cadastro de Disciplinas e possíveis Fields
        Disciplina = models.CharField(max_length=20, blank = True)
        carga_horaria = models.PositiveIntegerField(blank=True, null=True)
        professor = models.CharField(max_length=30, blank = True)
        mensalidade = models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True)
        coordenador = models.CharField(max_length = 30, blank = True)
        ano = models.PositiveIntegerField(default=0, null=True, blank=True)
        semestre = models.PositiveIntegerField(blank=True, null=True)

        #Cadastro de Professor e possíveis Fields
        cargo = models.CharField(max_length = 30, blank = True)

        # campos selects são inseridos na Field
        BOOK_CHOICES = (
                ('Sistemas de informação','Sistemas de informação'),
                ('Análise e Desenvolvimento de Sistemas','Análise e Desenvolvimento de Sistemas'),
                ('Redes','Redes'),                      
        )
         
        curso = models.CharField(max_length=150, choices=BOOK_CHOICES)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)

        class Meta:
                ordering = ['criado_em']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')
            

        def __unicode__(self):
                return self.nome

        def get_absolute_url(self):
             return u'/some_url/%d' % self.id 
        