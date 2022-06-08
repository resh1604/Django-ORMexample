from django.contrib.auth.base_user import BaseUserManager   #IMPORT OUR BASE CLASS

#THIS MANAGER WILL MANAGE OUR MODEL

class UserManager(BaseUserManager):
    use_in_migrations: True    #USE THIS USERMANAGER AT THE TIME OF MIGRATION

    #TWO METHODS HAVE TO BE OVERRIDDEN, NECCESSARY
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)     #NORMALIZATION IS REQUIRED TO BRING ALL EMAILS IN ONE FORMAT
        user = self.model(email = email, **extra_fields)
        user.set_password(password)    #USED TO HASH PASSWORD
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)    
        extra_fields.setdefault('is_superuser', True)    
        extra_fields.setdefault('is_active', True)    

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff= True')

        return self.create_user(email,password, **extra_fields)



class UserDataManager(BaseUserManager):
    
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user=self.model(
            email=self.normalize_email(email), #for lowercase
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def createsuperuser(self, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
