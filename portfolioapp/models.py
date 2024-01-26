from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
#from django.contrib.auth.models import Permission
#from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must enter email")
        user= self.model(email=self.normalize_email(email),username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_staffuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_staff= True
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_staff= True
        user.is_active= True
        user.save(using=self._db)
        return user
    """
    def create_member(self,email,username,password=None):
        user = self.create_user(email,password=password,username=username)
        user.is_member=True
        user.is_staff=True
        user.save(using=self._db)
        return user
    """
class UserProfile(AbstractBaseUser):
    email= models.EmailField(verbose_name='email',max_length=255,unique=True,)
    Fname= models.CharField(max_length=20,default='')
    Lname= models.CharField(max_length=20,default='')
    username= models.CharField(('username'),max_length=150,unique=True,)
    #is_member=models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    #groups=models.ManyToManyField(Group,blank=True,related_name='user_profiles', verbose_name='groups',help_text='grps user belong to')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()
    
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    

class PortfolioModel(models.Model):
    Fname= models.CharField(max_length=20,null=False)
    Lname= models.CharField(max_length=20,null=False)
    contact_no= models.PositiveIntegerField(null=False)
    email= models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # stock details
    stock_name= models.CharField(max_length=50)
    stock_number= models.IntegerField()
    stock_price= models.IntegerField()
    stock_date= models.DateField()
    # mutual fund details
    mf_name= models.CharField(max_length=50)
    mf_amt= models.IntegerField()
    mf_date= models.DateField()

class CurrentMarketModel(models.Model):
    stockname=models.CharField(max_length=20,null=True)
    stockamt=models.DecimalField(decimal_places=2, max_digits=3)
    symbol=models.CharField(max_length=50,null=True)
    exchange=models.CharField(max_length=100,null=True)
    type=models.CharField(max_length=50,null=True)

class InvestmentModel(models.Model):
    roi=models.IntegerField()
    valuation=models.IntegerField()
    email=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

class ResourcesModel(models.Model):
    books=models.CharField(max_length=100,default='')
    author=models.CharField(max_length=100, default='')
    link=models.URLField()

class MembershipModel(models.Model):
    mem_id=models.IntegerField()
    start_time=models.DateField(auto_now=True)
    time_period=models.IntegerField(default=30)
    email=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

class TransactionlogModel(models.Model):
    amount=models.CharField(max_length=100)
    trans_id=models.CharField(max_length=100)
    razorpay_id=models.CharField(max_length=100, blank=True)
    paid=models.BooleanField(default=False)
    

"""
#membership_content_type = ContentType.objects.get_for_model(MembershipModel)
membership_permissions = [
    Permission.objects.create(codename='add_membershipmodel'),
    #Permission.objects.create(codename='change_membershipmodel'),
    #Permission.objects.create(codename='delete_membershipmodel'),
    Permission.objects.create(codename='add_portfoliomodel'),
    Permission.objects.create(codename='change_portfoliomodel'),
    Permission.objects.create(codename='delete_portfoliomodel'),
    Permission.objects.create(codename='view_resourcesmodel'),
    Permission.objects.create(codename='view_investmentmodel'),
    Permission.objects.create(codename='view_currentmarketmodel'),
]

other_models_content_types = [
    ContentType.objects.get_for_model(PortfolioModel),
    ContentType.objects.get_for_model(CurrentMarketModel),
    ContentType.objects.get_for_model(InvestmentModel),
    ContentType.objects.get_for_model(ResourcesModel),
    ContentType.objects.get_for_model(TransactionlogModel),
]

membership_permissions += [
    Permission.objects.create(codename=f'add_{content_type.model.lower()}', name=f'Can add {content_type.model}', content_type=content_type)
    for content_type in other_models_content_types
] + [
    Permission.objects.create(codename=f'change_{content_type.model.lower()}', name=f'Can change {content_type.model}', content_type=content_type)
    for content_type in other_models_content_types
] + [
    Permission.objects.create(codename=f'delete_{content_type.model.lower()}', name=f'Can delete {content_type.model}', content_type=content_type)
    for content_type in other_models_content_types
]

non_membership_content_types = [
    ContentType.objects.get_for_model(PortfolioModel),
    ContentType.objects.get_for_model(CurrentMarketModel),
    ContentType.objects.get_for_model(ResourcesModel),
]
  
non_membership_permissions = [
    Permission.objects.create(codename='add_membershipmodel'),
    #Permission.objects.create(codename='change_membershipmodel'),
    #Permission.objects.create(codename='delete_membershipmodel'),
    Permission.objects.create(codename='add_portfoliomodel'),
    Permission.objects.create(codename='change_portfoliomodel'),
    Permission.objects.create(codename='delete_portfoliomodel'),
]


members_group = Group.objects.get(name='Members')
non_members_group = Group.objects.get(name='NonMembers')

members_group.permissions.add(*membership_permissions)
non_members_group.permissions.add(*non_membership_permissions)
"""