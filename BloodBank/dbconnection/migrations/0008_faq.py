# Migration que cria a tabela de FAQ e popula as perguntas iniciais (RF20 / RN09 / RN10).

from django.db import migrations, models


INITIAL_FAQS = [
    # Cadastro
    ('Como faço para me cadastrar como doador?',
     'Acesse o menu "Register", preencha o formulário com seus dados pessoais, '
     'grupo sanguíneo e disponibilidade, e confirme o cadastro.',
     'cadastro'),
    ('Posso editar meus dados depois do cadastro?',
     'Sim. Após fazer login, acesse o seu perfil para atualizar nome, contato, '
     'localização e disponibilidade para doação.',
     'cadastro'),
    # Doação
    ('Quais são os requisitos básicos para doar sangue?',
     'Em geral é necessário ter entre 18 e 69 anos, pesar no mínimo 50 kg, estar '
     'bem de saúde e não se enquadrar em impedimentos temporários. Use a seção '
     '"Posso ser doador?" para uma orientação inicial.',
     'doacao'),
    ('Com que frequência posso doar sangue?',
     'Homens podem doar a cada 2 meses (até 4 vezes ao ano) e mulheres a cada 3 '
     'meses (até 3 vezes ao ano).',
     'doacao'),
    # Solicitação de sangue
    ('Como solicito uma bolsa de sangue?',
     'Faça login e utilize a opção "Request" para registrar uma solicitação, '
     'informando grupo sanguíneo, hospital e demais dados do paciente.',
     'solicitacao'),
    ('Como encontro doadores ou bancos de sangue compatíveis?',
     'Use a opção "Search" para filtrar por grupo sanguíneo, estado e cidade, '
     'localizando doadores e bancos de sangue compatíveis.',
     'solicitacao'),
    # Acesso e login
    ('Esqueci minha senha. O que devo fazer?',
     'Na tela de login, clique em "Forgot Password", informe seu e-mail e siga as '
     'instruções enviadas para redefinir a senha.',
     'acesso'),
    ('Quais os requisitos para uma senha segura?',
     'A senha deve ter no mínimo 8 caracteres, incluindo ao menos uma letra '
     'maiúscula, uma minúscula, um número e um caractere especial.',
     'acesso'),
    # Uso geral
    ('Preciso estar logado para consultar o FAQ?',
     'Não. O FAQ e a seção "Posso ser doador?" estão disponíveis para todos os '
     'usuários, mesmo sem autenticação.',
     'geral'),
]


def seed_faqs(apps, schema_editor):
    FAQ = apps.get_model('dbconnection', 'FAQ')
    for question, answer, category in INITIAL_FAQS:
        FAQ.objects.get_or_create(
            question=question,
            defaults={'answer': answer, 'category': category, 'enabled': True},
        )


def unseed_faqs(apps, schema_editor):
    FAQ = apps.get_model('dbconnection', 'FAQ')
    questions = [q for q, _, _ in INITIAL_FAQS]
    FAQ.objects.filter(question__in=questions).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0007_bloodbankdetails_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('faq_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('category', models.CharField(
                    choices=[
                        ('cadastro', 'Cadastro'),
                        ('doacao', 'Doação'),
                        ('solicitacao', 'Solicitação de Sangue'),
                        ('acesso', 'Acesso e Login'),
                        ('geral', 'Uso Geral'),
                    ],
                    default='geral',
                    max_length=20)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'FAQ',
            },
        ),
        migrations.RunPython(seed_faqs, unseed_faqs),
    ]
