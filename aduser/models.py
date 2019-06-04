from django.db import models
from ldap3 import Server, Connection, ALL
from django.conf import settings
from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser, Group
import datetime


class aduser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, default=None)
    sid = models.CharField(max_length=46, null=True)
    telephoneNumber = models.CharField(max_length=20, null=True)
    DisplayName = models.CharField(max_length=255, null=True)
    PathToPic = models.CharField(max_length=255, null=True)
    Description = models.TextField(null=True)
    username =  models.TextField(null=False)
    password =  models.TextField(null=False)

    template_filter = '(userPrincipalName=%s)'
    connection = None
    groups = models.ManyToManyField('adgroups')

    def fill(self, user):
        domain = settings.JSON_SETTINGS['domain']
        s = Server(domain, get_info=ALL)
        c = Connection(s, user=('%s@%s' % (user.username, domain)),
        password=user.password)
        if c.bind():
            filter = self.template_filter % ('%s@%s' % (user.username, domain))
            c.search(settings.JSON_SETTINGS['BaseDN'], filter, attributes=['*'])
            print(c.entries[0])
            self.user = user
            self.user.is_staff = 1
            self.sid = c.entries[0]['objectSid'].value
            self.user.last_name = c.entries[0]['sn'].value
            self.user.first_name = c.entries[0]['givenName'].value
            self.user.email = c.entries[0]['mail'].value
            self.DisplayName = c.entries[0]['displayName'].value
            self.user.save()
            grs = c.entries[0]['memberOf']
            print(grs)
            gr = [x.split(',')[0][3:] for x in grs.values]
            self.telephoneNumber = c.entries[0]['telephoneNumber'].value
            self.save()
            for g in gr:
                print("g: %s" % g )
                if g == 'PBX-admin':
                    self.user.is_superuser = 1
                NewGroup, _ =Group.objects.get_or_create(name=g)
                NewGroup.save()
                group, gcreated = adgroups.objects.get_or_create(groupname=g,
                group = NewGroup)
                group.save()
                self.groups.add(group)
                self.user.groups.add(NewGroup)
                group.user.add(self)
            self.save()
        else:
            self.user = None
        if self.PathToPic is None:
            Staff = staff.objects.using('portal').filter(tel = user.aduser.telephoneNumber).get()
            self.PathToPic = "/%s%s%s.jpg" % (Staff.stafff, Staff.staffn, Staff.staffid)
            photo = open("%s%s" % (settings.JSON_SETTINGS['PathToPhoto'], self.PathToPic), 'wb')
            photo.write(Staff.photo)
            photo.flush()
            photo.close()
            self.Description = Staff.staffduties
        return self.user


class adgroups(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, default=None)
    user = models.ManyToManyField('aduser')
    groupname = models.TextField(null=True)
    #id = models.AutoField(primary_key=True, default=1)


