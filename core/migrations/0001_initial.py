# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(db_column='RA', unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=120)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=80, null=True)),
                ('celular', models.CharField(db_column='Celular', max_length=11)),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivoquestoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1)),
                ('arquivo', models.CharField(db_column='Arquivo', max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivorespostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1)),
                ('ra_aluno', models.IntegerField(db_column='RA_Aluno')),
                ('arquivo', models.CharField(db_column='Arquivo', max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(db_column='Sigla', max_length=5, unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cursoturma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=240, unique=True)),
                ('carga_horario', models.SmallIntegerField(db_column='Carga_Horario')),
                ('teoria', models.DecimalField(db_column='Teoria', decimal_places=0, max_digits=3)),
                ('pratica', models.DecimalField(db_column='Pratica', decimal_places=0, max_digits=3)),
                ('ementa', models.TextField(db_column='Ementa')),
                ('competencias', models.TextField(db_column='Competencias')),
                ('habilidades', models.TextField(db_column='Habilidades')),
                ('conteudo', models.TextField(db_column='Conteudo')),
                ('bibliografia_basica', models.TextField(db_column='Bibliografia_Basica')),
                ('bibliografia_complementar', models.TextField(db_column='Bibliografia_Complementar')),
            ],
        ),
        migrations.CreateModel(
            name='Gradecurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField(db_column='Ano')),
                ('semestre', models.CharField(db_column='Semestre', max_length=1, unique=True)),
                ('sigla_curso', models.ForeignKey(db_column='Sigla_Curso', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('id_turma', models.CharField(db_column='id_Turma', max_length=1, unique=True)),
                ('ra_aluno', models.ForeignKey(db_column='RA_Aluno', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('ano_grade', models.SmallIntegerField(db_column='Ano_Grade')),
                ('numero', models.SmallIntegerField(db_column='Numero', unique=True)),
                ('semestre_grade', models.ForeignKey(db_column='Semestre_Grade', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Gradecurricular')),
            ],
        ),
        migrations.CreateModel(
            name='Periododisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla_curso', models.CharField(db_column='Sigla_Curso', max_length=5)),
                ('ano_grade', models.SmallIntegerField(db_column='Ano_Grade')),
                ('semestre_grade', models.CharField(db_column='Semestre_Grade', max_length=1)),
                ('numero_periodo', models.SmallIntegerField(db_column='Numero_Periodo', unique=True)),
                ('nome_disciplina', models.ForeignKey(db_column='Nome_Disciplina', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(db_column='RA', unique=True)),
                ('apelido', models.CharField(db_column='Apelido', max_length=30, unique=True)),
                ('nome', models.CharField(db_column='Nome', max_length=120)),
                ('email', models.CharField(db_column='Email', max_length=80)),
                ('celular', models.CharField(db_column='Celular', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_discplina', models.CharField(db_column='Nome_Discplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('numero', models.IntegerField(db_column='Numero', unique=True)),
                ('data_limite_entrega', models.CharField(db_column='Data_Limite_Entrega', max_length=10)),
                ('descricao', models.TextField(blank=True, db_column='Descricao', null=True)),
                ('dia_publicacao', models.CharField(db_column='Dia_Publicacao', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('numero_questao', models.IntegerField(db_column='Numero_Questao', unique=True)),
                ('ra_aluno', models.IntegerField(db_column='RA_Aluno', unique=True)),
                ('data_avaliacao', models.CharField(db_column='Data_Avaliacao', max_length=10)),
                ('nota', models.DecimalField(db_column='Nota', decimal_places=2, max_digits=4)),
                ('avaliacao', models.TextField(blank=True, db_column='Avaliacao', null=True)),
                ('descricao', models.TextField(blank=True, db_column='Descricao', null=True)),
                ('data_de_envio', models.CharField(db_column='Data_de_Envio', max_length=10)),
                ('id_turma', models.ForeignKey(db_column='id_Turma', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Questoes')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(db_column='Nome_Disciplina', max_length=240)),
                ('ano_ofertado', models.SmallIntegerField(db_column='Ano_Ofertado')),
                ('semestre_ofertado', models.CharField(db_column='Semestre_Ofertado', max_length=1)),
                ('idTurma', models.CharField(max_length=1, unique=True)),
                ('turno', models.CharField(db_column='Turno', max_length=15)),
                ('ra_professor', models.ForeignKey(db_column='RA_Professor', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Professor')),
            ],
        ),
        migrations.AddField(
            model_name='questoes',
            name='id_turma',
            field=models.ForeignKey(db_column='id_Turma', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Turma', unique=True),
        ),
        migrations.AddField(
            model_name='cursoturma',
            name='id_turma',
            field=models.ForeignKey(db_column='id_Turma', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Turma', unique=True),
        ),
        migrations.AddField(
            model_name='arquivorespostas',
            name='numero_questao',
            field=models.ForeignKey(db_column='Numero_Questao', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Respostas'),
        ),
        migrations.AddField(
            model_name='arquivoquestoes',
            name='numero_questao',
            field=models.ForeignKey(db_column='Numero_Questao', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Questoes'),
        ),
    ]
