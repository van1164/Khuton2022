# Generated by Django 3.2.13 on 2022-09-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0003_auto_20220930_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject_table',
            old_name='subject_code',
            new_name='AI네트워킹',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='SorP',
            new_name='Professor',
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IT기술영어1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IT기술영어2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IT기술영어3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IoT네트워크',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IoT디지털시스템',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='IoT소프트웨어',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='SW스타트업비즈니스',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='SW스타트업프로젝트',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='Student_ID',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='UI_UX프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='객체지향프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='기계학습',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='논리회로',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='단기현장실습',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='데이터베이스',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='데이터센터프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='독립심화학습1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='독립심화학습2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='디자인적사고',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='딥러닝',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='로봇스프트웨어',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='리눅스시스템프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='멀티미디어시스템',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='멀티미디어처리',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='모바일프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='문제해결',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='물리학및실험1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='미분방정식',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='미분적분학',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='빅데이터프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='선형대수',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='소프트웨어공학',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='시스템분석및설계',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='신호와시스템',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='실전기계학습',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='알고리즘분석',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='연구연수활동1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='연구연수활동2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='영상처리',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='오픈소스SW개발',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='운영체제',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='웹서비스프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='웹파이선프로그래밍',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='이산구조',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='인간컴퓨터상호작용',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='인공지능',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='자료구조',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='장기현장실습',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='정보보호',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='졸업논문',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='최신기술콜로키움1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='최신기술콜로키움2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='최신기술프로젝트1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='최신기술프로젝트2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='캡스톤디자인1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='캡스톤디자인2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='컴퓨터구조',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='컴퓨터그래픽스',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='컴퓨터네트워크',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='컴퓨터비전',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='클라우드컴퓨팅',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='파일처리',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='프로그래밍언어구조론',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='형식언어및컴파일러',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject_table',
            name='확률및랜덤변수',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='subject_table',
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject_table',
            field=models.ManyToManyField(to='MAIN.subject_table'),
        ),
    ]