class staff(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    staffid = models.IntegerField(db_column='StaffID')
    interfaceid = models.CharField(max_length=10, db_column='InterfaceID')
    vertushkaid = models.IntegerField(db_column='VertushkaID')
    authby = models.IntegerField(db_column='AuthBy')
    staffcompany = models.CharField(max_length=50, db_column='Staff_Company')
    staffstat = models.CharField(max_length=50, db_column='Staff_Stat')
    memberofboardofdirectors = models.BooleanField(db_column='MemberOfBoardOfDirectors')
    staffn = models.CharField(max_length=50, db_column='Staff_N')
    staffsn = models.CharField(max_length=50, db_column='Staff_SN')
    stafff = models.CharField(max_length=50, db_column='Staff_F')
    staffbd = models.DateTimeField(db_column='Staff_BD')
    hidebirthdate = models.BooleanField(db_column='HideBirthDate')
    hidebirthyear = models.BooleanField(db_column='HideBirthYear')
    hideworkanniversary = models.BooleanField(db_column='HideWorkAnniversary')
    staffin = models.DateTimeField(db_column='Staff_IN')
    staffdpt = models.CharField(max_length=50, db_column='Staff_Dpt')
    departmentid = models.IntegerField(db_column='DepartmentID')
    staffblockid = models.IntegerField(db_column='StaffBlockID')
    staffposision = models.CharField(max_length=50, db_column='Staff_Posision')
    staffduties = models.TextField(db_column='Staff_Duties')
    staffemail = models.CharField(max_length=100, db_column='Staff_Email')
    staffpi = models.CharField(max_length=2048, db_column='Staff_PI')
    staffpicture = models.CharField(max_length=50, db_column='Staff_Picture')
    ip = models.CharField(max_length=255, db_column='IP')
    compname = models.CharField(max_length=255, db_column='CompName')
    plugno = models.CharField(max_length=255, db_column='PlugNo')
    externalaccess = models.BooleanField(db_column='ExternalAccess')
    budgetcode = models.CharField(max_length=50, db_column='BudgetCode')
    tel = models.CharField(max_length=50, db_column='Tel')
    mobphonework = models.CharField(max_length=255, db_column='MobPhoneWork')
    mobphoneprivate = models.CharField(max_length=50, db_column='MobPhonePrivate')
    homephone = models.CharField(max_length=50, db_column='HomePhone')
    alias = models.CharField(max_length=50, db_column='Alias')
    computer = models.BooleanField(db_column='Computer')
    acboard = models.BooleanField(db_column='ACBoard')
    staffshow = models.BooleanField(db_column='StaffShow')
    phoneshow = models.BooleanField(db_column='PhoneShow')
    vacationshow = models.BooleanField(db_column='VacationShow')
    courconfmember = models.BooleanField(db_column='CourConfMember')
    courtemp = models.BooleanField(db_column='CourTemp')
    reason = models.IntegerField(db_column='Reason')
    acreturn = models.DateTimeField(db_column='ACReturn')
    status = models.CharField(max_length=50, db_column='Status')
    events = models.CharField(max_length=255, db_column='Events')
    branch = models.CharField(max_length=50, db_column='Branch')
    complete = models.BooleanField(db_column='Complete')
    lastupdated = models.DateTimeField(db_column='LastUpdated')
    rowguid = models.UUIDField(db_column='rowguid')
    vacdays = models.IntegerField(db_column='VacDays')
    replaceid = models.IntegerField(db_column='ReplaceID')
    staffvac = models.DateTimeField(db_column='Staff_Vac')
    dirvacdays = models.IntegerField(db_column='DirVacDays')
    implant = models.BooleanField(db_column='Implant')
    implantcompany = models.CharField(max_length=50, db_column='ImplantCompany')
    photo = models.BinaryField(db_column='Photo')
    stafffrus = models.CharField(max_length=50, db_column='Staff_F_Rus')
    staffnrus = models.CharField(max_length=50, db_column='Staff_N_Rus')
    staffsnrus = models.CharField(max_length=50, db_column='Staff_SN_Rus')
    privateemail = models.CharField(max_length=255, db_column='PrivateEMail')
    timeworkin = models.DateTimeField(db_column='Time_work_in')
    timeworkout = models.DateTimeField(db_column='Time_work_out')
    isfeedbackrecipient = models.BooleanField(db_column='IsFeedBackRecipient')
    seatno = models.CharField(max_length=5, db_column='SeatNo')
    seatfloor = models.IntegerField(db_column='SeatFloor')
    lomurscount = models.IntegerField(db_column='LomursCount')
    thankscount = models.IntegerField(db_column='ThanksCount')
    initialvacationfromath = models.IntegerField(db_column='InitialVacationFromATH')
    vacationdays20170101 = models.FloatField(db_column='VacationDays20170101')
    vacationdaysperyear = models.IntegerField(db_column='VacationDaysPerYear')
    sex = models.BooleanField(db_column='Sex')
    directboss = models.IntegerField(db_column='DirectBoss')
    functionalboss = models.IntegerField(db_column='FunctionalBoss')

    class Meta:
        managed = False
        db_table = 'Staff'
