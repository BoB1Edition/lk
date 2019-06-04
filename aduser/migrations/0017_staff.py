# Generated by Django 2.1.7 on 2019-02-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0016_aduser_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('staffid', models.IntegerField(db_column='StaffID')),
                ('interfaceid', models.CharField(db_column='InterfaceID', max_length=10)),
                ('vertushkaid', models.IntegerField(db_column='VertushkaID')),
                ('authby', models.IntegerField(db_column='AuthBy')),
                ('staffcompany', models.CharField(db_column='Staff_Company', max_length=50)),
                ('staffstat', models.CharField(db_column='Staff_Stat', max_length=50)),
                ('memberofboardofdirectors', models.BooleanField(db_column='MemberOfBoardOfDirectors')),
                ('staffn', models.CharField(db_column='Staff_N', max_length=50)),
                ('staffsn', models.CharField(db_column='Staff_SN', max_length=50)),
                ('stafff', models.CharField(db_column='Staff_F', max_length=50)),
                ('staffbd', models.DateTimeField(db_column='Staff_BD')),
                ('hidebirthdate', models.BooleanField(db_column='HideBirthDate')),
                ('hidebirthyear', models.BooleanField(db_column='HideBirthYear')),
                ('hideworkanniversary', models.BooleanField(db_column='HideWorkAnniversary')),
                ('staffin', models.DateTimeField(db_column='Staff_IN')),
                ('staffdpt', models.CharField(db_column='Staff_Dpt', max_length=50)),
                ('departmentid', models.IntegerField(db_column='DepartmentID')),
                ('staffblockid', models.IntegerField(db_column='StaffBlockID')),
                ('staffposision', models.CharField(db_column='Staff_Posision', max_length=50)),
                ('staffduties', models.TextField(db_column='Staff_Duties')),
                ('staffemail', models.CharField(db_column='Staff_Email', max_length=100)),
                ('staffpi', models.CharField(db_column='Staff_PI', max_length=2048)),
                ('staffpicture', models.CharField(db_column='Staff_Picture', max_length=50)),
                ('ip', models.CharField(db_column='IP', max_length=255)),
                ('compname', models.CharField(db_column='CompName', max_length=255)),
                ('plugno', models.CharField(db_column='PlugNo', max_length=255)),
                ('externalaccess', models.BooleanField(db_column='ExternalAccess')),
                ('budgetcode', models.CharField(db_column='BudgetCode', max_length=50)),
                ('tel', models.CharField(db_column='Tel', max_length=50)),
                ('mobphonework', models.CharField(db_column='MobPhoneWork', max_length=255)),
                ('mobphoneprivate', models.CharField(db_column='MobPhonePrivate', max_length=50)),
                ('homephone', models.CharField(db_column='HomePhone', max_length=50)),
                ('alias', models.CharField(db_column='Alias', max_length=50)),
                ('computer', models.BooleanField(db_column='Computer')),
                ('acboard', models.BooleanField(db_column='ACBoard')),
                ('staffshow', models.BooleanField(db_column='StaffShow')),
                ('phoneshow', models.BooleanField(db_column='PhoneShow')),
                ('vacationshow', models.BooleanField(db_column='VacationShow')),
                ('courconfmember', models.BooleanField(db_column='CourConfMember')),
                ('courtemp', models.BooleanField(db_column='CourTemp')),
                ('reason', models.IntegerField(db_column='Reason')),
                ('acreturn', models.DateTimeField(db_column='ACReturn')),
                ('status', models.CharField(db_column='Status', max_length=50)),
                ('events', models.CharField(db_column='Events', max_length=255)),
                ('branch', models.CharField(db_column='Branch', max_length=50)),
                ('complete', models.BooleanField(db_column='Complete')),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('rowguid', models.UUIDField(db_column='rowguid')),
                ('vacdays', models.IntegerField(db_column='VacDays')),
                ('replaceid', models.IntegerField(db_column='ReplaceID')),
                ('staffvac', models.DateTimeField(db_column='Staff_Vac')),
                ('dirvacdays', models.IntegerField(db_column='DirVacDays')),
                ('implant', models.BooleanField(db_column='Implant')),
                ('implantcompany', models.CharField(db_column='ImplantCompany', max_length=50)),
                ('photo', models.BinaryField(db_column='Photo')),
                ('stafffrus', models.CharField(db_column='Staff_F_Rus', max_length=50)),
                ('staffnrus', models.CharField(db_column='Staff_N_Rus', max_length=50)),
                ('staffsnrus', models.CharField(db_column='Staff_SN_Rus', max_length=50)),
                ('privateemail', models.CharField(db_column='PrivateEMail', max_length=255)),
                ('timeworkin', models.DateTimeField(db_column='Time_work_in')),
                ('timeworkout', models.DateTimeField(db_column='Time_work_out')),
                ('isfeedbackrecipient', models.BooleanField(db_column='IsFeedBackRecipient')),
                ('seatno', models.CharField(db_column='SeatNo', max_length=5)),
                ('seatfloor', models.IntegerField(db_column='SeatFloor')),
                ('lomurscount', models.IntegerField(db_column='LomursCount')),
                ('thankscount', models.IntegerField(db_column='ThanksCount')),
                ('initialvacationfromath', models.IntegerField(db_column='InitialVacationFromATH')),
                ('vacationdays20170101', models.FloatField(db_column='VacationDays20170101')),
                ('vacationdaysperyear', models.IntegerField(db_column='VacationDaysPerYear')),
                ('sex', models.BooleanField(db_column='Sex')),
                ('directboss', models.IntegerField(db_column='DirectBoss')),
                ('functionalboss', models.IntegerField(db_column='FunctionalBoss')),
            ],
            options={
                'db_table': 'Staff',
                'managed': False,
            },
        ),
    ]